# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Energy Transfer (AQA 8463 4.5.1-4.5.2, Foundation tier)."""

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
PHYS = colors.HexColor('#B5762A')
MATHS = colors.HexColor('#3A5E85')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#F1EAD9')

MARGIN = 20 * mm

styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=26,
                             textColor=INK, spaceAfter=4, leading=30),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=10.5,
                                textColor=INK_SOFT, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=14,
                          textColor=PHYS, spaceBefore=16, spaceAfter=8),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.5,
                            textColor=INK, leading=15, spaceAfter=8, alignment=TA_LEFT),
    'bodyb': ParagraphStyle('bodyb', fontName='Helvetica-Bold', fontSize=10.5,
                             textColor=INK, leading=15, spaceAfter=8),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=10.5,
                              textColor=INK, leading=15, spaceAfter=4,
                              leftIndent=14, bulletIndent=0),
    'marks': ParagraphStyle('marks', fontName='Helvetica-Oblique', fontSize=9.5,
                             textColor=INK_SOFT, spaceAfter=10),
    'qtext': ParagraphStyle('qtext', fontName='Helvetica', fontSize=10.5,
                             textColor=INK, leading=15, spaceAfter=2),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=10.5,
                           textColor=INK, leading=15, spaceAfter=6),
    'note': ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=9.5,
                            textColor=INK_SOFT, leading=13, spaceBefore=14),
    'tablehead': ParagraphStyle('tablehead', fontName='Helvetica', fontSize=9.5,
                                 textColor=INK_SOFT),
    'tablecell': ParagraphStyle('tablecell', fontName='Helvetica', fontSize=10,
                                 textColor=INK),
}


def hr():
    return HRFlowable(width='100%', thickness=1, color=PAPER_LINE,
                       spaceBefore=6, spaceAfter=14)


def header(title, subtitle):
    return [Paragraph(title, styles['title']), Paragraph(subtitle, styles['subtitle']), hr()]


def table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEAD_BG),
        ('LINEBELOW', (0, 0), (-1, -1), 0.75, PAPER_LINE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (-1, 0), INK_SOFT),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def cell(text):
    return Paragraph(text, styles['tablecell'])


def headcell(text):
    return Paragraph(text, styles['tablehead'])


# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('energy_transfer_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Energy Transfer',
                 'Quick reference sheet &middot; Physics &middot; keep handy for revision')

    s.append(Paragraph('1. Energy stores', styles['h2']))
    s.append(Paragraph('A system (an object, or group of objects) stores energy in eight possible ways:', styles['body']))
    s.append(table([
        [headcell('Kinetic'), headcell('Gravitational potential'), headcell('Elastic potential'), headcell('Thermal')],
        [cell('anything moving'), cell('anything raised up'), cell('stretched/squashed springs'), cell('anything with a temperature')],
        [headcell('Chemical'), headcell('Nuclear'), headcell('Electrostatic'), headcell('Magnetic')],
        [cell('fuels, food, batteries'), cell('inside atomic nuclei'), cell('charges at a distance'), cell('magnets at a distance')],
    ], col_widths=[40 * mm, 46 * mm, 46 * mm, 38 * mm]))

    s.append(Paragraph('2. Conservation, transfer &amp; dissipation', styles['h2']))
    s.append(Paragraph('<b>Conservation of energy:</b> energy cannot be created or destroyed, only transferred, stored, or dissipated. The total energy before a change equals the total energy after.', styles['body']))
    s.append(Paragraph('Energy is transferred along four pathways:', styles['body']))
    s.append(Paragraph('<b>Mechanically</b> &mdash; a force acting through a distance', styles['bullet']))
    s.append(Paragraph('<b>Electrically</b> &mdash; charge moving through a circuit', styles['bullet']))
    s.append(Paragraph('<b>By heating</b> &mdash; due to a temperature difference', styles['bullet']))
    s.append(Paragraph('<b>By radiation</b> &mdash; light or sound waves spreading out', styles['bullet']))
    s.append(Paragraph('<b>Dissipation:</b> "wasted" energy spreads into the surroundings (usually as heat) and becomes hard to use further &mdash; it is not destroyed, just spread out.', styles['body']))

    s.append(Paragraph('3. Kinetic &amp; gravitational potential energy', styles['h2']))
    s.append(Paragraph('kinetic energy = &frac12; &times; mass &times; speed&sup2; &nbsp;&nbsp; <b>E<sub>k</sub> = &frac12;mv&sup2;</b>', styles['bodyb']))
    s.append(Paragraph('E<sub>k</sub> in joules, J &nbsp;&middot;&nbsp; m in kg &nbsp;&middot;&nbsp; v in m/s. Doubling speed <i>quadruples</i> E<sub>k</sub> (speed is squared).', styles['body']))
    s.append(Paragraph('gravitational potential energy = mass &times; g &times; height &nbsp;&nbsp; <b>E<sub>p</sub> = mgh</b>', styles['bodyb']))
    s.append(Paragraph('E<sub>p</sub> in J &nbsp;&middot;&nbsp; m in kg &nbsp;&middot;&nbsp; g = 9.8 N/kg near Earth&rsquo;s surface &nbsp;&middot;&nbsp; h in m', styles['body']))

    s.append(Paragraph('4. Elastic potential energy &amp; specific heat capacity', styles['h2']))
    s.append(Paragraph('elastic potential energy = &frac12; &times; spring constant &times; extension&sup2; &nbsp;&nbsp; <b>E<sub>e</sub> = &frac12;ke&sup2;</b>', styles['bodyb']))
    s.append(Paragraph('k in N/m &nbsp;&middot;&nbsp; e in m &nbsp;&middot;&nbsp; only valid up to the limit of proportionality', styles['body']))
    s.append(Paragraph('change in thermal energy = mass &times; specific heat capacity &times; temperature change &nbsp;&nbsp; <b>&Delta;E = mc&Delta;&theta;</b>', styles['bodyb']))
    s.append(Paragraph('&Delta;E in J &nbsp;&middot;&nbsp; m in kg &nbsp;&middot;&nbsp; c in J/kg&deg;C (a property of the material, e.g. water = 4200) &nbsp;&middot;&nbsp; &Delta;&theta; in &deg;C', styles['body']))

    s.append(Paragraph('5. Power &amp; efficiency', styles['h2']))
    s.append(Paragraph('power = energy transferred &divide; time &nbsp;&nbsp; <b>P = E / t</b> &nbsp;&nbsp; (measured in watts, W &mdash; 1 W = 1 J/s)', styles['bodyb']))
    s.append(Paragraph('efficiency = useful output energy transfer &divide; total input energy transfer &nbsp;&nbsp; (&times;100 for a %)', styles['bodyb']))
    s.append(Paragraph('No real machine is 100% efficient &mdash; some energy is always dissipated. Reduce unwanted transfers with <b>lubrication</b> (less friction) or <b>insulation</b> (less unwanted heating).', styles['body']))

    s.append(Paragraph('6. Worked examples', styles['h2']))
    s.append(table([
        [headcell('Given'), headcell('Find'), headcell('Working'), headcell('Answer')],
        [cell('m = 2 kg, v = 3 m/s'), cell('E<sub>k</sub>'), cell('&frac12; &times; 2 &times; 3&sup2;'), cell('9 J')],
        [cell('m = 5 kg, h = 2 m'), cell('E<sub>p</sub>'), cell('5 &times; 9.8 &times; 2'), cell('98 J')],
        [cell('k = 40 N/m, e = 0.2 m'), cell('E<sub>e</sub>'), cell('&frac12; &times; 40 &times; 0.2&sup2;'), cell('0.8 J')],
        [cell('m = 2 kg, c = 4200, &Delta;&theta; = 10&deg;C'), cell('&Delta;E'), cell('2 &times; 4200 &times; 10'), cell('8.4 &times; 10<super>4</super> J')],
        [cell('E = 600 J, t = 5 s'), cell('P'), cell('600 / 5'), cell('120 W')],
        [cell('input = 500 J, useful = 350 J'), cell('efficiency'), cell('350 / 500'), cell('70%')],
    ], col_widths=[50 * mm, 24 * mm, 44 * mm, 30 * mm]))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('energy_transfer_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Energy Transfer', 'Test &middot; 25 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 25'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Key ideas', styles['h2']))
    s += q('A1', 'Name the four ways that energy can be transferred.', 4)
    s.append(Spacer(1, 10))
    s += q('A2', 'State the principle of conservation of energy.', 1)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section B &mdash; Kinetic &amp; gravitational potential energy', styles['h2']))
    s += q('B1', 'Calculate the kinetic energy of a 1200 kg car travelling at 15 m/s.', 2)
    s.append(Spacer(1, 14))
    s += q('B2', 'A ball of mass 0.4 kg is lifted 3 m. Calculate its gravitational potential energy. (g = 9.8 N/kg)', 2)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section C &mdash; Elastic potential energy &amp; specific heat capacity', styles['h2']))
    s += q('C1', 'A spring with a spring constant of 25 N/m is stretched by 0.08 m. Calculate its elastic potential energy. Show your working.', 3)
    s.append(Spacer(1, 14))
    s += q('C2', '2 kg of water gains 42,000 J of energy when heated. The specific heat capacity of water is 4200 J/kg&deg;C. Calculate the temperature rise. Show how you rearranged the equation.', 3)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section D &mdash; Power &amp; efficiency', styles['h2']))
    s += q('D1', 'A kettle has a power rating of 2000 W. Calculate the energy it transfers when used for 3 minutes.', 3)
    s.append(Spacer(1, 14))
    s += q('D2', 'A lamp has a total energy input of 60 J, and produces 12 J of useful light energy. Calculate its efficiency as a percentage.', 2)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section E &mdash; Extended reasoning', styles['h2']))
    s += q('E1', 'Explain, in terms of energy, why no real machine can ever be 100% efficient, and give one way of reducing unwanted energy transfers caused by friction.', 3)
    s.append(Spacer(1, 30))

    s.append(Paragraph('Section F &mdash; Energy stores', styles['h2']))
    s.append(Paragraph('State the main energy store involved in each of the following:', styles['qtext']))
    s.append(Spacer(1, 4))
    s.append(Paragraph('(a) a stretched elastic band, before release &nbsp;&nbsp;&nbsp; (b) petrol in a car&rsquo;s fuel tank', styles['qtext']))
    s.append(Paragraph('[2 marks]', styles['marks']))

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('energy_transfer_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Energy Transfer', 'Answer sheet &middot; 25 marks total')

    s.append(Paragraph('Section A &mdash; Key ideas', styles['h2']))
    s.append(Paragraph('<b>A1.</b> Mechanically (1) &nbsp; electrically (1) &nbsp; by heating (1) &nbsp; by radiation (1)', styles['ans']))
    s.append(Paragraph('<b>A2.</b> Energy cannot be created or destroyed, only transferred, stored or dissipated (1).', styles['ans']))

    s.append(Paragraph('Section B &mdash; Kinetic &amp; gravitational potential energy', styles['h2']))
    s.append(Paragraph('<b>B1.</b> E<sub>k</sub> = &frac12;mv&sup2; = &frac12; &times; 1200 &times; 15&sup2; (1) &nbsp; <b>E<sub>k</sub> = 135,000 J (1.35 &times; 10<super>5</super> J)</b> (1)', styles['ans']))
    s.append(Paragraph('<b>B2.</b> E<sub>p</sub> = mgh = 0.4 &times; 9.8 &times; 3 (1) &nbsp; <b>E<sub>p</sub> = 11.76 J</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Elastic potential energy &amp; specific heat capacity', styles['h2']))
    s.append(Paragraph('<b>C1.</b> E<sub>e</sub> = &frac12;ke&sup2; (1) &nbsp; E<sub>e</sub> = &frac12; &times; 25 &times; 0.08&sup2; (1) &nbsp; <b>E<sub>e</sub> = 0.08 J</b> (1)', styles['ans']))
    s.append(Paragraph('<b>C2.</b> &Delta;&theta; = &Delta;E / (mc) (1) &nbsp; &Delta;&theta; = 42000 / (2 &times; 4200) (1) &nbsp; <b>&Delta;&theta; = 5&deg;C</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Power &amp; efficiency', styles['h2']))
    s.append(Paragraph('<b>D1.</b> 3 minutes = 180 s (1) &nbsp; E = Pt = 2000 &times; 180 (1) &nbsp; <b>E = 360,000 J (3.6 &times; 10<super>5</super> J)</b> (1)', styles['ans']))
    s.append(Paragraph('<b>D2.</b> efficiency = 12 / 60 (1) &nbsp; <b>efficiency = 0.2 = 20%</b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Extended reasoning', styles['h2']))
    s.append(Paragraph(
        '<b>E1.</b> Some of the input energy is always dissipated to the surroundings, usually as heat, due to friction/resistance (1). '
        'This wasted energy cannot be usefully recovered, so useful output energy transfer is always less than total input energy transfer (1). '
        'Lubrication (oiling/greasing moving parts) reduces friction and unwanted heat transfer (1) &mdash; insulation also accepted for a heat-transfer context.', styles['ans']))

    s.append(Paragraph('Section F &mdash; Energy stores', styles['h2']))
    s.append(Paragraph('(a) <b>Elastic potential</b> (1) &nbsp; (b) <b>Chemical</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly stated equation and correct substitution even if the '
        'final answer contains an arithmetic error. Accept answers in standard form where shown as equivalent.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
