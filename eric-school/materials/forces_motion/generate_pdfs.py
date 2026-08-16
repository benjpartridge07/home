# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Speed, Distance & Acceleration (AQA 8465 4.7.1, Foundation tier)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.graphics.shapes import Drawing, Line, String, Polygon
from reportlab.platypus.flowables import Flowable
from reportlab.pdfbase.pdfmetrics import stringWidth

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
    'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=10.5,
                            textColor=INK, spaceAfter=4),
    'qtext': ParagraphStyle('qtext', fontName='Helvetica', fontSize=10.5,
                             textColor=INK, leading=15, spaceAfter=2),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=10.5,
                           textColor=INK, leading=15, spaceAfter=6),
    'ansb': ParagraphStyle('ansb', fontName='Helvetica-Bold', fontSize=10.5,
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


def draw_label(d, x, y, text, font, size, color):
    # reportlab's base-14 fonts render Delta (U+0394) as a garbled/blank glyph in
    # shapes.String (unlike Paragraph text, which handles it fine) — and the 'Symbol'
    # font fallback isn't available either (renders as a solid box). Draw an actual
    # small triangle shape for Delta instead of relying on any font glyph for it.
    if 'Δ' in text:
        rest = text.replace('Δ', '')
        tri_w = size * 0.72
        tri_h = size * 0.72
        gap = size * 0.12
        rest_w = stringWidth(rest, font, size) if rest else 0
        start_x = x - (tri_w + gap + rest_w) / 2
        base_y = y - size * 0.06
        d.add(Polygon(points=[
            start_x, base_y,
            start_x + tri_w, base_y,
            start_x + tri_w / 2, base_y + tri_h,
        ], fillColor=None, strokeColor=color, strokeWidth=1.6))
        if rest:
            d.add(String(start_x + tri_w + gap, y, rest, fontName=font, fontSize=size,
                          textColor=color, textAnchor='start'))
    else:
        d.add(String(x, y, text, fontName=font, fontSize=size, textColor=color, textAnchor='middle'))


def formula_triangle(apex, apex_word, left, left_word, right, right_word, blank=False):
    w, h = 220, 190
    d = Drawing(w, h)
    apex_pt = (110, 175)
    left_pt = (20, 20)
    right_pt = (200, 20)
    mid_y = (apex_pt[1] + left_pt[1]) / 2
    t = 0.5
    lx_mid = apex_pt[0] + (left_pt[0] - apex_pt[0]) * t
    rx_mid = apex_pt[0] + (right_pt[0] - apex_pt[0]) * t

    d.add(Line(apex_pt[0], apex_pt[1], left_pt[0], left_pt[1], strokeColor=INK, strokeWidth=1.4))
    d.add(Line(apex_pt[0], apex_pt[1], right_pt[0], right_pt[1], strokeColor=INK, strokeWidth=1.4))
    d.add(Line(left_pt[0], left_pt[1], right_pt[0], right_pt[1], strokeColor=INK, strokeWidth=1.4))
    d.add(Line(lx_mid, mid_y, rx_mid, mid_y, strokeColor=INK, strokeWidth=1.4))
    d.add(Line(110, mid_y, 110, 20, strokeColor=INK, strokeWidth=1.4))

    if blank:
        d.add(String(110, 130, '?', fontName='Helvetica-Bold', fontSize=22,
                      textColor=INK_SOFT, textAnchor='middle'))
        d.add(String(64, 50, '?', fontName='Helvetica-Bold', fontSize=22,
                      textColor=INK_SOFT, textAnchor='middle'))
        d.add(String(156, 50, '?', fontName='Helvetica-Bold', fontSize=22,
                      textColor=INK_SOFT, textAnchor='middle'))
    else:
        draw_label(d, 110, 132, apex, 'Helvetica-Bold', 22, PHYS)
        d.add(String(110, 116, apex_word, fontName='Helvetica', fontSize=8,
                      textColor=INK_SOFT, textAnchor='middle'))
        draw_label(d, 64, 52, left, 'Helvetica-Bold', 20, MATHS)
        d.add(String(64, 38, left_word, fontName='Helvetica', fontSize=8,
                      textColor=INK_SOFT, textAnchor='middle'))
        draw_label(d, 156, 52, right, 'Helvetica-Bold', 20, MATHS)
        d.add(String(156, 38, right_word, fontName='Helvetica', fontSize=8,
                      textColor=INK_SOFT, textAnchor='middle'))
    return d


def distance_time_graph():
    w, h = 260, 170
    d = Drawing(w, h)
    ox, oy = 35, 20
    ax_len_x, ax_len_y = 210, 130
    d.add(Line(ox, oy, ox, oy + ax_len_y, strokeColor=INK, strokeWidth=1.2))
    d.add(Line(ox, oy, ox + ax_len_x, oy, strokeColor=INK, strokeWidth=1.2))
    d.add(String(ox + ax_len_x / 2, oy - 14, 'time', fontName='Helvetica', fontSize=9,
                  textColor=INK_SOFT, textAnchor='middle'))
    d.add(String(ox - 22, oy + ax_len_y / 2, 'distance', fontName='Helvetica', fontSize=9,
                  textColor=INK_SOFT, textAnchor='middle'))
    # constant speed segment
    p1 = (ox, oy)
    p2 = (ox + 90, oy + 80)
    d.add(Line(*p1, *p2, strokeColor=MATHS, strokeWidth=2))
    # stationary (flat) segment
    p3 = (ox + 90 + 50, oy + 80)
    d.add(Line(*p2, *p3, strokeColor=PHYS, strokeWidth=2))
    d.add(String((p1[0] + p2[0]) / 2 - 6, (p1[1] + p2[1]) / 2 + 8, 'moving',
                  fontName='Helvetica-Oblique', fontSize=8, textColor=MATHS, textAnchor='middle'))
    d.add(String((p2[0] + p3[0]) / 2, p2[1] + 8, 'stopped',
                  fontName='Helvetica-Oblique', fontSize=8, textColor=PHYS, textAnchor='middle'))
    return d


def velocity_time_graph():
    w, h = 260, 170
    d = Drawing(w, h)
    ox, oy = 35, 20
    ax_len_x, ax_len_y = 210, 130
    d.add(Line(ox, oy, ox, oy + ax_len_y, strokeColor=INK, strokeWidth=1.2))
    d.add(Line(ox, oy, ox + ax_len_x, oy, strokeColor=INK, strokeWidth=1.2))
    d.add(String(ox + ax_len_x / 2, oy - 14, 'time', fontName='Helvetica', fontSize=9,
                  textColor=INK_SOFT, textAnchor='middle'))
    d.add(String(ox - 22, oy + ax_len_y / 2, 'velocity', fontName='Helvetica', fontSize=9,
                  textColor=INK_SOFT, textAnchor='middle'))
    p1 = (ox, oy)
    p2 = (ox + 130, oy + 100)
    shaded = Polygon(points=[p1[0], p1[1], p2[0], p2[1], p2[0], p1[1]],
                      fillColor=colors.HexColor('#DDE6EF'), strokeColor=None)
    d.add(shaded)
    d.add(Line(*p1, *p2, strokeColor=MATHS, strokeWidth=2))
    label_x = (p1[0] + p2[0]) / 2 + 18
    label_y = (p1[1] + p2[1]) / 2 - 6
    d.add(String(label_x, label_y + 10, 'gradient',
                  fontName='Helvetica-Oblique', fontSize=8, textColor=MATHS, textAnchor='start'))
    d.add(String(label_x, label_y - 2, '= acceleration',
                  fontName='Helvetica-Oblique', fontSize=8, textColor=MATHS, textAnchor='start'))
    d.add(String(p2[0] - 55, oy + 10, 'area = distance',
                  fontName='Helvetica-Oblique', fontSize=8, textColor=PHYS, textAnchor='start'))
    return d


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
    doc = SimpleDocTemplate('speed_distance_acceleration_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Speed, Distance &amp; Acceleration',
                 'Quick reference sheet &middot; Physics &amp; Maths &middot; keep handy for revision')

    s.append(Paragraph('1. Scalars and vectors', styles['h2']))
    s.append(Paragraph(
        'Some quantities need a direction to be complete, and some don’t.', styles['body']))
    s.append(Paragraph('<b>Distance</b> — how far something moves. No direction needed — a <b>scalar</b> quantity.', styles['bullet']))
    s.append(Paragraph('<b>Displacement</b> — distance in a straight line from start to finish, <i>and</i> the direction of that line. A <b>vector</b> quantity.', styles['bullet']))
    s.append(Paragraph('<b>Speed</b> — how fast something moves. No direction needed — a <b>scalar</b> quantity.', styles['bullet']))
    s.append(Paragraph('<b>Velocity</b> — speed in a given direction. A <b>vector</b> quantity.', styles['bullet']))
    s.append(Spacer(1, 6))
    s.append(Paragraph('Typical speeds (worth memorising):', styles['body']))
    s.append(table([
        [headcell('Walking'), headcell('Running'), headcell('Cycling'), headcell('Sound in air')],
        [cell('1.5 m/s'), cell('3 m/s'), cell('6 m/s'), cell('330 m/s')],
    ], col_widths=[42 * mm, 42 * mm, 42 * mm, 44 * mm]))

    s.append(Paragraph('2. Distance, speed and time', styles['h2']))
    s.append(Paragraph('distance = speed &times; time &nbsp;&nbsp; or &nbsp;&nbsp; <b>s = vt</b>', styles['bodyb']))
    s.append(Paragraph('s &mdash; distance, in metres, m &nbsp;&middot;&nbsp; v &mdash; speed, in metres per second, m/s &nbsp;&middot;&nbsp; t &mdash; time, in seconds, s', styles['body']))
    s.append(formula_triangle('s', 'distance', 'v', 'speed', 't', 'time'))
    s.append(Paragraph('Cover the letter you want to find. Top-over-bottom means divide, side-by-side on the bottom means multiply.', styles['body']))
    s.append(Paragraph('Cover <b>s</b> → v next to t → <b>s = vt</b>. Cover <b>v</b> → s over t → <b>v = s / t</b>. Cover <b>t</b> → s over v → <b>t = s / v</b>.', styles['body']))

    s.append(Paragraph('3. Distance&ndash;time graphs', styles['h2']))
    s.append(distance_time_graph())
    s.append(Paragraph('The <b>gradient</b> (steepness) of a distance–time graph is equal to the <b>speed</b>. A steeper line means a faster speed. A <b>flat, horizontal</b> line means the object has stopped (zero speed).', styles['body']))

    s.append(Paragraph('4. Acceleration', styles['h2']))
    s.append(Paragraph('acceleration = change in velocity &divide; time &nbsp;&nbsp; or &nbsp;&nbsp; <b>a = &Delta;v / t</b>', styles['bodyb']))
    s.append(Paragraph('a &mdash; acceleration, in metres per second squared, m/s<super>2</super> &nbsp;&middot;&nbsp; &Delta;v &mdash; change in velocity, in m/s &nbsp;&middot;&nbsp; t &mdash; time, in s', styles['body']))
    s.append(formula_triangle('Δv', 'change in velocity', 'a', 'acceleration', 't', 'time'))
    s.append(Paragraph('A negative acceleration means the object is <b>decelerating</b> (slowing down). Near the Earth’s surface, an object in free fall accelerates at about <b>9.8 m/s<super>2</super></b>.', styles['body']))

    s.append(Paragraph('5. Velocity&ndash;time graphs', styles['h2']))
    s.append(velocity_time_graph())
    s.append(Paragraph('The <b>gradient</b> of a velocity–time graph is equal to the <b>acceleration</b>. The <b>area</b> underneath the graph (down to the time axis) is equal to the <b>distance travelled</b> — for straight-line graphs this is just the area of the triangle or rectangle formed.', styles['body']))

    s.append(Paragraph('6. Worked examples', styles['h2']))
    s.append(table([
        [headcell('Given'), headcell('Find'), headcell('Working'), headcell('Answer')],
        [cell('v = 15 m/s, t = 8 s'), cell('s'), cell('s = vt = 15 &times; 8'), cell('120 m')],
        [cell('s = 180 m, t = 12 s'), cell('v'), cell('v = s / t = 180 / 12'), cell('15 m/s')],
        [cell('s = 90 m, v = 6 m/s'), cell('t'), cell('t = s / v = 90 / 6'), cell('15 s')],
        [cell('&Delta;v = 18 m/s, t = 6 s'), cell('a'), cell('a = &Delta;v / t = 18 / 6'), cell('3 m/s<super>2</super>')],
        [cell('a = 5 m/s<super>2</super>, t = 4 s'), cell('&Delta;v'), cell('&Delta;v = at = 5 &times; 4'), cell('20 m/s')],
    ], col_widths=[46 * mm, 16 * mm, 56 * mm, 30 * mm]))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('speed_distance_acceleration_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Speed, Distance &amp; Acceleration', 'Test &middot; 27 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 27'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Complete the formula triangles', styles['h2']))
    s.append(Paragraph('A1. Fill in the three blanks with s, v and t in the correct places.', styles['qtext']))
    s.append(formula_triangle(None, None, None, None, None, None, blank=True))
    s.append(Paragraph('[3 marks]', styles['marks']))
    s.append(Paragraph('A2. Fill in the three blanks with &Delta;v, a and t in the correct places.', styles['qtext']))
    s.append(formula_triangle(None, None, None, None, None, None, blank=True))
    s.append(Paragraph('[3 marks]', styles['marks']))

    s.append(Paragraph('Section B &mdash; Straight substitution', styles['h2']))
    s += q('B1', 'A cyclist travels at a constant speed of 15 m/s for 8 s. Calculate the distance travelled.', 2)
    s.append(Spacer(1, 14))
    s += q('B2', 'An object accelerates at 5 m/s<super>2</super> for 3 s. Calculate the change in velocity.', 2)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section C &mdash; Rearrange and solve', styles['h2']))
    s += q('C1', 'A car travels 180 m in 12 s. Calculate its average speed. Show how you rearranged the equation.', 3)
    s.append(Spacer(1, 14))
    s += q('C2', 'A cyclist travels 90 m at a constant speed of 6 m/s. Calculate how long the journey takes. Show how you rearranged the equation.', 3)
    s.append(Spacer(1, 14))
    s += q('C3', 'An object accelerates from rest to a velocity of 20 m/s in 4 s. Calculate its acceleration.', 3)
    s.append(Spacer(1, 14))

    s.append(Paragraph('Section D &mdash; Scalar or vector?', styles['h2']))
    s.append(Paragraph('State whether each of the following is a scalar or a vector quantity.', styles['qtext']))
    s.append(Spacer(1, 4))
    s.append(Paragraph('(a) distance &nbsp;&nbsp;&nbsp; (b) displacement &nbsp;&nbsp;&nbsp; (c) speed &nbsp;&nbsp;&nbsp; (d) velocity', styles['qtext']))
    s.append(Paragraph('[4 marks]', styles['marks']))

    s.append(Paragraph('Section E &mdash; Graph interpretation', styles['h2']))
    s.append(Paragraph(
        '<b>E1.</b> A walker’s distance&ndash;time graph shows a straight diagonal line for the first 10 s, '
        'then a horizontal line for the next 5 s, then a diagonal line steeper than the first for the last 10 s.',
        styles['qtext']))
    s.append(Spacer(1, 4))
    s.append(Paragraph('(a) Describe the walker’s motion during each of the three parts. [3 marks]', styles['qtext']))
    s.append(Spacer(1, 20))
    s.append(Paragraph('(b) State which part shows the fastest speed, and explain how you know. [1 mark]', styles['qtext']))

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('speed_distance_acceleration_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Speed, Distance &amp; Acceleration', 'Answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Formula triangles', styles['h2']))
    s.append(Paragraph('A1. Top cell = <b>s</b> (distance) &nbsp;&nbsp; Bottom-left = <b>v</b> (speed) &nbsp;&nbsp; Bottom-right = <b>t</b> (time)', styles['ans']))
    s.append(Paragraph('[1 mark each, 3 marks total]', styles['marks']))
    s.append(Paragraph('A2. Top cell = <b>&Delta;v</b> (change in velocity) &nbsp;&nbsp; Bottom-left = <b>a</b> (acceleration) &nbsp;&nbsp; Bottom-right = <b>t</b> (time)', styles['ans']))
    s.append(Paragraph('[1 mark each, 3 marks total]', styles['marks']))

    s.append(Paragraph('Section B &mdash; Straight substitution', styles['h2']))
    s.append(Paragraph('<b>B1.</b> s = vt = 15 &times; 8 (1) &nbsp; s = <b>120 m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>B2.</b> &Delta;v = at = 5 &times; 3 (1) &nbsp; &Delta;v = <b>15 m/s</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Rearrange and solve', styles['h2']))
    s.append(Paragraph('<b>C1.</b> v = s / t (1) &nbsp; v = 180 / 12 (1) &nbsp; v = <b>15 m/s</b> (1)', styles['ans']))
    s.append(Paragraph('<b>C2.</b> t = s / v (1) &nbsp; t = 90 / 6 (1) &nbsp; t = <b>15 s</b> (1)', styles['ans']))
    s.append(Paragraph('<b>C3.</b> &Delta;v = 20 &minus; 0 = 20 m/s (1) &nbsp; a = &Delta;v / t = 20 / 4 (1) &nbsp; a = <b>5 m/s<super>2</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Scalar or vector?', styles['h2']))
    s.append(Paragraph('(a) distance &mdash; <b>scalar</b> (1) &nbsp; (b) displacement &mdash; <b>vector</b> (1) &nbsp; (c) speed &mdash; <b>scalar</b> (1) &nbsp; (d) velocity &mdash; <b>vector</b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Graph interpretation', styles['h2']))
    s.append(Paragraph(
        '(a) First 10 s: moving at a constant (steady) speed (1). Next 5 s: stationary / at rest, no distance covered (1). '
        'Last 10 s: moving at a constant speed, greater than the first part (1).', styles['ans']))
    s.append(Paragraph(
        '(b) The <b>last part</b> (final 10 s) is fastest, because it has the steepest gradient on the distance&ndash;time graph (1).', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly rearranged equation and correct substitution even if the '
        'final answer contains an arithmetic error. In Section E, accept any equivalent correct description of the motion.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
