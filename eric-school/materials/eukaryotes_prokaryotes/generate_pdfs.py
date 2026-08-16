# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Eukaryotes, Prokaryotes & the Scale of Cells (AQA 8465 4.1.3, Foundation tier)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.graphics.shapes import Drawing, Rect, String, Line

INK = colors.HexColor('#23201A')
INK_SOFT = colors.HexColor('#6B6355')
BIO = colors.HexColor('#2F8B57')
MATHS = colors.HexColor('#3A5E85')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#EAF2ED')
BOX_FILL = colors.HexColor('#DDE6EF')
BOX_FILL_HL = colors.HexColor('#DFF0E5')

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


def ladder_box(d, y, label, note, highlight=False):
    d.add(Rect(60, y, 180, 40, 6, fillColor=(BOX_FILL_HL if highlight else BOX_FILL),
                strokeColor=(BIO if highlight else MATHS), strokeWidth=(1.8 if highlight else 1.3)))
    d.add(String(150, y + 15, label, fontName='Helvetica-Bold', fontSize=13,
                  textColor=INK, textAnchor='middle'))
    for i, line in enumerate(note):
        d.add(String(250, y + 25 - i * 13, line, fontName='Helvetica', fontSize=9.5,
                      textColor=(BIO if highlight else INK_SOFT), textAnchor='start'))


def ladder_diagram():
    w, h = 400, 240
    d = Drawing(w, h)
    line = Line(150, 20, 150, 220, strokeColor=INK_SOFT, strokeWidth=1)
    line.strokeDashArray = [3, 4]
    d.add(line)
    ladder_box(d, 180, 'metre (m)', ['e.g. a doorway'])
    d.add(String(80, 165, '×1000 ↓', fontName='Helvetica-Bold', fontSize=9, textColor=MATHS, textAnchor='middle'))
    d.add(String(210, 165, '↑ ÷1000', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor('#B5762A'), textAnchor='middle'))
    ladder_box(d, 130, 'millimetre (mm)', ['e.g. a grain of rice'])
    d.add(String(80, 115, '×1000 ↓', fontName='Helvetica-Bold', fontSize=9, textColor=MATHS, textAnchor='middle'))
    d.add(String(210, 115, '↑ ÷1000', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor('#B5762A'), textAnchor='middle'))
    ladder_box(d, 80, 'micrometre (µm)', ['bacteria: 1-5 µm', 'cells: 10-100 µm'], highlight=True)
    d.add(String(80, 65, '×1000 ↓', fontName='Helvetica-Bold', fontSize=9, textColor=MATHS, textAnchor='middle'))
    d.add(String(210, 65, '↑ ÷1000', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor('#B5762A'), textAnchor='middle'))
    ladder_box(d, 30, 'nanometre (nm)', ['inside cells'])
    return d


# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('eukaryotes_prokaryotes_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Eukaryotes, Prokaryotes &amp; the Scale of Cells',
                 'Quick reference sheet &middot; Biology &amp; Maths &middot; keep handy for revision')

    s.append(Paragraph('1. Eukaryotic vs prokaryotic', styles['h2']))
    s.append(Paragraph('Animal and plant cells are <b>eukaryotic</b>: genetic material is enclosed in a nucleus. Bacterial cells are <b>prokaryotic</b>: much smaller, with a single DNA loop (plus possible plasmids) free in the cytoplasm, not in a nucleus.', styles['body']))
    s.append(table([
        [headcell('Feature'), headcell('Eukaryotic (animal/plant)'), headcell('Prokaryotic (bacteria)')],
        [cell('Size'), cell('Larger'), cell('Much smaller')],
        [cell('Genetic material'), cell('Enclosed in a nucleus'), cell('Single DNA loop, free in cytoplasm')],
        [cell('Plasmids'), cell('None'), cell('May have one or more')],
        [cell('Cytoplasm &amp; cell membrane'), cell('&check;'), cell('&check;')],
        [cell('Cell wall'), cell('Plants only (cellulose)'), cell('&check;')],
    ], col_widths=[40 * mm, 55 * mm, 59 * mm]))
    s.append(Paragraph('<b>The one thing to remember:</b> nucleus present &rarr; eukaryotic. No nucleus (DNA loop instead) &rarr; prokaryotic.', styles['bodyb']))
    s.append(Paragraph('<b>Where the names come from:</b> "eukaryotic" = true nucleus; "prokaryotic" = before nucleus. Animal and plant cells seal their DNA inside a nuclear membrane; a bacterium’s DNA is a single circular strand loose in the cytoplasm, with no membrane around it.', styles['body']))
    s.append(Paragraph('<b>Plasmids</b> are small circular pieces of DNA, separate from the main DNA loop &mdash; much smaller, carrying just a few genes (e.g. antibiotic resistance) rather than the full genome. They can be copied and passed between bacteria independently of the main loop, which is how antibiotic resistance spreads, and they can be extracted and modified to make bacteria produce useful proteins such as insulin (genetic engineering).', styles['body']))

    s.append(Paragraph('2. The scale of cells', styles['h2']))
    s.append(Paragraph('Each step down this ladder is &times;1000 smaller (each step up is &divide;1000):', styles['body']))
    s.append(ladder_diagram())
    s.append(Paragraph('Bacteria are about 1&ndash;5 &micro;m across; animal and plant cells are about 10&ndash;100 &micro;m across &mdash; roughly 10&times; bigger. <b>Worked conversion:</b> 0.02 mm &times; 1000 = <b>20 &micro;m</b> (mm &rarr; &micro;m, multiply by 1000; &micro;m &rarr; mm, divide by 1000).', styles['body']))
    s.append(Paragraph('You may also see <b>centimetres (cm)</b>: 1 cm = 10 mm. Cells are never measured in cm &mdash; it only appears on the exam skills list.', styles['body']))

    s.append(Paragraph('3. Standard form for tiny numbers', styles['h2']))
    s.append(Paragraph('Standard form: <b>A &times; 10<sup>n</sup></b>, where A is between 1 and 10.', styles['body']))
    s.append(table([
        [headcell('Given'), headcell('In metres'), headcell('Standard form')],
        [cell('2 &micro;m'), cell('0.000002 m'), cell('2 &times; 10<sup>-6</sup> m')],
        [cell('25 &micro;m'), cell('0.000025 m'), cell('2.5 &times; 10<sup>-5</sup> m')],
    ], col_widths=[30 * mm, 40 * mm, 84 * mm]))
    s.append(Paragraph('Shortcut: 1 &micro;m = 10<sup>-6</sup> m, so attach &times;10<sup>-6</sup> to a &micro;m value and adjust so the first digit is between 1 and 10.', styles['body']))

    s.append(Paragraph('4. Order of magnitude calculations', styles['h2']))
    s.append(Paragraph('An "order of magnitude" means a <b>factor of 10</b>. Divide the bigger size by the smaller size to find how many times bigger it is.', styles['body']))
    s.append(Paragraph('<b>Worked example:</b> bacterium 2 &micro;m, animal cell 20 &micro;m. &nbsp; 20 &divide; 2 = <b>10</b> &mdash; the animal cell is one order of magnitude bigger.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('eukaryotes_prokaryotes_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Eukaryotes, Prokaryotes &amp; the Scale of Cells', 'Test &middot; 24 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 24'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Eukaryotic or prokaryotic?', styles['h2']))
    s.append(Paragraph('State whether each description is eukaryotic or prokaryotic.', styles['qtext']))
    s.append(Spacer(1, 4))
    s.append(Paragraph('(a) A cell with genetic material enclosed in a nucleus.', styles['qtext']))
    s.append(Paragraph('(b) A cell with genetic material as a single DNA loop, not enclosed in a nucleus.', styles['qtext']))
    s.append(Paragraph('(c) A cell with plasmids.', styles['qtext']))
    s.append(Paragraph('(d) A cell with mitochondria.', styles['qtext']))
    s.append(Paragraph('[4 marks]', styles['marks']))

    s.append(Paragraph('Section B &mdash; Bacterial cell structure', styles['h2']))
    s += q('B1', 'List the three structures found in a bacterial cell.', 3)
    s.append(Spacer(1, 10))
    s += q('B2', 'State what a plasmid is.', 1)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section C &mdash; Unit conversion', styles['h2']))
    s += q('C1', 'Convert 0.05 mm to micrometres.', 2)
    s.append(Spacer(1, 10))
    s += q('C2', 'Convert 3000 nanometres to micrometres.', 2)
    s.append(Spacer(1, 10))
    s += q('C3', 'Convert 2 micrometres to millimetres.', 2)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section D &mdash; Standard form', styles['h2']))
    s += q('D1', 'A bacterium is 2 &micro;m across. Write this in metres, using standard form.', 2)
    s.append(Spacer(1, 10))
    s += q('D2', 'An animal cell is 25 &micro;m across. Write this in metres, using standard form.', 2)
    s.append(Spacer(1, 10))
    s += q('D3', 'Convert 4 &times; 10<sup>-5</sup> m to micrometres.', 2)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section E &mdash; Order of magnitude', styles['h2']))
    s += q('E1', 'A bacterium is about 2 &micro;m across and an animal cell is about 20 &micro;m across. Calculate how many times bigger the animal cell is, and state this as an order of magnitude.', 2)
    s.append(Spacer(1, 10))
    s += q('E2', 'A plant cell is 4 &times; 10<sup>-5</sup> m wide and a bacterium is 2 &times; 10<sup>-6</sup> m wide. Calculate how many times wider the plant cell is.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('eukaryotes_prokaryotes_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Eukaryotes, Prokaryotes &amp; the Scale of Cells', 'Answer sheet &middot; 24 marks total')

    s.append(Paragraph('Section A &mdash; Eukaryotic or prokaryotic?', styles['h2']))
    s.append(Paragraph('(a) Eukaryotic (1) &nbsp;&nbsp; (b) Prokaryotic (1) &nbsp;&nbsp; (c) Prokaryotic (1) &nbsp;&nbsp; (d) Eukaryotic (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Bacterial cell structure', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Cytoplasm (1), cell membrane (1), cell wall (1).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> A small ring of DNA, separate from the main DNA loop (1).', styles['ans']))

    s.append(Paragraph('Section C &mdash; Unit conversion', styles['h2']))
    s.append(Paragraph('<b>C1.</b> 0.05 &times; 1000 (1) &nbsp; = <b>50 &micro;m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>C2.</b> 3000 &divide; 1000 (1) &nbsp; = <b>3 &micro;m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>C3.</b> 2 &divide; 1000 (1) &nbsp; = <b>0.002 mm</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Standard form', styles['h2']))
    s.append(Paragraph('<b>D1.</b> 2 &micro;m = 0.000002 m (1) &nbsp; = <b>2 &times; 10<sup>-6</sup> m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>D2.</b> 25 &micro;m = 0.000025 m (1) &nbsp; = <b>2.5 &times; 10<sup>-5</sup> m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>D3.</b> 4 &times; 10<sup>-5</sup> m = 0.00004 m (1) &nbsp; = <b>40 &micro;m</b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Order of magnitude', styles['h2']))
    s.append(Paragraph('<b>E1.</b> 20 &divide; 2 = 10 times bigger (1) &nbsp; one order of magnitude (1)', styles['ans']))
    s.append(Paragraph('<b>E2.</b> (4 &times; 10<sup>-5</sup>) &divide; (2 &times; 10<sup>-6</sup>) = 20 (1) &nbsp; <b>20 times wider</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for correct working even if the final answer contains an arithmetic '
        'error. Accept any scientifically correct equivalent wording in Sections A and B.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
