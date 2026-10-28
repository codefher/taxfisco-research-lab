# -*- coding: utf-8 -*-
"""Actualiza el Word de la seccion 4.4 con el apartado 4.4.5 y los radares.

Operaciones:
  1. Renumera las tablas (4..8 -> 3..7) para igualar el HTML vigente.
  2. Renumera la figura de la sintesis (17 -> 19) y la seccion 4.4.5 -> 4.4.6.
  3. Inserta los dos parrafos nuevos de 4.4.4 sobre el resultado verificado.
  4. Inserta el apartado 4.4.5 con las Figuras 17 y 18 (radares).
  5. Actualiza el indice de la portada.

El texto se toma del HTML vigente para no duplicar redaccion a mano.
"""
import copy
import os
import re
import sys
from lxml import html as lhtml
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph
from docx.shared import Emu

RAIZ = r"F:\Maestria\tesis\taxfisco-research-lab"
HTML = os.path.join(RAIZ, 'resultados-prototipos', 'cap4-nuevo.html')
DOCX = os.path.join(RAIZ, 'resultados-prototipos', 'capitulo-4-4-resultados.docx')
IMG_LIB = os.path.join(RAIZ, 'resultados-prototipos', 'evidencia-visual', 'radares', 'radar-cap4-libelula.png')
IMG_SIN = os.path.join(RAIZ, 'resultados-prototipos', 'evidencia-visual', 'radares', 'radar-cap4-sin.png')

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
EMU_ANCHO = 5943600          # 16.51 cm, el ancho que usan las demas figuras
RATIO = 960 / 1240            # viewBox 1240 x 960 de los radares

MAPA_TABLA = {4: 3, 5: 4, 6: 5, 7: 6, 8: 7}


