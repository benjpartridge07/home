# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Ratio & Proportion (GCSE Maths, Ratio, Proportion & Rates of Change)."""

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
    'h3': ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=11.5,
                          textColor=INK, spaceBefore=8, spaceAfter=6),
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
    doc = SimpleDocTemplate('ratio_proportion_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Ratio &amp; Proportion',
                 'Quick reference sheet &middot; GCSE Maths, Ratio, Proportion &amp; Rates of Change &middot; keep handy for revision')

    s.append(Paragraph('1. Simplifying ratios', styles['h2']))
    s.append(Paragraph(
        'A ratio compares two or more quantities, written with a colon (e.g. 3:5). Simplify by dividing every '
        'part by their highest common factor &mdash; just like simplifying a fraction.', styles['body']))
    s.append(Paragraph('15:20 &rarr; divide both by 5 &rarr; <b>3:4</b>', styles['bullet']))
    s.append(Paragraph('If the quantities have different units, convert to the same unit first: 2 kg : 500 g &rarr; 2000 g : 500 g &rarr; <b>4:1</b>', styles['bullet']))
    s.append(Paragraph('A ratio can be written in the form <b>1:n</b> by dividing both sides by one part: 8:20 &rarr; divide by 8 &rarr; <b>1:2.5</b>', styles['bullet']))

    s.append(Paragraph('2. Sharing in a given ratio', styles['h2']))
    s.append(Paragraph('1. Add the ratio parts to find the <b>total number of parts</b>.', styles['bullet']))
    s.append(Paragraph('2. Divide the amount by the total parts to find <b>what one part is worth</b>.', styles['bullet']))
    s.append(Paragraph('3. Multiply that back up for each share.', styles['bullet']))
    s.append(Paragraph('Share &pound;60 in the ratio 2:3:5 &rarr; total parts = 10 &rarr; 1 part = &pound;6 &rarr; shares = <b>&pound;12 : &pound;18 : &pound;30</b>', styles['body']))
    s.append(Paragraph('<b>Working backwards</b>: if you know one share, divide by its number of parts to find 1 part, then use that to find the total.', styles['bodyb']))
    s.append(Paragraph('Ratio 3:4, larger share = &pound;48 &rarr; 4 parts = &pound;48 &rarr; 1 part = &pound;12 &rarr; total (7 parts) = <b>&pound;84</b>', styles['body']))

    s.append(Paragraph('3. Direct proportion', styles['h2']))
    s.append(Paragraph(
        'Two quantities are in <b>direct proportion</b> when they increase (or decrease) at the same rate: double one, the other doubles too. '
        'Written as <b>y = kx</b>. Most problems use the <b>unitary method</b>: find the value of 1 unit, then scale up.', styles['body']))
    s.append(Paragraph('5 pens cost &pound;3.50 &rarr; 1 pen = &pound;0.70 &rarr; 8 pens = 8 &times; &pound;0.70 = <b>&pound;5.60</b>', styles['bullet']))
    s.append(Paragraph('<b>Best buy</b>: find the price per single item (or per 100g/litre) for each option, then compare. Shop A: 6 apples for &pound;2.40 (&pound;0.40 each). Shop B: 10 apples for &pound;3.80 (&pound;0.38 each) &rarr; <b>Shop B</b> is better value.', styles['bullet']))

    s.append(Paragraph('4. Inverse proportion', styles['h2']))
    s.append(Paragraph(
        'Two quantities are in <b>inverse proportion</b> when one increases as the other decreases at a matching rate: double one, the other halves. '
        'Written as <b>y = k &divide; x</b> (equivalently xy = k, a constant).', styles['body']))
    s.append(Paragraph('4 workers take 15 hours to build a wall &rarr; total worker-hours = 4 &times; 15 = 60 &rarr; 6 workers: 60 &divide; 6 = <b>10 hours</b>', styles['bullet']))
    s.append(Paragraph('y is inversely proportional to x. When x = 5, y = 12 &rarr; k = xy = 60 &rarr; when x = 3, y = 60 &divide; 3 = <b>20</b>', styles['bullet']))
    s.append(Paragraph('<b>Spotting the difference</b>: quantities changing together (both up or both down) &rarr; direct. One up while the other goes down &rarr; inverse.', styles['bodyb']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('ratio_proportion_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Ratio &amp; Proportion', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Simplifying ratios', styles['h2']))
    s += q('A1', 'Simplify the ratio 16:20.', 1)
    s += q('A2', 'Simplify the ratio 45:18.', 1)
    s += q('A3', 'Write the ratio 5:12 in the form 1:n, giving n to 2 decimal places.', 2)
    s += q('A4', 'A bag contains red and blue counters in the ratio 3:7. What fraction of the counters are blue?', 1)

    s.append(Paragraph('Section B &mdash; Sharing in a given ratio', styles['h2']))
    s += q('B1', 'Share &pound;84 in the ratio 2:5.', 2)
    s += q('B2', 'Share 120 sweets in the ratio 1:2:3.', 3)
    s += q('B3', 'Two amounts are shared in the ratio 3:4. The larger share is &pound;48. Find the total amount shared.', 2)

    s.append(Paragraph('Section C &mdash; Direct proportion', styles['h2']))
    s += q('C1', '5 pens cost &pound;3.50. Find the cost of 8 pens.', 2)
    s += q('C2', 'A recipe for 4 people needs 200 g of rice. How much rice is needed for 10 people?', 2)
    s += q('C3', 'Shop A sells 6 apples for &pound;2.40. Shop B sells 10 apples for &pound;3.80. Which shop offers better value? Show your working.', 3)

    s.append(Paragraph('Section D &mdash; Inverse proportion', styles['h2']))
    s += q('D1', 'It takes 4 workers 15 hours to build a wall, all working at the same rate. How long would it take 6 workers?', 3)
    s += q('D2', 'y is inversely proportional to x. When x = 5, y = 12. Find y when x = 3.', 2)
    s += q('D3', 'A car travels a fixed distance. At 40 mph the journey takes 3 hours. How long would it take at 60 mph?', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('ratio_proportion_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Ratio &amp; Proportion', 'Answer sheet &middot; 26 marks total')

    s.append(Paragraph('Section A &mdash; Simplifying ratios', styles['h2']))
    s.append(Paragraph('A1. Divide both by 4 &rarr; <b>4:5</b> (1)', styles['ans']))
    s.append(Paragraph('A2. Divide both by 9 &rarr; <b>5:2</b> (1)', styles['ans']))
    s.append(Paragraph('A3. Divide both by 5 (1) &rarr; <b>1:2.40</b> (1)', styles['ans']))
    s.append(Paragraph('A4. Total parts = 10, blue = <b>7/10</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Sharing in a given ratio', styles['h2']))
    s.append(Paragraph('B1. 84 &divide; 7 = &pound;12 (1) &rarr; shares = <b>&pound;24 : &pound;60</b> (1)', styles['ans']))
    s.append(Paragraph('B2. 120 &divide; 6 = 20 (1) &rarr; shares = <b>20 : 40 : 60</b> (1) &rarr; check total = 120 (1)', styles['ans']))
    s.append(Paragraph('B3. 4 parts = &pound;48 &rarr; 1 part = &pound;12 (1) &rarr; total (7 parts) = <b>&pound;84</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Direct proportion', styles['h2']))
    s.append(Paragraph('C1. 3.50 &divide; 5 = &pound;0.70 (1) &rarr; 8 &times; 0.70 = <b>&pound;5.60</b> (1)', styles['ans']))
    s.append(Paragraph('C2. 200 &divide; 4 = 50 g per person (1) &rarr; 50 &times; 10 = <b>500 g</b> (1)', styles['ans']))
    s.append(Paragraph('C3. Shop A: 2.40 &divide; 6 = &pound;0.40 per apple (1) &nbsp; Shop B: 3.80 &divide; 10 = &pound;0.38 per apple (1) &rarr; <b>Shop B</b> is better value, cheaper per apple (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Inverse proportion', styles['h2']))
    s.append(Paragraph('D1. Worker-hours = 4 &times; 15 = 60 (1) &rarr; 60 &divide; 6 (1) &rarr; = <b>10 hours</b> (1)', styles['ans']))
    s.append(Paragraph('D2. k = 5 &times; 12 = 60 (1) &rarr; y = 60 &divide; 3 = <b>20</b> (1)', styles['ans']))
    s.append(Paragraph('D3. Distance = 40 &times; 3 = 120 miles (1) &rarr; time = 120 &divide; 60 = <b>2 hours</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for correctly identifying the total parts, the unitary value, or the '
        'constant of proportionality, even if the final answer contains an arithmetic error.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
