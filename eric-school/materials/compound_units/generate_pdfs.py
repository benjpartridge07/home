# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Compound Units: Speed, Density & Pressure (GCSE Maths, Ratio/Proportion/Rates of Change)."""

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
MATHS = colors.HexColor('#3A5E85')
ACC = colors.HexColor('#B5762A')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#F1EAD9')

MARGIN = 20 * mm

styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=26,
                             textColor=INK, spaceAfter=4, leading=30),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=10.5,
                                textColor=INK_SOFT, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=14,
                          textColor=MATHS, spaceBefore=16, spaceAfter=8),
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
    doc = SimpleDocTemplate('compound_units_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Compound Units: Speed, Density &amp; Pressure',
                 'Quick reference sheet &middot; GCSE Maths, Ratio, Proportion &amp; Rates of Change &middot; keep handy for revision')

    s.append(Paragraph('1. The three formulas', styles['h2']))
    s.append(Paragraph('All three have the same shape: one quantity &divide; another. Once you can rearrange one, you can rearrange all three.', styles['body']))
    s.append(table([
        [headcell('Quantity'), headcell('Formula'), headcell('Units')],
        [cell('Speed'), cell('speed = distance &divide; time'), cell('m/s or km/h')],
        [cell('Density'), cell('density = mass &divide; volume'), cell('g/cm<super>3</super> or kg/m<super>3</super>')],
        [cell('Pressure'), cell('pressure = force &divide; area'), cell('N/m<super>2</super> = pascal (Pa)')],
    ], col_widths=[28 * mm, 78 * mm, 44 * mm]))

    s.append(Paragraph('2. Formula triangles', styles['h2']))
    s.append(Paragraph('Cover the letter you want to find; the two remaining letters show the operation. Side-by-side (e.g. S next to T) means multiply; one on top of the other (e.g. D over T) means divide.', styles['body']))
    s.append(Paragraph('<b>Speed:</b> D over S&times;T &nbsp;&rarr;&nbsp; S = D&divide;T, &nbsp; D = S&times;T, &nbsp; T = D&divide;S', styles['bodyb']))
    s.append(Paragraph('<b>Density:</b> m over &rho;&times;V &nbsp;&rarr;&nbsp; &rho; = m&divide;V, &nbsp; m = &rho;&times;V, &nbsp; V = m&divide;&rho;', styles['bodyb']))
    s.append(Paragraph('<b>Pressure:</b> F over P&times;A &nbsp;&rarr;&nbsp; P = F&divide;A, &nbsp; F = P&times;A, &nbsp; A = F&divide;P', styles['bodyb']))

    s.append(Paragraph('3. Worked examples', styles['h2']))
    s.append(Paragraph('Speed: distance 200 m, time 25 s &nbsp;&rarr;&nbsp; speed = 200&divide;25 = <b>8 m/s</b>', styles['body']))
    s.append(Paragraph('Density: mass 54 g, volume 20 cm<super>3</super> &nbsp;&rarr;&nbsp; density = 54&divide;20 = <b>2.7 g/cm<super>3</super></b>', styles['body']))
    s.append(Paragraph('Pressure: force 300 N, area 0.5 m<super>2</super> &nbsp;&rarr;&nbsp; pressure = 300&divide;0.5 = <b>600 Pa</b>', styles['body']))
    s.append(Paragraph('Rearranged: speed 30 m/s for 12 s &nbsp;&rarr;&nbsp; distance = speed&times;time = 30&times;12 = <b>360 m</b>', styles['body']))
    s.append(Paragraph('For a fixed force, a <b>smaller area gives a bigger pressure</b> &mdash; e.g. a sharp knife or drawing pin.', styles['body']))

    s.append(Paragraph('4. Converting units', styles['h2']))
    s.append(table([
        [headcell('Conversion'), headcell('Rule')],
        [cell('km/h &rarr; m/s'), cell('&divide; 3.6')],
        [cell('m/s &rarr; km/h'), cell('&times; 3.6')],
        [cell('g/cm<super>3</super> &rarr; kg/m<super>3</super>'), cell('&times; 1000')],
        [cell('kg/m<super>3</super> &rarr; g/cm<super>3</super>'), cell('&divide; 1000')],
        [cell('cm<super>2</super> &rarr; m<super>2</super>'), cell('&divide; 10 000')],
        [cell('m<super>2</super> &rarr; cm<super>2</super>'), cell('&times; 10 000')],
    ], col_widths=[65 * mm, 65 * mm]))
    s.append(Paragraph('72 km/h &divide; 3.6 = <b>20 m/s</b> &nbsp;&middot;&nbsp; 2.7 g/cm<super>3</super> &times; 1000 = <b>2700 kg/m<super>3</super></b>', styles['body']))

    s.append(Paragraph('5. Common mistakes', styles['h2']))
    s.append(Paragraph('Forgetting to convert units so they match before calculating (e.g. mixing minutes and hours, or cm and m).', styles['bullet']))
    s.append(Paragraph('Writing the answer with no units, or the wrong units (always check what the formula produces).', styles['bullet']))
    s.append(Paragraph('Multiplying instead of dividing (or vice-versa) when rearranging &mdash; use the formula triangle to check.', styles['bullet']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('compound_units_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Compound Units: Speed, Density &amp; Pressure', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Speed', styles['h2']))
    s += q('A1', 'Distance 150 m, time 30 s. Calculate the speed.', 2)
    s += q('A2', 'Speed 25 m/s, time 8 s. Calculate the distance.', 2)
    s += q('A3', 'Distance 90 km, speed 45 km/h. Calculate the time.', 2)
    s += q('A4', 'Convert 54 km/h to m/s.', 1)

    s.append(Paragraph('Section B &mdash; Density', styles['h2']))
    s += q('B1', 'Mass 40 g, volume 20 cm&sup3;. Calculate the density.', 2)
    s += q('B2', 'Density 2.7 g/cm&sup3;, mass 54 g. Calculate the volume.', 2)
    s += q('B3', 'Convert 1.5 g/cm&sup3; to kg/m&sup3;.', 2)

    s.append(Paragraph('Section C &mdash; Pressure', styles['h2']))
    s += q('C1', 'Force 300 N, area 0.5 m&sup2;. Calculate the pressure in Pa.', 2)
    s += q('C2', 'Pressure 4000 Pa, area 0.25 m&sup2;. Calculate the force.', 2)
    s += q('C3', 'Explain, using the pressure formula, why a sharp knife cuts more easily than a blunt one.', 2)

    s.append(Paragraph('Section D &mdash; Mixed &amp; converting', styles['h2']))
    s += q('D1', 'A cyclist travels 12 km in 40 minutes. Calculate their average speed in km/h, then convert your answer to m/s.', 3)
    s += q('D2', 'A block has mass 250 g and volume 100 cm&sup3;. Calculate its density in g/cm&sup3;, then convert your answer to kg/m&sup3;.', 2)
    s += q('D3', 'A force of 150 N acts on an area of 0.03 m&sup2;. Calculate the pressure. State what would happen to the pressure if the area were halved and the force stayed the same.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('compound_units_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Compound Units: Speed, Density &amp; Pressure', 'Answer sheet &middot; 26 marks total')

    s.append(Paragraph('Section A &mdash; Speed', styles['h2']))
    s.append(Paragraph('A1. 150&divide;30 (1) &nbsp; = <b>5 m/s</b> (1)', styles['ans']))
    s.append(Paragraph('A2. 25&times;8 (1) &nbsp; = <b>200 m</b> (1)', styles['ans']))
    s.append(Paragraph('A3. 90&divide;45 (1) &nbsp; = <b>2 hours</b> (1)', styles['ans']))
    s.append(Paragraph('A4. 54&divide;3.6 = <b>15 m/s</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Density', styles['h2']))
    s.append(Paragraph('B1. 40&divide;20 (1) &nbsp; = <b>2 g/cm&sup3;</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 54&divide;2.7 (1) &nbsp; = <b>20 cm&sup3;</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1.5&times;1000 (1) &nbsp; = <b>1500 kg/m&sup3;</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Pressure', styles['h2']))
    s.append(Paragraph('C1. 300&divide;0.5 (1) &nbsp; = <b>600 Pa</b> (1)', styles['ans']))
    s.append(Paragraph('C2. 4000&times;0.25 (1) &nbsp; = <b>1000 N</b> (1)', styles['ans']))
    s.append(Paragraph('C3. A sharp knife has a much smaller contact area (1) &nbsp; for the same force, a smaller area produces a larger pressure (pressure = force&divide;area), so it cuts through more easily (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Mixed &amp; converting', styles['h2']))
    s.append(Paragraph('D1. 40 min = 2/3 hour &rarr; speed = 12&divide;(2/3) = <b>18 km/h</b> (1) &nbsp; 18&divide;3.6 (1) &nbsp; = <b>5 m/s</b> (1)', styles['ans']))
    s.append(Paragraph('D2. 250&divide;100 = <b>2.5 g/cm&sup3;</b> (1) &nbsp; &times;1000 = <b>2500 kg/m&sup3;</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 150&divide;0.03 = <b>5000 Pa</b> (1) &nbsp; halving the area (with the same force) <b>doubles the pressure</b> to 10 000 Pa (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly set-up calculation even if the final answer contains an '
        'arithmetic slip, and for correct unit-conversion working even if the final compound-unit calculation is '
        'then wrong. Missing or incorrect units on an otherwise-correct numerical answer should lose the final '
        'accuracy mark, not the method mark.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
