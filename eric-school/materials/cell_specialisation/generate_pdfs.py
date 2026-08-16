# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Cell Specialisation (AQA 8465 4.1.1/4.1.3, Foundation tier)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK = colors.HexColor('#23201A')
INK_SOFT = colors.HexColor('#6B6355')
BIO = colors.HexColor('#2F8B57')
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
    doc = SimpleDocTemplate('cell_specialisation_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Cell Specialisation',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('The 3-step method', styles['h2']))
    s.append(Paragraph('Every "explain how structure relates to function" question uses the same three steps &mdash; even for a cell you have never seen before:', styles['body']))
    s.append(Paragraph('<b>1.</b> Name the structural feature. &nbsp;&nbsp; <b>2.</b> Say what it physically does (longer/more/thinner). &nbsp;&nbsp; <b>3.</b> Link it to the cell&rsquo;s job.', styles['bodyb']))

    s.append(Paragraph('1. Specialised animal cells', styles['h2']))
    s.append(table([
        [headcell('Cell'), headcell('Key feature(s)'), headcell('Why it helps')],
        [cell('<b>Sperm cell</b>'), cell('Long tail; many mitochondria; acrosome (enzyme tip)'), cell('Swims to the egg; energy for swimming; digests through the egg membrane')],
        [cell('<b>Nerve cell</b>'), cell('Long axon; branched endings; insulating layer'), cell('Carries signals long distances; connects to many cells; speeds up the signal')],
        [cell('<b>Muscle cell</b>'), cell('Long fibre that contracts; many mitochondria'), cell('Shortening causes movement; energy for contraction')],
    ], col_widths=[26 * mm, 56 * mm, 61 * mm]))

    s.append(Paragraph('2. Specialised plant cells', styles['h2']))
    s.append(table([
        [headcell('Cell'), headcell('Key feature(s)'), headcell('Why it helps')],
        [cell('<b>Root hair cell</b>'), cell('Long hair-like extension'), cell('Large surface area for absorbing water &amp; mineral ions from soil')],
        [cell('<b>Xylem cell</b>'), cell('Hollow tube, no contents; lignin-thickened walls'), cell('Water flows through easily; strong enough to support the plant')],
        [cell('<b>Phloem cell</b>'), cell('Sieve tube with pores; companion cell alongside'), cell('Sugars flow through; companion cell provides energy for active transport of sugars')],
    ], col_widths=[26 * mm, 56 * mm, 61 * mm]))

    s.append(Paragraph('3. Worked example (unseen cell)', styles['h2']))
    s.append(Paragraph('<i>"A cell lining the small intestine has many finger-like projections on one surface. Suggest how this helps it absorb nutrients."</i>', styles['body']))
    s.append(Paragraph('1. Feature: finger-like projections. &nbsp; 2. What it does: greatly increases surface area. &nbsp; 3. Link: more surface area means more nutrients absorbed at once.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('cell_specialisation_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Cell Specialisation', 'Test &middot; 24 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 24'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Specialised animal cells', styles['h2']))
    s += q('A1', 'State one way a sperm cell is adapted for its function.', 2)
    s.append(Spacer(1, 8))
    s += q('A2', 'State one way a nerve cell is adapted for its function.', 2)
    s.append(Spacer(1, 8))
    s += q('A3', 'State one way a muscle cell is adapted for its function.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Specialised plant cells', styles['h2']))
    s += q('B1', 'State one way a root hair cell is adapted for its function.', 2)
    s.append(Spacer(1, 8))
    s += q('B2', 'State one way a xylem cell is adapted for its function.', 2)
    s.append(Spacer(1, 8))
    s += q('B3', 'State one way a phloem cell is adapted for its function.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; Explain in full', styles['h2']))
    s += q('C1', 'Explain how the structure of a sperm cell is adapted to its function.', 3)
    s.append(Spacer(1, 10))
    s += q('C2', 'Explain how the structure of a xylem cell is adapted to its function.', 3)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Unfamiliar cells', styles['h2']))
    s += q('D1', 'A cell lining the lung has many cilia (tiny hair-like projections) on its surface that constantly beat back and forth. Suggest how this structure helps the cell\'s function.', 3)
    s.append(Spacer(1, 10))
    s += q('D2', 'A gland cell that secretes hormones into the blood contains an unusually large number of mitochondria. Suggest why.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('cell_specialisation_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Cell Specialisation', 'Answer sheet &middot; 24 marks total')

    s.append(Paragraph('Section A &mdash; Specialised animal cells', styles['h2']))
    s.append(Paragraph('<b>A1.</b> Long tail (1), lets it swim to the egg (1). <i>[or: many mitochondria (1), for energy to swim (1); or: acrosome (1), digests through the egg membrane (1)]</i>', styles['ans']))
    s.append(Paragraph('<b>A2.</b> Long axon (1), carries signals over long distances (1). <i>[or: branched endings (1), connects to many other cells (1); or: insulating layer (1), speeds up the signal (1)]</i>', styles['ans']))
    s.append(Paragraph('<b>A3.</b> Long fibre that contracts (1), shortening causes movement (1). <i>[or: many mitochondria (1), energy for contraction (1)]</i>', styles['ans']))

    s.append(Paragraph('Section B &mdash; Specialised plant cells', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Long hair-like extension (1), gives a large surface area for absorbing water/mineral ions (1).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> Hollow tube with no contents (1), lets water flow through easily (1). <i>[or: lignin-thickened walls (1), gives strength/support (1)]</i>', styles['ans']))
    s.append(Paragraph('<b>B3.</b> Sieve tube with pores (1), lets sugars flow through (1). <i>[or: companion cell alongside (1), provides energy for active transport of sugars (1)]</i>', styles['ans']))

    s.append(Paragraph('Section C &mdash; Explain in full', styles['h2']))
    s.append(Paragraph('<b>C1.</b> Long tail lets it swim to the egg (1); many mitochondria release energy for swimming (1); acrosome contains enzymes that digest through the egg membrane (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> Hollow tube with no cell contents lets water flow through easily (1); walls are thickened with lignin, making it strong (1); this lets it support the plant as well as transport water (1).', styles['ans']))

    s.append(Paragraph('Section D &mdash; Unfamiliar cells', styles['h2']))
    s.append(Paragraph('<b>D1.</b> The cilia beat back and forth (1); this sweeps mucus (and trapped dust/bacteria) along and out of the airway (1); this helps protect the lungs from infection/damage (1).', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Secreting hormones requires energy (e.g. for active transport) (1); mitochondria are the site of respiration, which releases energy (1); more mitochondria means more energy is available for secretion (1).', styles['ans']))

    s.append(Paragraph(
        'Marking note: accept any scientifically correct feature/function pair in Sections A and B, even if different '
        'from the example shown &mdash; one correctly linked feature is worth both marks. In Section D, accept any '
        'logically sound application of the 3-step method.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