# ---------------------------------------------------------------- utilidades
def norm(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()


def texto_parrafo(p):
    return norm(p.text)


def fijar_texto(p, texto, rpr_origen=None):
    """Reemplaza el contenido del parrafo conservando el formato del run."""
    for child in list(p._p):
        if child.tag in (qn('w:r'), qn('w:hyperlink')):
            p._p.remove(child)
    r = OxmlElement('w:r')
    if rpr_origen is not None:
        r.append(copy.deepcopy(rpr_origen))
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = texto
    r.append(t)
    p._p.append(r)


def runs_con_formato(p):
    """Devuelve la lista de (texto, rPr) del parrafo."""
    out = []
    for r in p.runs:
        rpr = r._r.find(qn('w:rPr'))
        out.append((r.text, rpr))
    return out


def pr_primer_run(p):
    for r in p.runs:
        rpr = r._r.find(qn('w:rPr'))
        if rpr is not None:
            return rpr
    return None


# ------------------------------------------------------- extraccion del HTML
def extraer_html():
    tree = lhtml.parse(HTML).getroot()

    def sec(id_):
        for s in tree.iter('section'):
            if s.get('id') == id_:
                return s
        raise SystemExit('No se encontro la seccion ' + id_)

    def bloques(section):
        """Clasifica los bloques de una seccion en el orden del DOCX."""
        out = []
        for hijo in section:
            tag = hijo.tag if isinstance(hijo.tag, str) else ''
            if tag == 'h3':
                out.append(('H1', norm(hijo.text_content())))
            elif tag == 'h4':
                out.append(('H2', norm(hijo.text_content())))
            elif tag == 'p':
                cls = (hijo.get('class') or '').split()
                texto = norm(hijo.text_content())
                if 'lbl' in cls:
                    out.append(('CAPLBL', texto))
                elif 'sub' in cls:
                    out.append(('SUB', texto))
                else:
                    out.append(('PROSA', texto))
            elif tag == 'figure':
                desc = ''
                svg = None
                for sub in hijo:
                    st = sub.tag if isinstance(sub.tag, str) else ''
                    if st == 'figcaption':
                        desc = re.sub(r'^Figura\s+\d+\.\s*', '', norm(sub.text_content()))
                    elif st == 'svg':
                        svg = sub
                out.append(('CAPDESC', desc))
                out.append(('IMG', svg.get('aria-label') if svg is not None else ''))
            elif tag == 'div' and 'note' in (hijo.get('class') or '').split():
                texto = norm(hijo.text_content())
                texto = re.sub(r'^Nota\.\s*', '', texto)
                out.append(('NOTE', texto))
            elif tag == 'table':
                out.append(('TABLE', norm(hijo.text_content())))
        return out

    s444 = bloques(sec('s444'))
    s445 = bloques(sec('s445'))

    nuevos_444 = [t for k, t in s444 if k == 'PROSA' and t.startswith('El resultado verificado mejora')]
    if len(nuevos_444) != 2:
        raise SystemExit('Se esperaban 2 parrafos nuevos en 4.4.4 y se hallaron %d' % len(nuevos_444))
    return nuevos_444, s445


# ------------------------------------------------------------------ mutacion
def main():
    nuevos_444, s445 = extraer_html()
    doc = Document(DOCX)
    body = doc.element.body

    paras = lambda: [Paragraph(c, doc) for c in body.iterchildren() if c.tag == qn('w:p')]

    # ---- 1. renumeracion de tablas ------------------------------------
    camb_tabla = 0
    for p in paras():
        for r in p.runs:
            if 'Tabla ' not in r.text:
                continue
            nuevo = re.sub(r'\bTabla (\d+)\b',
                           lambda m: 'Tabla %d' % MAPA_TABLA.get(int(m.group(1)), int(m.group(1))),
                           r.text)
            if nuevo != r.text:
                r.text = nuevo
                camb_tabla += 1
    print('Tablas renumeradas en %d runs' % camb_tabla)

    # ---- 2. renumeracion de figura y seccion --------------------------
    for p in paras():
        t = texto_parrafo(p)
        if t == 'Figura 17':
            fijar_texto(p, 'Figura 19', pr_primer_run(p))
        elif 'Figura 17' in t and t.startswith('Tres precisiones'):
            fijar_texto(p, t.replace('Figura 17', 'Figura 19'), pr_primer_run(p))
        if t == '4.4.5 Síntesis de los resultados':
            fijar_texto(p, '4.4.6 Síntesis de los resultados', pr_primer_run(p))
        elif 'lectura conjunta del 4.4.5' in t:
            fijar_texto(p, t.replace('lectura conjunta del 4.4.5', 'lectura conjunta del 4.4.6'), pr_primer_run(p))
        elif t.startswith('La metodología Honeypot se aplica en dos ocasiones'):
            viejo = 'para finalizar con la comparación entre ambos y la síntesis de los principales hallazgos.'
            nuevo = ('para finalizar con la comparación entre ambos, la mejora del análisis situacional '
                     'y la síntesis de los principales hallazgos.')
            if viejo in t:
                fijar_texto(p, t.replace(viejo, nuevo), pr_primer_run(p))
    print('Figura de la sintesis renumerada a 19 y seccion 4.4.5 renumerada a 4.4.6')

    # ---- 3. clones de plantilla ---------------------------------------
    todas = paras()

    def primero_por(estilo, predicado=None):
        for p in todas:
            if (p.style is not None and p.style.name == estilo) and (predicado is None or predicado(p)):
                return p
        raise SystemExit('No se encontro el parrafo plantilla ' + estilo)

    tpl_h1 = primero_por('Heading 1', lambda p: texto_parrafo(p).startswith('4.4.1'))
    tpl_sub = primero_por('Normal', lambda p: texto_parrafo(p).startswith('Lectura de los indicadores declarados'))
    tpl_prosa = primero_por('Normal', lambda p: texto_parrafo(p).startswith('Los resultados de la aplicación'))
    tpl_caplbl = primero_por('Figure Caption', lambda p: texto_parrafo(p) == 'Figura 1')
    tpl_capdesc = primero_por('Figure Caption', lambda p: texto_parrafo(p).startswith('Panel con los seis'))
    tpl_img = primero_por('Figure Image')
    tpl_nota = primero_por('Table Note', lambda p: texto_parrafo(p).startswith('Nota.'))
    tpl_indice = primero_por('Normal', lambda p: texto_parrafo(p) == '4.4.1 Resultado global de la aplicación de la metodología')

    # ---- 4. insercion de los dos parrafos de 4.4.4 --------------------
    def nota_con(prefijo):
        for p in paras():
            if (p.style is not None and p.style.name == 'Table Note') and texto_parrafo(p).startswith(prefijo):
                return p
        raise SystemExit('No se encontro la nota ' + prefijo)

    nota_p1 = nota_con('Nota. El momento inicial del primer prototipo')
    nota_p2 = nota_con('Nota. Las dos vueltas comparten el mismo señuelo')

    def clonar_prosa(plantilla, texto):
        nuevo = copy.deepcopy(plantilla._p)
        fijar_texto(Paragraph(nuevo, doc), texto, pr_primer_run(plantilla))
        return nuevo

    n1 = clonar_prosa(tpl_prosa, nuevos_444[0])
    nota_p1._p.addnext(n1)
    n2 = clonar_prosa(tpl_prosa, nuevos_444[1])
    nota_p2._p.addnext(n2)
    print('Insertados 2 parrafos nuevos en 4.4.4')

    # ---- 5. imagenes ---------------------------------------------------
    rel_ids = []
    for p in paras():
        for b in p._p.findall('.//' + qn('a:blip')):
            rel_ids.append(b.get(qn('r:embed')))
    usados = set()
    for rid in rel_ids:
        m = re.match(r'rIdImg(\d+)$', rid or '')
        if m:
            usados.add(int(m.group(1)))
    siguiente = max(usados) + 1 if usados else 1

    docpr_ids = [int(e.get('id')) for e in body.findall('.//' + qn('wp:docPr')) if e.get('id')]
    siguiente_docpr = max(docpr_ids) + 1 if docpr_ids else 1

    def clonar_imagen(plantilla, ruta, nombre, alt, docpr_id):
        rid, _ = doc.part.get_or_add_image(ruta)
        nuevo = copy.deepcopy(plantilla._p)
        blip = nuevo.find('.//' + qn('a:blip'))
        blip.set(qn('r:embed'), rid)
        cy = int(round(EMU_ANCHO * RATIO))
        for ext in nuevo.findall('.//' + qn('wp:extent')):
            ext.set('cx', str(EMU_ANCHO))
            ext.set('cy', str(cy))
        for ext in nuevo.findall('.//' + qn('a:ext')):
            ext.set('cx', str(EMU_ANCHO))
            ext.set('cy', str(cy))
        for dpr in nuevo.findall('.//' + qn('wp:docPr')):
            dpr.set('id', str(docpr_id))
            dpr.set('name', nombre)
            dpr.set('descr', alt)
        for cnv in nuevo.findall('.//' + qn('pic:cNvPr')):
            cnv.set('name', nombre)
        return nuevo

    # ---- 6. bloque 4.4.5 ----------------------------------------------
    sintesis = None
    for p in paras():
        if (p.style is not None and p.style.name == 'Heading 1') and texto_parrafo(p).startswith('4.4.6 Síntesis'):
            sintesis = p
            break
    if sintesis is None:
        raise SystemExit('No se encontro el encabezado de la sintesis 4.4.6')

    idx_img = 0
    anterior = None
    for tipo, valor in s445:
        if tipo == 'H1':
            nuevo = copy.deepcopy(tpl_h1._p)
            fijar_texto(Paragraph(nuevo, doc), valor, pr_primer_run(tpl_h1))
        elif tipo == 'SUB':
            nuevo = copy.deepcopy(tpl_sub._p)
            fijar_texto(Paragraph(nuevo, doc), valor, pr_primer_run(tpl_sub))
        elif tipo == 'PROSA':
            nuevo = clonar_prosa(tpl_prosa, valor)
        elif tipo == 'CAPLBL':
            nuevo = copy.deepcopy(tpl_caplbl._p)
            fijar_texto(Paragraph(nuevo, doc), valor, pr_primer_run(tpl_caplbl))
        elif tipo == 'CAPDESC':
            nuevo = copy.deepcopy(tpl_capdesc._p)
            fijar_texto(Paragraph(nuevo, doc), valor, pr_primer_run(tpl_capdesc))
        elif tipo == 'NOTE':
            nuevo = copy.deepcopy(tpl_nota._p)
            runs = Paragraph(nuevo, doc).runs
            runs[0].text = 'Nota.'
            runs[1].text = ' ' + valor
        elif tipo == 'IMG':
            nombre = 'Figura 17' if idx_img == 0 else 'Figura 18'
            ruta = IMG_LIB if idx_img == 0 else IMG_SIN
            nuevo = clonar_imagen(tpl_img, ruta, nombre, valor, siguiente_docpr)
            siguiente_docpr += 1
            idx_img += 1
        else:
            continue
        if anterior is None:
            sintesis._p.addprevious(nuevo)
        else:
            anterior.addnext(nuevo)
        anterior = nuevo
    print('Insertado el apartado 4.4.5 con %d radares' % idx_img)

    # ---- 7. indice de la portada --------------------------------------
    entrada_sintesis = None
    for p in paras():
        if (p.style is not None and p.style.name == 'Normal') and texto_parrafo(p) == '4.4.6 Síntesis de los resultados':
            entrada_sintesis = p
            break
    if entrada_sintesis is None:
        raise SystemExit('No se encontro la entrada de indice de la sintesis')
    entrada = copy.deepcopy(tpl_indice._p)
    fijar_texto(Paragraph(entrada, doc),
                '4.4.5 Mejora del análisis situacional tras la aplicación de la metodología',
                pr_primer_run(tpl_indice))
    entrada_sintesis._p.addprevious(entrada)
    print('Actualizado el indice de la portada')

    doc.save(DOCX)
    print('Guardado ' + DOCX)


if __name__ == '__main__':
    main()
