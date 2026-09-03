# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Transformations & Constructions (GCSE Maths, Geometry & Measures)."""

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


# NOTE: reportlab's Helvetica encoding does not support Unicode super/subscript
# glyphs. Where a super/subscript is needed, use the <sup>/<sub> paragraph tags
# with plain characters (e.g. 'cm<sup>2</sup>') rather than literal Unicode
# super/subscript characters.

# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('transformations_constructions_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Transformations &amp; Constructions',
                 'Quick reference sheet &middot; GCSE Maths, Geometry &amp; Measures &middot; keep handy for revision')

    s.append(Paragraph('1. Translation', styles['h2']))
    s.append(Paragraph('A translation slides a shape &mdash; no turning, flipping or resizing. Described by a column vector (x on top = left/right, y on bottom = up/down). To translate a point, add the vector to its coordinates: (x, y) + (a, b) = (x + a, y + b).', styles['body']))

    s.append(Paragraph('2. Rotation', styles['h2']))
    s.append(Paragraph('A rotation turns a shape about a fixed point. Must state THREE things: angle, direction (clockwise/anticlockwise), and centre of rotation. About the origin: 90&#176; clockwise (x,y)&#8594;(y,&minus;x); 90&#176; anticlockwise (x,y)&#8594;(&minus;y,x); 180&#176; (x,y)&#8594;(&minus;x,&minus;y).', styles['body']))

    s.append(Paragraph('3. Reflection', styles['h2']))
    s.append(table([
        [headcell('Mirror line'), headcell('Effect on point (x, y)')],
        [cell('x-axis'), cell('(x, &minus;y)')],
        [cell('y-axis'), cell('(&minus;x, y)')],
        [cell('y = x'), cell('(y, x)')],
        [cell('y = &minus;x'), cell('(&minus;y, &minus;x)')],
        [cell('x = a (vertical line)'), cell('Same distance from x = a, on the other side')],
    ], col_widths=[65 * mm, 85 * mm]))

    s.append(Paragraph('4. Enlargement', styles['h2']))
    s.append(Paragraph('Described by a scale factor (SF) and a centre of enlargement. Each image point lies on the ray from the centre through the object point, at SF &times; the distance from the centre. <b>Area scale factor = (linear SF)<sup>2</sup></b>.', styles['body']))
    s.append(table([
        [headcell('Scale factor'), headcell('Size of image'), headcell('Position vs. centre')],
        [cell('SF &gt; 1'), cell('Bigger'), cell('Same side as object')],
        [cell('0 &lt; SF &lt; 1'), cell('Smaller'), cell('Same side as object')],
        [cell('SF &lt; 0'), cell('|SF| &times; object size'), cell('Opposite side, turned 180&#176;')],
    ], col_widths=[45 * mm, 55 * mm, 50 * mm]))

    s.append(Paragraph('5. Constructions (ruler and compasses only)', styles['h2']))
    s.append(Paragraph('<b>Perpendicular bisector of AB:</b> compasses set to more than half of AB; arcs from A and from B (same radius) crossing above and below the line; join the crossing points. Result cuts AB at 90&#176; through its midpoint.', styles['bullet']))
    s.append(Paragraph('<b>Angle bisector:</b> arc from the vertex crossing both arms; from each of those points, equal-radius arcs crossing inside the angle; join the vertex to the crossing point. Result splits the angle exactly in half.', styles['bullet']))
    s.append(Paragraph('<b>Perpendicular from a point to a line</b> (point not on the line): arc from the point crossing the line twice; equal-radius arcs from those two crossing points, meeting on the far side; join the point to that meeting point.', styles['bullet']))
    s.append(Paragraph('<b>Perpendicular at a point on a line</b>: mark two points on the line equidistant from the given point; equal-radius arcs from those two marks, meeting above (or below) the line; join the given point to that meeting point.', styles['bullet']))
    s.append(Paragraph('Never rub out construction arcs &mdash; they are part of the method and earn marks.', styles['body']))

    s.append(Paragraph('6. Common mistakes', styles['h2']))
    s.append(Paragraph('Describing a rotation without all three parts (angle, direction, centre).', styles['bullet']))
    s.append(Paragraph('Forgetting that a scale factor between 0 and 1 is still an enlargement, even though the shape gets smaller.', styles['bullet']))
    s.append(Paragraph('Placing the image on the wrong side of the centre for a negative scale factor.', styles['bullet']))
    s.append(Paragraph('Rubbing out compass arcs on a construction, or using a protractor instead of compasses.', styles['bullet']))
    s.append(Paragraph('Mixing up the top and bottom numbers in a column vector (top = left/right, bottom = up/down).', styles['bullet']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('transformations_constructions_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Transformations &amp; Constructions', 'Test &middot; 27 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 27'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Translation', styles['h2']))
    s += q('A1', 'Translate the point A(2, 5) by the vector (3, &minus;4). State the coordinates of the image.', 2)
    s += q('A2', 'Find the column vector that translates the point (1, 1) to the point (4, &minus;2).', 2)
    s += q('A3', 'True or false: a translation changes the size of a shape.', 1)

    s.append(Paragraph('Section B &mdash; Rotation', styles['h2']))
    s += q('B1', 'Name the three pieces of information needed to fully describe a rotation.', 3)
    s += q('B2', 'Rotate the point (2, 3) by 180&#176; about the origin. State the coordinates of the image.', 2)

    s.append(Paragraph('Section C &mdash; Reflection', styles['h2']))
    s += q('C1', 'Reflect the point (3, 2) in the y-axis. State the coordinates of the image.', 1)
    s += q('C2', 'Reflect the point (1, 4) in the line y = x. State the coordinates of the image.', 1)
    s += q('C3', 'The point P(5, 1) is reflected in the line x = 2. Find the coordinates of the image.', 2)

    s.append(Paragraph('Section D &mdash; Enlargement', styles['h2']))
    s += q('D1', 'A shape is enlarged by scale factor 3 from a centre of enlargement. A side on the object is 4 cm. Find the length of the corresponding side on the image.', 1)
    s += q('D2', 'A shape is enlarged by scale factor &frac12;. What effect does this have on the size of the shape?', 1)
    s += q('D3', 'A triangle has area 8 cm<sup>2</sup>. It is enlarged by scale factor 3. Find the area of the enlarged triangle.', 2)
    s += q('D4', 'A shape is enlarged by scale factor &minus;2 about a centre of enlargement. Describe two effects this has on the image compared with the object.', 2)
    s += q('D5', 'Explain why a scale factor between 0 and 1 still counts as an "enlargement", even though the shape gets smaller.', 1)

    s.append(Paragraph('Section E &mdash; Constructions', styles['h2']))
    s += q('E1', 'Describe how to construct the perpendicular bisector of a line segment AB, using only a ruler and compasses.', 3)
    s += q('E2', 'Describe how to construct the bisector of an angle, using only a ruler and compasses.', 2)
    s += q('E3', 'Why must construction lines and arcs never be rubbed out on an exam answer?', 1)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('transformations_constructions_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Transformations &amp; Constructions', 'Answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Translation', styles['h2']))
    s.append(Paragraph('A1. (2 + 3, 5 &minus; 4) (1) &nbsp; = <b>(5, 1)</b> (1)', styles['ans']))
    s.append(Paragraph('A2. 4 &minus; 1 = 3 (right), &minus;2 &minus; 1 = &minus;3 (down) (1) &nbsp; vector = <b>(3, &minus;3)</b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>False</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Rotation', styles['h2']))
    s.append(Paragraph('B1. <b>Angle</b> of rotation (1) &nbsp; <b>direction</b> &mdash; clockwise or anticlockwise (1) &nbsp; <b>centre</b> of rotation (1)', styles['ans']))
    s.append(Paragraph('B2. (&minus;2, &minus;3) (1) &nbsp; correct use of the 180&#176; rule (x,y)&#8594;(&minus;x,&minus;y) (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Reflection', styles['h2']))
    s.append(Paragraph('C1. <b>(&minus;3, 2)</b> (1)', styles['ans']))
    s.append(Paragraph('C2. <b>(4, 1)</b> (1)', styles['ans']))
    s.append(Paragraph('C3. Distance from x=2 to x=5 is 3, image x = 2&minus;3 = &minus;1 (1) &nbsp; image = <b>(&minus;1, 1)</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Enlargement', styles['h2']))
    s.append(Paragraph('D1. 4 &times; 3 = <b>12 cm</b> (1)', styles['ans']))
    s.append(Paragraph('D2. The shape becomes <b>smaller</b> (half the size) (1)', styles['ans']))
    s.append(Paragraph('D3. Area SF = 3<sup>2</sup> = 9 (1) &nbsp; 8 &times; 9 = <b>72 cm<sup>2</sup></b> (1)', styles['ans']))
    s.append(Paragraph('D4. Image is <b>twice the size</b> of the object (1) &nbsp; image is on the <b>opposite side</b> of the centre, turned 180&#176; (1)', styles['ans']))
    s.append(Paragraph('D5. The image is still formed by the same ray-from-centre process (just with SF &lt; 1), so it is still classed as an enlargement even though it gets smaller (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Constructions', styles['h2']))
    s.append(Paragraph('E1. Set compasses to a radius more than half of AB (1) &nbsp; draw arcs from A and from B (same radius) so they cross above and below the line (1) &nbsp; join the two crossing points with a straight line (1)', styles['ans']))
    s.append(Paragraph('E2. Draw an arc from the vertex crossing both arms of the angle (1) &nbsp; from each of those crossing points draw equal-radius arcs that meet inside the angle, then join the vertex to that meeting point (1)', styles['ans']))
    s.append(Paragraph('E3. They show the method used and earn marks &mdash; an examiner cannot award construction marks for a "correct-looking" line with no working shown (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly set-up calculation or equation even if the final answer '
        'contains an arithmetic slip. For construction questions, accept any correctly worded description of the '
        'method (exact wording does not need to match). Missing units on an otherwise-correct numerical answer '
        'should lose the final accuracy mark, not the method mark.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
