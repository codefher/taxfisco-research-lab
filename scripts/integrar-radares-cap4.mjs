// Integra los radares comparativos en el capitulo de resultados: retira los
// radares anteriores, inserta el apartado de mejora del analisis situacional
// con las dos figuras nuevas y renumera figuras y apartados.
//
// Uso: node scripts/integrar-radares-cap4.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const raiz = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const htmlRadares = path.join(raiz, 'resultados-prototipos', 'radares-comparativos.html');
const destino = path.join(raiz, 'resultados-prototipos', 'cap4-nuevo.html');

/* ------------------------------------------------------------------ */
/* 1. Se generan las dos figuras con el mismo codigo de los radares.   */
/* ------------------------------------------------------------------ */
const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage({ viewport: { width: 1400, height: 1200 } });
await pagina.goto('file:///' + htmlRadares.replace(/\\/g, '/'), { waitUntil: 'load' });
await pagina.waitForTimeout(500);

const figuras = await pagina.evaluate(() => {
  const NS = 'http://www.w3.org/2000/svg';
  const crear = (tag, attrs = {}) => {
    const n = document.createElementNS(NS, tag);
    for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
    return n;
  };
  const anchoTexto = (texto, tam) => {
    const c = document.createElement('canvas').getContext('2d');
    c.font = tam + 'px "Segoe UI", Arial, sans-serif';
    return c.measureText(texto).width;
  };

  const construir = (clave, titulo, subtitulo, fuente, aria) => {
    const config = FIGURAS[clave];
    const cont = document.createElement('div');
    const radar = dibujarRadar(cont, config);   // mismo dibujado del HTML de radares

    const W = 1240, H = 960, DESPLAZAMIENTO = 55;
    const svg = crear('svg', {
      viewBox: '0 0 ' + W + ' ' + H,
      xmlns: NS,
      role: 'img',
      'aria-label': aria,
    });
    svg.appendChild(crear('rect', { x: 0, y: 0, width: W, height: H, fill: '#FFFFFF' }));

    const t1 = crear('text', {
      x: 20, y: 28, 'font-family': 'Segoe UI,sans-serif', 'font-size': 16,
      'font-weight': 700, fill: '#1F3864',
    });
    t1.textContent = titulo;
    svg.appendChild(t1);

    const t2 = crear('text', {
      x: 20, y: 47, 'font-family': 'Segoe UI,sans-serif', 'font-size': 12, fill: '#5A6878',
    });
    t2.textContent = subtitulo;
    svg.appendChild(t2);

    svg.appendChild(crear('line', { x1: 20, y1: 59, x2: W - 20, y2: 59, stroke: '#D6DEE8' }));

    const grupo = crear('g', { transform: 'translate(0,' + DESPLAZAMIENTO + ')' });
    grupo.innerHTML = radar.innerHTML;
    svg.appendChild(grupo);

    // Leyenda centrada al pie de la figura
    const items = config.series.map((s) => ({
      nombre: s.nombre,
      color: s.color,
      ancho: anchoTexto(s.nombre, 11),
    }));
    const anchoTotal = items.reduce((a, i) => a + 26 + i.ancho, 0) + (items.length - 1) * 34;
    let x = (W - anchoTotal) / 2;
    const y = 922;
    for (const item of items) {
      svg.appendChild(crear('line', {
        x1: x, y1: y, x2: x + 20, y2: y, stroke: item.color, 'stroke-width': 2.6, 'stroke-linecap': 'round',
      }));
      svg.appendChild(crear('circle', {
        cx: x + 10, cy: y, r: 3.4, fill: item.color, stroke: '#FFFFFF', 'stroke-width': 1.5,
      }));
      const t = crear('text', {
        x: x + 26, y: y + 4, 'font-family': 'Segoe UI,sans-serif', 'font-size': 11, fill: '#5A6878',
      });
      t.textContent = item.nombre;
      svg.appendChild(t);
      x += 26 + item.ancho + 34;
    }

    const pie = crear('text', {
      x: W / 2, y: 945, 'font-family': 'Segoe UI,sans-serif', 'font-size': 9.5,
      fill: '#8A97A5', 'text-anchor': 'middle',
    });
    pie.textContent = fuente;
    svg.appendChild(pie);

    return svg.outerHTML;
  };

  return {
    libelula: construir(
      'libelula',
      'Perfil comparativo de Libélula SRL',
      'Diagnóstico situacional inicial y resultados del Prototipo 1',
      'Datos del análisis comparativo unificado de Libélula SRL y de los indicadores técnicos del Prototipo 1',
      'Radar de catorce dimensiones de la gestión de incidentes en Libélula SRL que enfrenta el diagnóstico situacional inicial y el perfil posterior a la aplicación del Prototipo 1. ' +
      'Detección y registro 31,25 frente a 85 por ciento; clasificación y evidencia 33,33 frente a 98; respuesta y tiempos de atención 41,67 frente a 70; lecciones aprendidas 25 frente a 98; ' +
      'integridad y custodia de evidencias 8,33 frente a 100; respaldos y restauración 25 frente a 100; retención y acceso a evidencias 50 frente a 100; control de accesos 33,33 frente a 100; ' +
      'desarrollo seguro 41,67 frente a 100; gestión de vulnerabilidades 25 frente a 100; integridad y trazabilidad de registros 50 frente a 100; gestión de riesgos 50 frente a 100; ' +
      'capacitación y concienciación 25 frente a 98; métricas y mejora continua 50 frente a 95 por ciento.'
    ),
    sin: construir(
      'sin',
      'Perfil comparativo del diagnóstico del SIN y el Prototipo 2',
      'Estado inicial, primera vuelta y medición final · 14 dimensiones',
      'Datos del análisis comparativo unificado del Servicio de Impuestos Nacionales y de los indicadores técnicos del Prototipo 2',
      'Radar de catorce dimensiones de la gestión de incidentes en el Servicio de Impuestos Nacionales que enfrenta el diagnóstico inicial, la primera vuelta y la medición final del Prototipo 2. ' +
      'La serie de cierre alcanza el 100 por ciento en doce dimensiones, con la respuesta y los tiempos de atención en 93, la capacitación y concienciación en 98 y las métricas y mejora continua en 96.'
    ),
  };
});

