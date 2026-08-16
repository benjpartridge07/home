# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Cells: Structure, Transport & Division (AQA 8465 4.1.3, Foundation tier)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.graphics.shapes import Drawing, Line, String

INK = colors.HexColor('#23201A')
INK_SOFT = colors.HexColor('#6B6355')
BIO = colors.HexColor('#2F8B57')
MATHS = colors.HexColor('#3A5E85')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#EAF2ED')

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
    'bodyb': ParagraphStyle('bodyb', fontName='Helvetica-Bold', fontSize=10,
                             textColor=INK, leading=14, spaceAfter=7),
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
}


def hr():
    return HRFlowable(width='100%', thickness=1, color=PAPER_LINE,
                       spaceBefore=6, spaceAfter=12)


def header(title, subtitle):
    return [Paragraph(title, styles['title']), Paragraph(subtitle, styles['subtitle']), hr()]


def formula_triangle(apex, apex_word, left, left_word, right, right_word, blank=False):
    w, h = 200, 175
    d = Drawing(w, h)
    apex_pt = (100, 160)
    left_pt = (15, 15)
    right_pt = (185, 15)
    mid_y = (apex_pt[1] + left_pt[1]) / 2
    t = 0.5
    lx_mid = apex_pt[0] + (left_pt[0] - apex_pt[0]) * t
    rx_mid = apex_pt[0] + (right_pt[0] - apex_pt[0]) * t

    d.add(Line(apex_pt[0], apex_pt[1], left_pt[0], left_pt[1], strokeColor=INK, strokeWidth=1.4))
    d.add(Line(apex_pt[0], apex_pt[1], right_pt[0], right_pt[1], strokeColor=INK, strokeWidth=1.4))
    d.add(Line(left_pt[0], left_pt[1], right_pt[0], right_pt[1], strokeColor=INK, strokeWidth=1.4))
    d.add(Line(lx_mid, mid_y, rx_mid, mid_y, strokeColor=INK, strokeWidth=1.4))
    d.add(Line(100, mid_y, 100, 15, strokeColor=INK, strokeWidth=1.4))

    if blank:
        d.add(String(100, 120, '?', fontName='Helvetica-Bold', fontSize=22,
                      textColor=INK_SOFT, textAnchor='middle'))
        d.add(String(58, 45, '?', fontName='Helvetica-Bold', fontSize=22,
                      textColor=INK_SOFT, textAnchor='middle'))
        d.add(String(142, 45, '?', fontName='Helvetica-Bold', fontSize=22,
                      textColor=INK_SOFT, textAnchor='middle'))
    else:
        d.add(String(100, 122, apex, fontName='Helvetica-Bold', fontSize=22,
                      textColor=BIO, textAnchor='middle'))
        d.add(String(100, 107, apex_word, fontName='Helvetica', fontSize=8,
                      textColor=INK_SOFT, textAnchor='middle'))
        d.add(String(58, 47, left, fontName='Helvetica-Bold', fontSize=20,
                      textColor=MATHS, textAnchor='middle'))
        d.add(String(58, 33, left_word, fontName='Helvetica', fontSize=8,
                      textColor=INK_SOFT, textAnchor='middle'))
        d.add(String(142, 47, right, fontName='Helvetica-Bold', fontSize=20,
                      textColor=MATHS, textAnchor='middle'))
        d.add(String(142, 33, right_word, fontName='Helvetica', fontSize=8,
                      textColor=INK_SOFT, textAnchor='middle'))
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


# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('cells_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Cells: Structure, Transport &amp; Division',
                 'Quick reference sheet &middot; Biology &amp; Maths &middot; keep handy for revision')

    s.append(Paragraph('1. Microscopy &amp; magnification', styles['h2']))
    s.append(Paragraph('An electron microscope has far higher resolving power than a light microscope (up to &times;1,000,000 vs &times;1,000), so it reveals much finer sub-cellular detail.', styles['body']))
    s.append(Paragraph('magnification = size of image &divide; size of real object &nbsp;&nbsp; or &nbsp;&nbsp; <b>M = I / R</b>', styles['bodyb']))
    s.append(Paragraph('Image and real size must be in the <b>same units</b> before dividing. 1 mm = 1000 &micro;m.', styles['body']))
    s.append(formula_triangle('I', 'image size', 'M', 'magnification', 'R', 'real size'))
    s.append(Paragraph('Cover <b>I</b> &rarr; M next to R &rarr; <b>I = M &times; R</b>. Cover <b>M</b> &rarr; I over R &rarr; <b>M = I / R</b>. Cover <b>R</b> &rarr; I over M &rarr; <b>R = I / M</b>.', styles['body']))

    s.append(Paragraph('2. Cell structures', styles['h2']))
    s.append(Paragraph('Animal &amp; plant cells are <b>eukaryotic</b> (genetic material in a nucleus). Bacterial cells are <b>prokaryotic</b> &mdash; smaller, with a single DNA loop and plasmids, not in a nucleus.', styles['body']))
    s.append(table([
        [headcell('Structure'), headcell('Animal'), headcell('Plant'), headcell('Bacterial'), headcell('Function')],
        [cell('Nucleus'), cell('&check;'), cell('&check;'), cell('&mdash;'), cell('Contains genetic material')],
        [cell('Cytoplasm'), cell('&check;'), cell('&check;'), cell('&check;'), cell('Most chemical reactions')],
        [cell('Cell membrane'), cell('&check;'), cell('&check;'), cell('&check;'), cell('Controls entry/exit')],
        [cell('Mitochondria'), cell('&check;'), cell('&check;'), cell('&mdash;'), cell('Respiration (releases energy)')],
        [cell('Ribosomes'), cell('&check;'), cell('&check;'), cell('&check;'), cell('Protein synthesis')],
        [cell('Cell wall'), cell('&mdash;'), cell('&check; (cellulose)'), cell('&check;'), cell('Strengthens the cell')],
        [cell('Chloroplasts'), cell('&mdash;'), cell('&check;'), cell('&mdash;'), cell('Photosynthesis')],
        [cell('Permanent vacuole'), cell('&mdash;'), cell('&check;'), cell('&mdash;'), cell('Cell sap, keeps cell rigid')],
        [cell('DNA loop &amp; plasmids'), cell('&mdash;'), cell('&mdash;'), cell('&check;'), cell('Genetic material (no nucleus)')],
    ], col_widths=[34 * mm, 15 * mm, 20 * mm, 18 * mm, 47 * mm]))

    s.append(Paragraph('3. Transport across membranes', styles['h2']))
    s.append(Paragraph('All three processes move particles across the cell membrane &mdash; the difference is <b>what</b> moves, <b>which way</b>, and whether <b>energy</b> is needed. A "concentration gradient" just means one side has more particles of something than the other.', styles['body']))
    s.append(table([
        [headcell('Process'), headcell('What moves'), headcell('Direction'), headcell('Energy'), headcell('Example')],
        [cell('<b>Diffusion</b>'), cell('Particles'), cell('High &rarr; low conc.'), cell('No'), cell('O<sub>2</sub> alveoli &rarr; blood')],
        [cell('<b>Osmosis</b>'), cell('Water only'), cell('High &rarr; low water conc., partially permeable membrane'), cell('No'), cell('Water into root hairs')],
        [cell('<b>Active transport</b>'), cell('Dissolved substances'), cell('Low &rarr; high conc. (against gradient)'), cell('<b>Yes</b>'), cell('Mineral ions into root hairs')],
    ], col_widths=[27 * mm, 23 * mm, 38 * mm, 16 * mm, 30 * mm]))
    s.append(Paragraph('<b>Diffusion</b> &mdash; the <b>net</b> movement of particles from an area of <b>higher concentration</b> to an area of <b>lower concentration</b>, until the particles are evenly spread out. It happens because particles are always randomly moving, and needs <b>no energy</b> from the cell. Example: oxygen diffuses from the air in the alveoli (high O<sub>2</sub>) into the blood (lower O<sub>2</sub>); carbon dioxide diffuses the opposite way.', styles['body']))
    s.append(Paragraph('<b>Osmosis</b> &mdash; a <b>special case of diffusion for water only</b>: the net movement of water from a region of <b>higher water concentration</b> to a region of <b>lower water concentration</b>, through a <b>partially permeable membrane</b> (one that lets small water molecules through but not larger dissolved particles). No energy is needed. Example: water moves from the soil (dilute, lots of water) into root hair cells (more concentrated cell sap, less water).', styles['body']))
    s.append(Paragraph('<b>Active transport</b> &mdash; the movement of dissolved substances from a <b>lower</b> to a <b>higher</b> concentration &mdash; i.e. <b>against</b> the concentration gradient, the opposite way to diffusion. Because this doesn\'t happen naturally, the cell must supply <b>energy from respiration</b> to make it happen. Example: mineral ions (e.g. nitrate) are often more concentrated <i>inside</i> root hair cells than in the soil, so they can only get in via active transport &mdash; diffusion alone couldn\'t move them "uphill".', styles['body']))
    s.append(Paragraph('<b>Exam tip:</b> for an "explain" question (like E3), always give the <b>direction</b> of movement first, say whether that is <b>with</b> or <b>against</b> the gradient, then link to <b>energy from respiration</b> if it\'s against the gradient. For a "define" question (E1/E2), state <b>what moves</b> and the <b>direction</b> &mdash; for osmosis, also mention "partially permeable membrane".', styles['note']))

    s.append(Paragraph('4. Cell division: mitosis &amp; meiosis', styles['h2']))
    s.append(Paragraph('Human body cells have <b>46 chromosomes</b> (23 pairs) &mdash; thread-like structures made of DNA that carry genes. Before any division, the cell first copies (replicates) all its chromosomes and organelles, so it has everything needed to make new complete cells.', styles['body']))
    s.append(Paragraph('<b>Mitosis</b> produces <b>2 genetically identical</b> cells, each with the full 46 chromosomes &mdash; used for two reasons: <b>growth</b> (making an organism bigger by adding new cells) and <b>repair</b> (replacing damaged or worn-out cells, e.g. healing skin). This is the only type of division most body cells ever use.', styles['body']))
    s.append(Paragraph('<b>Meiosis</b> only happens in reproductive organs (ovaries/testes), to make <b>gametes</b> (sex cells: eggs and sperm). The cell divides <b>twice</b>, producing <b>4 cells</b>, each with <b>half</b> the chromosome number (23, one from each pair) &mdash; and each gamete is <b>genetically different</b> from the others because the chromosome pairs are shuffled before splitting. At <b>fertilisation</b>, an egg (23) and sperm (23) fuse to restore the full number (46) in the new cell, which then divides by mitosis to grow into an embryo.', styles['body']))
    s.append(table([
        [headcell(''), headcell('Mitosis'), headcell('Meiosis')],
        [cell('Purpose'), cell('Growth &amp; repair'), cell('Making gametes')],
        [cell('Divisions'), cell('One'), cell('Two')],
        [cell('Cells produced'), cell('2'), cell('4')],
        [cell('Chromosome no.'), cell('Same as parent (46)'), cell('Half the parent (23)')],
        [cell('Genetically identical?'), cell('Yes'), cell('No &mdash; all different')],
    ], col_widths=[38 * mm, 60 * mm, 60 * mm]))
    s.append(Paragraph('<b>Exam tip:</b> "state the number of chromosomes and explain why" (like F2) needs three things &mdash; the body-cell number (46), the gamete number (23), <b>and</b> the reason: meiosis halves the number so that fertilisation (joining two gametes) can restore 46 without doubling it every generation.', styles['note']))

    s.append(Paragraph('5. Cell differentiation &amp; stem cells', styles['h2']))
    s.append(Paragraph('Early embryo cells are unspecialised <b>stem cells</b> &mdash; they can divide repeatedly and become almost any type of cell in the body. As the embryo develops, most cells <b>differentiate</b>: they change to become <b>specialised</b> for one particular job, developing a shape and sub-cellular structures suited to that function &mdash; e.g. a red blood cell loses its nucleus to carry more oxygen, a nerve cell grows a long fibre to carry electrical signals, a sperm cell grows a tail and packs in mitochondria for energy.', styles['body']))
    s.append(Paragraph('Differentiation is normally a <b>one-way process</b>: once a cell has specialised, it <b>cannot</b> change into a different cell type. This is why a nerve cell can never become a muscle cell, even though both came from the same original stem cell.', styles['body']))
    s.append(Paragraph('Most adult tissues keep a small number of <b>adult stem cells</b> (e.g. in bone marrow), which stay unspecialised and can divide to replace damaged or worn-out cells &mdash; but adult stem cells can usually only become a <b>limited range</b> of cell types (e.g. bone marrow stem cells make different blood cells). <b>Embryonic</b> stem cells are more versatile and can become <b>any</b> cell type, which is why scientists research them for treating diseases (e.g. repairing damaged nerves or growing new tissue) &mdash; though this raises ethical questions since it involves using embryos.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('cells_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Cells: Structure, Transport &amp; Division', 'Test &middot; 33 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 33'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Complete the formula triangle', styles['h2']))
    s.append(Paragraph('A1. Fill in the three blanks with I, M and R in the correct places.', styles['qtext']))
    s.append(formula_triangle(None, None, None, None, None, None, blank=True))
    s.append(Paragraph('[3 marks]', styles['marks']))

    s.append(Paragraph('Section B &mdash; Straight substitution', styles['h2']))
    s += q('B1', 'A cell has an image size of 6 mm and a real size of 0.3 mm. Calculate the magnification.', 2)
    s.append(Spacer(1, 10))
    s += q('B2', 'A structure has an image size of 15 mm and a real size of 0.05 mm. Calculate the magnification.', 2)
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section C &mdash; Rearrange and solve', styles['h2']))
    s += q('C1', 'A real structure is 0.002 mm across and is magnified &times;500. Calculate the image size, in mm. Show how you rearranged the equation.', 3)
    s.append(Spacer(1, 10))
    s += q('C2', 'An image measures 4 mm across at a magnification of &times;800. Calculate the real size, in mm. Show how you rearranged the equation.', 3)
    s.append(Spacer(1, 10))
    s += q('C3', 'A real structure is 20 &micro;m across and is magnified &times;50. Calculate the image size, in mm. (Convert units first.)', 3)
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section D &mdash; Cell structures', styles['h2']))
    s += q('D1', 'Name two structures found in a plant cell but not in an animal cell.', 2)
    s.append(Spacer(1, 10))
    s += q('D2', 'Name two structures found in a bacterial cell that are not found in an animal cell.', 2)
    s.append(Spacer(1, 10))
    s += q('D3', 'State the function of the mitochondria.', 1)
    s.append(Spacer(1, 10))
    s += q('D4', 'State the function of a chloroplast.', 1)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section E &mdash; Transport across membranes', styles['h2']))
    s += q('E1', 'Define diffusion.', 2)
    s.append(Spacer(1, 10))
    s += q('E2', 'Define osmosis, and state what makes it different from diffusion of a dissolved substance.', 2)
    s.append(Spacer(1, 10))
    s += q('E3', 'Explain why active transport requires energy from respiration, using the example of mineral ion uptake by plant root hairs.', 2)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section F &mdash; Cell division &amp; differentiation', styles['h2']))
    s += q('F1', 'State two reasons why body cells divide by mitosis.', 2)
    s.append(Spacer(1, 10))
    s += q('F2', 'State the number of chromosomes in a normal human body cell and in a human gamete, and explain why the gamete has this number.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('cells_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Cells: Structure, Transport &amp; Division', 'Answer sheet &middot; 33 marks total')

    s.append(Paragraph('Section A &mdash; Formula triangle', styles['h2']))
    s.append(Paragraph('Top cell = <b>I</b> (image size) &nbsp;&nbsp; Bottom-left = <b>M</b> (magnification) &nbsp;&nbsp; Bottom-right = <b>R</b> (real size)', styles['ans']))
    s.append(Paragraph('[1 mark each, 3 marks total]', styles['marks']))

    s.append(Paragraph('Section B &mdash; Straight substitution', styles['h2']))
    s.append(Paragraph('<b>B1.</b> M = I / R = 6 / 0.3 (1) &nbsp; M = <b>&times;20</b> (1)', styles['ans']))
    s.append(Paragraph('<b>B2.</b> M = I / R = 15 / 0.05 (1) &nbsp; M = <b>&times;300</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Rearrange and solve', styles['h2']))
    s.append(Paragraph('<b>C1.</b> I = M &times; R (1) &nbsp; I = 500 &times; 0.002 (1) &nbsp; I = <b>1 mm</b> (1)', styles['ans']))
    s.append(Paragraph('<b>C2.</b> R = I / M (1) &nbsp; R = 4 / 800 (1) &nbsp; R = <b>0.005 mm</b> (1)', styles['ans']))
    s.append(Paragraph('<b>C3.</b> 20 &micro;m = 0.02 mm (1) &nbsp; I = M &times; R = 50 &times; 0.02 (1) &nbsp; I = <b>1 mm</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Cell structures', styles['h2']))
    s.append(Paragraph('<b>D1.</b> Any two of: cell wall, chloroplasts, permanent vacuole (1 mark each, 2 marks total)', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Any two of: cell wall, single DNA loop / plasmids (note: bacterial cells do NOT have a nucleus, mitochondria or chloroplasts &mdash; do not accept these) (1 mark each, 2 marks total)', styles['ans']))
    s.append(Paragraph('<b>D3.</b> Site of respiration, which releases energy for the cell (1)', styles['ans']))
    s.append(Paragraph('<b>D4.</b> Site of photosynthesis (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Transport across membranes', styles['h2']))
    s.append(Paragraph('<b>E1.</b> The net movement of particles (1) from a region of higher concentration to a region of lower concentration (1).', styles['ans']))
    s.append(Paragraph('<b>E2.</b> The movement of water (1) from a region of higher water concentration to lower water concentration, through a partially permeable membrane (1).', styles['ans']))
    s.append(Paragraph('<b>E3.</b> Mineral ions move from a lower to a higher concentration in the root hair, i.e. against the concentration gradient (1); this does not happen naturally, so energy from respiration is needed to move them (1).', styles['ans']))

    s.append(Paragraph('Section F &mdash; Cell division &amp; differentiation', styles['h2']))
    s.append(Paragraph('<b>F1.</b> Growth (1) and repair of damaged tissue (1).', styles['ans']))
    s.append(Paragraph('<b>F2.</b> Body cell = 46 (1); gamete = 23 (1); because meiosis halves the chromosome number, so that fertilisation (joining two gametes) restores the normal number, 46 (1).', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly rearranged equation and correct substitution even if the '
        'final answer contains an arithmetic error. In Sections D&ndash;F, accept any scientifically correct equivalent wording.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
