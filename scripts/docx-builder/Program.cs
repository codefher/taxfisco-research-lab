using Builder;
using DocumentFormat.OpenXml.Packaging;

// ─────────────────────────────────────────────────────────────────────────────
// Genera el capitulo de resultados en Word a partir de los datos verificados
// del tablero integrado. Backend S: OpenXML directo, porque el CLI del skill
// no admite tablas ni imagenes.
// ─────────────────────────────────────────────────────────────────────────────

var raiz = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "..", ".."));
if (!File.Exists(Path.Combine(raiz, "resultados-prototipos", "dashboard-resultados-integrado.html")))
    raiz = Directory.GetCurrentDirectory();

var salida = Path.Combine(raiz, "resultados-prototipos", "capitulo-4-resultados.docx");
var imagenes = Path.Combine(raiz, "resultados-prototipos", "evidencia-visual");

var (doc, main, body) = Scaffold.Create(salida, "Metodología Honeypot en servicios fiscales");
var ctx = new Ctx { Main = main, Body = body, ImageDir = imagenes };

const int ANCHO = 576;   // 6.0 pulgadas: cabe en la columna de texto de Carta y de A4
const int ANCHO_AUX = 420; // ancho de los graficos auxiliares

void P(string texto) => body.Append(ctx.P(texto));
void Sec(int n, string titulo) => body.Append(ctx.Heading(n + ". " + titulo, 1));
void Sub(string titulo) => body.Append(ctx.Heading(titulo, 2));

void Fig(int n, string archivo, string titulo, string nota, int ancho, string alt)
{
    ctx.FigureTitle(n, titulo);
    ctx.FigureImage(archivo, n, alt, ancho);
    ctx.FigureNote(nota);
}

void Tbl(int n, string titulo, string[] cabeceras, string[][] filas, int[] anchos,
         string nota, bool[] derecha = null)
{
    ctx.TableTitle(n, titulo);
    ctx.Table(cabeceras, filas, anchos, derecha);
    ctx.TableNote(nota);
}

// ── Portada ────────────────────────────────────────────────────────────────
ctx.Cover("Metodología Honeypot para la Gestión de Incidentes en Servicios Fiscales conforme a Normas Internacionales", title: true);
ctx.Cover("Tesis de maestría");
ctx.Cover("");
ctx.Cover("Capítulo IV. Marco Práctico");
ctx.Cover("Resultados de la aplicación de la metodología Honeypot en dos laboratorios de servicios fiscales", bold: true);
ctx.Cover("");
ctx.Cover("Laboratorio TaxFisco Research Lab y laboratorio del Servicio de Impuestos Nacionales");
ctx.Cover("2026");
ctx.PageBreak();

// ── Tabla de contenido ─────────────────────────────────────────────────────
body.Append(ctx.Heading("Tabla de contenido", 1));
ctx.Toc(new List<(string, int)>
{
    ("Resumen del capítulo", 3),
    ("1. Alcance del capítulo y forma de leer los resultados", 4),
    ("2. Resultados del Prototipo 1 en el laboratorio TaxFisco", 6),
    ("3. El puente entre los dos laboratorios", 16),
    ("4. Las dos vueltas del laboratorio del Prototipo 2", 17),
    ("5. Tiempo de detección por escenario en el Prototipo 2", 21),
    ("6. Distribución del tiempo de detección en la medición final", 22),
    ("7. Ciclo de iteraciones del segundo laboratorio", 23),
    ("8. Cobertura de MITRE ATT&CK", 25),
    ("9. Aportación de cada fase de la metodología", 26),
    ("10. Registro de lecciones aprendidas", 28),
    ("11. Volumen de actividad de los dos laboratorios", 30),
    ("12. Síntesis de los resultados", 32),
    ("13. Evidencia visual de los tableros", 33),
    ("14. Naturaleza del dato y trazabilidad de la medición", 36),
    ("Referencias", 37),
});
ctx.PageBreak();

// ── Resumen ────────────────────────────────────────────────────────────────
body.Append(ctx.Heading("Resumen del capítulo", 1));
P("Este capítulo expone los resultados de dos aplicaciones de la metodología Honeypot orientada a la gestión de incidentes en servicios fiscales. La primera aplicación se desarrolla en el TaxFisco Research Lab, que opera sobre una entidad homologada del rubro de los servicios fiscales digitales, mientras que la segunda se aplica en el laboratorio del Servicio de Impuestos Nacionales.");
P("Los resultados se organizan en tres bloques de datos que responden a preguntas distintas y que no comparten escala entre sí. El primero recoge la madurez declarada por la organización antes de la intervención, de manera que funciona como diagnóstico previo, mientras que los otros dos miden qué detecta y qué ejecuta cada laboratorio y exigen una lectura autónoma basada en la evidencia que el propio ejercicio produce.");
P("La comparación principal del capítulo se concentra en el antes y el después de cada prototipo medido por resultado verificado. El primer laboratorio documenta el punto de partida de la cadena de detección y el segundo muestra el efecto de la corrección iterativa, de manera que cada indicador se lea contra el momento que lo precede y la comparación se apoye en el archivo de evidencia que la sostiene.");
P("Los apartados sobre el Prototipo 1 documentan la verificación de la cadena de detección y la corrección que el Prototipo 2 aplica sobre ella. Otros cuatro apartados describen la medición posterior del segundo laboratorio, su cobertura, sus tiempos de detección y el ciclo de iteraciones que la sostiene. Cuatro apartados más abordan la cobertura de técnicas, la aportación de cada fase de la metodología, el registro de lecciones aprendidas y el volumen de actividad registrado.");
P("El capítulo se cierra con la síntesis de los resultados, con la evidencia visual de los tres tableros y con la explicación de la naturaleza del dato y su trazabilidad. Ninguna cifra del capítulo es estimada, completada por analogía ni tomada de una fuente distinta de la que el texto declara junto a la tabla correspondiente.");
P("Cada apartado declara el denominador de sus indicadores y la procedencia de su evidencia, de manera que el lector pueda reconstruir cualquier cifra desde su archivo de origen. Las condiciones de medición, la cobertura normativa y el origen de cada resultado figuran en tablas que remiten al archivo correspondiente del repositorio.");

// ── 1. Alcance ─────────────────────────────────────────────────────────────
Sec(1, "Alcance del capítulo y forma de leer los resultados");
P("La lectura de los resultados exige separar el marco de la medición, porque el capítulo reúne datos que provienen de instrumentos distintos y que se interpretan con reglas distintas. La Tabla 1 identifica los tres bloques, declara qué mide cada uno y señala el archivo del que proceden, lo que permite al lector rastrear el origen de cualquier cifra que encuentre más adelante.");
Tbl(1, "Bloques de datos del capítulo, unidad de medida y origen",
    new[] { "Bloque", "Qué mide", "Archivo de origen", "Naturaleza del dato" },
    new[]
    {
        new[] { "Línea base institucional", "Madurez declarada por la organización antes de la intervención", "2026-06-25_Calculo_Alfa_Cronbach_Encuesta_v05.xlsx, hoja «Resultados de madurez»", "Medida sobre treinta respondentes reales, alfa de Cronbach 0,868989" },
        new[] { "Prototipo 1", "Ejecución instrumentada en el laboratorio TaxFisco", "evidencias/07-metricas/ y evidencias/03-aislamiento-red/", "Verificada sobre archivos de evidencia" },
        new[] { "Prototipo 2", "Ejecución instrumentada en el laboratorio del Servicio de Impuestos Nacionales", "evidencias/v2.0-it1/ y evidencias/v2.1-it2/", "Verificada sobre archivos de evidencia" },
    },
    new[] { 1900, 2400, 2800, 2260 },
    "La muestra de la línea base institucional comprende treinta respondentes, veinte del Servicio de Impuestos Nacionales y diez de Libélula. Los bloques de los dos prototipos proceden de los archivos de evidencia del repositorio, verificados escenario por escenario.");
P("La Tabla 2 recoge las fuentes de resultado que el capítulo declara, de manera que el lector sepa qué respalda cada cifra y con qué grado de detalle puede reconstruirla. Las tres filas proceden de la ejecución instrumentada en los dos laboratorios.");
Tbl(2, "Fuentes de resultado que declara el capítulo",
    new[] { "Fuente", "Resultado", "Naturaleza del dato", "Respaldo disponible" },
    new[]
    {
        new[] { "Laboratorio · Prototipo 1", "9 de 10 escenarios medidos", "Ejecución verificada sobre archivos de evidencia", "Reporte de indicadores y reporte de cobertura de técnicas" },
        new[] { "Laboratorio · Prototipo 2", "10 de 10 escenarios medidos", "Ejecución verificada sobre archivos de evidencia", "Reportes de indicadores de las dos iteraciones" },
        new[] { "Laboratorio · Prototipo 2", "Percentil 95 de 9,266 s", "Ejecución verificada sobre archivos de evidencia", "Reporte de indicadores de la segunda iteración" },
    },
    new[] { 2500, 1900, 2600, 2360 },
    "Las tres filas proceden de la ejecución instrumentada en los laboratorios. No comparten escala ni unidad de medida entre sí, de manera que la relación entre ellas se resuelve por función y no por magnitud. Los datos proceden de los reportes de indicadores de los dos prototipos.",
    new[] { false, true, false, false });
P("La lectura de los resultados obedece a dos reglas que separan los bloques de datos según la naturaleza de la medida que cada uno contiene. La primera establece que el bloque institucional responde a la pregunta de cuánto mide la organización antes de la intervención, de manera que funciona como diagnóstico y no como resultado de la metodología, mientras que la segunda establece que los dos bloques de laboratorio responden a la pregunta de qué detecta y qué ejecuta el señuelo y no comparten eje con el anterior.");
P("El tablero que acompaña este capítulo respeta esa separación y presenta cada bloque en un apartado propio, enlazados por la metodología que los une. La verificación escenario por escenario, que ocurre dentro de cada laboratorio, constituye el nexo que permite leer los tres bloques como un cuerpo único de resultados.");

