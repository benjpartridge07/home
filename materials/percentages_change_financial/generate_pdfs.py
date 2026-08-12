# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Percentages: Change, Interest & Financial Maths (GCSE Maths, Number)."""

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
    doc = SimpleDocTemplate('percentages_change_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Percentages: Change, Interest &amp; Financial Maths',
                 'Quick reference sheet &middot; GCSE Maths, Number &middot; keep handy for revision')

    s.append(Paragraph('1. The multiplier method', styles['h2']))
    s.append(Paragraph('<b>Increase</b> by X% &rarr; multiplier = 1 + (X &divide; 100). e.g. increase by 15% &rarr; <b>1.15</b>', styles['bullet']))
    s.append(Paragraph('<b>Decrease</b> by X% &rarr; multiplier = 1 &minus; (X &divide; 100). e.g. decrease by 20% &rarr; <b>0.80</b>', styles['bullet']))
    s.append(Paragraph('Apply it by multiplying once: new amount = original &times; multiplier.', styles['body']))
    s.append(table([
        [headcell('Change'), headcell('Multiplier')],
        [cell('Increase by 8%'), cell('1.08')],
        [cell('Increase by 50%'), cell('1.50')],
        [cell('Decrease by 12%'), cell('0.88')],
        [cell('Decrease by 35%'), cell('0.65')],
    ], col_widths=[65 * mm, 65 * mm]))

    s.append(Paragraph('2. Reverse percentages', styles['h2']))
    s.append(Paragraph(
        'Given the amount <i>after</i> a change, find the original (100%) amount by <b>dividing by the multiplier</b> '
        '&mdash; do not add or subtract the percentage from the final amount.', styles['body']))
    s.append(Paragraph('&pound;69 after a 15% increase &nbsp;&rarr;&nbsp; 69 &divide; 1.15 = <b>&pound;60</b> (original)', styles['body']))
    s.append(Paragraph('&pound;120 after a 20% decrease &nbsp;&rarr;&nbsp; 120 &divide; 0.8 = <b>&pound;150</b> (original)', styles['body']))

    s.append(Paragraph('3. Simple interest', styles['h2']))
    s.append(Paragraph('<b>I = P &times; R &times; T &divide; 100</b> &mdash; P = principal, R = rate (%), T = time (years). Adds the same amount each year.', styles['bodyb']))
    s.append(Paragraph('&pound;500 at 4% for 3 years &nbsp;&rarr;&nbsp; I = 500 &times; 4 &times; 3 &divide; 100 = <b>&pound;60</b>', styles['body']))

    s.append(Paragraph('4. Compound interest', styles['h2']))
    s.append(Paragraph('<b>Amount = P &times; (multiplier)<super>T</super></b> &mdash; interest is earned on interest, so it grows faster than simple interest.', styles['bodyb']))
    s.append(Paragraph('&pound;500 at 4% for 3 years &nbsp;&rarr;&nbsp; 500 &times; 1.04<super>3</super> = <b>&pound;562.43</b>', styles['body']))
    s.append(table([
        [headcell('Year'), headcell('Simple total (&pound;500 @ 4%)'), headcell('Compound total (&pound;500 @ 4%)')],
        [cell('1'), cell('520.00'), cell('520.00')],
        [cell('2'), cell('540.00'), cell('540.80')],
        [cell('3'), cell('560.00'), cell('562.43')],
    ], col_widths=[25 * mm, 65 * mm, 65 * mm]))

    s.append(Paragraph('5. Before you start: what is 100%?', styles['h2']))
    s.append(Paragraph(
        'For "increase/decrease by X%" questions, 100% is the <b>original</b> amount. For reverse percentage '
        'questions, the amount given is <b>not</b> 100% &mdash; it is the multiplier percentage, so divide by the '
        'multiplier to get back to the original.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('percentages_change_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Percentages: Change, Interest &amp; Financial Maths', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Multipliers', styles['h2']))
    s += q('A1', 'Write the multiplier for a 6% increase.', 1)
    s += q('A2', 'Write the multiplier for a 40% increase.', 1)
    s += q('A3', 'Write the multiplier for an 18% decrease.', 1)
    s += q('A4', 'Write the multiplier for a 5% decrease.', 1)

    s.append(Paragraph('Section B &mdash; Percentage increase / decrease', styles['h2']))
    s += q('B1', 'Increase &pound;150 by 8%.', 2)
    s += q('B2', 'Decrease &pound;64 by 15%.', 2)
    s += q('B3', 'A salary of &pound;24,000 increases by 3%. Find the new salary.', 2)
    s += q('B4', 'A car worth &pound;12,000 depreciates by 25%. Find its new value.', 2)

    s.append(Paragraph('Section C &mdash; Reverse percentages', styles['h2']))
    s += q('C1', 'After a 20% increase, a price is &pound;96. Find the original price.', 2)
    s += q('C2', 'After a 15% decrease, a price is &pound;127.50. Find the original price.', 2)
    s += q('C3', "A shop's sale reduces prices by 30%. A jacket now costs &pound;42. What was its original price?", 2)

    s.append(Paragraph('Section D &mdash; Simple &amp; compound interest', styles['h2']))
    s += q('D1', 'Calculate the simple interest on &pound;800 at 5% per year for 3 years.', 3)
    s += q('D2', 'Calculate the total amount (principal + interest) if &pound;1200 earns simple interest at 2.5% per year for 4 years.', 2)
    s += q('D3', '&pound;600 is invested at 3% compound interest for 2 years. Calculate the total amount, to the nearest penny.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('percentages_change_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Percentages: Change, Interest &amp; Financial Maths', 'Answer sheet &middot; 26 marks total')

    s.append(Paragraph('Section A &mdash; Multipliers', styles['h2']))
    s.append(Paragraph('A1. <b>1.06</b> (1) &nbsp; A2. <b>1.40</b> (1) &nbsp; A3. <b>0.82</b> (1) &nbsp; A4. <b>0.95</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Percentage increase / decrease', styles['h2']))
    s.append(Paragraph('B1. 150 &times; 1.08 (1) &nbsp; = <b>&pound;162</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 64 &times; 0.85 (1) &nbsp; = <b>&pound;54.40</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 24000 &times; 1.03 (1) &nbsp; = <b>&pound;24,720</b> (1)', styles['ans']))
    s.append(Paragraph('B4. 12000 &times; 0.75 (1) &nbsp; = <b>&pound;9,000</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Reverse percentages', styles['h2']))
    s.append(Paragraph('C1. 96 &divide; 1.2 (1) &nbsp; = <b>&pound;80</b> (1)', styles['ans']))
    s.append(Paragraph('C2. 127.50 &divide; 0.85 (1) &nbsp; = <b>&pound;150</b> (1)', styles['ans']))
    s.append(Paragraph('C3. 42 &divide; 0.7 (1) &nbsp; = <b>&pound;60</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Simple &amp; compound interest', styles['h2']))
    s.append(Paragraph('D1. I = 800 &times; 5 &times; 3 &divide; 100 (1) &nbsp; = 12000 &divide; 100 (1) &nbsp; = <b>&pound;120</b> (1)', styles['ans']))
    s.append(Paragraph('D2. I = 1200 &times; 2.5 &times; 4 &divide; 100 = &pound;120 (1) &nbsp; total = 1200 + 120 = <b>&pound;1,320</b> (1)', styles['ans']))
    s.append(Paragraph('D3. Amount = 600 &times; 1.03<super>2</super> (1) &nbsp; = 600 &times; 1.0609 (1) &nbsp; = <b>&pound;636.54</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correct multiplier or correctly substituted formula even if the '
        'final answer contains an arithmetic error. Accept working shown in any equivalent correct order.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
