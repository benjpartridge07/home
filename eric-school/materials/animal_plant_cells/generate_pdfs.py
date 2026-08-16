# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Animal & Plant Cells (AQA 8465 4.1.3.2, Foundation tier)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.graphics.shapes import Drawing, Ellipse, Rect, Circle, String

INK = colors.HexColor('#23201A')
INK_SOFT = colors.HexColor('#6B6355')
BIO = colors.HexColor('#2F8B57')
MATHS = colors.HexColor('#3A5E85')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#EAF2ED')
MEMBRANE_FILL = colors.HexColor('#F4F1EA')
NUCLEUS_FILL = colors.HexColor('#DDE6EF')
ORGANELLE_FILL = colors.HexColor('#F1E3CE')
CHLORO_FILL = colors.HexColor('#DFF0E5')

MARGIN = 18 * mm

styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=26,
                             textColor=INK, spaceAfter=4, leading=30),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=10.5,
                                textColor=INK_SOFT, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=13.5,
                          textColor=BIO, spaceBefore=14, spaceAfter=7),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10,
                            textColor=INK, leading=14, spaceAfter=7, alignment=TA_LEFT),
    'marks': ParagraphStyle('marks', fontName='Helvetica-Oblique', fontSize=9,
                             textColor=INK_SOFT, spaceAfter=9),
    'qtext': ParagraphStyle('qtext', fontName='Helvetica', fontSize=10,
                             textColor=INK, leading=14, spaceAfter=2),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=10,
                           textColor=INK, leading=14, spaceAfter=6),
    'note': ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=9,
                            textColor=INK_SOFT, leading=12, spaceBefore=12),
    'tablehead': ParagraphStyle('tablehead', fontName='Helvetica', fontSize=8.7,
                                 textColor=INK_SOFT),
    'tablecell': ParagraphStyle('tablecell', fontName='Helvetica', fontSize=9.3,
                                 textColor=INK, leading=12.5),
    'labellist': ParagraphStyle('labellist', fontName='Helvetica', fontSize=10.5,
                                 textColor=INK, leading=22),
}


def hr():
    return HRFlowable(width='100%', thickness=1, color=PAPER_LINE,
                       spaceBefore=6, spaceAfter=12)


def header(title, subtitle):
    return [Paragraph(title, styles['title']), Paragraph(subtitle, styles['subtitle']), hr()]


def badge(d, x, y, num):
    d.add(Circle(x, y, 14, fillColor=INK, strokeColor=colors.white, strokeWidth=2))
    d.add(String(x, y - 5, str(num), fontName='Helvetica-Bold', fontSize=14.5,
                  textColor=colors.white, textAnchor='middle'))


def animal_cell_drawing():
    w, h = 300, 220
    d = Drawing(w, h)
    d.add(Ellipse(150, 110, 125, 95, fillColor=MEMBRANE_FILL, strokeColor=INK, strokeWidth=1.6))
    d.add(Circle(105, 115, 38, fillColor=NUCLEUS_FILL, strokeColor=MATHS, strokeWidth=1.3))
    d.add(Ellipse(205, 70, 18, 10, fillColor=ORGANELLE_FILL, strokeColor=colors.HexColor('#B5762A'), strokeWidth=1.2))
    for dx, dy in [(-5, 0), (5, 7), (-5, 12)]:
        d.add(Circle(175 + dx, 175 + dy, 2.5, fillColor=BIO, strokeColor=None))
    badge(d, 105, 115, 1)
    badge(d, 205, 70, 2)
    badge(d, 176, 180, 3)
    badge(d, 150, 20, 4)
    badge(d, 230, 140, 5)
    return d


def plant_cell_drawing():
    w, h = 300, 220
    d = Drawing(w, h)
    d.add(Rect(15, 10, 270, 200, 6, fillColor=None, strokeColor=BIO, strokeWidth=4))
    d.add(Rect(23, 18, 254, 184, 4, fillColor=MEMBRANE_FILL, strokeColor=INK, strokeWidth=1.3))
    d.add(Ellipse(195, 110, 68, 72, fillColor=NUCLEUS_FILL, strokeColor=MATHS, strokeWidth=1.3))
    d.add(Circle(85, 140, 32, fillColor=ORGANELLE_FILL, strokeColor=colors.HexColor('#B5762A'), strokeWidth=1.2))
    d.add(Ellipse(70, 50, 14, 8, fillColor=CHLORO_FILL, strokeColor=BIO, strokeWidth=1.2))
    d.add(Ellipse(110, 70, 14, 8, fillColor=CHLORO_FILL, strokeColor=BIO, strokeWidth=1.2))
    badge(d, 23, 20, 1)
    badge(d, 277, 25, 2)
    badge(d, 85, 140, 3)
    badge(d, 70, 50, 4)
    badge(d, 195, 110, 5)
    badge(d, 130, 180, 6)
    return d