// ── 4. Prototipo 1 ─────────────────────────────────────────────────────────
Sec(2, "Resultados del Prototipo 1 en el laboratorio TaxFisco");
P("El primer laboratorio comprueba que cada componente de la cadena de detección opera por separado, para lo que su señuelo sigue la clasificación de señuelos de producción que describe Spitzner (2003) y responde al atacante como si sus servicios fueran reales. El ejercicio ejecuta una sola medición, registrada el catorce de septiembre de 2026, de manera que no existe comparación interna entre dos vueltas.");
P("La Tabla 3 declara las condiciones en que se produjo esa medición, de manera que el lector conozca el laboratorio, la entidad, el método de cálculo y el alcance de la campaña antes de leer los tiempos.");
Tbl(3, "Condiciones de la medición del Prototipo 1",
    new[] { "Condición", "Valor" },
    new[]
    {
        new[] { "Laboratorio", "TaxFisco Research Lab" },
        new[] { "Entidad", "Homologada del rubro de servicios fiscales digitales" },
        new[] { "Fecha del reporte", "14 de septiembre de 2026, 07:31:44 UTC" },
        new[] { "Método de cálculo", "Tiempo desde el inicio del escenario hasta el primer evento que lo registra" },
        new[] { "Escenarios ejecutados", "10" },
        new[] { "Escenarios con medición", "9" },
        new[] { "Duración del ciclo de medición", "Una sola vuelta, con la evidencia de la ejecución completa y verificada" },
    },
    new[] { 3000, 6360 },
    "Las condiciones proceden del reporte de indicadores del Prototipo 1, archivo evidencias/07-metricas/07_kpi-report.json. La fecha y la hora se expresan en tiempo universal y corresponden al registro del reporte. El método de cálculo sitúa el instante inicial en el arranque de cada escenario y el instante final en el primer evento que registra una fuente.",
    new[] { false, false });
P("La Figura 1 reúne los ocho indicadores del primer laboratorio, de manera que el lector vea de una sola vez la cobertura de la campaña, la velocidad de la detección, la calidad de la evidencia y el despliegue de la red.");
Fig(1, "integrado-03-prototipo-1-indicadores.png", "Indicadores del Prototipo 1 en una sola vista",
    "Las tarjetas recogen los escenarios ejecutados y medidos, la detección típica por mediana, la detección por debajo de un minuto, las técnicas y las tácticas con detección, la calidad de la evidencia y los segmentos de red verificados. Los datos proceden del reporte de indicadores del Prototipo 1.",
    ANCHO, "Tarjetas con los ocho indicadores del Prototipo 1, desde los escenarios ejecutados hasta los segmentos de red verificados.");
P("Diez escenarios se ejecutan y nueve de ellos alcanzan medición, de manera que la campaña cubre el conjunto de técnicas que activa. La detección típica se sitúa en 0,826 segundos de mediana, mientras que la media de los nueve valores alcanza 41,598 segundos. Los dos escenarios de larga duración elevan esa media sin alterar la lectura del comportamiento típico del laboratorio.");
P("Cinco escenarios se resuelven por debajo de un segundo y siete por debajo de un minuto, de manera que la velocidad de la cadena se concentra en el rango corto. La Tabla 4 recoge el tiempo de cada escenario junto con la fuente que lo registra, mientras que la Figura 2 presenta esa misma información en orden de duración.");
Fig(2, "d-tiempo-prototipo-1.png", "Tiempo de detección de los nueve escenarios medidos en el Prototipo 1",
    "Cada barra representa el tiempo de detección de un escenario del Prototipo 1, expresado en segundos. El escenario S10 no produjo tiempo de detección en esta ejecución.",
    ANCHO, "Tiempo de detección de los nueve escenarios medidos del Prototipo 1 en segundos.");
Tbl(4, "Tiempo de detección por escenario en el Prototipo 1 y fuente que lo registra",
    new[] { "Escenario", "Técnica", "Tiempo", "Fuente que lo registra" },
    new[]
    {
        new[] { "S01 · Reconocimiento activo",        "T1595",     "16,405 s", "Interfaz de servicios, vista del atacante" },
        new[] { "S02 · Escaneo web",                   "T1595.002", "0,826 s",  "Portal del señuelo" },
        new[] { "S03 · Fuerza bruta por acceso remoto","T1110.001", "85,000 s", "Emulador de acceso remoto" },
        new[] { "S04 · Inyección de consultas",        "T1190",     "260,108 s","Interfaz de servicios" },
        new[] { "S05 · Suplantación de credenciales",  "T1110.004", "0,141 s",  "Interfaz de servicios" },
        new[] { "S06 · Inyección en el navegador",     "T1059.007", "0,824 s",  "Interfaz de servicios" },
        new[] { "S07 · Abuso de la interfaz",           "T1078",     "0,543 s",  "Interfaz de servicios, registro de ruta" },
        new[] { "S08 · Depósito de archivo",           "T1105",     "0,533 s",  "Interfaz de servicios, registro de ruta" },
        new[] { "S09 · Conexión inversa",              "T1059.004", "10,000 s", "Emulador de acceso remoto" },
        new[] { "S10 · Exfiltración por nombres de dominio", "T1048.003", "Fuera de la medición", "Ninguna fuente lo registró" },
    },
    new[] { 3100, 1300, 1600, 3360 },
    "El tiempo de detección se expresa en segundos y corresponde al intervalo entre el inicio del escenario y la primera señal registrada. El escenario S10 no produjo tiempo de detección en esta ejecución, porque el cálculo consultaba tres fuentes y ninguna leía el tráfico DNS. Los datos proceden del reporte de indicadores del Prototipo 1, archivo evidencias/07-metricas/07_kpi-report.json.",
    new[] { false, true, true, false });
P("La Tabla 5 agrupa los nueve escenarios medidos por tramo de duración, de manera que el lector comprueba que el comportamiento típico del laboratorio se sitúa por debajo de un segundo. La Tabla 6 muestra los cinco componentes que registran la detección, de manera que cada fila indica cuántos de los nueve escenarios medidos aporta cada componente a la cadena de alerta.");
Fig(3, "d-distribucion-tiempo-1.png", "Distribución del tiempo de detección de los nueve escenarios medidos del Prototipo 1",
    "El histograma agrupa los nueve escenarios medidos del Prototipo 1 por tramo de duración. Los tramos reproducen los tiempos de la Tabla 4.",
    ANCHO_AUX, "Histograma de los nueve escenarios medidos del Prototipo 1 por tramo de duración.");
Tbl(5, "Distribución del tiempo de detección de los nueve escenarios medidos del Prototipo 1",
    new[] { "Tramo de duración", "Escenarios", "Identificación de los escenarios" },
    new[]
    {
        new[] { "Por debajo de un segundo",     "5", "S02, S05, S06, S07, S08" },
        new[] { "De uno a diez segundos",        "1", "S09" },
        new[] { "De diez a sesenta segundos",    "1", "S01" },
        new[] { "Más de sesenta segundos",      "2", "S03, S04" },
        new[] { "Total de escenarios medidos",  "9", "S01 a S09" },
    },
    new[] { 2700, 1300, 5360 },
    "Los tramos agrupan los nueve escenarios que alcanzaron medición en el Prototipo 1. El tramo de uno a diez segundos incluye el valor de 10,000 segundos. La mediana de 0,826 segundos y la media de 41,598 segundos son cálculos propios sobre los nueve valores declarados. Los datos proceden del reporte de indicadores del Prototipo 1.",
    new[] { false, true, false });
Fig(4, "d-componentes-deteccion.png", "Componentes que registran la detección en el Prototipo 1",
    "Cada barra indica cuántos de los nueve escenarios medidos aporta cada componente a la cadena de alerta. Los cinco componentes cubren los nueve escenarios sin solapamiento.",
    ANCHO_AUX, "Barras con el número de escenarios que aporta cada componente a la cadena de alerta.");
Tbl(6, "Componentes que registran la detección en los nueve escenarios medidos del Prototipo 1",
    new[] { "Componente que registra la detección", "Escenarios que cubre", "Cantidad" },
    new[]
    {
        new[] { "Interfaz de servicios",                    "S04, S05, S06",           "3" },
        new[] { "Interfaz de servicios con registro de ruta","S07, S08",                "2" },
        new[] { "Emulador de acceso remoto",                "S03, S09",                "2" },
        new[] { "Interfaz de servicios con vista del atacante","S01",                  "1" },
        new[] { "Portal del señuelo",                       "S02",                     "1" },
        new[] { "Total de escenarios medidos",              "S01 a S09",               "9" },
    },
    new[] { 3900, 3300, 2160 },
    "Cada fila agrupa los escenarios que comparten el mismo componente como fuente de registro, de manera que los nueve escenarios medidos se reparten entre las cinco categorías sin solapamiento. Los datos proceden del reporte de indicadores del Prototipo 1, archivo evidencias/07-metricas/07_kpi-report.json.",
    new[] { false, false, true });
P("El inventario del señuelo comprende diecisiete técnicas repartidas en ocho tácticas, mientras que la campaña activa diez de esas técnicas y cada escenario ejerce una distinta. La Figura 5 contrasta el inventario completo con las técnicas que un escenario activa, de manera que la cobertura se lee sin ambigüedad.");
Fig(5, "d-tecnicas-por-tactica.png", "Técnicas del inventario por táctica y técnicas activadas por la campaña",
    "La barra gris declara las técnicas que ofrece el inventario del señuelo y la barra verde las que activa un escenario de la campaña.",
    ANCHO_AUX, "Comparación por táctica entre las técnicas del inventario y las activadas por un escenario.");
