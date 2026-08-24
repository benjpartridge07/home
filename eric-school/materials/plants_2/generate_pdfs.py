# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Plants, Part 2: Photosynthesis (AQA 8465 4.2.2, Foundation tier)."""

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
    'eqn': ParagraphStyle('eqn', fontName='Helvetica-Bold', fontSize=11.5,
                           textColor=INK, alignment=1, spaceBefore=4, spaceAfter=4),
    'eqncond': ParagraphStyle('eqncond', fontName='Helvetica-Oblique', fontSize=9,
                               textColor=INK_SOFT, alignment=1, spaceAfter=10),
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
    doc = SimpleDocTemplate('plants_2_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Plants, Part 2: Photosynthesis',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('1. Where photosynthesis happens', styles['h2']))
    s.append(Paragraph(
        'Photosynthesis takes place inside <b>chloroplasts</b>, which contain <b>chlorophyll</b> &mdash; a green '
        'pigment that absorbs light energy. <b>Palisade mesophyll cells</b>, near the top of the leaf, are packed '
        'with chloroplasts and adapted to absorb the most light.', styles['body']))

    s.append(Paragraph('2. The photosynthesis equation', styles['h2']))
    s.append(Paragraph('carbon dioxide + water &rarr; glucose + oxygen', styles['eqn']))
    s.append(Paragraph('(light energy, absorbed by chlorophyll, in the chloroplasts)', styles['eqncond']))
    s.append(Paragraph(
        'Photosynthesis is <b>endothermic</b> &mdash; it takes in light energy rather than releasing it. CO<sub>2</sub> diffuses '
        'in through the stomata; water arrives via the xylem. Glucose can be used for respiration, stored as starch, '
        'or used to make cellulose or proteins. Oxygen is released as a waste product through the stomata.', styles['body']))

    s.append(Paragraph('3. Factors affecting the rate of photosynthesis', styles['h2']))
    s.append(table([
        [headcell('Factor'), headcell('Increases the rate when...'), headcell('Why')],
        [cell('Light intensity'), cell('higher'), cell('more light energy for chlorophyll to absorb')],
        [cell('CO<sub>2</sub> concentration'), cell('higher'), cell('more raw material available for the reaction')],
        [cell('Temperature'), cell('higher, up to a point'), cell('reactions speed up; too hot denatures enzymes, slowing it back down')],
    ], col_widths=[38 * mm, 45 * mm, 90 * mm]))
    s.append(Paragraph(
        'A <b>limiting factor</b> is whichever factor is in shortest supply, stopping the rate rising further even if '
        'the other two increase &mdash; shown as the point a rate graph levels off.', styles['body']))

    s.append(Paragraph('4. Translocation', styles['h2']))
    s.append(Paragraph(
        'Glucose made in the leaf is often converted to <b>sucrose</b> and transported around the plant (to growing '
        'parts or storage organs) through the <b>phloem</b>, in both directions. This is called <b>translocation</b>.', styles['body']))

    s.append(Paragraph('5. Plant nutrition &amp; disease', styles['h2']))
    s.append(table([
        [headcell('Deficiency'), headcell('Symptom'), headcell('Why')],
        [cell('Nitrate'), cell('Stunted growth'), cell('needed to make proteins, for cell growth')],
        [cell('Magnesium'), cell('Yellow leaves (chlorosis)'), cell('needed to make chlorophyll')],
    ], col_widths=[30 * mm, 55 * mm, 88 * mm]))
    s.append(Paragraph(
        'Plants can also be affected by disease (fungi, bacteria, viruses) or insect attack &mdash; look for stunted '
        'growth, leaf spots, decay, growths, discolouration or wilting, and compare against reference charts to identify the cause.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('plants_2_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Plants, Part 2: Photosynthesis', 'Test &middot; 30 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 30'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Where photosynthesis happens', styles['h2']))
    s += q('A1', 'Name the organelle where photosynthesis takes place.', 1)
    s.append(Spacer(1, 8))
    s += q('A2', 'Name the green pigment that absorbs light energy for photosynthesis.', 1)
    s.append(Spacer(1, 8))
    s += q('A3', 'Palisade mesophyll cells are found near the top of the leaf and are packed with chloroplasts. Explain how this adapts them for photosynthesis.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; The photosynthesis equation', styles['h2']))
    s += q('B1', 'Write the word equation for photosynthesis.', 2)
    s.append(Spacer(1, 8))
    s += q('B2', 'State where the two reactants for photosynthesis come from.', 2)
    s.append(Spacer(1, 8))
    s += q('B3', 'Explain why photosynthesis is described as an endothermic reaction.', 2)
    s.append(Spacer(1, 8))
    s += q('B4', 'State three things a plant might do with the glucose it produces.', 3)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; Factors affecting the rate', styles['h2']))
    s += q('C1', 'State three factors that affect the rate of photosynthesis.', 3)
    s.append(Spacer(1, 8))
    s += q('C2', 'Explain why increasing carbon dioxide concentration increases the rate of photosynthesis.', 2)
    s.append(Spacer(1, 8))
    s += q('C3', 'Explain why photosynthesis rate falls at very high temperatures, even though light and CO2 are plentiful.', 2)
    s.append(Spacer(1, 8))
    s += q('C4', 'What name is given to the factor that is limiting the rate of photosynthesis at a given moment?', 1)
    s.append(Spacer(1, 8))
    s += q('C5', 'A student increases light intensity but the rate of photosynthesis does not increase. Suggest why.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Translocation, nutrition &amp; disease', styles['h2']))
    s += q('D1', 'What is translocation?', 2)
    s.append(Spacer(1, 8))
    s += q('D2', 'Name the transport tissue involved in translocation.', 1)
    s.append(Spacer(1, 8))
    s += q('D3', 'A plant has yellow leaves but is growing at a normal rate. Suggest which mineral ion it is short of, and explain the symptom.', 2)
    s.append(Spacer(1, 8))
    s += q('D4', 'A plant is stunted (small) for its age. Suggest which mineral ion it is short of, and explain why this causes the symptom.', 2)
    s.append(Spacer(1, 8))
    s += q('D5', 'Give three visible signs that a plant might be diseased.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('plants_2_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Plants, Part 2: Photosynthesis', 'Answer sheet &middot; 30 marks total')

    s.append(Paragraph('Section A &mdash; Where photosynthesis happens', styles['h2']))
    s.append(Paragraph('<b>A1.</b> Chloroplast (1).', styles['ans']))
    s.append(Paragraph('<b>A2.</b> Chlorophyll (1).', styles['ans']))
    s.append(Paragraph('<b>A3.</b> Being near the top of the leaf means they receive more light (1); having many chloroplasts means more chlorophyll is available to absorb it, increasing the rate of photosynthesis (1).', styles['ans']))

    s.append(Paragraph('Section B &mdash; The photosynthesis equation', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Carbon dioxide + water &rarr; glucose + oxygen (2, allow 1 if one side is wrong/missing).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> Carbon dioxide diffuses in through the stomata (1); water is delivered by the xylem (1).', styles['ans']))
    s.append(Paragraph('<b>B3.</b> Endothermic reactions take in energy from the surroundings (1); photosynthesis takes in light energy to drive the reaction (1).', styles['ans']))
    s.append(Paragraph('<b>B4.</b> Any three: used for respiration (1); converted to starch for storage (1); used to make cellulose for cell walls (1); used to make plant proteins (1); converted to sucrose for transport (1).', styles['ans']))

    s.append(Paragraph('Section C &mdash; Factors affecting the rate', styles['h2']))
    s.append(Paragraph('<b>C1.</b> Light intensity (1); carbon dioxide concentration (1); temperature (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> CO<sub>2</sub> is a raw material/reactant for photosynthesis (1); more of it available means the reaction can proceed faster (1).', styles['ans']))
    s.append(Paragraph('<b>C3.</b> High temperatures denature the enzymes needed for the reaction (1); denatured enzymes can no longer catalyse the reaction efficiently, so the rate falls (1).', styles['ans']))
    s.append(Paragraph('<b>C4.</b> The limiting factor (1).', styles['ans']))
    s.append(Paragraph('<b>C5.</b> Another factor (e.g. CO<sub>2</sub> or temperature) has become the limiting factor (1); increasing light intensity alone cannot raise the rate further until that other factor increases too (1).', styles['ans']))

    s.append(Paragraph('Section D &mdash; Translocation, nutrition &amp; disease', styles['h2']))
    s.append(Paragraph('<b>D1.</b> The movement of dissolved sugars (1) around the plant through the phloem (1).', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Phloem (1).', styles['ans']))
    s.append(Paragraph('<b>D3.</b> Magnesium (1); magnesium is needed to make chlorophyll, so a shortage reduces the green pigment in the leaves (1).', styles['ans']))
    s.append(Paragraph('<b>D4.</b> Nitrate (1); nitrate is needed to make proteins, which are needed for cell growth (1).', styles['ans']))
    s.append(Paragraph('<b>D5.</b> Any three: stunted growth (1); spots on leaves (1); patches of decay/rot (1); growths/galls (1); discolouration (1); wilting (1).', styles['ans']))

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