await navegador.close();

/* ------------------------------------------------------------------ */
/* 2. Se arma el apartado nuevo con las dos figuras.                  */
/* ------------------------------------------------------------------ */
const seccion = `<!-- ══════════ 4.4.5 MEJORA DEL ANALISIS SITUACIONAL ══════════ -->
<section id="s445">
<h3>4.4.5 Mejora del análisis situacional tras la aplicación de la metodología</h3>
<p class="sub">Lectura del diagnóstico inicial y del perfil posterior en los dos casos de estudio, sobre las catorce dimensiones del instrumento de diagnóstico.</p>

<p class="prosa">El análisis situacional inicial de cada caso de estudio quedó registrado en el apartado 4.1.4, donde el instrumento de diagnóstico de madurez se aplicó sobre las catorce dimensiones de la gestión de incidentes en el Servicio de Impuestos Nacionales y en la empresa homologada Libélula SRL. Los dos perfiles que de ese diagnóstico resultan constituyen la línea de base sobre la que se aplica la metodología Honeypot, de manera que la comparación entre el inicio y el momento posterior a la aplicación mida la mejora que el ejercicio produce sobre cada dimensión. Las Figuras 17 y 18 recogen esa lectura en un mismo sistema de catorce ejes, con el perfil inicial en la serie azul y el perfil posterior en la serie de cierre, de manera que la diferencia entre ambos momentos se lea de un vistazo y con la misma escala en los dos casos.</p>

<p class="prosa">El caso de Libélula SRL muestra el desplazamiento más amplio. El diagnóstico inicial se sitúa en el 34,52 % acumulado, con la integridad y custodia de evidencias en su valor más bajo, 8,33 %, y cinco dimensiones en el 50,00 %. Después de la aplicación de la metodología, el perfil se concentra en el extremo superior del diagrama: la integridad y custodia de evidencias pasa de 8,33 % al 100 %, la detección y registro sube de 31,25 % al 85 % y las dimensiones de custodia, trazabilidad, respaldo y control de accesos alcanzan la totalidad de la escala. La respuesta y los tiempos de atención quedan en el 70 %, que es el valor más bajo del perfil posterior, mientras que la clasificación de incidentes, el aprendizaje de las lecciones y la concienciación del personal se sitúan en el 98 % y las métricas de mejora continua en el 95 %. La lectura muestra que la metodología actúa sobre las dimensiones que presentaban brechas de cobertura y no sobre las que ya alcanzaban un cumplimiento intermedio.</p>

<p class="lbl">Figura 17</p>
<figure>
${figuras.libelula}
<figcaption><i>Figura 17.</i> Perfil comparativo de Libélula SRL: análisis situacional inicial y perfil posterior a la aplicación del Prototipo 1, sobre las catorce dimensiones del instrumento de diagnóstico. La serie azul corresponde al diagnóstico inicial y la serie roja al perfil posterior a la aplicación.</figcaption>
</figure>
<div class="note"><i>Nota.</i> Los valores iniciales son los porcentajes que el diagnóstico de madurez calcula sobre los puntajes declarados en el documento de análisis comparativo unificado, cuyo resultado acumulado es de 58 puntos sobre un máximo de 168. La serie posterior es una visualización orientativa, porque el apartado 4.4 solo publica indicadores técnicos agregados del Prototipo 1 y no puntajes posteriores por cada una de estas catorce dimensiones, de manera que la serie roja no deba interpretarse como medición directa por dimensión.</div>

<p class="prosa">El segundo caso, el laboratorio del Servicio de Impuestos Nacionales, parte de un diagnóstico inicial algo más alto, 38,10 % acumulado, con la retención y el acceso a evidencias como dimensión más elevada, 62,50 %, y cinco dimensiones en el 25,00 %. Su perfil posterior se dibuja en dos momentos, la primera vuelta y la medición final del Prototipo 2, de manera que se distinga el avance de la primera aplicación del ajuste que introduce la medición final verificada. El estado inicial permanece en la banda intermedia del diagrama, entre el 25,00 % y el 62,50 %, mientras que la primera vuelta eleva ya la custodia y la retención de evidencias a la totalidad de la escala y deja las demás dimensiones entre el 40 % y el 50 %. La medición final alcanza el 100 % en doce de las catorce dimensiones, con la respuesta y los tiempos de atención en el 93 %, la concienciación del personal en el 98 % y las métricas de mejora continua en el 96 %. La distancia entre la primera vuelta y la medición final es la medida del efecto de las correcciones que las lecciones aprendidas de la primera aplicación originaron.</p>

<p class="lbl">Figura 18</p>
<figure>
${figuras.sin}
<figcaption><i>Figura 18.</i> Perfil comparativo del Servicio de Impuestos Nacionales: diagnóstico inicial, primera vuelta y medición final del Prototipo 2, sobre las catorce dimensiones del instrumento de diagnóstico. La serie azul corresponde al diagnóstico inicial, la naranja a la primera vuelta y la verde a la medición final verificada.</figcaption>
</figure>
<div class="note"><i>Nota.</i> Los valores iniciales son los porcentajes que el diagnóstico de madurez calcula sobre los puntajes declarados en el documento de análisis comparativo unificado, cuyo resultado acumulado es de 64 puntos sobre un máximo de 168. Las series de la primera vuelta y de la medición final son una visualización orientativa de los indicadores técnicos agregados que el apartado 4.4 publica para el Prototipo 2, con los valores al 100 % donde el indicador correspondiente queda verificado y con valores finales entre el 93 % y el 98 % en las dimensiones que no alcanzan la totalidad de la escala.</div>

<p class="prosa">La lectura conjunta de las dos figuras muestra que la mejora se concentra en un mismo patrón en los dos casos, aunque con intensidades distintas. En ambos, la dimensión con menor cumplimiento en el diagnóstico inicial alcanza la escala completa después de la aplicación, porque la custodia de la evidencia se consolida sobre los archivos que el propio ejercicio produce y verifica. En ambos, las dimensiones que dependen de la conducta organizativa, como la clasificación de incidentes, el aprendizaje de las lecciones y la concienciación del personal, quedan por debajo de la totalidad, lo que delimita la parte de la mejora que exige un cambio de hábito organizativo y no una capacidad técnica. El apartado siguiente presenta la síntesis de los resultados medidos, donde esos perfiles se leen junto con los denominadores declarados en la Tabla 5.</p>
</section>

<!-- ══════════ 4.4.6 ══════════ -->`.replace(/\n/g, '\r\n');

