# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Fractions, Decimals & Percentages (GCSE Maths, Number)."""

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
    doc = SimpleDocTemplate('fdp_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Fractions, Decimals &amp; Percentages',
                 'Quick reference sheet &middot; GCSE Maths, Number &middot; keep handy for revision')

    s.append(Paragraph('1. Equivalences worth memorising', styles['h2']))
    s.append(table([
        [headcell('Fraction'), headcell('Decimal'), headcell('Percentage')],
        [cell('1/2'), cell('0.5'), cell('50%')],
        [cell('1/4'), cell('0.25'), cell('25%')],
        [cell('1/5'), cell('0.2'), cell('20%')],
        [cell('1/10'), cell('0.1'), cell('10%')],
        [cell('1/8'), cell('0.125'), cell('12.5%')],
        [cell('1/3'), cell('0.333&hellip;'), cell('33.3%')],
    ], col_widths=[45 * mm, 45 * mm, 45 * mm]))

    s.append(Paragraph('2. Converting between the three', styles['h2']))
    s.append(Paragraph('<b>Fraction &rarr; Decimal:</b> divide top by bottom. e.g. 3/4 = 3 &divide; 4 = 0.75', styles['bullet']))
    s.append(Paragraph('<b>Decimal &rarr; Percentage:</b> &times;100 (move the point two places right). e.g. 0.75 &rarr; 75%', styles['bullet']))
    s.append(Paragraph('<b>Percentage &rarr; Decimal:</b> &divide;100 (move the point two places left). e.g. 45% &rarr; 0.45', styles['bullet']))
    s.append(Paragraph('<b>Decimal &rarr; Fraction:</b> use place value, then simplify. e.g. 0.6 = 6/10 = 3/5', styles['bullet']))
    s.append(Paragraph('<b>Fraction &rarr; Percentage:</b> convert to a decimal first, then &times;100. e.g. 9/20 = 0.45 = 45%', styles['bullet']))

    s.append(Paragraph('3. Ordering mixed values', styles['h2']))
    s.append(Paragraph('Convert everything into the <b>same form</b> &mdash; decimals are usually quickest &mdash; then compare.', styles['body']))
    s.append(Paragraph('Example: order 7/20, 30%, 0.28, 1/3 &nbsp;&rarr;&nbsp; 0.35, 0.30, 0.28, 0.333&hellip; &nbsp;&rarr;&nbsp; <b>0.28, 30%, 1/3, 7/20</b>', styles['body']))

    s.append(Paragraph('4. Fraction / percentage of an amount', styles['h2']))
    s.append(Paragraph('<b>Fraction of an amount:</b> &divide; by the denominator, &times; by the numerator.', styles['body']))
    s.append(Paragraph('3/5 of 40 &nbsp;&rarr;&nbsp; 40 &divide; 5 = 8, &nbsp; 8 &times; 3 = <b>24</b>', styles['body']))
    s.append(Paragraph('<b>Percentage of an amount (no calculator):</b> find 10% (&divide;10), then 1% (&divide;10 again), and combine.', styles['body']))
    s.append(Paragraph('35% of &pound;60 &nbsp;&rarr;&nbsp; 10% = &pound;6, so 30% = &pound;18, 5% = &pound;3 &nbsp;&rarr;&nbsp; 30% + 5% = <b>&pound;21</b>', styles['body']))

    s.append(Paragraph('5. Worked examples', styles['h2']))
    s.append(table([
        [headcell('Start'), headcell('Working'), headcell('Result')],
        [cell('3/4'), cell('3 &divide; 4 = 0.75, &times;100'), cell('0.75 &middot; 75%')],
        [cell('0.6'), cell('6/10, simplify &divide;2'), cell('3/5 &middot; 60%')],
        [cell('45%'), cell('&divide;100, place value'), cell('0.45 &middot; 9/20')],
    ], col_widths=[35 * mm, 65 * mm, 35 * mm]))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('fdp_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Fractions, Decimals &amp; Percentages', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Quick conversions', styles['h2']))
    s += q('A1', 'Convert 3/8 to a decimal.', 1)
    s += q('A2', 'Convert 0.45 to a percentage.', 1)
    s += q('A3', 'Convert 70% to a decimal.', 1)
    s += q('A4', 'Convert 0.12 to a fraction in its simplest form.', 1)
    s += q('A5', 'Convert 5/8 to a percentage.', 1)
    s += q('A6', 'Convert 0.9 to a fraction in its simplest form.', 1)
    s += q('A7', 'Convert 24% to a fraction in its simplest form.', 1)
    s += q('A8', 'Convert 11/20 to a decimal.', 1)

    s.append(Paragraph('Section B &mdash; Ordering', styles['h2']))
    s += q('B1', 'Write these in order, smallest to largest: 0.4, 35%, 3/8, 0.42', 3)

    s.append(Paragraph('Section C &mdash; Fraction / percentage of an amount', styles['h2']))
    s += q('C1', 'Calculate 2/3 of 60.', 2)
    s += q('C2', 'Calculate 5/6 of 144.', 2)
    s += q('C3', 'Calculate 40% of &pound;85 without a calculator. Show your method.', 2)
    s += q('C4', 'Calculate 65% of 300.', 2)

    s.append(Paragraph('Section D &mdash; Problem solving', styles['h2']))
    s += q('D1', 'Ben scored 42 out of 60 on a test. Write his score as a percentage.', 2)
    s += q('D2', 'A recipe uses 3/4 of a 500 g bag of flour. How many grams of flour are used?', 2)
    s += q('D3', 'In a class of 32 students, 3/8 walk to school. How many students walk to school?', 2)
    s += q('D4', 'Which is bigger: 7/10 or 68%? Show your working.', 1)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('fdp_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Fractions, Decimals &amp; Percentages', 'Answer sheet &middot; 26 marks total')

    s.append(Paragraph('Section A &mdash; Quick conversions', styles['h2']))
    s.append(Paragraph('A1. <b>0.375</b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>45%</b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>0.7</b> (1)', styles['ans']))
    s.append(Paragraph('A4. 12/100 = <b>3/25</b> (1)', styles['ans']))
    s.append(Paragraph('A5. <b>62.5%</b> (1)', styles['ans']))
    s.append(Paragraph('A6. 9/10 &mdash; already simplest form &mdash; <b>9/10</b> (1)', styles['ans']))
    s.append(Paragraph('A7. 24/100 = <b>6/25</b> (1)', styles['ans']))
    s.append(Paragraph('A8. <b>0.55</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Ordering', styles['h2']))
    s.append(Paragraph('B1. Convert: 0.4, 0.35, 0.375, 0.42 (1) &nbsp; Order: <b>35%, 3/8, 0.4, 0.42</b> (2)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Fraction / percentage of an amount', styles['h2']))
    s.append(Paragraph('C1. 60 &divide; 3 = 20 (1) &nbsp; 20 &times; 2 = <b>40</b> (1)', styles['ans']))
    s.append(Paragraph('C2. 144 &divide; 6 = 24 (1) &nbsp; 24 &times; 5 = <b>120</b> (1)', styles['ans']))
    s.append(Paragraph('C3. 10% = &pound;8.50 (1) &nbsp; 40% = 8.50 &times; 4 = <b>&pound;34</b> (1)', styles['ans']))
    s.append(Paragraph('C4. 10% = 30 (1) &nbsp; 65% = 30 &times; 6.5 = <b>195</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Problem solving', styles['h2']))
    s.append(Paragraph('D1. 42/60 = 0.7 (1) &nbsp; = <b>70%</b> (1)', styles['ans']))
    s.append(Paragraph('D2. 500 &divide; 4 = 125 (1) &nbsp; 125 &times; 3 = <b>375 g</b> (1)', styles['ans']))
    s.append(Paragraph('D3. 32 &divide; 8 = 4 (1) &nbsp; 4 &times; 3 = <b>12 students</b> (1)', styles['ans']))
    s.append(Paragraph('D4. 7/10 = 70% (1) &nbsp; <b>7/10 is bigger</b> than 68%', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for correct working (e.g. finding 10% first) even if the final '
        'answer contains an arithmetic error. Accept equivalent fractions unless a question asks for simplest form.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