Tbl(7, "Técnicas del inventario por táctica y técnicas activadas por la campaña",
    new[] { "Táctica", "En el inventario", "Activadas por un escenario" },
    new[]
    {
        new[] { "Execution",              "4", "2" },
        new[] { "Initial Access",         "3", "2" },
        new[] { "Reconnaissance",         "3", "2" },
        new[] { "Credential Access",      "2", "2" },
        new[] { "Collection",             "2", "0" },
        new[] { "Command and Control",    "1", "1" },
        new[] { "Discovery",              "1", "0" },
        new[] { "Exfiltration",           "1", "1" },
        new[] { "Total",                  "17", "10" },
    },
    new[] { 4000, 2680, 2680 },
    "La columna de técnicas activadas cuenta únicamente las técnicas que ejecuta un escenario de la campaña, no las que el inventario ofrece. La campaña ejecuta diez escenarios y cada uno ejerce una técnica distinta. Los datos proceden del archivo evidencias/07-metricas/08_mitre-coverage.json.",
    new[] { false, true, true });
P("El despliegue verificado distribuye treinta contenedores en cuatro segmentos separados, de manera que el señuelo expuesto no comparte segmento con la gestión ni con los sensores. La Tabla 8 declara la subred, el número de contenedores y la función de cada segmento, mientras que la Figura 6 presenta la misma distribución.");
Fig(6, "d-contenedores-por-segmento.png", "Contenedores desplegados en cada segmento de red del Prototipo 1",
    "La distribución de los treinta contenedores entre los cuatro segmentos verificados. Cada segmento declara su subred a la derecha de la barra.",
    ANCHO_AUX, "Barras con la cantidad de contenedores de cada segmento de red y su subred.");
Tbl(8, "Segmentación verificada del señuelo del Prototipo 1",
    new[] { "Red", "Subred", "Contenedores", "Función del segmento" },
    new[]
    {
        new[] { "taxfisco-dmz",      "10.20.0.0/24", "6",  "Segmento del señuelo expuesto" },
        new[] { "taxfisco-honeypot", "10.21.0.0/24", "3",  "Segmento interior del señuelo" },
        new[] { "taxfisco-soc",      "10.22.0.0/24", "19", "Segmento de gestión y análisis" },
        new[] { "taxfisco-ids",      "10.23.0.0/24", "2",  "Segmento de los sensores de red" },
        new[] { "Total",              "",              "30", "Cuatro segmentos verificados" },
    },
    new[] { 2100, 1750, 1450, 4060 },
    "Los segmentos de red se verifican sobre el archivo de subredes del despliegue. Las subredes corresponden a las redes declaradas en la composición efectiva del laboratorio. El segmento del señuelo expuesto no comparte red con la gestión ni con los sensores. Los datos proceden del archivo evidencias/03-aislamiento-red/02_subnets.txt.",
    new[] { false, false, true, false });
P("La cobertura normativa que el laboratorio sustenta figura en la Tabla 9, de manera que cada fase y cada control de las normas quede enlazado con el componente concreto que lo evidenció.");
Tbl(9, "Cobertura normativa que el laboratorio sustenta",
    new[] { "Marco", "Fase o control", "Evidencia en el laboratorio" },
    new[]
    {
        new[] { "ISO/IEC 27035", "Fase 1 · Planificar y preparar", "Gestor de eventos preconfigurado, plantillas de casos, flujos de orquestación, caceras previas y reglas propias de red" },
        new[] { "ISO/IEC 27035", "Fase 2 · Detección y reporte", "Reglas de correlación del gestor, firmas del motor de red, registros del sensor y señuelos instrumentados" },
        new[] { "ISO/IEC 27035", "Fase 3 · Evaluación y decisión", "Gestión de casos, analizadores de inteligencia, correlación de indicadores y flujos de enriquecimiento" },
        new[] { "ISO/IEC 27035", "Fase 4 · Respuesta", "Recetas de contención, caceras de aislamiento, distribución de indicadores y segmentación de redes" },
        new[] { "ISO/IEC 27035", "Fase 5 · Lecciones aprendidas", "Informes de cierre de caso, tablero de indicadores y actualización de reglas desde la observación" },
        new[] { "ISO/IEC 27001", "Controles de gestión de incidentes", "Planificación, evaluación, respuesta, aprendizaje y preservación de la evidencia" },
        new[] { "ISO/IEC 27001", "Controles de monitoreo y red", "Actividades de monitoreo y seguridad de las redes" },
    },
    new[] { 1700, 2600, 5060 },
    "Las cinco fases de ISO/IEC 27035 se corresponden con las cinco fases de la metodología que el laboratorio ejecuta, de manera que cada una de ellas queda respaldada por un componente verificable del entorno de laboratorio. Los controles de ISO/IEC 27001 cubren la gestión de incidentes y las actividades de monitoreo y seguridad de las redes. Los datos proceden de la composición verificada del despliegue del Prototipo 1.",
    new[] { false, false, false });
P("La Tabla 10 declara los diez indicadores del Prototipo 1 con lo que cada uno cuenta y con el denominador que lo sostiene, de manera que ninguna cifra del apartado se lea fuera del universo que la respalda.");
Tbl(10, "Los indicadores del Prototipo 1 y su denominador",
    new[] { "Indicador", "Qué cuenta", "Denominador", "Archivo de origen" },
    new[]
    {
        new[] { "Escenarios ejecutados", "Escenarios que la campaña lanza contra el señuelo", "Los diez escenarios que define la campaña", "Reporte de indicadores" },
        new[] { "Escenarios con medición", "Escenarios a los que el instrumental atribuye una detección y registra su hora", "Los diez escenarios que ejecuta la campaña", "Reporte de indicadores" },
        new[] { "Tiempo mediano de detección", "Valor que ordena los nueve tiempos medidos y toma el central", "Las nueve mediciones disponibles", "Reporte de indicadores" },
        new[] { "Tiempo medio de detección", "Promedio aritmético de los nueve tiempos medidos", "Las nueve mediciones disponibles", "Reporte de indicadores" },
        new[] { "Detección por debajo de un minuto", "Escenarios cuyo tiempo de detección no supera los sesenta segundos", "Los diez escenarios que ejecuta la campaña", "Reporte de indicadores" },
        new[] { "Técnicas con detección", "Técnicas que un escenario activa y que reciben fuente de atribución", "Las diez técnicas que activa la campaña", "Reporte de cobertura" },
        new[] { "Tácticas con detección", "Tácticas del marco que cubren esas técnicas", "Las seis tácticas que la campaña recorre", "Reporte de cobertura" },
        new[] { "Componentes que registran detección", "Componentes que dejan un registro legible por el calculador", "Los cinco declarados en el reporte", "Reporte de indicadores" },
        new[] { "Calidad de la evidencia", "Puntuación de integridad verificada sobre los archivos con huella", "Los sesenta y ocho archivos de evidencia", "Reporte de indicadores" },
        new[] { "Segmentos de red verificados", "Redes del señuelo con composición efectiva inspeccionada", "Las cuatro redes declaradas", "Captura de aislamiento" },
    },
    new[] { 2100, 3400, 2200, 1660 },
    "Los diez indicadores declaran el denominador con que se calculan. El tiempo mediano y el tiempo medio comparten denominador, porque los dos se calculan sobre las nueve mediciones disponibles. Los datos proceden del reporte de indicadores, del reporte de cobertura de técnicas y de la captura de aislamiento del Prototipo 1.",
    new[] { false, false, false, false });
P("El volumen registrado durante el ejercicio declara 8 875 peticiones recibidas por el portal del señuelo, 1 758 atendidas por la interfaz de servicios, 46 ataques registrados y 68 archivos de evidencia con huella verificada. La calidad de la evidencia alcanza 100 de 100, de manera que cada archivo conserva su validez forense.");
P("La Figura 7 presenta ese mismo volumen en forma de indicadores destacados, de manera que el lector perciba de inmediato la magnitud de la actividad capturada.");
Fig(7, "integrado-04-volumen-de-la-ejecucion.png", "Volumen de actividad registrada en la ejecución del Prototipo 1",
    "Las tarjetas declaran las peticiones recibidas por el portal del señuelo, las peticiones atendidas por la interfaz de servicios, los ataques registrados y los archivos de evidencia con huella verificada. Los datos proceden de los archivos de evidencia del Prototipo 1.",
    ANCHO, "Tarjetas con las peticiones del portal, las peticiones atendidas, los ataques registrados y los archivos de evidencia.");
Tbl(11, "Volumen de actividad registrado en la ejecución del Prototipo 1",
    new[] { "Indicador", "Valor" },
    new[]
    {
        new[] { "Peticiones recibidas por el portal del señuelo", "8 875" },
        new[] { "Peticiones atendidas por la interfaz de servicios", "1 758" },
        new[] { "Ataques registrados por el señuelo", "46" },
        new[] { "Conexiones capturadas por el emulador", "8" },
        new[] { "Archivos de evidencia con huella verificada", "68" },
        new[] { "Calidad de la evidencia verificada", "100 de 100" },
    },
    new[] { 6360, 3000 },
    "Los registros corresponden a la ejecución del Prototipo 1 del 14 de septiembre de 2026. La calidad de la evidencia se verifica sobre la huella de cada archivo conservado. Los datos proceden de los archivos de evidencia del Prototipo 1.",
    new[] { false, true });
P("La media de 41,598 segundos y la mediana de 0,826 segundos describen la misma medición desde dos planos distintos. La media la elevan dos escenarios de larga duración, la inyección de consultas con 260,108 segundos y la fuerza bruta por acceso remoto con 85 segundos, mientras que los otros siete escenarios se resuelven entre los 141 milisegundos y los 16,405 segundos.");
P("La mediana es un cálculo propio sobre los nueve valores que declara el reporte, de manera que no sustituye a ningún indicador publicado. El capítulo la emplea como titular porque describe el comportamiento típico de la cadena, mientras que la media queda como dato complementario en la tabla de referencia.");