/* ------------------------------------------------------------------ */
/* 3. Se retira los radares anteriores y se inserta el apartado nuevo. */
/* ------------------------------------------------------------------ */
let html = fs.readFileSync(destino, 'utf8');
const antes = html.length;

const quitar = (texto, desde, hasta) => {
  const i = texto.indexOf(desde);
  if (i < 0) throw new Error('No se encuentra el anclaje de inicio: ' + desde.slice(0, 70));
  const j = texto.indexOf(hasta, i);
  if (j < 0) throw new Error('No se encuentra el anclaje de fin: ' + hasta.slice(0, 70));
  return texto.slice(0, i) + texto.slice(j);
};

// Radares anteriores: Figura 17 (primer prototipo) con su prosa y su nota.
html = quitar(
  html,
  '<p class="prosa">La Figura 17 reúne los ocho indicadores del primer prototipo',
  '<p class="prosa">El resultado verificado mejora cuatro de los ocho indicadores del primer prototipo'
);
// Radares anteriores: Figura 18 (segundo prototipo) con su prosa y su nota.
html = quitar(
  html,
  '<p class="prosa">La Figura 18 aplica la misma lectura al segundo prototipo',
  '<p class="prosa">El resultado verificado mejora cinco de los ocho indicadores del segundo prototipo'
);
// Radar anterior: Figura 19 (perfil verificado de los dos prototipos).
html = quitar(html, '<p class="lbl">Figura 19</p>', '</section>');

