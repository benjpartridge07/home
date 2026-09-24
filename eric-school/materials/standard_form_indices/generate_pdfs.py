# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Standard Form & Indices (GCSE Maths, Number)."""

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
    doc = SimpleDocTemplate('standard_form_indices_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices',
                 'Quick reference sheet &middot; GCSE Maths, Number &middot; keep handy for revision')

    s.append(Paragraph('1. Laws of indices', styles['h2']))
    s.append(Paragraph('<b>Multiplying</b> (same base): a<super>m</super> &times; a<super>n</super> = a<super>m+n</super> &mdash; add the powers.', styles['bullet']))
    s.append(Paragraph('<b>Dividing</b> (same base): a<super>m</super> &divide; a<super>n</super> = a<super>m&minus;n</super> &mdash; subtract the powers.', styles['bullet']))
    s.append(Paragraph('<b>Power of a power</b>: (a<super>m</super>)<super>n</super> = a<super>m&times;n</super> &mdash; multiply the powers.', styles['bullet']))
    s.append(Paragraph('These laws only apply when the base is the same on both sides.', styles['body']))
    s.append(Paragraph('e.g. 3<super>4</super> &times; 3<super>2</super> = 3<super>6</super> &nbsp;&middot;&nbsp; 5<super>7</super> &divide; 5<super>3</super> = 5<super>4</super> &nbsp;&middot;&nbsp; (2<super>3</super>)<super>2</super> = 2<super>6</super> = <b>64</b>', styles['body']))

    s.append(Paragraph('2. Powers to know by heart, and estimating roots', styles['h2']))
    s.append(Paragraph('Recall (no calculator): powers of 2 up to 2<super>10</super>=1024, powers of 3 up to 3<super>5</super>=243, powers of 4 up to 4<super>4</super>=256, powers of 5 up to 5<super>4</super>=625, and square numbers up to 15&times;15.', styles['body']))
    s.append(Paragraph('Also know: 1000 = 10<super>3</super>, 1,000,000 = 10<super>6</super>.', styles['body']))
    s.append(Paragraph('<b>Estimating a root</b>: find the two whole numbers either side. e.g. &radic;50: 7<super>2</super>=49 and 8<super>2</super>=64, so &radic;50 is between <b>7 and 8</b>.', styles['bullet']))

    s.append(Paragraph('3. Zero and negative indices', styles['h2']))
    s.append(Paragraph('<b>a<super>0</super> = 1</b> for any non-zero a. &nbsp;e.g. 9<super>0</super> = 1, 100<super>0</super> = 1.', styles['bullet']))
    s.append(Paragraph('<b>a<super>&minus;n</super> = 1 &divide; a<super>n</super></b> &mdash; a negative index flips the number into a fraction, it does not make the answer negative.', styles['bullet']))
    s.append(table([
        [headcell('Expression'), headcell('Value')],
        [cell('7<super>0</super>'), cell('1')],
        [cell('3<super>&minus;1</super>'), cell('1/3')],
        [cell('4<super>&minus;2</super>'), cell('1/16')],
        [cell('10<super>&minus;2</super>'), cell('0.01')],
    ], col_widths=[65 * mm, 65 * mm]))

    s.append(Paragraph('4. Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('The same three laws from Section 1 apply when the base is a letter. If there is a coefficient (number in front), handle the numbers and letters separately.', styles['body']))
    s.append(Paragraph('e.g. x<super>4</super> &times; x<super>3</super> = x<super>7</super> &nbsp;&middot;&nbsp; x<super>9</super> &divide; x<super>2</super> = x<super>7</super> &nbsp;&middot;&nbsp; (x<super>2</super>)<super>5</super> = x<super>10</super>', styles['body']))
    s.append(Paragraph('e.g. 2x<super>3</super> &times; 3x<super>4</super> = 6x<super>7</super> &nbsp;&middot;&nbsp; (2x<super>3</super>)<super>2</super> = 2<super>2</super> &times; x<super>3&times;2</super> = <b>4x<super>6</super></b>', styles['body']))
    s.append(Paragraph('x<super>0</super> = 1, and x<super>&minus;2</super> = 1 &divide; x<super>2</super> (same rules as Section 3).', styles['bullet']))

    s.append(Paragraph('5. Fractional indices <font color="#B5762A">(Higher)</font>', styles['h2']))
    s.append(Paragraph('A fractional index means a root: the denominator says which root to take, the numerator is a power applied after.', styles['body']))
    s.append(Paragraph('<b>a<super>1/n</super> = <super>n</super>&radic;a</b> &nbsp;&middot;&nbsp; <b>a<super>m/n</super> = (<super>n</super>&radic;a)<super>m</super></b>', styles['bodyb']))
    s.append(Paragraph('e.g. 8<super>1/3</super> = cube root of 8 = <b>2</b>. &nbsp; 4<super>3/2</super> = (&radic;4)<super>3</super> = 2<super>3</super> = <b>8</b>. &nbsp; 9<super>&minus;1/2</super> = 1 &divide; &radic;9 = <b>1/3</b>.', styles['body']))

    s.append(Paragraph('6. Standard form: writing large and small numbers', styles['h2']))
    s.append(Paragraph(
        'Standard form writes any number as <b>A &times; 10<super>n</super></b>, where <b>1 &le; A &lt; 10</b> and n is an integer. '
        'Large numbers (10 or more) use a positive power; small numbers (less than 1) use a negative power.', styles['body']))
    s.append(table([
        [headcell('Ordinary number'), headcell('Standard form')],
        [cell('8,000'), cell('8 &times; 10<super>3</super>')],
        [cell('450,000'), cell('4.5 &times; 10<super>5</super>')],
        [cell('0.006'), cell('6 &times; 10<super>&minus;3</super>')],
        [cell('0.00072'), cell('7.2 &times; 10<super>&minus;4</super>')],
    ], col_widths=[65 * mm, 65 * mm]))

    s.append(Paragraph('7. Calculating with standard form', styles['h2']))
    s.append(Paragraph('<b>Multiply</b>: (A &times; 10<super>m</super>) &times; (B &times; 10<super>n</super>) = (A &times; B) &times; 10<super>m+n</super>', styles['bodyb']))
    s.append(Paragraph('<b>Divide</b>: (A &times; 10<super>m</super>) &divide; (B &times; 10<super>n</super>) = (A &divide; B) &times; 10<super>m&minus;n</super>', styles['bodyb']))
    s.append(Paragraph(
        'If the front numbers multiply to 10 or more, adjust back into standard form. '
        'e.g. (5 &times; 10<super>6</super>) &times; (4 &times; 10<super>3</super>) = 20 &times; 10<super>9</super> = <b>2 &times; 10<super>10</super></b>.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('standard_form_indices_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test &middot; 41 marks total &middot; Sections F &amp; G include Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 41'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s += q('A1', 'Write 4<super>5</super> &times; 4<super>3</super> as a single power of 4.', 1)
    s += q('A2', 'Write 7<super>9</super> &divide; 7<super>2</super> as a single power of 7.', 1)
    s += q('A3', 'Write (6<super>2</super>)<super>3</super> as a single power of 6.', 1)
    s += q('A4', 'Work out the value of 2<super>3</super> &times; 2<super>2</super>.', 2)

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s += q('B1', 'Work out the value of 12<super>0</super>.', 1)
    s += q('B2', 'Work out the value of 5<super>&minus;2</super>. Give your answer as a fraction.', 2)
    s += q('B3', 'Work out the value of 10<super>&minus;3</super>. Give your answer as a decimal.', 2)

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s += q('C1', 'Write 72,000 in standard form.', 2)
    s += q('C2', 'Write 8,300,000 in standard form.', 2)
    s += q('C3', 'Write 0.0048 in standard form.', 2)
    s += q('C4', 'Write 0.00003 in standard form.', 2)

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s += q('D1', 'Write 6.5 &times; 10<super>4</super> as an ordinary number.', 1)
    s += q('D2', 'Write 3 &times; 10<super>&minus;5</super> as an ordinary number.', 1)
    s += q('D3', 'Work out (4 &times; 10<super>3</super>) &times; (2 &times; 10<super>5</super>). Give your answer in standard form.', 3)
    s += q('D4', 'Work out (9 &times; 10<super>8</super>) &divide; (3 &times; 10<super>3</super>). Give your answer in standard form.', 3)

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s += q('E1', 'Write down the value of 3<super>4</super>.', 1)
    s += q('E2', '&radic;60 lies between which two consecutive whole numbers?', 1)

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s += q('F1', 'Simplify a<super>6</super> &times; a<super>4</super>.', 1)
    s += q('F2', 'Simplify b<super>10</super> &divide; b<super>3</super>.', 1)
    s += q('F3', 'Simplify (c<super>3</super>)<super>4</super>.', 1)
    s += q('F4', 'Simplify 5d<super>2</super> &times; 2d<super>6</super>.', 2)
    s += q('F5', 'Simplify (3e<super>2</super>)<super>3</super>.', 2)

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s += q('G1', 'Work out the value of 49<super>1/2</super>.', 1)
    s += q('G2', 'Work out the value of 27<super>1/3</super>.', 1)
    s += q('G3', 'Work out the value of 16<super>3/4</super>.', 2)
    s += q('G4', 'Work out the value of 9<super>&minus;1/2</super>.', 2)

    doc.build(s)


# ---------------------------------------------------------------- TEST 2

def build_test2():
    doc = SimpleDocTemplate('standard_form_indices_test2.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 2 &middot; 41 marks total &middot; Sections F &amp; G include Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 41'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s += q('A1', 'Write 3<super>6</super> &times; 3<super>2</super> as a single power of 3.', 1)
    s += q('A2', 'Write 8<super>7</super> &divide; 8<super>3</super> as a single power of 8.', 1)
    s += q('A3', 'Write (5<super>3</super>)<super>2</super> as a single power of 5.', 1)
    s += q('A4', 'Work out the value of 3<super>2</super> &times; 3<super>3</super>.', 2)

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s += q('B1', 'Work out the value of 9<super>0</super>.', 1)
    s += q('B2', 'Work out the value of 4<super>&minus;2</super>. Give your answer as a fraction.', 2)
    s += q('B3', 'Work out the value of 10<super>&minus;4</super>. Give your answer as a decimal.', 2)

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s += q('C1', 'Write 54,000 in standard form.', 2)
    s += q('C2', 'Write 6,200,000 in standard form.', 2)
    s += q('C3', 'Write 0.0067 in standard form.', 2)
    s += q('C4', 'Write 0.00009 in standard form.', 2)

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s += q('D1', 'Write 4.2 &times; 10<super>3</super> as an ordinary number.', 1)
    s += q('D2', 'Write 7 &times; 10<super>&minus;4</super> as an ordinary number.', 1)
    s += q('D3', 'Work out (3 &times; 10<super>2</super>) &times; (3 &times; 10<super>4</super>). Give your answer in standard form.', 3)
    s += q('D4', 'Work out (8 &times; 10<super>7</super>) &divide; (2 &times; 10<super>2</super>). Give your answer in standard form.', 3)

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s += q('E1', 'Write down the value of 2<super>6</super>.', 1)
    s += q('E2', '&radic;90 lies between which two consecutive whole numbers?', 1)

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s += q('F1', 'Simplify p<super>5</super> &times; p<super>4</super>.', 1)
    s += q('F2', 'Simplify q<super>11</super> &divide; q<super>4</super>.', 1)
    s += q('F3', 'Simplify (r<super>2</super>)<super>5</super>.', 1)
    s += q('F4', 'Simplify 4s<super>3</super> &times; 3s<super>4</super>.', 2)
    s += q('F5', 'Simplify (2t<super>3</super>)<super>4</super>.', 2)

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s += q('G1', 'Work out the value of 36<super>1/2</super>.', 1)
    s += q('G2', 'Work out the value of 8<super>1/3</super>.', 1)
    s += q('G3', 'Work out the value of 81<super>3/4</super>.', 2)
    s += q('G4', 'Work out the value of 16<super>&minus;1/2</super>.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('standard_form_indices_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Answer sheet &middot; 41 marks total')

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s.append(Paragraph('A1. <b>4<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>7<super>7</super></b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>6<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('A4. 2<super>3</super> &times; 2<super>2</super> = 2<super>5</super> (1) &nbsp; = <b>32</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s.append(Paragraph('B1. <b>1</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 1 &divide; 5<super>2</super> = 1 &divide; 25 (1) &nbsp; = <b>1/25</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1 &divide; 10<super>3</super> = 1 &divide; 1000 (1) &nbsp; = <b>0.001</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s.append(Paragraph('C1. 7.2 (1) &nbsp; = <b>7.2 &times; 10<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('C2. 8.3 (1) &nbsp; = <b>8.3 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('C3. 4.8 (1) &nbsp; = <b>4.8 &times; 10<super>&minus;3</super></b> (1)', styles['ans']))
    s.append(Paragraph('C4. 3 (1) &nbsp; = <b>3 &times; 10<super>&minus;5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s.append(Paragraph('D1. <b>65,000</b> (1)', styles['ans']))
    s.append(Paragraph('D2. <b>0.00003</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 4 &times; 2 = 8, 10<super>3</super> &times; 10<super>5</super> = 10<super>8</super> (1) &nbsp; = 8 &times; 10<super>8</super> (1) &nbsp; already in standard form: <b>8 &times; 10<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. 9 &divide; 3 = 3, 10<super>8</super> &divide; 10<super>3</super> = 10<super>5</super> (1) &nbsp; = 3 &times; 10<super>5</super> (1) &nbsp; already in standard form: <b>3 &times; 10<super>5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s.append(Paragraph('E1. <b>81</b> (1)', styles['ans']))
    s.append(Paragraph('E2. 7<super>2</super>=49, 8<super>2</super>=64 &nbsp; = between <b>7 and 8</b> (1)', styles['ans']))

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('F1. <b>a<super>10</super></b> (1)', styles['ans']))
    s.append(Paragraph('F2. <b>b<super>7</super></b> (1)', styles['ans']))
    s.append(Paragraph('F3. <b>c<super>12</super></b> (1)', styles['ans']))
    s.append(Paragraph('F4. 5 &times; 2 = 10 (1) &nbsp; d<super>2+6</super> = d<super>8</super> (1) &nbsp; = <b>10d<super>8</super></b>', styles['ans']))
    s.append(Paragraph('F5. 3<super>3</super> = 27 (1) &nbsp; e<super>2&times;3</super> = e<super>6</super> (1) &nbsp; = <b>27e<super>6</super></b>', styles['ans']))

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s.append(Paragraph('G1. &radic;49 = <b>7</b> (1)', styles['ans']))
    s.append(Paragraph('G2. cube root of 27 = <b>3</b> (1)', styles['ans']))
    s.append(Paragraph('G3. 4th root of 16 = 2 (1) &nbsp; 2<super>3</super> = <b>8</b> (1)', styles['ans']))
    s.append(Paragraph('G4. &radic;9 = 3 (1) &nbsp; 1 &divide; 3 = <b>1/3</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- TEST 3

def build_test3():
    doc = SimpleDocTemplate('standard_form_indices_test3.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 3 &middot; 41 marks total &middot; Sections F &amp; G include Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 41'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s += q('A1', 'Write 2<super>5</super> &times; 2<super>4</super> as a single power of 2.', 1)
    s += q('A2', 'Write 6<super>8</super> &divide; 6<super>5</super> as a single power of 6.', 1)
    s += q('A3', 'Write (4<super>2</super>)<super>3</super> as a single power of 4.', 1)
    s += q('A4', 'Work out the value of 5<super>1</super> &times; 5<super>2</super>.', 2)

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s += q('B1', 'Work out the value of 7<super>0</super>.', 1)
    s += q('B2', 'Work out the value of 3<super>&minus;2</super>. Give your answer as a fraction.', 2)
    s += q('B3', 'Work out the value of 10<super>&minus;5</super>. Give your answer as a decimal.', 2)

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s += q('C1', 'Write 83,000 in standard form.', 2)
    s += q('C2', 'Write 9,100,000 in standard form.', 2)
    s += q('C3', 'Write 0.0025 in standard form.', 2)
    s += q('C4', 'Write 0.00006 in standard form.', 2)

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s += q('D1', 'Write 5.1 &times; 10<super>3</super> as an ordinary number.', 1)
    s += q('D2', 'Write 6 &times; 10<super>&minus;4</super> as an ordinary number.', 1)
    s += q('D3', 'Work out (2 &times; 10<super>3</super>) &times; (4 &times; 10<super>4</super>). Give your answer in standard form.', 3)
    s += q('D4', 'Work out (6 &times; 10<super>6</super>) &divide; (3 &times; 10<super>2</super>). Give your answer in standard form.', 3)

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s += q('E1', 'Write down the value of 2<super>7</super>.', 1)
    s += q('E2', '&radic;110 lies between which two consecutive whole numbers?', 1)

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s += q('F1', 'Simplify m<super>7</super> &times; m<super>2</super>.', 1)
    s += q('F2', 'Simplify n<super>9</super> &divide; n<super>5</super>.', 1)
    s += q('F3', 'Simplify (k<super>4</super>)<super>2</super>.', 1)
    s += q('F4', 'Simplify 3x<super>2</super> &times; 5x<super>4</super>.', 2)
    s += q('F5', 'Simplify (2y<super>4</super>)<super>3</super>.', 2)

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s += q('G1', 'Work out the value of 25<super>1/2</super>.', 1)
    s += q('G2', 'Work out the value of 64<super>1/3</super>.', 1)
    s += q('G3', 'Work out the value of 32<super>2/5</super>.', 2)
    s += q('G4', 'Work out the value of 4<super>&minus;3/2</super>.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS 2

def build_answers2():
    doc = SimpleDocTemplate('standard_form_indices_test2_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 2 &middot; Answer sheet &middot; 41 marks total')

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s.append(Paragraph('A1. <b>3<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>8<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>5<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('A4. 3<super>2</super> &times; 3<super>3</super> = 3<super>5</super> (1) &nbsp; = <b>243</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s.append(Paragraph('B1. <b>1</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 1 &divide; 4<super>2</super> = 1 &divide; 16 (1) &nbsp; = <b>1/16</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1 &divide; 10<super>4</super> = 1 &divide; 10000 (1) &nbsp; = <b>0.0001</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s.append(Paragraph('C1. 5.4 (1) &nbsp; = <b>5.4 &times; 10<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('C2. 6.2 (1) &nbsp; = <b>6.2 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('C3. 6.7 (1) &nbsp; = <b>6.7 &times; 10<super>&minus;3</super></b> (1)', styles['ans']))
    s.append(Paragraph('C4. 9 (1) &nbsp; = <b>9 &times; 10<super>&minus;5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s.append(Paragraph('D1. <b>4,200</b> (1)', styles['ans']))
    s.append(Paragraph('D2. <b>0.0007</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 3 &times; 3 = 9, 10<super>2</super> &times; 10<super>4</super> = 10<super>6</super> (1) &nbsp; = 9 &times; 10<super>6</super> (1) &nbsp; already in standard form: <b>9 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. 8 &divide; 2 = 4, 10<super>7</super> &divide; 10<super>2</super> = 10<super>5</super> (1) &nbsp; = 4 &times; 10<super>5</super> (1) &nbsp; already in standard form: <b>4 &times; 10<super>5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s.append(Paragraph('E1. <b>64</b> (1)', styles['ans']))
    s.append(Paragraph('E2. 9<super>2</super>=81, 10<super>2</super>=100 &nbsp; = between <b>9 and 10</b> (1)', styles['ans']))

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('F1. <b>p<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('F2. <b>q<super>7</super></b> (1)', styles['ans']))
    s.append(Paragraph('F3. <b>r<super>10</super></b> (1)', styles['ans']))
    s.append(Paragraph('F4. 4 &times; 3 = 12 (1) &nbsp; s<super>3+4</super> = s<super>7</super> (1) &nbsp; = <b>12s<super>7</super></b>', styles['ans']))
    s.append(Paragraph('F5. 2<super>4</super> = 16 (1) &nbsp; t<super>3&times;4</super> = t<super>12</super> (1) &nbsp; = <b>16t<super>12</super></b>', styles['ans']))

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s.append(Paragraph('G1. &radic;36 = <b>6</b> (1)', styles['ans']))
    s.append(Paragraph('G2. cube root of 8 = <b>2</b> (1)', styles['ans']))
    s.append(Paragraph('G3. 4th root of 81 = 3 (1) &nbsp; 3<super>3</super> = <b>27</b> (1)', styles['ans']))
    s.append(Paragraph('G4. &radic;16 = 4 (1) &nbsp; 1 &divide; 4 = <b>1/4</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS 3

def build_answers3():
    doc = SimpleDocTemplate('standard_form_indices_test3_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 3 &middot; Answer sheet &middot; 41 marks total')

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s.append(Paragraph('A1. <b>2<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>6<super>3</super></b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>4<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('A4. 5<super>1</super> &times; 5<super>2</super> = 5<super>3</super> (1) &nbsp; = <b>125</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s.append(Paragraph('B1. <b>1</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 1 &divide; 3<super>2</super> = 1 &divide; 9 (1) &nbsp; = <b>1/9</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1 &divide; 10<super>5</super> = 1 &divide; 100000 (1) &nbsp; = <b>0.00001</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s.append(Paragraph('C1. 8.3 (1) &nbsp; = <b>8.3 &times; 10<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('C2. 9.1 (1) &nbsp; = <b>9.1 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('C3. 2.5 (1) &nbsp; = <b>2.5 &times; 10<super>&minus;3</super></b> (1)', styles['ans']))
    s.append(Paragraph('C4. 6 (1) &nbsp; = <b>6 &times; 10<super>&minus;5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s.append(Paragraph('D1. <b>5,100</b> (1)', styles['ans']))
    s.append(Paragraph('D2. <b>0.0006</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 2 &times; 4 = 8, 10<super>3</super> &times; 10<super>4</super> = 10<super>7</super> (1) &nbsp; = 8 &times; 10<super>7</super> (1) &nbsp; already in standard form: <b>8 &times; 10<super>7</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. 6 &divide; 3 = 2, 10<super>6</super> &divide; 10<super>2</super> = 10<super>4</super> (1) &nbsp; = 2 &times; 10<super>4</super> (1) &nbsp; already in standard form: <b>2 &times; 10<super>4</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s.append(Paragraph('E1. <b>128</b> (1)', styles['ans']))
    s.append(Paragraph('E2. 10<super>2</super>=100, 11<super>2</super>=121 &nbsp; = between <b>10 and 11</b> (1)', styles['ans']))

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('F1. <b>m<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('F2. <b>n<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('F3. <b>k<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('F4. 3 &times; 5 = 15 (1) &nbsp; x<super>2+4</super> = x<super>6</super> (1) &nbsp; = <b>15x<super>6</super></b>', styles['ans']))
    s.append(Paragraph('F5. 2<super>3</super> = 8 (1) &nbsp; y<super>4&times;3</super> = y<super>12</super> (1) &nbsp; = <b>8y<super>12</super></b>', styles['ans']))

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s.append(Paragraph('G1. &radic;25 = <b>5</b> (1)', styles['ans']))
    s.append(Paragraph('G2. cube root of 64 = <b>4</b> (1)', styles['ans']))
    s.append(Paragraph('G3. 5th root of 32 = 2 (1) &nbsp; 2<super>2</super> = <b>4</b> (1)', styles['ans']))
    s.append(Paragraph('G4. &radic;4 = 2 (1) &nbsp; 2<super>3</super> = 8, 1 &divide; 8 = <b>1/8</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- TEST 4

def build_test4():
    doc = SimpleDocTemplate('standard_form_indices_test4.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 4 &middot; 41 marks total &middot; Sections F &amp; G include Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 41'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s += q('A1', 'Write 5<super>6</super> &times; 5<super>3</super> as a single power of 5.', 1)
    s += q('A2', 'Write 9<super>10</super> &divide; 9<super>4</super> as a single power of 9.', 1)
    s += q('A3', 'Write (7<super>2</super>)<super>4</super> as a single power of 7.', 1)
    s += q('A4', 'Work out the value of 4<super>2</super> &times; 4<super>1</super>.', 2)

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s += q('B1', 'Work out the value of 15<super>0</super>.', 1)
    s += q('B2', 'Work out the value of 2<super>&minus;3</super>. Give your answer as a fraction.', 2)
    s += q('B3', 'Work out the value of 10<super>&minus;6</super>. Give your answer as a decimal.', 2)

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s += q('C1', 'Write 91,000 in standard form.', 2)
    s += q('C2', 'Write 5,600,000 in standard form.', 2)
    s += q('C3', 'Write 0.0039 in standard form.', 2)
    s += q('C4', 'Write 0.00008 in standard form.', 2)

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s += q('D1', 'Write 3.4 &times; 10<super>4</super> as an ordinary number.', 1)
    s += q('D2', 'Write 9 &times; 10<super>&minus;5</super> as an ordinary number.', 1)
    s += q('D3', 'Work out (6 &times; 10<super>3</super>) &times; (5 &times; 10<super>4</super>). Give your answer in standard form.', 3)
    s += q('D4', 'Work out (8 &times; 10<super>9</super>) &divide; (4 &times; 10<super>4</super>). Give your answer in standard form.', 3)

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s += q('E1', 'Write down the value of 5<super>3</super>.', 1)
    s += q('E2', '&radic;130 lies between which two consecutive whole numbers?', 1)

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s += q('F1', 'Simplify u<super>8</super> &times; u<super>5</super>.', 1)
    s += q('F2', 'Simplify v<super>12</super> &divide; v<super>6</super>.', 1)
    s += q('F3', 'Simplify (w<super>5</super>)<super>2</super>.', 1)
    s += q('F4', 'Simplify 6f<super>3</super> &times; 2f<super>5</super>.', 2)
    s += q('F5', 'Simplify (3g<super>2</super>)<super>3</super>.', 2)

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s += q('G1', 'Work out the value of 64<super>1/2</super>.', 1)
    s += q('G2', 'Work out the value of 125<super>1/3</super>.', 1)
    s += q('G3', 'Work out the value of 27<super>2/3</super>.', 2)
    s += q('G4', 'Work out the value of 25<super>&minus;1/2</super>.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS 4

def build_answers4():
    doc = SimpleDocTemplate('standard_form_indices_test4_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 4 &middot; Answer sheet &middot; 41 marks total')

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s.append(Paragraph('A1. <b>5<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>9<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>7<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('A4. 4<super>2</super> &times; 4<super>1</super> = 4<super>3</super> (1) &nbsp; = <b>64</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s.append(Paragraph('B1. <b>1</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 1 &divide; 2<super>3</super> = 1 &divide; 8 (1) &nbsp; = <b>1/8</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1 &divide; 10<super>6</super> = 1 &divide; 1000000 (1) &nbsp; = <b>0.000001</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s.append(Paragraph('C1. 9.1 (1) &nbsp; = <b>9.1 &times; 10<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('C2. 5.6 (1) &nbsp; = <b>5.6 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('C3. 3.9 (1) &nbsp; = <b>3.9 &times; 10<super>&minus;3</super></b> (1)', styles['ans']))
    s.append(Paragraph('C4. 8 (1) &nbsp; = <b>8 &times; 10<super>&minus;5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s.append(Paragraph('D1. <b>34,000</b> (1)', styles['ans']))
    s.append(Paragraph('D2. <b>0.00009</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 6 &times; 5 = 30, 10<super>3</super> &times; 10<super>4</super> = 10<super>7</super> (1) &nbsp; = 30 &times; 10<super>7</super> (1) &nbsp; adjust to standard form: <b>3 &times; 10<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. 8 &divide; 4 = 2, 10<super>9</super> &divide; 10<super>4</super> = 10<super>5</super> (1) &nbsp; = 2 &times; 10<super>5</super> (1) &nbsp; already in standard form: <b>2 &times; 10<super>5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s.append(Paragraph('E1. <b>125</b> (1)', styles['ans']))
    s.append(Paragraph('E2. 11<super>2</super>=121, 12<super>2</super>=144 &nbsp; = between <b>11 and 12</b> (1)', styles['ans']))

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('F1. <b>u<super>13</super></b> (1)', styles['ans']))
    s.append(Paragraph('F2. <b>v<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('F3. <b>w<super>10</super></b> (1)', styles['ans']))
    s.append(Paragraph('F4. 6 &times; 2 = 12 (1) &nbsp; f<super>3+5</super> = f<super>8</super> (1) &nbsp; = <b>12f<super>8</super></b>', styles['ans']))
    s.append(Paragraph('F5. 3<super>3</super> = 27 (1) &nbsp; g<super>2&times;3</super> = g<super>6</super> (1) &nbsp; = <b>27g<super>6</super></b>', styles['ans']))

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s.append(Paragraph('G1. &radic;64 = <b>8</b> (1)', styles['ans']))
    s.append(Paragraph('G2. cube root of 125 = <b>5</b> (1)', styles['ans']))
    s.append(Paragraph('G3. cube root of 27 = 3 (1) &nbsp; 3<super>2</super> = <b>9</b> (1)', styles['ans']))
    s.append(Paragraph('G4. &radic;25 = 5 (1) &nbsp; 1 &divide; 5 = <b>1/5</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- TEST 5

def build_test5():
    doc = SimpleDocTemplate('standard_form_indices_test5.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 5 &middot; 41 marks total &middot; Sections F &amp; G include Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 41'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s += q('A1', 'Write 3<super>7</super> &times; 3<super>2</super> as a single power of 3.', 1)
    s += q('A2', 'Write 8<super>11</super> &divide; 8<super>3</super> as a single power of 8.', 1)
    s += q('A3', 'Write (6<super>3</super>)<super>3</super> as a single power of 6.', 1)
    s += q('A4', 'Work out the value of 3<super>2</super> &times; 3<super>2</super>.', 2)

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s += q('B1', 'Work out the value of 23<super>0</super>.', 1)
    s += q('B2', 'Work out the value of 6<super>&minus;2</super>. Give your answer as a fraction.', 2)
    s += q('B3', 'Work out the value of 10<super>&minus;2</super>. Give your answer as a decimal.', 2)

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s += q('C1', 'Write 47,000 in standard form.', 2)
    s += q('C2', 'Write 2,800,000 in standard form.', 2)
    s += q('C3', 'Write 0.0074 in standard form.', 2)
    s += q('C4', 'Write 0.0003 in standard form.', 2)

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s += q('D1', 'Write 7.2 &times; 10<super>5</super> as an ordinary number.', 1)
    s += q('D2', 'Write 4 &times; 10<super>&minus;3</super> as an ordinary number.', 1)
    s += q('D3', 'Work out (5 &times; 10<super>4</super>) &times; (8 &times; 10<super>2</super>). Give your answer in standard form.', 3)
    s += q('D4', 'Work out (2 &times; 10<super>7</super>) &divide; (5 &times; 10<super>3</super>). Give your answer in standard form.', 3)

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s += q('E1', 'Write down the value of 3<super>5</super>.', 1)
    s += q('E2', '&radic;75 lies between which two consecutive whole numbers?', 1)

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s += q('F1', 'Simplify p<super>6</super> &times; p<super>4</super>.', 1)
    s += q('F2', 'Simplify q<super>15</super> &divide; q<super>7</super>.', 1)
    s += q('F3', 'Simplify (r<super>3</super>)<super>5</super>.', 1)
    s += q('F4', 'Simplify 4h<super>2</super> &times; 7h<super>6</super>.', 2)
    s += q('F5', 'Simplify (5j<super>3</super>)<super>2</super>.', 2)

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s += q('G1', 'Work out the value of 81<super>1/2</super>.', 1)
    s += q('G2', 'Work out the value of 1000<super>1/3</super>.', 1)
    s += q('G3', 'Work out the value of 125<super>2/3</super>.', 2)
    s += q('G4', 'Work out the value of 8<super>&minus;2/3</super>.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS 5

def build_answers5():
    doc = SimpleDocTemplate('standard_form_indices_test5_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 5 &middot; Answer sheet &middot; 41 marks total')

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s.append(Paragraph('A1. <b>3<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>8<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>6<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('A4. 3<super>2</super> &times; 3<super>2</super> = 3<super>4</super> (1) &nbsp; = <b>81</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s.append(Paragraph('B1. <b>1</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 1 &divide; 6<super>2</super> = 1 &divide; 36 (1) &nbsp; = <b>1/36</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1 &divide; 10<super>2</super> = 1 &divide; 100 (1) &nbsp; = <b>0.01</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s.append(Paragraph('C1. 4.7 (1) &nbsp; = <b>4.7 &times; 10<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('C2. 2.8 (1) &nbsp; = <b>2.8 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('C3. 7.4 (1) &nbsp; = <b>7.4 &times; 10<super>&minus;3</super></b> (1)', styles['ans']))
    s.append(Paragraph('C4. 3 (1) &nbsp; = <b>3 &times; 10<super>&minus;4</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s.append(Paragraph('D1. <b>720,000</b> (1)', styles['ans']))
    s.append(Paragraph('D2. <b>0.004</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 5 &times; 8 = 40, 10<super>4</super> &times; 10<super>2</super> = 10<super>6</super> (1) &nbsp; = 40 &times; 10<super>6</super> (1) &nbsp; adjust to standard form: <b>4 &times; 10<super>7</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. 2 &divide; 5 = 0.4, 10<super>7</super> &divide; 10<super>3</super> = 10<super>4</super> (1) &nbsp; = 0.4 &times; 10<super>4</super> (1) &nbsp; adjust to standard form: <b>4 &times; 10<super>3</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s.append(Paragraph('E1. <b>243</b> (1)', styles['ans']))
    s.append(Paragraph('E2. 8<super>2</super>=64, 9<super>2</super>=81 &nbsp; = between <b>8 and 9</b> (1)', styles['ans']))

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('F1. <b>p<super>10</super></b> (1)', styles['ans']))
    s.append(Paragraph('F2. <b>q<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('F3. <b>r<super>15</super></b> (1)', styles['ans']))
    s.append(Paragraph('F4. 4 &times; 7 = 28 (1) &nbsp; h<super>2+6</super> = h<super>8</super> (1) &nbsp; = <b>28h<super>8</super></b>', styles['ans']))
    s.append(Paragraph('F5. 5<super>2</super> = 25 (1) &nbsp; j<super>3&times;2</super> = j<super>6</super> (1) &nbsp; = <b>25j<super>6</super></b>', styles['ans']))

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s.append(Paragraph('G1. &radic;81 = <b>9</b> (1)', styles['ans']))
    s.append(Paragraph('G2. cube root of 1000 = <b>10</b> (1)', styles['ans']))
    s.append(Paragraph('G3. cube root of 125 = 5 (1) &nbsp; 5<super>2</super> = <b>25</b> (1)', styles['ans']))
    s.append(Paragraph('G4. cube root of 8 = 2, 2<super>2</super> = 4 (1) &nbsp; 1 &divide; 4 = <b>1/4</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- TEST 6

def build_test6():
    doc = SimpleDocTemplate('standard_form_indices_test6.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 6 &middot; 41 marks total &middot; Sections F &amp; G include Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 41'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s += q('A1', 'Write 7<super>4</super> &times; 7<super>5</super> as a single power of 7.', 1)
    s += q('A2', 'Write 5<super>12</super> &divide; 5<super>7</super> as a single power of 5.', 1)
    s += q('A3', 'Write (3<super>4</super>)<super>2</super> as a single power of 3.', 1)
    s += q('A4', 'Work out the value of 2<super>4</super> &times; 2<super>2</super>.', 2)

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s += q('B1', 'Work out the value of 100<super>0</super>.', 1)
    s += q('B2', 'Work out the value of 7<super>&minus;2</super>. Give your answer as a fraction.', 2)
    s += q('B3', 'Work out the value of 10<super>&minus;7</super>. Give your answer as a decimal.', 2)

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s += q('C1', 'Write 36,000 in standard form.', 2)
    s += q('C2', 'Write 7,400,000 in standard form.', 2)
    s += q('C3', 'Write 0.0052 in standard form.', 2)
    s += q('C4', 'Write 0.0007 in standard form.', 2)

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s += q('D1', 'Write 8.3 &times; 10<super>3</super> as an ordinary number.', 1)
    s += q('D2', 'Write 2 &times; 10<super>&minus;6</super> as an ordinary number.', 1)
    s += q('D3', 'Work out (7 &times; 10<super>3</super>) &times; (3 &times; 10<super>5</super>). Give your answer in standard form.', 3)
    s += q('D4', 'Work out (3 &times; 10<super>9</super>) &divide; (6 &times; 10<super>4</super>). Give your answer in standard form.', 3)

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s += q('E1', 'Write down the value of 2<super>8</super>.', 1)
    s += q('E2', '&radic;50 lies between which two consecutive whole numbers?', 1)

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s += q('F1', 'Simplify x<super>9</super> &times; x<super>3</super>.', 1)
    s += q('F2', 'Simplify y<super>14</super> &divide; y<super>9</super>.', 1)
    s += q('F3', 'Simplify (z<super>6</super>)<super>2</super>.', 1)
    s += q('F4', 'Simplify 3m<super>5</super> &times; 8m<super>2</super>.', 2)
    s += q('F5', 'Simplify (4n<super>2</super>)<super>3</super>.', 2)

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s += q('G1', 'Work out the value of 100<super>1/2</super>.', 1)
    s += q('G2', 'Work out the value of 216<super>1/3</super>.', 1)
    s += q('G3', 'Work out the value of 32<super>3/5</super>.', 2)
    s += q('G4', 'Work out the value of 36<super>&minus;1/2</super>.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS 6

def build_answers6():
    doc = SimpleDocTemplate('standard_form_indices_test6_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 6 &middot; Answer sheet &middot; 41 marks total')

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s.append(Paragraph('A1. <b>7<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>5<super>5</super></b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>3<super>8</super></b> (1)', styles['ans']))
    s.append(Paragraph('A4. 2<super>4</super> &times; 2<super>2</super> = 2<super>6</super> (1) &nbsp; = <b>64</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s.append(Paragraph('B1. <b>1</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 1 &divide; 7<super>2</super> = 1 &divide; 49 (1) &nbsp; = <b>1/49</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1 &divide; 10<super>7</super> = 1 &divide; 10000000 (1) &nbsp; = <b>0.0000001</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s.append(Paragraph('C1. 3.6 (1) &nbsp; = <b>3.6 &times; 10<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('C2. 7.4 (1) &nbsp; = <b>7.4 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('C3. 5.2 (1) &nbsp; = <b>5.2 &times; 10<super>&minus;3</super></b> (1)', styles['ans']))
    s.append(Paragraph('C4. 7 (1) &nbsp; = <b>7 &times; 10<super>&minus;4</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s.append(Paragraph('D1. <b>8,300</b> (1)', styles['ans']))
    s.append(Paragraph('D2. <b>0.000002</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 7 &times; 3 = 21, 10<super>3</super> &times; 10<super>5</super> = 10<super>8</super> (1) &nbsp; = 21 &times; 10<super>8</super> (1) &nbsp; adjust to standard form: <b>2.1 &times; 10<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. 3 &divide; 6 = 0.5, 10<super>9</super> &divide; 10<super>4</super> = 10<super>5</super> (1) &nbsp; = 0.5 &times; 10<super>5</super> (1) &nbsp; adjust to standard form: <b>5 &times; 10<super>4</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s.append(Paragraph('E1. <b>256</b> (1)', styles['ans']))
    s.append(Paragraph('E2. 7<super>2</super>=49, 8<super>2</super>=64 &nbsp; = between <b>7 and 8</b> (1)', styles['ans']))

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('F1. <b>x<super>12</super></b> (1)', styles['ans']))
    s.append(Paragraph('F2. <b>y<super>5</super></b> (1)', styles['ans']))
    s.append(Paragraph('F3. <b>z<super>12</super></b> (1)', styles['ans']))
    s.append(Paragraph('F4. 3 &times; 8 = 24 (1) &nbsp; m<super>5+2</super> = m<super>7</super> (1) &nbsp; = <b>24m<super>7</super></b>', styles['ans']))
    s.append(Paragraph('F5. 4<super>3</super> = 64 (1) &nbsp; n<super>2&times;3</super> = n<super>6</super> (1) &nbsp; = <b>64n<super>6</super></b>', styles['ans']))

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s.append(Paragraph('G1. &radic;100 = <b>10</b> (1)', styles['ans']))
    s.append(Paragraph('G2. cube root of 216 = <b>6</b> (1)', styles['ans']))
    s.append(Paragraph('G3. fifth root of 32 = 2 (1) &nbsp; 2<super>3</super> = <b>8</b> (1)', styles['ans']))
    s.append(Paragraph('G4. &radic;36 = 6 (1) &nbsp; 1 &divide; 6 = <b>1/6</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- TEST 7

def build_test7():
    doc = SimpleDocTemplate('standard_form_indices_test7.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 7 &middot; 41 marks total &middot; Sections F &amp; G include Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 41'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s += q('A1', 'Write 9<super>3</super> &times; 9<super>6</super> as a single power of 9.', 1)
    s += q('A2', 'Write 4<super>13</super> &divide; 4<super>8</super> as a single power of 4.', 1)
    s += q('A3', 'Write (8<super>2</super>)<super>5</super> as a single power of 8.', 1)
    s += q('A4', 'Work out the value of 10<super>2</super> &times; 10<super>1</super>.', 2)

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s += q('B1', 'Work out the value of 58<super>0</super>.', 1)
    s += q('B2', 'Work out the value of 9<super>&minus;2</super>. Give your answer as a fraction.', 2)
    s += q('B3', 'Work out the value of 2<super>&minus;2</super>. Give your answer as a decimal.', 2)

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s += q('C1', 'Write 29,000 in standard form.', 2)
    s += q('C2', 'Write 4,500,000 in standard form.', 2)
    s += q('C3', 'Write 0.0081 in standard form.', 2)
    s += q('C4', 'Write 0.0000006 in standard form.', 2)

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s += q('D1', 'Write 1.8 &times; 10<super>6</super> as an ordinary number.', 1)
    s += q('D2', 'Write 5 &times; 10<super>&minus;3</super> as an ordinary number.', 1)
    s += q('D3', 'Work out (9 &times; 10<super>2</super>) &times; (4 &times; 10<super>6</super>). Give your answer in standard form.', 3)
    s += q('D4', 'Work out (4 &times; 10<super>8</super>) &divide; (8 &times; 10<super>2</super>). Give your answer in standard form.', 3)

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s += q('E1', 'Write down the value of 5<super>4</super>.', 1)
    s += q('E2', '&radic;40 lies between which two consecutive whole numbers?', 1)

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s += q('F1', 'Simplify d<super>7</super> &times; d<super>8</super>.', 1)
    s += q('F2', 'Simplify e<super>16</super> &divide; e<super>10</super>.', 1)
    s += q('F3', 'Simplify (t<super>4</super>)<super>4</super>.', 1)
    s += q('F4', 'Simplify 9k<super>4</super> &times; 2k<super>3</super>.', 2)
    s += q('F5', 'Simplify (2w<super>5</super>)<super>4</super>.', 2)

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s += q('G1', 'Work out the value of 144<super>1/2</super>.', 1)
    s += q('G2', 'Work out the value of 343<super>1/3</super>.', 1)
    s += q('G3', 'Work out the value of 9<super>3/2</super>.', 2)
    s += q('G4', 'Work out the value of 1000<super>&minus;2/3</super>.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS 7

def build_answers7():
    doc = SimpleDocTemplate('standard_form_indices_test7_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Test 7 &middot; Answer sheet &middot; 41 marks total')

    s.append(Paragraph('Section A &mdash; Laws of indices', styles['h2']))
    s.append(Paragraph('A1. <b>9<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>4<super>5</super></b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>8<super>10</super></b> (1)', styles['ans']))
    s.append(Paragraph('A4. 10<super>2</super> &times; 10<super>1</super> = 10<super>3</super> (1) &nbsp; = <b>1000</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Zero and negative indices', styles['h2']))
    s.append(Paragraph('B1. <b>1</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 1 &divide; 9<super>2</super> = 1 &divide; 81 (1) &nbsp; = <b>1/81</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 1 &divide; 2<super>2</super> = 1 &divide; 4 (1) &nbsp; = <b>0.25</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Writing standard form', styles['h2']))
    s.append(Paragraph('C1. 2.9 (1) &nbsp; = <b>2.9 &times; 10<super>4</super></b> (1)', styles['ans']))
    s.append(Paragraph('C2. 4.5 (1) &nbsp; = <b>4.5 &times; 10<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('C3. 8.1 (1) &nbsp; = <b>8.1 &times; 10<super>&minus;3</super></b> (1)', styles['ans']))
    s.append(Paragraph('C4. 6 (1) &nbsp; = <b>6 &times; 10<super>&minus;7</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Converting back, and calculating', styles['h2']))
    s.append(Paragraph('D1. <b>1,800,000</b> (1)', styles['ans']))
    s.append(Paragraph('D2. <b>0.005</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 9 &times; 4 = 36, 10<super>2</super> &times; 10<super>6</super> = 10<super>8</super> (1) &nbsp; = 36 &times; 10<super>8</super> (1) &nbsp; adjust to standard form: <b>3.6 &times; 10<super>9</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. 4 &divide; 8 = 0.5, 10<super>8</super> &divide; 10<super>2</super> = 10<super>6</super> (1) &nbsp; = 0.5 &times; 10<super>6</super> (1) &nbsp; adjust to standard form: <b>5 &times; 10<super>5</super></b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Powers to know, and estimating roots', styles['h2']))
    s.append(Paragraph('E1. <b>625</b> (1)', styles['ans']))
    s.append(Paragraph('E2. 6<super>2</super>=36, 7<super>2</super>=49 &nbsp; = between <b>6 and 7</b> (1)', styles['ans']))

    s.append(Paragraph('Section F &mdash; Laws of indices with algebra', styles['h2']))
    s.append(Paragraph('F1. <b>d<super>15</super></b> (1)', styles['ans']))
    s.append(Paragraph('F2. <b>e<super>6</super></b> (1)', styles['ans']))
    s.append(Paragraph('F3. <b>t<super>16</super></b> (1)', styles['ans']))
    s.append(Paragraph('F4. 9 &times; 2 = 18 (1) &nbsp; k<super>4+3</super> = k<super>7</super> (1) &nbsp; = <b>18k<super>7</super></b>', styles['ans']))
    s.append(Paragraph('F5. 2<super>4</super> = 16 (1) &nbsp; w<super>5&times;4</super> = w<super>20</super> (1) &nbsp; = <b>16w<super>20</super></b>', styles['ans']))

    s.append(Paragraph('Section G &mdash; Fractional indices (Higher)', styles['h2']))
    s.append(Paragraph('G1. &radic;144 = <b>12</b> (1)', styles['ans']))
    s.append(Paragraph('G2. cube root of 343 = <b>7</b> (1)', styles['ans']))
    s.append(Paragraph('G3. &radic;9 = 3 (1) &nbsp; 3<super>3</super> = <b>27</b> (1)', styles['ans']))
    s.append(Paragraph('G4. cube root of 1000 = 10, 10<super>2</super> = 100 (1) &nbsp; 1 &divide; 100 = <b>1/100</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    build_test2()
    build_answers2()
    build_test3()
    build_answers3()
    build_test4()
    build_answers4()
    build_test5()
    build_answers5()
    build_test6()
    build_answers6()
    build_test7()
    build_answers7()
    print('done')
