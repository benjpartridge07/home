# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Straight-Line Graphs (GCSE Maths, Algebra)."""

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
    doc = SimpleDocTemplate('straight_line_graphs_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Straight-Line Graphs',
                 'Quick reference sheet &middot; GCSE Maths, Algebra &middot; keep handy for revision')

    s.append(Paragraph('1. y = mx + c', styles['h2']))
    s.append(Paragraph('<b>m</b> = gradient (steepness &amp; direction) &nbsp;&middot;&nbsp; <b>c</b> = y-intercept (where the line crosses the y-axis, when x = 0).', styles['bodyb']))
    s.append(Paragraph('A bigger gradient is steeper. A negative gradient slopes downward left to right.', styles['body']))
    s.append(Paragraph('e.g. y = 2x + 1 &rarr; gradient <b>2</b>, y-intercept <b>1</b>.', styles['body']))

    s.append(Paragraph('2. Finding the gradient from two points', styles['h2']))
    s.append(Paragraph('<b>m = (y&#8322; &minus; y&#8321;) &divide; (x&#8322; &minus; x&#8321;)</b> &mdash; change in y over change in x.', styles['bodyb']))
    s.append(Paragraph('(1, 3) and (4, 9) &nbsp;&rarr;&nbsp; m = (9&minus;3) &divide; (4&minus;1) = 6&divide;3 = <b>2</b>', styles['body']))

    s.append(Paragraph('3. Plotting from a table, and parallel lines', styles['h2']))
    s.append(Paragraph('Pick x-values, work out matching y-values, plot the points, then join with a straight line.', styles['body']))
    s.append(table([
        [headcell('x'), headcell('&minus;1'), headcell('0'), headcell('1'), headcell('2')],
        [cell('y = 2x + 1'), cell('&minus;1'), cell('1'), cell('3'), cell('5')],
    ], col_widths=[35 * mm, 25 * mm, 25 * mm, 25 * mm, 25 * mm]))
    s.append(Paragraph('<b>Parallel lines have the same gradient</b> (but a different y-intercept). e.g. y = 2x + 1 and y = 2x &minus; 3 are parallel.', styles['body']))

    s.append(Paragraph('4. Finding the equation of a line', styles['h2']))
    s.append(Paragraph(
        'From a table: m = how much y changes each time x increases by 1. c = the y-value when x = 0.', styles['body']))
    s.append(table([
        [headcell('x'), headcell('0'), headcell('1'), headcell('2'), headcell('3')],
        [cell('y'), cell('4'), cell('7'), cell('10'), cell('13')],
    ], col_widths=[35 * mm, 25 * mm, 25 * mm, 25 * mm, 25 * mm]))
    s.append(Paragraph('y increases by 3 each time &rarr; m = 3. When x = 0, y = 4 &rarr; c = 4. &nbsp;&rarr;&nbsp; <b>y = 3x + 4</b>', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('straight_line_graphs_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Straight-Line Graphs', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Reading gradient and y-intercept', styles['h2']))
    s += q('A1', 'State the gradient of y = 6x &minus; 4.', 1)
    s += q('A2', 'State the y-intercept of y = 6x &minus; 4.', 1)
    s += q('A3', 'State the gradient of y = &minus;2x + 9.', 1)
    s += q('A4', 'State the y-intercept of y = &minus;2x + 9.', 1)

    s.append(Paragraph('Section B &mdash; Finding the gradient from two points', styles['h2']))
    s += q('B1', 'Find the gradient of the line through (1, 2) and (3, 10).', 2)
    s += q('B2', 'Find the gradient of the line through (0, 7) and (4, &minus;1).', 2)
    s += q('B3', 'Find the gradient of the line through (&minus;3, &minus;4) and (1, 4).', 2)

    s.append(Paragraph('Section C &mdash; Tables and equations from data', styles['h2']))
    s += q('C1', 'Complete a table of values for y = 3x &minus; 2 when x = &minus;1, 0, 1, 2, and state the coordinates of each point.', 3)
    s += q('C2', 'A line passes through the points (0, &minus;1), (1, 1), (2, 3), (3, 5). Find its equation in the form y = mx + c.', 3)

    s.append(Paragraph('Section D &mdash; Parallel lines and forming equations', styles['h2']))
    s += q('D1', 'A line is parallel to y = 4x + 1 and passes through (0, 6). Write down its equation.', 2)
    s += q('D2', 'Are the lines y = 3x &minus; 5 and y = 3x + 2 parallel? Give a reason.', 2)
    s += q('D3', 'A straight line passes through (2, 5) and (6, 13). Find the equation of the line in the form y = mx + c.', 4)
    s += q('D4', 'Does the point (3, 7) lie on the line y = 2x + 1? Show your working.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('straight_line_graphs_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Straight-Line Graphs', 'Answer sheet &middot; 26 marks total')

    s.append(Paragraph('Section A &mdash; Reading gradient and y-intercept', styles['h2']))
    s.append(Paragraph('A1. <b>6</b> (1) &nbsp; A2. <b>&minus;4</b> (1) &nbsp; A3. <b>&minus;2</b> (1) &nbsp; A4. <b>9</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Finding the gradient from two points', styles['h2']))
    s.append(Paragraph('B1. (10&minus;2) &divide; (3&minus;1) (1) &nbsp; = 8&divide;2 = <b>4</b> (1)', styles['ans']))
    s.append(Paragraph('B2. (&minus;1&minus;7) &divide; (4&minus;0) (1) &nbsp; = &minus;8&divide;4 = <b>&minus;2</b> (1)', styles['ans']))
    s.append(Paragraph('B3. (4&minus;(&minus;4)) &divide; (1&minus;(&minus;3)) (1) &nbsp; = 8&divide;4 = <b>2</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Tables and equations from data', styles['h2']))
    s.append(Paragraph('C1. y-values: &minus;5, &minus;2, 1, 4 (1) &nbsp; points: (&minus;1,&minus;5), (0,&minus;2), (1,1), (2,4) (1) &nbsp; all lie on a straight line (1)', styles['ans']))
    s.append(Paragraph('C2. gradient = (5&minus;(&minus;1)) &divide; (3&minus;0) = 6&divide;3 = 2 (1) &nbsp; y-intercept c = &minus;1 (from x=0) (1) &nbsp; = <b>y = 2x &minus; 1</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Parallel lines and forming equations', styles['h2']))
    s.append(Paragraph('D1. parallel &rarr; gradient = 4 (1) &nbsp; using (0,6): c = 6 &rarr; <b>y = 4x + 6</b> (1)', styles['ans']))
    s.append(Paragraph('D2. both lines have gradient 3 (1) &nbsp; so <b>yes</b>, they are parallel (1)', styles['ans']))
    s.append(Paragraph('D3. gradient = (13&minus;5) &divide; (6&minus;2) = 8&divide;4 = 2 (1) &nbsp; substitute (2,5): 5 = 2(2) + c (1) &nbsp; 5 = 4 + c &rarr; c = 1 (1) &nbsp; = <b>y = 2x + 1</b> (1)', styles['ans']))
    s.append(Paragraph('D4. substitute x = 3: y = 2(3) + 1 = 7 (1) &nbsp; matches the given y-value, so <b>yes</b>, the point lies on the line (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly substituted gradient formula or correctly identified '
        'gradient/intercept, even if the final answer contains an arithmetic error.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