// La frase que remitía a los dos radares anteriores se reorienta al apartado nuevo.
html = html.replace(
  'La lectura conjunta de los dos radares muestra que ambos prototipos comparten el mismo momento final verificado, porque el estado final del primero se verifica en el segundo laboratorio, de manera que la diferencia entre las dos figuras se concentre en el punto de partida de cada campaña.',
  'La lectura conjunta de los dos casos de estudio, con el perfil inicial y el perfil posterior sobre las mismas catorce dimensiones, se presenta en el apartado siguiente.'
);

// Renumeracion de apartados y figuras.
html = html.replace('<section id="s445">', '<section id="s446">');
html = html.replace('<h3>4.4.5 Síntesis de los resultados</h3>', '<h3>4.4.6 Síntesis de los resultados</h3>');
html = html.replace('lectura conjunta del 4.4.5.', 'lectura conjunta del 4.4.6.');
html = html.replace('<!-- ══════════ 4.4.5 ══════════ -->', '<!-- ══════════ 4.4.6 ══════════ -->');
html = html.replace('<p class="lbl">Figura 20</p>', '<p class="lbl">Figura 19</p>');
html = html.replace('<figcaption><i>Figura 20.</i>', '<figcaption><i>Figura 19.</i>');
html = html.replace(
  '  <li><a href="#s445">4.4.5 Síntesis de los resultados</a></li>',
  '  <li><a href="#s445">4.4.5 Mejora del análisis situacional tras la aplicación de la metodología</a></li>\n  <li><a href="#s446">4.4.6 Síntesis de los resultados</a></li>'
);
html = html.replace(
  'para finalizar con la comparación entre ambos y la síntesis de los principales hallazgos.',
  'para finalizar con la comparación entre ambos, la mejora del análisis situacional y la síntesis de los principales hallazgos.'
);

// Insercion del apartado nuevo antes de la sintesis.
html = html.replace('<!-- ══════════ 4.4.6 ══════════ -->', seccion);

fs.writeFileSync(destino, html, 'utf8');
console.log('cap4-nuevo.html actualizado: ' + antes + ' -> ' + html.length + ' bytes');