// ── 5. El puente ───────────────────────────────────────────────────────────
Sec(3, "El puente entre los dos laboratorios");
P("Los dos prototipos se necesitan entre sí, de manera que cada uno cubre lo que el otro deja ver. El primero comprueba que cada componente opera por separado, mientras que el segundo comprueba qué mejora produce la corrección de los vacíos que el primero expone. La conexión más clara aparece en el escenario S10, que corresponde a la exfiltración por nombres de dominio.");
P("En el primer laboratorio ese escenario no produce tiempo de detección, porque el cálculo solo consulta tres fuentes y ninguna de ellas lee el tráfico DNS. El registro de lecciones del segundo laboratorio recoge el mismo hallazgo en la lección L14, cuya corrección incorpora la consulta DNS como fuente adicional, de manera que en la medición final ese escenario registra 0,646 segundos con el sensor de red como fuente.");
Tbl(12, "Escenarios que producen medición en los dos laboratorios",
    new[] { "Escenario", "Prototipo 1", "Prototipo 2, medición final", "Qué cambió" },
    new[]
    {
        new[] { "S10 · Exfiltración por nombres de dominio", "Fuera de la medición", "0,646 s",  "La fuente DNS del sensor de red entra en el cálculo" },
        new[] { "S08 · Depósito de archivo",                  "0,533 s",             "0,562 s",  "El archivo señuelo pasa a ser fuente propia" },
        new[] { "S09 · Conexión inversa",                     "10,000 s",            "0,000 s",  "El emulador de acceso remoto queda verificado desde el arranque" },
    },
    new[] { 2800, 1700, 1900, 2960 },
    "Los tiempos de S08 y S09 son comparables porque el mismo escenario produce una medición en los dos laboratorios. Los tiempos medios no son comparables, porque el primer laboratorio promedia nueve escenarios y el segundo promedia diez.",
    new[] { false, true, true, false });
P("Los tiempos de S08 y S09 resultan comparables porque el mismo escenario produce una medición en los dos casos. El tiempo medio de cada laboratorio no resulta comparable, porque el primero promedia nueve escenarios y el segundo promedia diez, de manera que ese contraste mide el cambio de cobertura de la medición y no el cambio de velocidad de la detección.");

P("La comparación del antes y el después se mide por resultado verificado, de manera que cada indicador se lea contra el momento que lo precede y cada cambio tenga un archivo que lo sostenga. El primer prototipo se mide una sola vez, porque su objetivo de diseño consiste en comprobar que cada componente del sistema opera por separado antes de medir su efecto en conjunto, de manera que su estado inicial no admita una segunda medición propia.");
Tbl(13, "Antes y después del Prototipo 1 según los indicadores verificados en los dos laboratorios",
    new[] { "Indicador", "Momento inicial", "Momento final verificado", "Qué cambió" },
    new[]
    {
        new[] { "Escenarios con tiempo de detección registrado", "9 de 10", "10 de 10", "El escenario de exfiltración por nombres alcanza medición con el sensor de red" },
        new[] { "Técnicas de la campaña con fuente de detección", "10 de 10", "10 de 10", "Sin variación, la campaña conserva las diez técnicas con fuente" },
        new[] { "Tácticas con fuente de detección", "6 de 6", "6 de 6", "Sin variación, las seis tácticas conservan su fuente" },
        new[] { "Escenarios con detección inferior a 1 s", "5 de 9", "7 de 10", "La atribución instrumentada alcanza valores subsegundo en siete escenarios" },
        new[] { "Tiempo medio de detección", "41,598 s sobre 9 mediciones", "2,0219 s sobre 10 mediciones", "El promedio baja junto con la ampliación del conjunto medido" },
        new[] { "Detección mínima", "0,141 s", "0,000 s", "El mínimo llega a cero por dos detecciones en el instante de arranque" },
        new[] { "Percentil 95 del tiempo de detección", "No declarado", "9,266 s", "El primer reporte no declara el percentil, de manera que la comparación arranca en el segundo laboratorio" },
        new[] { "Lecciones aprendidas registradas y resueltas", "3", "14 de 14", "Las tres lecciones originan las reparaciones que el segundo laboratorio aplica" },
        new[] { "Fases de ISO/IEC 27035 sustentadas", "5 de 5", "1 de 5", "La lectura cambia de fuente, porque el verificador automático confirma una sola fase" },
        new[] { "Archivos de evidencia con huella verificada", "68", "91", "El segundo laboratorio captura veintitrés archivos adicionales" },
        new[] { "Calidad de la evidencia verificada", "100 de 100", "100 de 100", "Sin variación, la custodia mantiene la integridad verificada" },
    },
    new[] { 2500, 1800, 1800, 3260 },
    "El momento inicial del Prototipo 1 recoge la única ejecución disponible en el TaxFisco Research Lab, y el momento final verificado corresponde a la medición final del Prototipo 2, en la que se aplican las correcciones que las tres lecciones de la primera campaña originan. La fila de correspondencia normativa cambia de fuente, porque el valor de cinco de cinco procede de la revisión manual de correspondencia del primer laboratorio y el valor de una de cinco del verificador automático que los tres momentos comparten. Los once indicadores declaran su denominador y se leen contra los valores verificados en los apartados de resultados del Prototipo 1 y del Prototipo 2.",
    new[] { false, true, true, false });
P("Su estado final se verifica en el segundo laboratorio, porque allí se aplican las tres correcciones que sus tres lecciones originan, de manera que la comparación entre los dos prototipos se resuelve por el ciclo de la metodología y no por una repetición del ejercicio en el primer laboratorio.");
Tbl(14, "Antes y después del Prototipo 2 según los indicadores verificados en sus dos vueltas",
    new[] { "Indicador", "Momento inicial", "Momento final", "Qué cambió" },
    new[]
    {
        new[] { "Escenarios con tiempo de detección registrado", "4 de 10", "10 de 10", "El instrumental de atribución reparado alcanza los seis escenarios sin medición" },
        new[] { "Técnicas de la campaña con fuente de detección", "4 de 10", "10 de 10", "Seis técnicas que carecían de fuente la obtienen con el instrumental reparado" },
        new[] { "Tácticas con fuente de detección", "3 de 6", "6 de 6", "Las tres tácticas restantes alcanzan fuente con el instrumental reparado" },
        new[] { "Escenarios con detección inferior a 1 s", "0 de 10", "7 de 10", "La atribución instrumentada sitúa siete escenarios por debajo del segundo" },
        new[] { "Tiempo medio de detección", "5,2155 s sobre 4 mediciones", "2,0219 s sobre 10 mediciones", "El promedio baja al mismo tiempo que se amplía el conjunto medido" },
        new[] { "Detección mínima", "1,063 s", "0,000 s", "El mínimo llega a cero por dos detecciones en el instante de arranque" },
        new[] { "Percentil 95 del tiempo de detección", "14,583 s", "9,266 s", "El percentil 95 se reduce en 5,317 segundos" },
        new[] { "Lecciones aprendidas registradas y resueltas", "7 de 7", "14 de 14", "Las siete lecciones de la vuelta inicial se cierran y la medición final registra otras siete" },
        new[] { "Fases de ISO/IEC 27035 sustentadas", "1 de 5", "1 de 5", "Sin variación, el verificador automático confirma una sola fase" },
        new[] { "Archivos de evidencia con huella verificada", "91", "91", "Sin variación, la campaña conserva el volumen de custodia" },
        new[] { "Calidad de la evidencia verificada", "100 de 100", "100 de 100", "Sin variación, la custodia mantiene la integridad verificada" },
    },
    new[] { 2500, 1800, 1800, 3260 },
    "Las dos vueltas comparten el mismo señuelo, la misma campaña de diez escenarios y el mismo instrumental de custodia, de manera que la variación se atribuya a las once correcciones de instrumental y a las tres mitigaciones documentadas. Los once indicadores declaran su denominador y se leen contra los valores verificados en el apartado de las dos vueltas del Prototipo 2.",
    new[] { false, true, true, false });
P("Esa salvedad acota la lectura de la comparación, porque el estado final del primer prototipo se observa en otro laboratorio y con una campaña de mayor cobertura, de manera que la diferencia entre los dos momentos sea atribuible a la corrección del instrumental y no al cambio de escenario. Las dos tablas que cierran este apartado declaran los once indicadores de cada prototipo con su denominador, de manera que la comparación se pueda leer sin buscar la cifra en otro lugar. La comparación del Prototipo 2 no arrastra esa salvedad, porque sus dos vueltas comparten el mismo señuelo, la misma campaña de diez escenarios y el mismo instrumental de custodia, de manera que la variación se atribuya a las once correcciones de instrumental y a las tres mitigaciones documentadas.");

// ── 6. Prototipo 2 ─────────────────────────────────────────────────────────
Sec(4, "Las dos vueltas del laboratorio del Prototipo 2");
P("El segundo laboratorio comprueba qué produce la metodología cuando se aplica por segunda vez sobre el mismo señuelo. El señuelo ejecuta los mismos diez escenarios en las dos vueltas con las mismas técnicas, de manera que la diferencia entre las columnas corresponde al trabajo de la metodología y no a un cambio de instrumentación.");
P("Seis indicadores cambian entre la vuelta 1 y la medición posterior, mientras que cuatro permanecen constantes en las dos vueltas del ejercicio. Los escenarios con medición pasan de cuatro a diez, lo mismo que ocurre con las técnicas que cuentan con fuente de detección, de manera que las fuentes de registro pasan de tres a seis al igual que las tácticas con fuente asignada.");
Fig(8, "f-cobertura-prototipo-2.png", "Cobertura de la medición en la vuelta 1 y en la medición final del Prototipo 2",
    "Cada par de barras compara la vuelta 1 con la medición final del Prototipo 2. La cobertura de medición pasa de cuatro a diez escenarios.",
    ANCHO_AUX, "Comparación de la cobertura de medición entre la vuelta 1 y la medición final.");
