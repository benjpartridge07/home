# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Area, Perimeter & Volume (GCSE Maths, Geometry & Measures)."""

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


# Note: reportlab's Helvetica (WinAnsi) encoding does not reliably render
# literal/entity Unicode superscript-two / superscript-three glyphs (&sup2;/&sup3;)
# in every viewer. Use reportlab's own <super> paragraph tag with a plain
# digit instead, e.g. 'cm<super>2</super>'.
SQ = '<super>2</super>'
CU = '<super>3</super>'


# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('area_perimeter_volume_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Area, Perimeter &amp; Volume',
                 'Quick reference sheet &middot; GCSE Maths, Geometry &amp; Measures &middot; keep handy for revision')

    s.append(Paragraph('1. Rectangles, triangles &amp; parallelograms', styles['h2']))
    s.append(table([
        [headcell('Shape'), headcell('Area'), headcell('Perimeter')],
        [cell('Rectangle'), cell('length &times; width'), cell('2 &times; (length + width)')],
        [cell('Triangle'), cell('&frac12; &times; base &times; height'), cell('sum of the three sides')],
        [cell('Parallelogram'), cell('base &times; height'), cell('sum of the four sides')],
    ], col_widths=[38 * mm, 68 * mm, 54 * mm]))
    s.append(Paragraph('For triangles and parallelograms, always use the <b>perpendicular</b> (vertical) height &mdash; never a slanted side.', styles['body']))

    s.append(Paragraph('2. Trapeziums', styles['h2']))
    s.append(Paragraph(f'A trapezium has one pair of parallel sides, a and b, separated by perpendicular height h.', styles['body']))
    s.append(Paragraph('Area = &frac12; &times; (a + b) &times; h', styles['bodyb']))
    s.append(Paragraph(f'Example: a = 6 cm, b = 10 cm, h = 4 cm &nbsp;&rarr;&nbsp; area = &frac12; &times; 16 &times; 4 = <b>32 cm{SQ}</b>', styles['body']))

    s.append(Paragraph('3. Circles', styles['h2']))
    s.append(table([
        [headcell('Quantity'), headcell('Formula')],
        [cell('Diameter'), cell('d = 2 &times; r')],
        [cell('Area'), cell(f'&pi;r{SQ}')],
        [cell('Circumference'), cell('&pi;d &nbsp;or&nbsp; 2&pi;r')],
    ], col_widths=[38 * mm, 78 * mm]))
    s.append(Paragraph(f'Example: r = 5 cm &nbsp;&rarr;&nbsp; area = &pi; &times; 5{SQ} = <b>78.5 cm{SQ}</b> (1 d.p.) &nbsp;&middot;&nbsp; circumference = 2&pi; &times; 5 = <b>31.4 cm</b> (1 d.p.)', styles['body']))
    s.append(Paragraph('Watch out for questions that give the diameter instead of the radius &mdash; halve it first before squaring for the area.', styles['body']))

    s.append(Paragraph('4. Volume of prisms &amp; cylinders', styles['h2']))
    s.append(table([
        [headcell('Solid'), headcell('Volume')],
        [cell('Cuboid'), cell('length &times; width &times; height')],
        [cell('Prism (any cross-section)'), cell('cross-sectional area &times; length')],
        [cell('Cylinder'), cell(f'&pi;r{SQ} &times; height')],
    ], col_widths=[55 * mm, 61 * mm]))
    s.append(Paragraph(f'A cylinder is a prism with a circular cross-section, and a cuboid is a prism with a rectangular cross-section &mdash; the same rule (cross-sectional area &times; length) applies to all of them.', styles['body']))
    s.append(Paragraph(f'Example (triangular prism): cross-section base 6 cm, height 4 cm, prism length 10 cm &nbsp;&rarr;&nbsp; area = &frac12; &times; 6 &times; 4 = 12 cm{SQ} &nbsp;&rarr;&nbsp; volume = 12 &times; 10 = <b>120 cm{CU}</b>', styles['body']))
    s.append(Paragraph(f'Example (cylinder): r = 3 cm, height = 8 cm &nbsp;&rarr;&nbsp; volume = &pi; &times; 3{SQ} &times; 8 = <b>226.2 cm{CU}</b> (1 d.p.)', styles['body']))

    s.append(Paragraph('5. Common mistakes', styles['h2']))
    s.append(Paragraph('Using a slanted side instead of the perpendicular height for triangles, parallelograms and trapeziums.', styles['bullet']))
    s.append(Paragraph('Forgetting to halve the diameter to get the radius before using it in a circle or cylinder formula.', styles['bullet']))
    s.append(Paragraph(f'Confusing area (cm{SQ}-type units) with volume (cm{CU}-type units) &mdash; check the units the question expects.', styles['bullet']))
    s.append(Paragraph('Rounding too early in a multi-step calculation, which makes the final answer inaccurate &mdash; only round the final answer.', styles['bullet']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('area_perimeter_volume_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Area, Perimeter &amp; Volume', 'Test &middot; 27 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 27'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Rectangles, triangles &amp; parallelograms', styles['h2']))
    s += q('A1', 'A rectangle has length 8 cm and width 5 cm. Calculate its area.', 1)
    s += q('A2', 'A rectangle has length 8 cm and width 5 cm. Calculate its perimeter.', 1)
    s += q('A3', 'A triangle has a base of 10 cm and a perpendicular height of 7 cm. Calculate its area.', 2)
    s += q('A4', 'A parallelogram has a base of 13 cm and a perpendicular height of 4 cm. Calculate its area.', 2)

    s.append(Paragraph('Section B &mdash; Trapeziums', styles['h2']))
    s += q('B1', 'A trapezium has parallel sides of 7 cm and 11 cm, and a perpendicular height of 6 cm. Calculate its area.', 3)
    s += q('B2', f'A trapezium has an area of 60 cm{SQ} and parallel sides of 9 cm and 15 cm. Calculate its perpendicular height.', 3)

    s.append(Paragraph('Section C &mdash; Circles', styles['h2']))
    s += q('C1', 'A circle has a radius of 7 cm. Calculate its area, giving your answer to 1 decimal place.', 2)
    s += q('C2', 'A circle has a diameter of 18 cm. Calculate its circumference, giving your answer to 1 decimal place.', 2)
    s += q('C3', 'A semicircle has a diameter of 14 cm. Calculate the perimeter of the semicircle (the curved part plus the straight edge), giving your answer to 1 decimal place.', 3)

    s.append(Paragraph('Section D &mdash; Volume', styles['h2']))
    s += q('D1', 'A cuboid has length 7 cm, width 4 cm and height 5 cm. Calculate its volume.', 2)
    s += q('D2', 'A triangular prism has a cross-section with base 8 cm and perpendicular height 5 cm, and the prism is 12 cm long. Calculate its volume.', 3)
    s += q('D3', 'A cylinder has radius 5 cm and height 9 cm. Calculate its volume, giving your answer to 1 decimal place.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('area_perimeter_volume_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Area, Perimeter &amp; Volume', 'Answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Rectangles, triangles &amp; parallelograms', styles['h2']))
    s.append(Paragraph(f'A1. 8 &times; 5 = <b>40 cm{SQ}</b> (1)', styles['ans']))
    s.append(Paragraph('A2. 2 &times; (8+5) = <b>26 cm</b> (1)', styles['ans']))
    s.append(Paragraph(f'A3. &frac12; &times; 10 &times; 7 (1) &nbsp; = <b>35 cm{SQ}</b> (1)', styles['ans']))
    s.append(Paragraph(f'A4. 13 &times; 4 (1) &nbsp; = <b>52 cm{SQ}</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Trapeziums', styles['h2']))
    s.append(Paragraph(f'B1. &frac12; &times; (7+11) (1) &nbsp; &times; 6 (1) &nbsp; = <b>54 cm{SQ}</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 60 = &frac12; &times; (9+15) &times; h &nbsp; 60 = 12h (1) &nbsp; h = 60&divide;12 (1) &nbsp; = <b>5 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Circles', styles['h2']))
    s.append(Paragraph(f'C1. &pi; &times; 7{SQ} (1) &nbsp; = <b>153.9 cm{SQ}</b> (1)', styles['ans']))
    s.append(Paragraph('C2. &pi; &times; 18 (1) &nbsp; = <b>56.5 cm</b> (1)', styles['ans']))
    s.append(Paragraph('C3. Curved part = &frac12; &times; &pi; &times; 14 = 22.0 cm (1) &nbsp; straight edge = 14 cm (1) &nbsp; total = 22.0 + 14 = <b>36.0 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Volume', styles['h2']))
    s.append(Paragraph(f'D1. 7 &times; 4 &times; 5 (1) &nbsp; = <b>140 cm{CU}</b> (1)', styles['ans']))
    s.append(Paragraph(f'D2. Cross-sectional area = &frac12; &times; 8 &times; 5 = 20 cm{SQ} (1) &nbsp; volume = 20 &times; 12 (1) &nbsp; = <b>240 cm{CU}</b> (1)', styles['ans']))
    s.append(Paragraph(f'D3. &pi; &times; 5{SQ} &times; 9 (1) &nbsp; = &pi; &times; 225 (1) &nbsp; = <b>706.9 cm{CU}</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly set-up calculation or formula substitution even if the '
        f'final answer contains an arithmetic slip. Accept answers left in terms of &pi; (e.g. 225&pi; cm{CU}) as '
        'fully correct unless the question specifically asks for a decimal answer. Missing or incorrect units on an '
        'otherwise-correct numerical answer should lose the final accuracy mark, not the method mark.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