def table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEAD_BG),
        ('LINEBELOW', (0, 0), (-1, -1), 0.75, PAPER_LINE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 8.7),
        ('TEXTCOLOR', (0, 0), (-1, 0), INK_SOFT),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def cell(text):
    return Paragraph(text, styles['tablecell'])


def headcell(text):
    return Paragraph(text, styles['tablehead'])


def label_lines(n):
    return Paragraph('   '.join(
        f'{i}.&nbsp;________________________' for i in range(1, n + 1)
    ), styles['labellist'])


# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('animal_plant_cells_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Animal &amp; Plant Cells',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('1. Animal cells', styles['h2']))
    s.append(Paragraph('Most animal cells have the same five basic parts.', styles['body']))
    s.append(animal_cell_drawing())
    s.append(table([
        [headcell('#'), headcell('Structure'), headcell('Function')],
        [cell('1'), cell('Nucleus'), cell('Contains the genetic material (DNA), controls the cell&rsquo;s activities')],
        [cell('2'), cell('Mitochondria'), cell('Site of respiration &mdash; releases energy the cell needs')],
        [cell('3'), cell('Ribosomes'), cell('Where proteins are made')],
        [cell('4'), cell('Cell membrane'), cell('Controls what substances enter and leave the cell')],
        [cell('5'), cell('Cytoplasm'), cell('Jelly-like substance where many chemical reactions happen')],
    ], col_widths=[10 * mm, 38 * mm, 106 * mm]))

    s.append(Paragraph('2. Plant cells', styles['h2']))
    s.append(Paragraph('Plant cells have everything an animal cell has, <b>plus</b> three extra structures.', styles['body']))
    s.append(plant_cell_drawing())
    s.append(table([
        [headcell('#'), headcell('Structure'), headcell('Function')],
        [cell('1'), cell('Cell wall'), cell('Made of <b>cellulose</b>; strengthens and supports the cell')],
        [cell('2'), cell('Cell membrane'), cell('Controls what substances enter and leave the cell')],
        [cell('3'), cell('Nucleus'), cell('Contains the genetic material (DNA)')],
        [cell('4'), cell('Chloroplast'), cell('Site of photosynthesis (contains chlorophyll)')],
        [cell('5'), cell('Permanent vacuole'), cell('Filled with cell sap; helps keep the cell rigid')],
        [cell('6'), cell('Cytoplasm'), cell('Jelly-like substance where many chemical reactions happen')],
    ], col_widths=[10 * mm, 38 * mm, 106 * mm]))

    s.append(Paragraph('3. Animal vs plant: what&rsquo;s the difference?', styles['h2']))
    s.append(table([
        [headcell('Structure'), headcell('Animal'), headcell('Plant')],
        [cell('Nucleus, cytoplasm, cell membrane'), cell('&check;'), cell('&check;')],
        [cell('Mitochondria, ribosomes'), cell('&check;'), cell('&check;')],
        [cell('Cell wall (cellulose)'), cell('&mdash;'), cell('&check;')],
        [cell('Chloroplasts'), cell('&mdash;'), cell('&check;')],
        [cell('Permanent vacuole'), cell('&mdash;'), cell('&check;')],
    ], col_widths=[70 * mm, 34 * mm, 50 * mm]))
    s.append(Paragraph('Plants can&rsquo;t move to escape danger or find support, so the <b>cell wall</b> gives each cell a rigid shape &mdash; millions of rigid cells stacked together let a plant stand upright. Only cells that photosynthesise (e.g. leaf cells) need <b>chloroplasts</b>; root cells, for example, have none.', styles['body']))

    s.append(Paragraph('4. A quick look at bacterial cells', styles['h2']))
    s.append(Paragraph('Bacterial cells are much simpler and smaller than animal or plant cells. Their genetic material is not held in a nucleus &mdash; it is a single loop of DNA floating in the cytoplasm, plus small extra rings of DNA called <b>plasmids</b>.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('animal_plant_cells_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Animal &amp; Plant Cells', 'Test &middot; 22 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 22'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Label the animal cell', styles['h2']))
    s.append(Paragraph('A1. Write the name of each numbered structure.', styles['qtext']))
    s.append(animal_cell_drawing())
    s.append(label_lines(5))
    s.append(Paragraph('[5 marks]', styles['marks']))

    s.append(Paragraph('Section B &mdash; Label the plant cell', styles['h2']))
    s.append(Paragraph('B1. Write the name of each numbered structure.', styles['qtext']))
    s.append(plant_cell_drawing())
    s.append(label_lines(6))
    s.append(Paragraph('[6 marks]', styles['marks']))

    s.append(Paragraph('Section C &mdash; Function matching', styles['h2']))
    s.append(Paragraph('State the function of each structure.', styles['qtext']))
    s.append(Spacer(1, 4))
    s += q('C1', 'Nucleus', 1)
    s.append(Spacer(1, 8))
    s += q('C2', 'Mitochondria', 1)
    s.append(Spacer(1, 8))
    s += q('C3', 'Ribosomes', 1)
    s.append(Spacer(1, 8))
    s += q('C4', 'Chloroplast', 1)
    s.append(Spacer(1, 8))
    s += q('C5', 'Cell wall', 1)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section D &mdash; Animal vs plant', styles['h2']))
    s += q('D1', 'Name two structures found in a plant cell but not in an animal cell.', 2)
    s.append(Spacer(1, 10))
    s += q('D2', 'Explain why plant cells need a cell wall, but animal cells do not.', 2)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section E &mdash; Bacterial cells', styles['h2']))
    s += q('E1', 'Name the structure in a bacterial cell that carries extra genes, separate from the main DNA loop.', 1)
    s.append(Spacer(1, 8))
    s += q('E2', 'State one way the genetic material in a bacterial cell differs from that in an animal cell.', 1)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('animal_plant_cells_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Animal &amp; Plant Cells', 'Answer sheet &middot; 22 marks total')

    s.append(Paragraph('Section A &mdash; Label the animal cell', styles['h2']))
    s.append(Paragraph('1. Nucleus &nbsp;&nbsp; 2. Mitochondria &nbsp;&nbsp; 3. Ribosomes &nbsp;&nbsp; 4. Cell membrane &nbsp;&nbsp; 5. Cytoplasm', styles['ans']))
    s.append(Paragraph('[1 mark each, 5 marks total]', styles['marks']))

    s.append(Paragraph('Section B &mdash; Label the plant cell', styles['h2']))
    s.append(Paragraph('1. Cell wall &nbsp;&nbsp; 2. Cell membrane &nbsp;&nbsp; 3. Nucleus &nbsp;&nbsp; 4. Chloroplast &nbsp;&nbsp; 5. Permanent vacuole &nbsp;&nbsp; 6. Cytoplasm', styles['ans']))
    s.append(Paragraph('[1 mark each, 6 marks total]', styles['marks']))

    s.append(Paragraph('Section C &mdash; Function matching', styles['h2']))
    s.append(Paragraph('<b>C1.</b> Nucleus &mdash; contains the genetic material (DNA), controls the cell&rsquo;s activities (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> Mitochondria &mdash; site of respiration, releases energy (1).', styles['ans']))
    s.append(Paragraph('<b>C3.</b> Ribosomes &mdash; where proteins are made (1).', styles['ans']))
    s.append(Paragraph('<b>C4.</b> Chloroplast &mdash; site of photosynthesis (1).', styles['ans']))
    s.append(Paragraph('<b>C5.</b> Cell wall &mdash; strengthens/supports the cell (1).', styles['ans']))

    s.append(Paragraph('Section D &mdash; Animal vs plant', styles['h2']))
    s.append(Paragraph('<b>D1.</b> Any two of: cell wall, chloroplasts, permanent vacuole (1 mark each, 2 marks total).', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Plant cells need a rigid shape / structural support because plants cannot move around (1); the cell wall gives the cell this rigidity/strength, which an animal cell does not need (1).', styles['ans']))

    s.append(Paragraph('Section E &mdash; Bacterial cells', styles['h2']))
    s.append(Paragraph('<b>E1.</b> Plasmid(s) (1).', styles['ans']))
    s.append(Paragraph('<b>E2.</b> In a bacterial cell the genetic material is a single DNA loop free in the cytoplasm (not in a nucleus); in an animal cell it is enclosed in a nucleus (1).', styles['ans']))

    s.append(Paragraph(
        'Marking note: accept any scientifically correct equivalent wording throughout. For labelling sections, '
        'accept minor spelling errors as long as the structure is clearly identifiable.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
