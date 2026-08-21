# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Plants, Part 1: Structure & Transpiration (AQA 8465 4.2.2, Foundation tier)."""

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
    doc = SimpleDocTemplate('plants_1_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Plants, Part 1: Structure &amp; Transpiration',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('1. Plant organs &amp; meristem tissue', styles['h2']))
    s.append(Paragraph('<b>Root</b>: anchors the plant; absorbs water &amp; mineral ions (root hair cells give a large surface area).', styles['body']))
    s.append(Paragraph('<b>Stem</b>: supports the plant, holds leaves up to the light; transports substances between roots and leaves.', styles['body']))
    s.append(Paragraph('<b>Leaf</b>: main site of photosynthesis; has stomata for gas exchange and water loss.', styles['body']))
    s.append(Paragraph(
        '<b>Meristem tissue</b> is found at the tips of roots and shoots. It is made of unspecialised cells that '
        'divide continuously by mitosis, producing new cells throughout the plant\'s life. These new cells then '
        '<b>differentiate</b> into specialised cells (e.g. root hair, xylem, phloem) &mdash; this is how a plant keeps growing.', styles['body']))

    s.append(Paragraph('2. Xylem &amp; phloem: the transport tissues', styles['h2']))
    s.append(table([
        [headcell('Tissue'), headcell('Transports'), headcell('Direction'), headcell('Cells')],
        [cell('<b>Xylem</b>'), cell('Water &amp; dissolved mineral ions'), cell('One way: up (roots &rarr; leaves)'), cell('Dead, no cytoplasm, walls strengthened with lignin')],
        [cell('<b>Phloem</b>'), cell('Dissolved sugars (mainly sucrose)'), cell('Both ways (up &amp; down)'), cell('Living cells')],
    ], col_widths=[22 * mm, 48 * mm, 48 * mm, 55 * mm]))
    s.append(Paragraph('Moving sugars around the plant through phloem is called <b>translocation</b>.', styles['body']))

    s.append(Paragraph('3. Transpiration: what it is &amp; the pathway', styles['h2']))
    s.append(Paragraph(
        '<b>Transpiration</b> is the loss of water vapour from a plant\'s leaves, mainly through the stomata, by '
        'evaporation and diffusion. As water is lost, more is drawn up from the roots to replace it &mdash; this '
        'continuous flow is the <b>transpiration stream</b>.', styles['body']))
    s.append(Paragraph('The pathway, step by step:', styles['bodyb']))
    s.append(Paragraph('1. Water is absorbed from the soil by <b>root hair cells</b>, by osmosis', styles['body']))
    s.append(Paragraph('2. It moves across the root and into the <b>xylem</b>', styles['body']))
    s.append(Paragraph('3. It travels up the xylem, through the stem, into the leaves', styles['body']))
    s.append(Paragraph('4. It evaporates from cells inside the leaf into the air spaces, then diffuses out through tiny pores called <b>stomata</b>', styles['body']))
    s.append(Paragraph('5. Each stoma is surrounded by a pair of <b>guard cells</b>, which control whether it is open or closed', styles['body']))

    s.append(Paragraph('4. Factors affecting the rate of transpiration', styles['h2']))
    s.append(table([
        [headcell('Factor'), headcell('Increases the rate when...'), headcell('Why')],
        [cell('Temperature'), cell('higher'), cell('molecules have more energy, so evaporate &amp; diffuse faster')],
        [cell('Humidity'), cell('lower'), cell('bigger difference in water vapour concentration inside/outside the leaf')],
        [cell('Air movement (wind)'), cell('higher'), cell('removes water vapour from around the leaf, keeping the gradient steep')],
        [cell('Light intensity'), cell('higher'), cell('more stomata open (for gas exchange), so more water can escape')],
    ], col_widths=[35 * mm, 40 * mm, 98 * mm]))
    s.append(Paragraph(
        'A <b>potometer</b> measures the rate of water uptake by a cut shoot (used as an estimate of transpiration '
        'rate) by timing how far an air bubble moves along a capillary tube.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('plants_1_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Plants, Part 1: Structure &amp; Transpiration', 'Test &middot; 31 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 31'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Plant organs &amp; meristem tissue', styles['h2']))
    s += q('A1', 'State one function each of the root, the stem, and the leaf.', 3)
    s.append(Spacer(1, 8))
    s += q('A2', 'What is meristem tissue?', 1)
    s.append(Spacer(1, 8))
    s += q('A3', 'Where in a plant would you find meristem tissue?', 1)
    s.append(Spacer(1, 8))
    s += q('A4', 'Explain why meristem tissue is essential for a plant to keep growing throughout its life.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Xylem &amp; phloem', styles['h2']))
    s += q('B1', 'Name the plant tissue that transports water and dissolved mineral ions from the roots to the leaves.', 1)
    s.append(Spacer(1, 8))
    s += q('B2', 'Name the plant tissue that transports dissolved sugars around the plant.', 1)
    s.append(Spacer(1, 8))
    s += q('B3', 'State the direction(s) in which substances move in xylem, and in phloem.', 2)
    s.append(Spacer(1, 8))
    s += q('B4', 'Xylem cells are dead, with no cytoplasm, and their walls are strengthened with lignin. Explain how this helps xylem carry out its function.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; Transpiration', styles['h2']))
    s += q('C1', 'Define transpiration.', 2)
    s.append(Spacer(1, 8))
    s += q('C2', 'Describe the pathway water takes from the soil to the air, starting at the root hair cell.', 4)
    s.append(Spacer(1, 8))
    s += q('C3', 'What is the name of the small pores water vapour diffuses out through, mostly on the underside of a leaf?', 1)
    s.append(Spacer(1, 8))
    s += q('C4', 'What is the function of guard cells?', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Factors affecting transpiration rate', styles['h2']))
    s += q('D1', 'State four factors that affect the rate of transpiration.', 4)
    s.append(Spacer(1, 8))
    s += q('D2', 'Explain why increasing the temperature increases the rate of transpiration.', 2)
    s.append(Spacer(1, 8))
    s += q('D3', 'Explain why increasing air movement (wind) around a plant increases the rate of transpiration.', 2)
    s.append(Spacer(1, 8))
    s += q('D4', 'A student wants to measure the rate of water uptake by a cut plant shoot. Name a piece of apparatus they could use.', 1)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('plants_1_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Plants, Part 1: Structure &amp; Transpiration', 'Answer sheet &middot; 31 marks total')

    s.append(Paragraph('Section A &mdash; Plant organs &amp; meristem tissue', styles['h2']))
    s.append(Paragraph('<b>A1.</b> Root: anchors the plant / absorbs water and mineral ions (1). Stem: supports the plant / holds leaves up to the light / transports substances (1). Leaf: main site of photosynthesis / gas exchange (1).', styles['ans']))
    s.append(Paragraph('<b>A2.</b> Unspecialised (undifferentiated) cells that continuously divide by mitosis to produce new cells (1).', styles['ans']))
    s.append(Paragraph('<b>A3.</b> At the tips of roots and shoots (root tip / shoot tip) (1).', styles['ans']))
    s.append(Paragraph('<b>A4.</b> New cells produced by meristem tissue can differentiate into specialised cells (1), allowing the plant to grow new tissue/organs throughout its life, not just when young (1).', styles['ans']))

    s.append(Paragraph('Section B &mdash; Xylem &amp; phloem', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Xylem (1).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> Phloem (1).', styles['ans']))
    s.append(Paragraph('<b>B3.</b> Xylem: one direction only, upwards, from roots to leaves (1). Phloem: both directions, up and down (1).', styles['ans']))
    s.append(Paragraph('<b>B4.</b> No cytoplasm/being dead leaves a hollow tube, so water can flow through with little resistance (1); lignin strengthens the walls, helping xylem withstand the pressure of water movement and support the plant (1).', styles['ans']))

    s.append(Paragraph('Section C &mdash; Transpiration', styles['h2']))
    s.append(Paragraph('<b>C1.</b> The loss of water vapour (1) from a plant\'s leaves, mainly through the stomata, by evaporation and diffusion (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> Absorbed from the soil by root hair cells, by osmosis (1); moves across the root into the xylem (1); travels up the xylem through the stem to the leaves (1); evaporates from cells inside the leaf and diffuses out through the stomata (1).', styles['ans']))
    s.append(Paragraph('<b>C3.</b> Stomata (1).', styles['ans']))
    s.append(Paragraph('<b>C4.</b> Guard cells control the opening and closing of stomata (1); e.g. opening them for gas exchange, or closing them to reduce water loss (1).', styles['ans']))

    s.append(Paragraph('Section D &mdash; Factors affecting transpiration rate', styles['h2']))
    s.append(Paragraph('<b>D1.</b> Any four: temperature (1); humidity (1); air movement/wind (1); light intensity (1).', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Higher temperature gives water molecules more energy, so they evaporate faster (1); this increases the rate of diffusion out of the stomata (1).', styles['ans']))
    s.append(Paragraph('<b>D3.</b> Wind removes water vapour from around the leaf (1), maintaining a steeper concentration gradient between the inside and outside of the leaf, increasing diffusion (1).', styles['ans']))
    s.append(Paragraph('<b>D4.</b> A potometer (1).', styles['ans']))

    s.append(Paragraph(
        'Marking note: accept any scientifically correct alternative answer with the same reasoning, even if '
        'different from the example shown &mdash; award marks for a correctly linked point, not for matching '
        'these exact words.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
