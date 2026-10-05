#!/usr/bin/env node
/**
 * render-terminal-win.mjs
 * ======================
 * Rasterizador de figuras de terminal para Windows.
 *
 * Por que existe
 * --------------
 * `render-terminal.py` compone las figuras y las rasteriza, pero su rasterizado
 * depende de Playwright en Linux (rutas /home/fer/...). En una estacion Windows
 * no arranca. Este script cubre SOLO la parte de medicion + captura, que es
 * independiente del sistema:
 *
 *   1. Mide el tamano real de `.win` en el navegador, con el Chrome que ya
 *      este instalado (Chrome o Edge), via Chrome DevTools Protocol. Sin
 *      Playwright y sin descargar nada.
 *   2. Captura con `Page.captureScreenshot` al tamano exacto y a escala 2.
 *   3. NO toca el texto: la composicion y la verificacion siguen siendo
 *      responsabilidad de `render-terminal.py`, que es quien guarantee que la
 *      figura reproduce el .txt caracter a caracter.
 *
 * Uso:
 *   node scripts/render-terminal-win.mjs <figura.html> <figura.png> [escala]
 *
 * Salida: el PNG. Codigo de salida 0 si la captura se genero.
 */

import { spawn } from "node:child_process";
import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve, dirname } from "node:path";
import { pathToFileURL } from "node:url";

// --- Localizar un navegador Chromium ----------------------------------------

const CANDIDATOS = [
  ["chrome", join(process.env["ProgramFiles"] ?? "C:/Program Files", "Google/Chrome/Application/chrome.exe")],
  ["chrome", join(process.env["ProgramFiles(x86)"] ?? "C:/Program Files (x86)", "Google/Chrome/Application/chrome.exe")],
  ["chrome", join(process.env.LOCALAPPDATA ?? "", "Google/Chrome/Application/chrome.exe")],
  ["edge", join(process.env["ProgramFiles(x86)"] ?? "C:/Program Files (x86)", "Microsoft/Edge/Application/msedge.exe")],
  ["edge", join(process.env["ProgramFiles"] ?? "C:/Program Files", "Microsoft/Edge/Application/msedge.exe")],
];

function navegador() {
  for (const [nombre, ruta] of CANDIDATOS) {
    if (ruta && existsSync(ruta)) return { nombre, ruta };
  }
  throw new Error(
    "No se encontro Chrome ni Edge. Instala uno o ajusta CANDIDATOS en este script."
  );
}

// --- Cliente minimo de CDP sobre el WebSocket nativo de Node 18+ ------------

class CDP {
  constructor(ws) {
    this.ws = ws;
    this.id = 0;
    this.pendientes = new Map();
    this.eventos = new Map();
    ws.addEventListener("message", (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id !== undefined) {
        const p = this.pendientes.get(msg.id);
        if (!p) return;
        this.pendientes.delete(msg.id);
        if (msg.error) p.rechaza(new Error(`${msg.error.message} (${JSON.stringify(msg.error.data ?? "")})`));
        else p.resuelve(msg.result);
      } else if (msg.method) {
        const waits = this.eventos.get(msg.method);
        if (waits) waits.forEach((fn) => fn(msg.params));
      }
    });
  }

  enviar(method, params = {}) {
    const id = ++this.id;
    this.ws.send(JSON.stringify({ id, method, params }));
    return new Promise((resuelve, rechaza) => {
      this.pendientes.set(id, { resuelve, rechaza });
    });
  }

  esperarEvento(method) {
    return new Promise((resuelve) => {
      const lista = this.eventos.get(method) ?? [];
      lista.push(resuelve);
      this.eventos.set(method, lista);
    });
  }
}

const esperar = (ms) => new Promise((r) => setTimeout(r, ms));

