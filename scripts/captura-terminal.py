#!/usr/bin/env python3
"""
Captura de terminal real para la evidencia del Prototipo II (SIN).

Restricciones del proyecto
--------------------------
La evidencia de terminal del capitulo 4 tiene que ser una captura CRUDA de una
terminal. No se generan imagenes con IA ni se componen capturas: si no se puede
obtener, se reporta como pendiente.

Como se obtiene
---------------
1. xfce4-terminal con --disable-server. Sin ese flag, el terminal reutiliza la
   instancia del servidor y abre una PESTAÑA en una terminal ya abierta, con lo
   cual la captura muestra la ventana de otro usuario en vez de la nueva.
2. El comando se ejecuta de verdad en esa terminal. La linea con el prompt y el
   comando se imprime antes de ejecutarlo para que la figura muestre que se
   ejecuto (con un pty se intentaba que el eco de la tty lo mostrara, pero el
   eco llega con retardo y la captura salia a medio teclear).
3. xwd -id <x_window> + conversor XWD a PNG: captura los pixelos de ESA ventana
   aunque este tapada por otras. Capturar la pantalla completa y recortar fallaba
   porque el navegador y el editor del usuario quedan por encima.

Todos los subprocesos llevan timeout para que el script no pueda quedarse
esperando.

Uso:
    python3 scripts/captura-terminal.py <salida.png> "<comando>" [segundos]
                                        [cols] [rows]
"""

import os
import re
import subprocess
import sys
import tempfile
import time

DISPLAY = os.environ.get("DISPLAY", ":0.0")
REPO = "/home/fer/Maestria/tesis/new/taxfisco-research-lab"
BG, FG = "#12141a", "#e8e8e8"
USER_HOST = "fer@fer"


def envd():
    return {**os.environ, "DISPLAY": DISPLAY}


def run(cmd, timeout=20, **kw):
    try:
        return subprocess.run(cmd, capture_output=True, text=True,
                              timeout=timeout, env=envd(), **kw)
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(cmd, 124, "", "timeout")


def find_x_window(title, tries=15):
    """Localiza el id de la ventana X cuyo titulo coincide."""
    for _ in range(tries):
        out = run(["xwininfo", "-root", "-tree"], timeout=25).stdout
        for line in out.splitlines():
            m = re.search(r'(0x[0-9a-fA-F]+)\s+"' + re.escape(title) + r'"', line)
            if m:
                return m.group(1)
        time.sleep(1.0)
    return None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    salida, comando = sys.argv[1], sys.argv[2]
    espera = float(sys.argv[3]) if len(sys.argv) > 3 else 10.0
    cols = sys.argv[4] if len(sys.argv) > 4 else "120"
    rows = sys.argv[5] if len(sys.argv) > 5 else "32"
    titulo = "SINCAP%d" % (int(time.time()) % 100000)

    # El prompt y el comando se imprimen antes de ejecutar para que la figura
    # muestre que se ejecuto; la salida que viene detras es real. El comando se
    # escribe en un fichero para no depender de comillas anidadas.
    ps1 = f"{USER_HOST}:~{REPO}$ "
    inner = "/tmp/_sincap_inner.sh"
    with open(inner, "w") as fh:
        fh.write("#!/bin/bash\n")
        fh.write(f"printf '\\n{ps1}{comando}\\n\\n'\n")
        fh.write(f"{comando}\n")
        fh.write(f"printf '\\n{ps1}'\n")
        fh.write("sleep 900\n")
    os.chmod(inner, 0o755)

    run(["pkill", "-f", "xfce4-terminal.*SINCAP"], timeout=15)
    run(["xfce4-terminal", "--disable-server", "--title=" + titulo,
         "--dynamic-title-mode=none", f"--geometry={cols}x{rows}+140+320",
         "--font=Monospace 11", "--color-bg=" + BG, "--color-text=" + FG,
         "--working-directory=" + REPO,
         "--command", f"bash {inner}"],
        timeout=25)

    try:
        win = find_x_window(titulo)
        if not win:
            print("ERROR: no se localizo la ventana X", file=sys.stderr)
            return 1
        print(f"  ventana X: {win}")

        time.sleep(espera)

        xwd_path = tempfile.mktemp(suffix=".xwd")
        with open(xwd_path, "wb") as fh:
            subprocess.run(["xwd", "-id", win, "-silent"], stdout=fh,
                           stderr=subprocess.DEVNULL, timeout=60, env=envd())
        size = os.path.getsize(xwd_path)
        print(f"  xwd: {size} bytes")
        if size < 200:
            print("ERROR: xwd no capturo la ventana", file=sys.stderr)
            return 1

        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import xwd2png
        os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
        xwd2png.parse(xwd_path, salida)
        os.remove(xwd_path)
        return 0
    finally:
        run(["pkill", "-f", "xfce4-terminal.*SINCAP"], timeout=15)


if __name__ == "__main__":
    sys.exit(main())
