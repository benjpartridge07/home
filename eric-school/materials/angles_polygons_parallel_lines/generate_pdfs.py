# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Angles, Polygons & Parallel Lines (GCSE Maths, Geometry & Measures)."""

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
    doc = SimpleDocTemplate('angles_polygons_parallel_lines_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Angles, Polygons &amp; Parallel Lines',
                 'Quick reference sheet &middot; GCSE Maths, Geometry &amp; Measures &middot; keep handy for revision')

    s.append(Paragraph('1. Angle facts: lines and points', styles['h2']))
    s.append(Paragraph('Angles on a straight line sum to <b>180&#176;</b>. Angles around a point sum to <b>360&#176;</b>. Vertically opposite angles (where two lines cross) are <b>equal</b>.', styles['body']))

    s.append(Paragraph('2. Triangles &amp; quadrilaterals', styles['h2']))
    s.append(Paragraph('Angles in a <b>triangle</b> sum to <b>180&#176;</b>. Angles in a <b>quadrilateral</b> sum to <b>360&#176;</b> (split into two triangles). Isosceles triangles have two equal angles; equilateral triangles have three 60&#176; angles.', styles['body']))

    s.append(Paragraph('3. Angles in parallel lines', styles['h2']))
    s.append(table([
        [headcell('Angle pair'), headcell('Shape'), headcell('Rule')],
        [cell('Corresponding'), cell('F-shape'), cell('Equal')],
        [cell('Alternate'), cell('Z-shape'), cell('Equal')],
        [cell('Co-interior (allied)'), cell('C/U-shape'), cell('Sum to 180&#176;')],
        [cell('Vertically opposite'), cell('X-shape'), cell('Equal')],
    ], col_widths=[52 * mm, 38 * mm, 60 * mm]))
    s.append(Paragraph('Corresponding and alternate angles are equal; co-interior (allied) angles add up to 180&#176;.', styles['body']))

    s.append(Paragraph('4. Interior &amp; exterior angles of polygons', styles['h2']))
    s.append(Paragraph('Sum of interior angles = <b>(n &minus; 2) &times; 180&#176;</b>, where n is the number of sides. Exterior angles of any convex polygon always sum to <b>360&#176;</b>. At each vertex, interior + exterior = 180&#176;.', styles['body']))
    s.append(table([
        [headcell('Polygon'), headcell('Sides (n)'), headcell('Interior angle sum')],
        [cell('Triangle'), cell('3'), cell('180&#176;')],
        [cell('Quadrilateral'), cell('4'), cell('360&#176;')],
        [cell('Pentagon'), cell('5'), cell('540&#176;')],
        [cell('Hexagon'), cell('6'), cell('720&#176;')],
        [cell('Heptagon'), cell('7'), cell('900&#176;')],
        [cell('Octagon'), cell('8'), cell('1080&#176;')],
    ], col_widths=[52 * mm, 38 * mm, 60 * mm]))

    s.append(Paragraph('5. Regular polygons', styles['h2']))
    s.append(Paragraph('Each exterior angle = <b>360&#176; &divide; n</b>. Each interior angle = <b>180&#176; &minus; exterior angle</b>. Working backwards: n = 360&#176; &divide; exterior angle.', styles['body']))
    s.append(table([
        [headcell('Regular polygon'), headcell('n'), headcell('Exterior'), headcell('Interior')],
        [cell('Square'), cell('4'), cell('90&#176;'), cell('90&#176;')],
        [cell('Pentagon'), cell('5'), cell('72&#176;'), cell('108&#176;')],
        [cell('Hexagon'), cell('6'), cell('60&#176;'), cell('120&#176;')],
        [cell('Octagon'), cell('8'), cell('45&#176;'), cell('135&#176;')],
        [cell('Decagon'), cell('10'), cell('36&#176;'), cell('144&#176;')],
    ], col_widths=[45 * mm, 20 * mm, 30 * mm, 30 * mm]))

    s.append(Paragraph('6. Common mistakes', styles['h2']))
    s.append(Paragraph('Using 360&#176; instead of 180&#176; for a triangle, or vice versa for a quadrilateral.', styles['bullet']))
    s.append(Paragraph('Mixing up alternate (equal) and co-interior (sum to 180&#176;) angles &mdash; check whether the angles are on the same or opposite sides of the transversal.', styles['bullet']))
    s.append(Paragraph('Forgetting that exterior angles of ANY polygon sum to 360&#176;, regardless of the number of sides.', styles['bullet']))
    s.append(Paragraph('Using the interior angle formula (n&minus;2)&times;180&#176; when the question actually gives an exterior angle, or vice versa.', styles['bullet']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('angles_polygons_parallel_lines_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Angles, Polygons &amp; Parallel Lines', 'Test &middot; 28 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 28'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Angle facts', styles['h2']))
    s += q('A1', 'Two angles lie on a straight line. One angle is 118&#176;. Find the other angle.', 1)
    s += q('A2', 'Three angles meet at a point: 95&#176;, 140&#176; and x&#176;. Find x.', 1)
    s += q('A3', 'Two straight lines cross. One angle is 42&#176;. State the size of the angle vertically opposite to it, giving a reason.', 2)
    s += q('A4', 'Two angles on a straight line are (4x)&#176; and (2x + 30)&#176;. Find the value of x.', 2)

    s.append(Paragraph('Section B &mdash; Triangles &amp; quadrilaterals', styles['h2']))
    s += q('B1', 'A triangle has angles 48&#176;, 76&#176; and x&#176;. Find x.', 2)
    s += q('B2', 'An isosceles triangle has a base angle of 70&#176;. Find the other two angles of the triangle.', 2)
    s += q('B3', 'A quadrilateral has angles 90&#176;, 105&#176;, 88&#176; and x&#176;. Find x.', 2)
    s += q('B4', 'A kite has angles 100&#176;, 70&#176;, x&#176; and x&#176; (the last two angles are equal). Find x.', 2)

    s.append(Paragraph('Section C &mdash; Parallel lines', styles['h2']))
    s += q('C1', 'What name is given to a pair of angles that form a "Z" shape between two parallel lines?', 1)
    s += q('C2', 'One angle is 108&#176;. Find the size of its corresponding angle.', 1)
    s += q('C3', 'One angle is 62&#176;. Find the size of its co-interior (allied) angle.', 1)
    s += q('C4', 'Two parallel lines are cut by a transversal. One angle is (2x + 15)&#176;, and its corresponding angle is 85&#176;. Find the value of x.', 3)

    s.append(Paragraph('Section D &mdash; Polygons', styles['h2']))
    s += q('D1', 'Calculate the sum of the interior angles of a hexagon.', 2)
    s += q('D2', 'A regular polygon has 12 sides. Calculate the size of each exterior angle.', 2)
    s += q('D3', 'Calculate the size of each interior angle of a regular decagon (10 sides).', 2)
    s += q('D4', 'A regular polygon has an interior angle of 150&#176;. How many sides does it have?', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('angles_polygons_parallel_lines_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Angles, Polygons &amp; Parallel Lines', 'Answer sheet &middot; 28 marks total')

    s.append(Paragraph('Section A &mdash; Angle facts', styles['h2']))
    s.append(Paragraph('A1. 180&minus;118 = <b>62&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('A2. 360&minus;95&minus;140 = <b>125&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>42&#176;</b> (1) &nbsp; vertically opposite angles are equal (1)', styles['ans']))
    s.append(Paragraph('A4. 4x + 2x+30 = 180 (1) &nbsp; 6x = 150, x = <b>25</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Triangles &amp; quadrilaterals', styles['h2']))
    s.append(Paragraph('B1. 180&minus;48&minus;76 (1) &nbsp; = <b>56&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('B2. Other base angle = <b>70&#176;</b> (1) &nbsp; apex angle = 180&minus;70&minus;70 = <b>40&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 360&minus;90&minus;105&minus;88 (1) &nbsp; = <b>77&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('B4. 100+70+2x = 360 (1) &nbsp; 2x = 190, x = <b>95&#176;</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Parallel lines', styles['h2']))
    s.append(Paragraph('C1. <b>Alternate</b> angles (1)', styles['ans']))
    s.append(Paragraph('C2. <b>108&#176;</b> (corresponding angles are equal) (1)', styles['ans']))
    s.append(Paragraph('C3. 180&minus;62 = <b>118&#176;</b> (co-interior angles sum to 180&#176;) (1)', styles['ans']))
    s.append(Paragraph('C4. Corresponding angles are equal, so 2x+15 = 85 (1) &nbsp; 2x = 70 (1) &nbsp; x = <b>35</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Polygons', styles['h2']))
    s.append(Paragraph('D1. (6&minus;2)&times;180 (1) &nbsp; = <b>720&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('D2. 360&divide;12 (1) &nbsp; = <b>30&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('D3. Exterior = 360&divide;10 = 36&#176;, interior = 180&minus;36 (1) &nbsp; = <b>144&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('D4. Exterior angle = 180&minus;150 = 30&#176; (1) &nbsp; n = 360&divide;30 = <b>12 sides</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly set-up equation or calculation even if the final answer '
        'contains an arithmetic slip. Accept equivalent correct reasoning for "giving a reason" parts (e.g. naming '
        'the angle rule used). Missing units (&#176;) on an otherwise-correct numerical answer should lose the final '
        'accuracy mark, not the method mark.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