Tbl(15, "Lectura del cambio entre las dos vueltas del Prototipo 2",
    new[] { "Indicador", "Vuelta 1", "Medición final", "Cambio" },
    new[]
    {
        new[] { "Escenarios con tiempo medido",        "4",       "10",  "+6" },
        new[] { "Fuentes de registro",                "3",       "6",   "+3" },
        new[] { "Técnicas con fuente de detección",   "4",       "10",  "+6" },
        new[] { "Tácticas con fuente de detección",   "3",       "6",   "+3" },
        new[] { "Percentil 95 de detección",          "14,583 s", "9,266 s", "−5,317 s" },
        new[] { "Lecciones cerradas",                 "7",       "14",  "+7" },
        new[] { "Escenarios ejecutados",              "10",      "10",  "=" },
        new[] { "Técnicas del inventario",            "17",      "17",  "=" },
        new[] { "Archivos de evidencia",              "91",      "91",  "=" },
        new[] { "Calidad de la evidencia",            "100",     "100", "=" },
    },
    new[] { 4560, 1600, 1900, 1300 },
    "Las filas con cambio corresponden a los indicadores que dependen del instrumental de medición, mientras que las filas con signo igual corresponden a los indicadores que permanecen constantes en las dos vueltas. El percentil 95 se calcula sobre los valores de origen con tres decimales. Los datos proceden de los reportes de indicadores de las dos vueltas del Prototipo 2.",
    new[] { false, true, true, true });
P("Los cuatro indicadores constantes constituyen la prueba de que la diferencia procede de la corrección del instrumental, de manera que un cambio en el volumen de evidencia o en el catálogo de amenazas habría producido una comparación sin control y la igualdad de esas cuatro variables sostiene la lectura de las seis que cambian.");
P("El percentil 95 de detección desciende de 14,583 a 9,266 segundos, lo que supone una reducción de 5,317 segundos y confirma que la mejora se sostiene en la cola de la distribución y no solo en el promedio. El registro de lecciones aprendidas pasa de siete a catorce entradas cerradas, de manera que la segunda vuelta incorpora la corrección de todo lo que la primera dejó ver.");
P("La Figura 9 muestra qué componente registra la detección de cada escenario en las dos vueltas, de manera que la ampliación de la cobertura se lea como un efecto directo sobre las fuentes de registro.");
Fig(9, "f-fuentes-que-registran-deteccion.png", "Componentes que registran la detección en la vuelta 1 y en la medición final del Prototipo 2",
    "Cada barra compara el número de escenarios que registra cada componente en la vuelta 1 y en la medición final. Los componentes añadidos durante el ciclo son el emulador de acceso remoto, el archivo señuelo y el sensor de red.",
    ANCHO, "Comparación de los seis componentes que registran detección en la vuelta 1 y en la medición final.");
P("Los tres componentes que se añaden durante el ciclo son el emulador de acceso remoto, el archivo señuelo y el sensor de red, de manera que cada corrección de la fase de detección aparece como una fuente nueva en la medición final. El portal del señuelo pasa de un escenario a tres, porque en la medición final registra el escaneo web, la inyección de consultas y la inyección en el navegador.");
P("La Tabla 16 declara los ocho indicadores del Prototipo 2 con su denominador, de manera que la comparación entre las dos vueltas se lea sobre un universo estable de diez escenarios.");
Tbl(16, "Los indicadores del Prototipo 2 y su denominador",
    new[] { "Indicador", "Qué cuenta", "Denominador", "Archivo de origen" },
    new[]
    {
        new[] { "Escenarios con medición", "Escenarios de la campaña a los que el instrumental atribuye una detección y registra su hora", "Los diez escenarios que ejecuta cada vuelta", "Reporte de indicadores de cada vuelta" },
        new[] { "Componentes que registran detección", "Componentes que dejan un registro legible por el calculador", "Los seis componentes desplegados", "Reporte de indicadores" },
        new[] { "Técnicas con detección", "Técnicas que un escenario activa y que reciben fuente de atribución", "Las diez técnicas que activa la campaña", "Reporte de cobertura de técnicas" },
        new[] { "Tácticas con detección", "Tácticas del marco que cubren esas técnicas", "Las seis tácticas que la campaña recorre", "Reporte de cobertura de técnicas" },
        new[] { "Percentil 95 de detección", "Percentil 95 de la distribución de los tiempos de detección", "Los diez tiempos de cada vuelta", "Reporte de indicadores" },
        new[] { "Tiempo medio de detección", "Promedio aritmético de los tiempos de detección", "Cuatro tiempos en la línea base y diez en la medición final", "Reporte de indicadores" },
        new[] { "Ciclo de corrección", "Tiempo transcurrido entre las dos mediciones", "No aplica, porque es una duración", "Marcas de tiempo de ambos reportes" },
        new[] { "Lecciones resueltas", "Hallazgos con una resolución documentada, por corrección o por mitigación", "Las catorce lecciones registradas", "Registro de lecciones aprendidas" },
    },
    new[] { 2100, 3400, 2200, 1660 },
    "Los ocho indicadores declaran el denominador con que se calculan. El tiempo medio es el único indicador cuyo denominador cambia entre las dos vueltas, porque promedia cuatro tiempos en la línea base y diez en la medición final. Los datos proceden de los reportes de indicadores, del reporte de cobertura de técnicas y del registro de lecciones aprendidas del Prototipo 2.",
    new[] { false, false, false, false });

// ── 7. Tiempo por escenario ────────────────────────────────────────────────
Sec(5, "Tiempo de detección por escenario en el Prototipo 2");
P("Solo cuatro escenarios conservan medición en las dos vueltas, de manera que esos cuatro constituyen la base comparable. Los otros seis amplían la cobertura en la medición final y se listan aparte con la fuente que registra cada uno, mientras que la Figura 10 presenta la comparación de los cuatro escenarios medidos en ambas vueltas.");
Fig(10, "g-tiempo-escenarios-comparables.png", "Tiempo de detección de los cuatro escenarios medidos en las dos vueltas del Prototipo 2",
    "Las barras grises corresponden a la vuelta 1 y las verdes a la medición final. La cifra de la derecha es la reducción porcentual de cada escenario.",
    ANCHO, "Comparación de los cuatro escenarios medidos en ambas vueltas, con la reducción porcentual a la derecha.");
Tbl(17, "Escenarios que conservan medición en las dos vueltas del Prototipo 2",
    new[] { "Escenario", "Técnica", "Vuelta 1", "Medición final", "Reducción", "Origen del dato" },
    new[]
    {
        new[] { "S01 · Reconocimiento activo",       "T1595",     "16,851 s", "15,910 s", "5,6 %",  "Interfaz de servicios del atacante" },
        new[] { "S02 · Escaneo web",                  "T1595.002", "1,214 s",  "1,095 s",  "9,8 %",  "Portal del señuelo" },
        new[] { "S05 · Suplantación de credenciales", "T1110.004", "1,734 s",  "1,145 s",  "34,0 %", "Interfaz de servicios del señuelo" },
        new[] { "S07 · Abuso de la interfaz",          "T1078",     "1,063 s",  "0,264 s",  "75,2 %", "Interfaz de servicios del señuelo" },
    },
    new[] { 2400, 1150, 1200, 1400, 1100, 2110 },
    "La reducción se calcula sobre los valores de origen con tres decimales, no sobre los valores redondeados de la tabla. Solo cuatro escenarios conservan medición en las dos vueltas, de manera que la comparación se sostiene en el escenario y no en el promedio. Los datos proceden de los reportes de indicadores de las dos vueltas del Prototipo 2.",
    new[] { false, true, true, true, true, false });
P("La reducción más marcada corresponde al abuso de la interfaz, que pasa de 1,063 a 0,264 segundos, con una reducción del 75,2 %. El reconocimiento activo obtiene la menor reducción, con un 5,6 %, porque su primer evento tarda en llegar al señuelo a través de la red, mientras que la Tabla 18 recoge los seis escenarios que amplían la cobertura.");
Tbl(18, "Escenarios que amplían la cobertura de medición en la medición final del Prototipo 2",
    new[] { "Escenario", "Técnica", "Vuelta 1", "Medición final", "Fuente que lo registra" },
    new[]
    {
        new[] { "S03 · Fuerza bruta por acceso remoto", "T1110.001", "Fuera de la referencia", "0,000 s", "Emulador de acceso remoto" },
        new[] { "S04 · Inyección de consultas",         "T1190",     "Fuera de la referencia", "0,137 s", "Portal del señuelo" },
        new[] { "S06 · Inyección en el navegador",      "T1059.007", "Fuera de la referencia", "0,460 s", "Portal del señuelo" },
        new[] { "S08 · Depósito de archivo",            "T1105",     "Fuera de la referencia", "0,562 s", "Archivo señuelo" },
        new[] { "S09 · Conexión inversa",               "T1059.004", "Fuera de la referencia", "0,000 s", "Emulador de acceso remoto" },
        new[] { "S10 · Exfiltración por nombres de dominio", "T1048.003", "Fuera de la referencia", "0,646 s", "Sensor de red" },
    },
    new[] { 2600, 1200, 1700, 1400, 2460 },
    "Los seis escenarios que amplían la cobertura no tienen valor de referencia en la vuelta 1, de manera que la tabla no les asigna ese dato. Los valores de 0,000 segundos corresponden a detecciones registradas en el mismo segundo del arranque del escenario.",
    new[] { false, true, false, true, false });
P("El señuelo captura los diez escenarios en las dos vueltas, de manera que lo que se amplía es la cobertura de la medición y no la captura de la actividad del atacante. Los dos valores de 0,000 segundos delatan que la cadena de registro opera desde el inicio de la campaña, de manera que la cobertura final no depende de una activación tardía de los sensores.");

