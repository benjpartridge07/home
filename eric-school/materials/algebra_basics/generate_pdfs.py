# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Expanding, Factorising & Solving Equations (GCSE Maths, Algebra)."""

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
    doc = SimpleDocTemplate('algebra_basics_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Expanding, Factorising &amp; Solving Equations',
                 'Quick reference sheet &middot; GCSE Maths, Algebra &middot; keep handy for revision')

    s.append(Paragraph('1. Expanding single brackets', styles['h2']))
    s.append(Paragraph('<b>a(b + c) = ab + ac</b> &mdash; multiply everything inside by what is outside. A negative multiplier flips every sign inside.', styles['bodyb']))
    s.append(Paragraph('3(x + 4) = <b>3x + 12</b> &nbsp;&middot;&nbsp; &minus;2(x + 6) = <b>&minus;2x &minus; 12</b> &nbsp;&middot;&nbsp; &minus;(3x &minus; 5) = <b>&minus;3x + 5</b>', styles['body']))

    s.append(Paragraph('2. Expanding double brackets (FOIL)', styles['h2']))
    s.append(Paragraph('Multiply every term in the first bracket by every term in the second: <b>First, Outer, Inner, Last</b>.', styles['body']))
    s.append(table([
        [headcell('Brackets'), headcell('Expanded &amp; simplified')],
        [cell('(x + 2)(x + 6)'), cell('x&sup2; + 8x + 12')],
        [cell('(x &minus; 2)(x + 7)'), cell('x&sup2; + 5x &minus; 14')],
        [cell('(x &minus; 4)(x &minus; 3)'), cell('x&sup2; &minus; 7x + 12')],
    ], col_widths=[65 * mm, 65 * mm]))

    s.append(Paragraph('3. Factorising', styles['h2']))
    s.append(Paragraph('<b>Common factor</b>: take out the highest common factor of every term. e.g. 6x + 9 = <b>3(2x + 3)</b>', styles['bullet']))
    s.append(Paragraph('<b>Quadratic x&sup2; + bx + c</b>: find two numbers that multiply to c and add to b.', styles['bullet']))
    s.append(Paragraph('x&sup2; + 7x + 12 &mdash; 3 and 4 multiply to 12, add to 7 &rarr; <b>(x + 3)(x + 4)</b>', styles['body']))
    s.append(Paragraph('x&sup2; + 2x &minus; 15 &mdash; 5 and &minus;3 multiply to &minus;15, add to 2 &rarr; <b>(x + 5)(x &minus; 3)</b>', styles['body']))

    s.append(Paragraph('4. Solving linear equations', styles['h2']))
    s.append(Paragraph('<b>Balance method</b>: do the same operation to both sides until x is alone. Expand any brackets first; collect x terms onto one side if x appears twice.', styles['bodyb']))
    s.append(Paragraph('3x + 7 = 22 &rarr; 3x = 15 &rarr; <b>x = 5</b>', styles['body']))
    s.append(Paragraph('2(x + 3) = 16 &rarr; 2x + 6 = 16 &rarr; 2x = 10 &rarr; <b>x = 5</b>', styles['body']))
    s.append(Paragraph('5x &minus; 3 = 2x + 9 &rarr; 3x &minus; 3 = 9 &rarr; 3x = 12 &rarr; <b>x = 4</b>', styles['body']))

    s.append(Paragraph('5. Check your work', styles['h2']))
    s.append(Paragraph(
        'After factorising, expand your answer back out &mdash; it should match the original expression. '
        'After solving an equation, substitute your value of x back in to check both sides are equal.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('algebra_basics_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Expanding, Factorising &amp; Solving Equations', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Expanding single brackets', styles['h2']))
    s += q('A1', 'Expand 3(x + 5).', 1)
    s += q('A2', 'Expand 6(2x &minus; 1).', 1)
    s += q('A3', 'Expand &minus;4(x &minus; 3).', 1)
    s += q('A4', 'Expand &minus;(2x + 7).', 1)

    s.append(Paragraph('Section B &mdash; Expanding double brackets', styles['h2']))
    s += q('B1', 'Expand and simplify (x + 3)(x + 5).', 2)
    s += q('B2', 'Expand and simplify (x &minus; 2)(x + 6).', 2)
    s += q('B3', 'Expand and simplify (x &minus; 4)(x &minus; 3).', 2)

    s.append(Paragraph('Section C &mdash; Factorising', styles['h2']))
    s += q('C1', 'Factorise 8x + 20.', 1)
    s += q('C2', 'Factorise 15x &minus; 9.', 1)
    s += q('C3', 'Factorise x&sup2; + 8x + 15.', 2)
    s += q('C4', 'Factorise x&sup2; &minus; 2x &minus; 24.', 2)

    s.append(Paragraph('Section D &mdash; Solving equations', styles['h2']))
    s += q('D1', 'Solve 4x + 5 = 21.', 2)
    s += q('D2', 'Solve 3(x &minus; 2) = 15.', 2)
    s += q('D3', 'Solve 6x &minus; 5 = 2x + 11.', 3)
    s += q('D4', 'Solve 2(2x + 3) = x + 21.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('algebra_basics_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Expanding, Factorising &amp; Solving Equations', 'Answer sheet &middot; 26 marks total')

    s.append(Paragraph('Section A &mdash; Expanding single brackets', styles['h2']))
    s.append(Paragraph('A1. <b>3x + 15</b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>12x &minus; 6</b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>&minus;4x + 12</b> (1)', styles['ans']))
    s.append(Paragraph('A4. <b>&minus;2x &minus; 7</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Expanding double brackets', styles['h2']))
    s.append(Paragraph('B1. x&sup2; + 5x + 3x + 15 (1) &nbsp; = <b>x&sup2; + 8x + 15</b> (1)', styles['ans']))
    s.append(Paragraph('B2. x&sup2; + 6x &minus; 2x &minus; 12 (1) &nbsp; = <b>x&sup2; + 4x &minus; 12</b> (1)', styles['ans']))
    s.append(Paragraph('B3. x&sup2; &minus; 3x &minus; 4x + 12 (1) &nbsp; = <b>x&sup2; &minus; 7x + 12</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Factorising', styles['h2']))
    s.append(Paragraph('C1. <b>4(2x + 5)</b> (1)', styles['ans']))
    s.append(Paragraph('C2. <b>3(5x &minus; 3)</b> (1)', styles['ans']))
    s.append(Paragraph('C3. Numbers multiply to 15, add to 8: 3 and 5 (1) &nbsp; = <b>(x + 3)(x + 5)</b> (1)', styles['ans']))
    s.append(Paragraph('C4. Numbers multiply to &minus;24, add to &minus;2: &minus;6 and 4 (1) &nbsp; = <b>(x &minus; 6)(x + 4)</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Solving equations', styles['h2']))
    s.append(Paragraph('D1. 4x = 16 (1) &nbsp; = <b>x = 4</b> (1)', styles['ans']))
    s.append(Paragraph('D2. 3x &minus; 6 = 15 &rarr; 3x = 21 (1) &nbsp; = <b>x = 7</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 6x &minus; 2x = 11 + 5 (1) &nbsp; 4x = 16 (1) &nbsp; = <b>x = 4</b> (1)', styles['ans']))
    s.append(Paragraph('D4. 4x + 6 = x + 21 (1) &nbsp; 3x = 15 (1) &nbsp; = <b>x = 5</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for correctly expanding brackets or correctly identifying the factor '
        'pair, even if the final answer contains an arithmetic error. Accept equivalent forms (e.g. (x+4)(x+5) '
        'or (x+5)(x+4)).',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