async function abrirCDP(puerto, intentos = 40) {
  for (let i = 0; i < intentos; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${puerto}/json/list`);
      if (res.ok) {
        const targets = await res.json();
        const pagina = targets.find((t) => t.type === "page" && t.webSocketDebuggerUrl);
        if (pagina) return pagina.webSocketDebuggerUrl;
      }
    } catch {
      // El navegador aun no escucha: se reintenta.
    }
    await esperar(250);
  }
  throw new Error("El navegador no abrio el puerto de depuracion a tiempo");
}

// --- Medir y capturar -------------------------------------------------------

async function main() {
  const [htmlArg, pngArg, escalaArg] = process.argv.slice(2);
  if (!htmlArg || !pngArg) {
    console.error("Uso: node render-terminal-win.mjs <figura.html> <figura.png> [escala]");
    process.exit(2);
  }
  const escala = Number(escalaArg ?? 2);
  const htmlPath = resolve(htmlArg);
  const pngPath = resolve(pngArg);
  if (!existsSync(htmlPath)) throw new Error(`No existe el HTML: ${htmlPath}`);

  const { nombre, ruta } = navegador();
  const puerto = 9200 + Math.floor(Math.random() * 400);
  const perfil = mkdtempSync(join(tmpdir(), "fig-render-"));

  const proc = spawn(
    ruta,
    [
      "--headless=new",
      "--disable-gpu",
      "--no-sandbox",
      "--hide-scrollbars",
      "--disable-extensions",
      "--no-first-run",
      "--no-default-browser-check",
      "--disable-lcd-text",
      `--remote-debugging-port=${puerto}`,
      `--user-data-dir=${perfil}`,
      "about:blank",
    ],
    { stdio: "ignore" }
  );

  let cdp = null;
  try {
    const wsUrl = await abrirCDP(puerto);
    const ws = new WebSocket(wsUrl);
    await new Promise((resuelve, rechaza) => {
      ws.addEventListener("open", resuelve, { once: true });
      ws.addEventListener("error", () => rechaza(new Error("No se pudo abrir el WebSocket de CDP")), { once: true });
    });
    cdp = new CDP(ws);

    await cdp.enviar("Page.enable");
    await cdp.enviar("Emulation.setDeviceMetricsOverride", {
      width: 1600,
      height: 1200,
      deviceScaleFactor: 1,
      mobile: false,
    });

    const url = pathToFileURL(htmlPath).href;
    const cargado = cdp.esperarEvento("Page.loadEventFired");
    await cdp.enviar("Page.navigate", { url });
    await cargado;
    await esperar(120); // asentar la tipografia antes de medir

    // Medir el bloque .win, que es lo que se quiere recortar.
    const { result } = await cdp.enviar("Runtime.evaluate", {
      expression: `(() => {
        const el = document.querySelector('.win');
        if (!el) return null;
        const r = el.getBoundingClientRect();
        return { w: Math.ceil(r.width), h: Math.ceil(r.height) };
      })()`,
      returnByValue: true,
    });
    if (!result.value) throw new Error("El HTML no contiene un elemento .win que medir");
    const { w, h } = result.value;

    // Captura al tamano exacto. clip va en pixeles CSS.
    const cap = await cdp.enviar("Page.captureScreenshot", {
      format: "png",
      captureBeyondViewport: true,
      clip: { x: 0, y: 0, width: w, height: h, scale: escala },
    });
    writeFileSync(pngPath, Buffer.from(cap.data, "base64"));

    const px = { w: w * escala, h: h * escala };
    console.log(
      `  ${nombre}: ${w}x${h} CSS -> ${px.w}x${px.h} px (escala ${escala})  ${pngPath}`
    );
  } finally {
    try { cdp?.ws.close(); } catch { /* ignorado */ }
    proc.kill();
    await esperar(150);
    try { rmSync(perfil, { recursive: true, force: true }); } catch { /* ignorado */ }
  }
}

main().catch((err) => {
  console.error("ERROR:", err.message);
  process.exit(1);
});