// ── 8. Distribución final ──────────────────────────────────────────────────
Sec(6, "Distribución del tiempo de detección en la medición final");
P("La distribución del tiempo de detección describe el conjunto de los diez escenarios del segundo laboratorio, de manera que la lectura del comportamiento global no dependa de un caso aislado. La Tabla 19 agrupa los escenarios por tramo de tiempo y la Figura 11 presenta esa misma agrupación en forma de gráfico.");
Fig(11, "h-distribucion-tiempo-final.png", "Distribución del tiempo de detección de los diez escenarios de la medición final",
    "El histograma agrupa los diez escenarios de la medición final por tramo de tiempo. Los tramos reproducen los tiempos de la tabla del apartado sobre el tiempo de detección por escenario.",
    ANCHO, "Histograma de los diez escenarios de la medición final agrupados por tramo de tiempo.");
Tbl(19, "Distribución del tiempo de detección de los diez escenarios de la medición final",
    new[] { "Tramo de tiempo", "Escenarios", "Identificación de los escenarios" },
    new[]
    {
        new[] { "Por debajo de 0,2 segundos",   "3", "S03, S04, S09" },
        new[] { "De 0,2 a 0,5 segundos",         "2", "S06, S07" },
        new[] { "De 0,5 a 1,0 segundos",         "2", "S08, S10" },
        new[] { "De 1,0 a 2,0 segundos",         "2", "S02, S05" },
        new[] { "Más de 2,0 segundos",           "1", "S01" },
        new[] { "Total de escenarios medidos",   "10", "S01 a S10" },
    },
    new[] { 2700, 1300, 5360 },
    "Los tramos reproducen los diez tiempos de la medición final que declara el reporte de indicadores. El percentil 95 de esa medición es 9,266 segundos. Los datos proceden del reporte de indicadores de la medición final del Prototipo 2.",
    new[] { false, true, false });
P("Siete de los diez escenarios se detectan por debajo de un segundo, de manera que la cadena resuelve la mayor parte de la campaña en el rango inferior al segundo. Los dos escenarios más lentos son el reconocimiento activo con 15,910 segundos y la suplantación de credenciales con 1,145 segundos. El reconocimiento activo tarda más porque el primer evento del atacante llega al señuelo a través de la red.");

// ── 9. Ciclo de iteraciones ────────────────────────────────────────────────
Sec(7, "Ciclo de iteraciones del segundo laboratorio");
P("La metodología se aplica dos veces sobre el mismo señuelo, de manera que la segunda vuelta mide el efecto de las correcciones que la primera origina. La Figura 12 sitúa los cinco hitos del ciclo sobre una línea de tiempo, mientras que la Tabla 20 los detalla con su momento, su contenido y la evidencia que los respalda.");
Fig(12, "i-ciclo-iteraciones.png", "Ciclo de iteraciones del laboratorio del Prototipo 2",
    "La línea de tiempo sitúa los cinco hitos del ciclo de corrección, desde la vuelta 1 hasta la medición final.",
    ANCHO, "Línea de tiempo con los cinco hitos del ciclo de iteraciones del Prototipo 2.");
Tbl(20, "Hitos del ciclo de iteraciones del Prototipo 2",
    new[] { "Hito", "Momento", "Qué ocurrió", "Evidencia" },
    new[]
    {
        new[] { "Medición de la vuelta 1",         "4 oct 2026 · 16:07 UTC", "Diez escenarios ejecutados, medición en cuatro de ellos", "Reporte de indicadores de la vuelta 1" },
        new[] { "Cadena de alertas e indexación",  "4 oct 2026 · 16:08 UTC", "Publicador propio operativo, tablero con datos reales", "Commits 20ee788 y 2d13573" },
        new[] { "Reinicio de la posición de lectura","4 oct 2026 · 16:17 UTC", "Motor de red estable para la lectura del tráfico", "Registro de la cadena de alertas" },
        new[] { "Registro de lecciones cerrado",    "4 oct 2026 · 18:32 UTC", "Catorce lecciones con hallazgo, causa raíz y mejora aplicada", "Registro de lecciones aprendidas" },
        new[] { "Medición posterior",              "4 oct 2026 · 20:33 UTC", "Diez escenarios ejecutados, medición en los diez", "Reporte de indicadores de la vuelta 2" },
        new[] { "Duración total del ciclo",        "4 h 26 min", "De la vuelta 1 a la medición final", "Marcas de ambos reportes" },
    },
    new[] { 2300, 1800, 2900, 2360 },
    "Los momentos corresponden al tiempo universal, registrado en las marcas de los dos reportes de indicadores. La duración total se obtiene de la diferencia entre la primera y la última marca.");
P("La primera medición del ciclo produce el conjunto de catorce lecciones que origina las correcciones, de manera que la cadena de mejora se apoya en evidencia y no en intuición. El ciclo completo, desde la línea base hasta la medición final, toma cuatro horas con veintiséis minutos, de manera que el esquema de iteración resulta operable dentro de una sola jornada de trabajo.");

// ── 10. MITRE ATT&CK ───────────────────────────────────────────────────────
Sec(8, "Cobertura de MITRE ATT&CK");
P("El inventario del señuelo sigue la taxonomía de MITRE ATT&CK (MITRE Corporation, 2024), que clasifica las técnicas en ocho tácticas. La campaña ejecuta diez escenarios y cada escenario activa una técnica distinta, lo que fija el denominador de la cobertura en diez dentro de los dos laboratorios.");
Fig(13, "j-cobertura-mitre-attack.png", "Inventario de técnicas y tácticas del señuelo frente a las que cuentan con fuente de detección",
    "La barra gris declara el tamaño del inventario del señuelo y la verde las técnicas y tácticas que cuentan con fuente de detección en la medición final.",
    ANCHO_AUX, "Comparación entre el inventario de técnicas y tácticas y las que cuentan con fuente de detección.");
Tbl(21, "Las diecisiete técnicas del inventario del señuelo y su fuente de detección",
    new[] { "Técnica", "Táctica", "Escenario", "Fuente en la medición final" },
    new[]
    {
        new[] { "T1048.003", "Exfiltration",        "S10", "Sensor de red" },
        new[] { "T1059",     "Execution",           "—",   "En inventario" },
        new[] { "T1059.004", "Execution",           "S09", "Emulador de acceso remoto" },
        new[] { "T1059.006", "Execution",           "—",   "En inventario" },
        new[] { "T1059.007", "Execution",           "S06", "Portal del señuelo" },
        new[] { "T1078",     "Initial Access",      "S07", "Interfaz de servicios" },
        new[] { "T1078.001", "Initial Access",      "—",   "En inventario" },
        new[] { "T1083",     "Discovery",           "—",   "En inventario" },
        new[] { "T1105",     "Command and Control", "S08", "Archivo señuelo" },
        new[] { "T1110.001", "Credential Access",   "S03", "Emulador de acceso remoto" },
        new[] { "T1110.004", "Credential Access",   "S05", "Interfaz de servicios" },
        new[] { "T1190",     "Initial Access",      "S04", "Portal del señuelo" },
        new[] { "T1213",     "Collection",          "—",   "En inventario" },
        new[] { "T1530",     "Collection",          "—",   "En inventario" },
        new[] { "T1595",     "Reconnaissance",      "S01", "Interfaz de servicios" },
        new[] { "T1595.002", "Reconnaissance",      "S02", "Portal del señuelo" },
        new[] { "T1595.003", "Reconnaissance",      "—",   "En inventario" },
    },
    new[] { 1400, 2200, 1300, 4460 },
    "Las siete técnicas marcadas como en inventario pertenecen al catálogo del señuelo sin que ningún escenario las ejerza. La columna de fuente recoge la medición final del Prototipo 2, porque es la única vuelta en la que los diez escenarios tienen una fuente asignada. Los datos proceden del archivo evidencias/07-metricas/08_mitre-coverage.json del Prototipo 1 y del reporte de indicadores de la medición final del Prototipo 2.",
    new[] { true, false, true, false });
P("Siete técnicas pertenecen al inventario sin que ningún escenario las ejerza, de manera que la tabla las marca como tales y el lector no suma diecisiete mediciones donde solo existen diez. En el primer laboratorio el escenario S10 queda fuera de la medición, de manera que la cobertura completa de esa vuelta es de nueve escenarios sobre diez, mientras que el apartado sobre el puente entre los dos laboratorios desarrolla esa diferencia y su corrección.");

