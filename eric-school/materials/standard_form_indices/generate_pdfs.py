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

    s.append(Paragraph('2. Zero and negative indices', styles['h2']))
    s.append(Paragraph('<b>a<super>0</super> = 1</b> for any non-zero a. &nbsp;e.g. 9<super>0</super> = 1, 100<super>0</super> = 1.', styles['bullet']))
    s.append(Paragraph('<b>a<super>&minus;n</super> = 1 &divide; a<super>n</super></b> &mdash; a negative index flips the number into a fraction, it does not make the answer negative.', styles['bullet']))
    s.append(table([
        [headcell('Expression'), headcell('Value')],
        [cell('7<super>0</super>'), cell('1')],
        [cell('3<super>&minus;1</super>'), cell('1/3')],
        [cell('4<super>&minus;2</super>'), cell('1/16')],
        [cell('10<super>&minus;2</super>'), cell('0.01')],
    ], col_widths=[65 * mm, 65 * mm]))

    s.append(Paragraph('3. Standard form: writing large and small numbers', styles['h2']))
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

    s.append(Paragraph('4. Calculating with standard form', styles['h2']))
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
    s += header('Standard Form &amp; Indices', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
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

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('standard_form_indices_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form &amp; Indices', 'Answer sheet &middot; 26 marks total')

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

    s.append(Paragraph(
        'Marking note: award method marks for a correctly identified front number/power, or correctly applied law '
        'of indices, even if the final answer contains an arithmetic error. Accept equivalent fractions/decimals.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