// ── 11. Fases ──────────────────────────────────────────────────────────────
Sec(9, "Aportación de cada fase de la metodología");
P("La metodología se estructura en cinco fases encadenadas, de manera que cada una aporta un elemento distinto al resultado final. La gestión de incidentes que el laboratorio aplica se articula con los principios y el proceso que establece ISO/IEC 27035-1:2023 (ISO, 2023), de manera que las fases cubren el ciclo completo desde la preparación hasta la mejora.");
Tbl(22, "Aportación de cada fase de la metodología y medición que la verifica",
    new[] { "Fase", "Qué aporta", "Indicador", "Prototipo 1", "Prototipo 2" },
    new[]
    {
        new[] { "1 · Diseño del señuelo", "Define el activo que se engaña, el nivel de interacción y el perfil del atacante, de manera que la campaña tenga un denominador fijo de diez escenarios", "Escenarios ejecutados", "10 de 10", "10 de 10" },
        new[] { "2 · Despliegue aislado", "Aísla el señuelo en redes separadas y verifica la composición efectiva desde el propio contenedor atacante, de manera que se demuestre qué queda alcanzable desde fuera", "Segmentos de red verificados", "4", "3" },
        new[] { "3 · Captura, enriquecimiento y custodia", "Registra las acciones del adversario con validez forense y conserva cada archivo con su huella, de manera que la evidencia del ciclo se pueda auditar", "Calidad de la evidencia", "100 de 100", "100 de 100" },
        new[] { "4 · Correlación con gestión de incidentes", "Vincula cada evento capturado con la alerta clasificada y con su técnica, de manera que el tiempo medido sea el del ciclo completo y no el de un registro suelto", "Fuentes que registran detección", "5", "6" },
        new[] { "5 · Medición de impacto y lecciones aprendidas", "Cuantifica la efectividad y convierte la medición en un proceso repetible, contrasta las dos vueltas y registra cada discrepancia con su causa raíz, de manera que la mejora del ciclo quede verificada", "Escenarios con medición", "9 de 10", "10 de 10" },
        new[] { "5 · Medición de impacto y lecciones aprendidas", "Cuantifica la efectividad y convierte la medición en un proceso repetible, contrasta las dos vueltas y registra cada discrepancia con su causa raíz, de manera que la mejora del ciclo quede verificada", "Lecciones resueltas", "—", "14 de 14" },
    },
    new[] { 2000, 3200, 1700, 1230, 1230 },
    "La columna de indicador identifica la medición que entrega cada fase de la metodología. La quinta fase aporta dos mediciones, porque el segundo laboratorio añade el registro de lecciones aprendidas a la cobertura de escenarios. El guion largo de la columna del Prototipo 1 indica que esa fase no registra lecciones, de manera que la medición corresponde al segundo laboratorio. Los valores proceden de los reportes de indicadores de cada prototipo y del archivo de subredes del Prototipo 1.",
    new[] { false, false, false, true, true });
P("Las cinco fases aportan en planos distintos, de manera que ninguna de ellas queda sin un resultado comprobable. La fase de despliegue aislado verifica un número diferente de segmentos en cada laboratorio, porque esa diferencia responde a la configuración del sensor de red en cada entorno. La fase de medición concentra la diferencia más clara entre los dos laboratorios, porque el primer laboratorio aporta el vacío del instrumental que el segundo corrige.");

// ── 12. Lecciones ──────────────────────────────────────────────────────────
Sec(10, "Registro de lecciones aprendidas");
P("El segundo laboratorio registra catorce lecciones entre las dos vueltas, de manera que todas ellas cuentan con una resolución documentada. Once se resuelven con su causa raíz identificada y su corrección aplicada, mientras que las tres restantes se resuelven con una mitigación, porque su causa se sitúa fuera del segmento que controla la metodología.");
P("La revisión sistemática de Fraunholz et al. (2018) organiza el conocimiento acumulado sobre la tecnología de engaño y sus fuentes de fallo más frecuentes, de manera que el registro de este apartado se sitúa en esa línea de trabajo. La Figura 14 muestra la distribución de las catorce lecciones según la fase en la que se registran, lo que permite ver dónde se concentra el esfuerzo de corrección.");
Fig(14, "l-lecciones-por-fase.png", "Distribución de las catorce lecciones aprendidas según la fase de la metodología",
    "Cada barra declara en qué fase de la metodología se registró cada una de las catorce lecciones.",
    ANCHO, "Barras con la cantidad de lecciones aprendidas registradas en cada fase de la metodología.");
Tbl(23, "Detalle de las catorce lecciones aprendidas del Prototipo 2",
    new[] { "ID", "Fase", "Hallazgo", "Causa raíz", "Corrección aplicada", "Estado" },
    new[]
    {
        new[] { "L1",  "F3", "El módulo de análisis no ingería los registros de los sensores", "El archivo de configuración quedaba con XML inválido porque el bloque de registro local se añadía después del elemento raíz", "Script que inserta los registros dentro de la raíz y absorbe el bloque sobrante", "Cerrada" },
        new[] { "L2",  "F3", "Las alertas nunca llegaban al índice", "El recolector incluye un campo que el motor de búsqueda de destino rechaza en cada envío masivo", "Publicador propio que indexa las alertas por HTTP sin ese campo", "Cerrada" },
        new[] { "L3",  "F2", "El gestor de registros se reiniciaba cada dos minutos", "El recolector entra en pánico al negociar el canal cifrado y el supervisor interpreta la caída como fin del contenedor", "El recolector queda con salida por consola y un lector inerte", "Cerrada" },
        new[] { "L4",  "F3", "El motor de red seguía detectando pero el gestor dejó de alertar", "El lector conserva la posición de lectura y el desplazamiento queda desfasado", "Script que trunca el archivo para forzar el reinicio de lectura", "Cerrada" },
        new[] { "L5",  "F5", "Los paneles mostraban ausencia de datos", "Incompatibilidad de versión entre el generador de consultas y el motor de búsqueda", "Script que convierte las diecisiete consultas del tablero a un formato admitido", "Cerrada" },
        new[] { "L6",  "F5", "Los paneles devolvían cero con documentos indexados", "Las alertas llevan el campo de tiempo con otro nombre del que usan el patrón de índice", "El publicador copia el campo de tiempo al nombre esperado y añade la severidad", "Cerrada" },
        new[] { "L7",  "F2", "Un fallo puntual de arranque tumbaba el laboratorio entero", "Los scripts de arranque usaban modo de interrupción ante error", "Los tres scripts restauran la copia de seguridad y terminan siempre con éxito", "Cerrada" },
        new[] { "L8",  "F3", "El tablero nativo cargaba el shell pero no renderizaba las vistas", "La imagen local del producto aparece incompleta", "Se aplica una mitigación documentada que sustituye la visualización por el tablero de métricas", "Con mitigación" },
        new[] { "L9",  "F4", "La plataforma de incidentes redirigía toda ruta al módulo de organizaciones", "Estado de licencia en prueba del producto de gestión de incidentes", "Se aplica una mitigación documentada que deja el flujo verificado hasta la generación de la alerta", "Con mitigación" },
        new[] { "L10", "F2", "El segmento declarado para los sensores nunca llegaba a crearse", "Los sensores se ejecutan en modo host y el segmento declarado no se materializa", "Se aplica una mitigación documentada que verifica la composición efectiva en tres segmentos", "Con mitigación" },
        new[] { "L11", "F5", "Seis escenarios quedaban fuera de la referencia pese a que el señuelo registró el ataque", "El calculador leía una sola clave para atribuir la detección y cada escenario la escribía con un nombre distinto", "La función acepta las tres variantes de clave y los escenarios sin objetivo lo declaran", "Cerrada" },
        new[] { "L12", "F2", "La campaña se bloqueaba en el cuarto escenario", "Las herramientas de ataque se ejecutaban sin límite de tiempo", "Se fija un límite de tiempo en las herramientas y en sus conexiones", "Cerrada" },
        new[] { "L13", "F2", "Un escenario informaba captura de sesión sin que hubiera conexión", "La herramienta de prueba no estaba instalada y el script ocultaba el resultado parcial", "Se comprueba la herramienta al inicio y se instalaron las que faltaban", "Cerrada" },
        new[] { "L14", "F3", "Dos escenarios no podían detectarse por falta de fuente", "El calculador solo consultaba tres fuentes y ninguna leía el archivo señuelo ni el tráfico DNS", "Se añaden el archivo señuelo y el sensor de red como fuentes de detección", "Cerrada" },
    },
    new[] { 520, 700, 2240, 2400, 2300, 1200 },
    "Once lecciones se cierran con la causa raíz identificada y la corrección aplicada, mientras que tres se cierran con una mitigación documentada porque su causa se sitúa fuera del segmento que controla la metodología. La columna de fase remite a las cinco fases de la metodología. Los datos proceden del archivo evidencias/lecciones-aprendidas.md del Prototipo 2.",
    new[] { false, true, false, false, false, false });
P("El contenido de las lecciones muestra que los vacíos del primer laboratorio no se limitan a la configuración de las herramientas. Una parte de ellos corresponde a la integración entre componentes y otra parte a la robustez de los scripts de arranque, de manera que la metodología cubre el laboratorio completo y no solo el señuelo.");

// ── 13. Volumen ────────────────────────────────────────────────────────────
Sec(11, "Volumen de actividad de los dos laboratorios");
P("El volumen de actividad muestra cuántos registros producen el señuelo y los sensores en cada ejecución, de manera que el segundo laboratorio registra más volumen en su medición final y la comparación de totales requiere leer la ampliación de la cobertura como causa de ese incremento.");
Tbl(24, "Volumen de actividad de los dos laboratorios",
    new[] { "Indicador", "Prototipo 1", "Qué lo produce en el Prototipo 1", "Prototipo 2, vuelta 1", "Prototipo 2, final", "Variación en el Prototipo 2" },
    new[]
    {
        new[] { "Escenarios ejecutados",                         "10",       "La campaña de escenarios", "10",     "10",     "Constante" },
        new[] { "Ataques registrados en el señuelo",             "46",       "Interfaz de servicios del señuelo", "54", "254", "+370 %" },
        new[] { "Peticiones atendidas por la interfaz de servicios","1 758",  "Interfaz de servicios del señuelo", "725", "1 508", "+108 %" },
        new[] { "Conexiones capturadas por el emulador",         "8",        "Emulador de acceso remoto", "7",      "38",     "+443 %" },
        new[] { "Peticiones recibidas por el portal",            "8 875",    "Portal del señuelo", "15 765",   "78 186", "+396 %" },
        new[] { "Archivos de evidencia con huella",              "68",       "Custodia de la evidencia", "91",   "91",     "Constante" },
        new[] { "Calidad de la evidencia verificada",            "100 de 100", "Verificación de integridad", "100 de 100", "100 de 100", "Constante" },
    },
    new[] { 2500, 1150, 2200, 1250, 1250, 1010 },
    "Los tres momentos de la tabla corresponden al Prototipo 1, a la vuelta 1 del Prototipo 2 y a su medición final. La columna de producción declara qué componente genera cada registro en el primer laboratorio, mientras que la columna de variación mide el incremento porcentual entre las dos vueltas del segundo laboratorio. Los datos proceden de los archivos de evidencia de los dos laboratorios.",
    new[] { false, true, false, true, true, true });
P("El aumento del volumen en la medición final se explica por la ampliación de la cobertura de medición, de manera que los seis escenarios que la vuelta 1 dejó fuera de la referencia producen ahora eventos que antes no llegan a ningún componente de registro. La calidad de la evidencia permanece en 100 de 100 en las tres ejecuciones, de manera que el incremento de volumen no afecta la validez de la custodia.");
P("La columna de variación muestra que los tres indicadores de tráfico del señuelo crecen entre las dos vueltas del segundo laboratorio, mientras que el volumen de evidencia y la calidad de la custodia permanecen constantes. Esa combinación sostiene la lectura de que el incremento procede de la cobertura y no de un cambio en el instrumento de captura.");

// ── 14. Síntesis ───────────────────────────────────────────────────────────
Sec(12, "Síntesis de los resultados");
P("Los dos planos de resultado se leen juntos sin superponerse, de manera que cada cifra conserve el sentido que le corresponde. El primer laboratorio verifica que la cadena de detección opera por separado y el segundo comprueba que la metodología corrige los vacíos que el primero deja ver, de manera que la comparación se resuelva por función y no por magnitud.");
Fig(15, "o-sintesis.png", "Estado inicial y estado final de los dos planos de resultado",
    "Cada fila compara el estado inicial y el estado final de uno de los dos planos de resultado. La diferencia se expresa en número de elementos para los indicadores de laboratorio.",
    ANCHO, "Comparación del estado inicial y el estado final de los dos planos de resultado del capítulo.");
Tbl(25, "Síntesis de los dos planos de resultado",
    new[] { "Plano", "Pregunta que responde", "Resultado", "Fuente" },
    new[]
    {
        new[] { "Verificación de la cadena","Si cada componente opera por separado","9 de 10 escenarios medidos", "Reporte de indicadores del Prototipo 1" },
        new[] { "Mejora del instrumental",  "Qué produce la corrección aplicada", "4 de 10 a 10 de 10", "Reportes de indicadores del Prototipo 2" },
    },
    new[] { 2200, 2600, 2200, 2360 },
    "Cada plano de resultado remite a una fuente distinta, de manera que las cifras no comparten escala. Los datos proceden de los reportes de indicadores de los dos prototipos.",
    new[] { false, false, true, false });
P("La metodología aporta en los dos planos a la vez, de manera que la verificación técnica de la cadena de detección conviva con la mejora del instrumental que la segunda vuelta produce. El primer laboratorio cumple la función de línea de base técnica, porque muestra qué falta antes de que el segundo laboratorio lo resuelva. La cobertura de medición del segundo laboratorio pasa de cuatro a diez escenarios, de manera que el resultado de la metodología se expresa en la ampliación del alcance verificado.");

// ── 15. Evidencia visual ───────────────────────────────────────────────────
Sec(13, "Evidencia visual de los tableros");
P("El capítulo incluye tres paneles que documentan el estado de los tableros en cada uno de los tres momentos del ciclo de laboratorio. El primero corresponde al TaxFisco Research Lab y los otros dos al laboratorio del Servicio de Impuestos Nacionales, en su vuelta 1 y en su medición final.");
P("El panel del primer laboratorio declara 199 alertas indexadas, distribuidas en 152 de severidad baja, 45 alta y dos media, con un nivel medio de 3,92 y un nivel máximo de 7. El tablero de la vuelta 1 del segundo laboratorio registra 434 alertas indexadas, con un nivel medio de alerta de 4,88 y una serie temporal de picos aislados. La medición final eleva el nivel medio de alerta a 6,20 y muestra una actividad sostenida a lo largo de toda la ventana de observación.");
Tbl(26, "Evidencia visual de los tres tableros de los dos laboratorios",
    new[] { "Panel", "Ventana temporal", "Alertas indexadas", "Nivel medio de alerta", "Archivo de origen" },
    new[]
    {
        new[] { "TaxFisco Research Lab, panel de indicadores", "Medición del Prototipo 1", "199", "3,92, con un máximo de 7", "evidencias/07-metricas/04_grafana-kpis.png" },
        new[] { "Servicio de Impuestos Nacionales, vuelta 1", "Tres horas", "434", "4,88", "v2.0-it1/04-captura-eventos/02_grafana-dashboard-siem.png" },
        new[] { "Servicio de Impuestos Nacionales, medición final", "Veinticuatro horas", "35,1 mil", "6,20", "v2.1-it2/04-captura-eventos/05_grafana-dashboard-siem.png" },
    },
    new[] { 2500, 1700, 1300, 1700, 2160 },
    "Las ventanas temporales de los dos paneles del segundo laboratorio difieren porque la cadena de indexación se puso en marcha entre una captura y la otra, de manera que el lector no interprete los totales como una serie homogénea. La cifra de 35,1 mil se reproduce tal como la declara la captura del tablero.",
    new[] { false, false, true, true, false });
P("La diferencia de ventanas responde a la puesta en marcha de la cadena de indexación entre una captura y la otra, de manera que la comparación de paneles se apoya en la tendencia y no en la igualdad de los totales, mientras que las tres figuras siguientes reproducen cada panel con su nota de origen.");
Fig(16, "prototipo-1-indicadores.png", "Panel de indicadores del TaxFisco Research Lab",
    "El panel declara 199 alertas indexadas, distribuidas en 152 de severidad baja, 45 alta y dos media. La imagen procede del archivo evidencias/07-metricas/04_grafana-kpis.png.",
    ANCHO, "Panel de indicadores del TaxFisco Research Lab con 199 alertas indexadas, nivel medio 3,92 y nivel máximo 7.");
Fig(17, "prototipo-2-vuelta-1.png", "Tablero de alertas del laboratorio del Servicio de Impuestos Nacionales en la vuelta 1",
    "La serie temporal muestra picos aislados y un nivel medio de alerta de 4,88 sobre cuatrocientas treinta y cuatro alertas indexadas. La imagen procede del archivo v2.0-it1/04-captura-eventos/02_grafana-dashboard-siem.png.",
    ANCHO, "Tablero de alertas del laboratorio SIN en la vuelta 1 con 434 alertas indexadas y picos aislados en la serie temporal.");
Fig(18, "prototipo-2-vuelta-2.png", "Tablero de alertas del laboratorio del Servicio de Impuestos Nacionales en la medición final",
    "La serie temporal sostiene actividad a lo largo de toda la ventana y el nivel medio de alerta sube a 6,20. La imagen procede del archivo v2.1-it2/04-captura-eventos/05_grafana-dashboard-siem.png.",
    ANCHO, "Tablero de alertas del laboratorio SIN en la medición final con 35,1 mil alertas indexadas y actividad sostenida.");

// ── 16. Naturaleza del dato ────────────────────────────────────────────────
Sec(14, "Naturaleza del dato y trazabilidad de la medición");
P("El capítulo distingue la naturaleza de los datos que presenta, de manera que la comparación conserve su valor interpretativo. La línea base institucional de 52,70 % se calcula sobre una matriz real de treinta respondentes con distribución natural de cero a cuatro, de manera que el alfa de Cronbach de 0,868989 acompañe ese conjunto de respuestas.");
P("Los resultados de los dos laboratorios tienen una naturaleza distinta, porque cada cifra se apoya en un archivo de evidencia que el repositorio conserva y que el lector puede abrir. Esa trazabilidad permite reconstruir el valor de cada indicador desde su archivo de origen, de manera que el capítulo se pueda auditar sin intermediarios.");
P("El capítulo registra esa diferencia de trazabilidad porque el lector necesita saber qué grado de detalle respalda cada cifra. La comparación entre los dos prototipos se sostiene en indicadores que los dos laboratorios registran con el mismo denominador, no en un desglose que uno de los dos ofrece y el otro no. La trazabilidad del dato es un requisito habitual en los marcos de medición de la gestión de incidentes (Cawthra et al., 2024), de manera que declararla forma parte del resultado y no de sus límites.");
P("El diagnóstico institucional que el capítulo toma como punto de partida conserva esa misma propiedad, porque su archivo de origen acompaña la matriz real de treinta respondentes junto con el cálculo del alfa de Cronbach. La diferencia entre ambos conjuntos de datos no está en la calidad de la evidencia, de manera que se lee en el tipo de medida que cada uno ofrece.");

// ── Referencias ────────────────────────────────────────────────────────────
body.Append(ctx.Heading("Referencias", 1));
ctx.Ref("Cawthra, J., Ekstrom, M., Lusty, L., Sexton, J., & Sweetnam, J. (2024). *NIST SP 800-61 Rev. 3: Incident response recommendations and considerations for cybersecurity risk management*. National Institute of Standards and Technology.");
ctx.Ref("Fraunholz, D., Duong, H. H. D., Pohl, M., Ruland, C., & Schotten, H. D. (2018). Demystifying deception technology: A systematic literature review. *Computers & Security*.");
ctx.Ref("International Organization for Standardization. (2022). *ISO/IEC 27001:2022. Information security, cybersecurity and privacy protection. Information security management systems. Requirements*.");
ctx.Ref("International Organization for Standardization. (2023). *ISO/IEC 27035-1:2023. Information security incident management. Part 1: Principles and process*.");
ctx.Ref("MITRE Corporation. (2024). *MITRE ATT&CK Enterprise matrix*. https://attack.mitre.org/");
ctx.Ref("Spitzner, L. (2003). *Honeypots: Tracking hackers*. Addison-Wesley.");

Scaffold.Close(main, body);
main.Document.Save();
doc.Dispose();

Console.WriteLine("Documento generado: " + salida);
Console.WriteLine("Tamaño: " + new FileInfo(salida).Length + " bytes");
