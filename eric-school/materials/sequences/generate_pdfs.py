# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Sequences (GCSE Maths, Algebra)."""

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
    doc = SimpleDocTemplate('sequences_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Sequences',
                 'Quick reference sheet &middot; GCSE Maths, Algebra &middot; keep handy for revision')

    s.append(Paragraph('1. Term-to-term rules', styles['h2']))
    s.append(Paragraph(
        'A sequence is a list of numbers following a pattern; each number is a <b>term</b>. The '
        '<b>term-to-term rule</b> says how to get from one term to the next (e.g. "add 4", "subtract 3", '
        '"multiply by 2"). To continue a sequence, apply the rule to the last term you know.', styles['body']))
    s.append(Paragraph('3, 7, 11, 15, 19, ... &rarr; rule is <b>add 4</b>', styles['bullet']))
    s.append(Paragraph('50, 44, 38, 32, ... &rarr; rule is <b>subtract 6</b>', styles['bullet']))
    s.append(Paragraph('2, 6, 18, 54, ... &rarr; rule is <b>multiply by 3</b> (not every rule adds or subtracts)', styles['bullet']))

    s.append(Paragraph('2. Special sequences', styles['h2']))
    s.append(table([
        [headcell('Name'), headcell('Sequence'), headcell('Pattern')],
        [cell('Square numbers'), cell('1, 4, 9, 16, 25, ...'), cell('n &times; n')],
        [cell('Cube numbers'), cell('1, 8, 27, 64, 125, ...'), cell('n &times; n &times; n')],
        [cell('Triangular numbers'), cell('1, 3, 6, 10, 15, ...'), cell('add 2, then 3, then 4, ...')],
        [cell('Fibonacci-type'), cell('1, 1, 2, 3, 5, 8, 13, ...'), cell('each term = sum of previous 2')],
    ], col_widths=[38 * mm, 62 * mm, 60 * mm]))

    s.append(Paragraph('3. Finding the nth term (arithmetic sequences)', styles['h2']))
    s.append(Paragraph(
        'The nth term is a formula that lets you jump straight to any term, without listing every term before it. '
        'It only works this simply when the sequence adds/subtracts the <b>same amount</b> each time.', styles['body']))
    s.append(Paragraph('<b>nth term = dn + (a &minus; d)</b> &nbsp;&mdash;&nbsp; d = common difference, a = first term', styles['bodyb']))
    s.append(Paragraph('Method, step by step, for 3, 7, 11, 15, 19, ...', styles['h3']))
    s.append(Paragraph('1. Find the common difference: d = 4 (each term goes up by 4)', styles['bullet']))
    s.append(Paragraph('2. Note the first term: a = 3', styles['bullet']))
    s.append(Paragraph('3. Work out a &minus; d: 3 &minus; 4 = &minus;1', styles['bullet']))
    s.append(Paragraph('4. Write the nth term: <b>4n &minus; 1</b>', styles['bullet']))
    s.append(Paragraph('5. Check it: substitute n = 1 &rarr; 4(1) &minus; 1 = 3 &#10003; (matches the first term)', styles['bullet']))
    s.append(Paragraph('With a negative (decreasing) difference: 50, 44, 38, 32, ...', styles['body']))
    s.append(Paragraph('d = &minus;6, a = 50, a &minus; d = 50 &minus; (&minus;6) = 56 &nbsp;&rarr;&nbsp; nth term = <b>&minus;6n + 56</b>', styles['body']))

    s.append(Paragraph('4. Using the nth term', styles['h2']))
    s.append(Paragraph('<b>To find a specific term</b>, substitute the term number in for n.', styles['bodyb']))
    s.append(Paragraph('nth term = 3n + 4 &nbsp;&rarr;&nbsp; 10th term = 3(10) + 4 = <b>34</b>', styles['body']))
    s.append(Paragraph('<b>To check if a number is in the sequence</b>, set the nth term formula equal to that number and solve for n.', styles['bodyb']))
    s.append(Paragraph('If n comes out as a <b>positive whole number</b>, it is in the sequence. If not (a decimal, a fraction, or negative), it is not.', styles['body']))
    s.append(Paragraph('Is 50 a term in the sequence with nth term 4n &minus; 1?', styles['body']))
    s.append(Paragraph('4n &minus; 1 = 50 &rarr; 4n = 51 &rarr; n = 12.75 &rarr; not a whole number &rarr; <b>No</b>', styles['body']))
    s.append(Paragraph('Is 47 a term in the sequence with nth term 3n + 2?', styles['body']))
    s.append(Paragraph('3n + 2 = 47 &rarr; 3n = 45 &rarr; n = 15 &rarr; whole number &rarr; <b>Yes</b> (it is the 15th term)', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('sequences_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Sequences', 'Test &middot; 26 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 26'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Term-to-term rules', styles['h2']))
    s += q('A1', 'Write the next term of 12, 17, 22, 27, ...', 1)
    s += q('A2', 'Write the next term of 60, 52, 44, ...', 1)
    s += q('A3', 'State the term-to-term rule for 3, 6, 12, 24, ...', 1)
    s += q('A4', 'State the term-to-term rule for 90, 81, 72, 63, ...', 1)

    s.append(Paragraph('Section B &mdash; Special sequences', styles['h2']))
    s += q('B1', 'Write the first five square numbers.', 2)
    s += q('B2', 'Write the first five triangular numbers.', 2)
    s += q('B3', 'This is a Fibonacci-type sequence: 3, 5, 8, 13, ... Find the next two terms.', 2)

    s.append(Paragraph('Section C &mdash; Finding the nth term', styles['h2']))
    s += q('C1', 'Find the nth term of the sequence 2, 5, 8, 11, ...', 3)
    s += q('C2', 'Find the nth term of the sequence 40, 33, 26, 19, ...', 3)

    s.append(Paragraph('Section D &mdash; Using the nth term', styles['h2']))
    s += q('D1', 'The nth term of a sequence is 4n + 5. Find the 12th term.', 2)
    s += q('D2', 'The nth term of a sequence is 6n &minus; 4. Is 100 a term in this sequence? Show your working.', 3)
    s += q('D3', 'The first term of a sequence is 9 and the term-to-term rule is "add 5". Find the nth term, and use it to find the 20th term.', 5)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('sequences_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Sequences', 'Answer sheet &middot; 26 marks total')

    s.append(Paragraph('Section A &mdash; Term-to-term rules', styles['h2']))
    s.append(Paragraph('A1. <b>32</b> (1)', styles['ans']))
    s.append(Paragraph('A2. <b>36</b> (1)', styles['ans']))
    s.append(Paragraph('A3. <b>Multiply by 2</b> (1)', styles['ans']))
    s.append(Paragraph('A4. <b>Subtract 9</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Special sequences', styles['h2']))
    s.append(Paragraph('B1. <b>1, 4, 9, 16, 25</b> (2, 1 if one error)', styles['ans']))
    s.append(Paragraph('B2. <b>1, 3, 6, 10, 15</b> (2, 1 if one error)', styles['ans']))
    s.append(Paragraph('B3. <b>21, 34</b> (1 each)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Finding the nth term', styles['h2']))
    s.append(Paragraph('C1. d = 3 (1) &nbsp; a &minus; d = 2 &minus; 3 = &minus;1 (1) &nbsp; = <b>3n &minus; 1</b> (1)', styles['ans']))
    s.append(Paragraph('C2. d = &minus;7 (1) &nbsp; a &minus; d = 40 &minus; (&minus;7) = 47 (1) &nbsp; = <b>&minus;7n + 47</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Using the nth term', styles['h2']))
    s.append(Paragraph('D1. 4(12) + 5 (1) &nbsp; = <b>53</b> (1)', styles['ans']))
    s.append(Paragraph('D2. 6n &minus; 4 = 100 &rarr; 6n = 104 &rarr; n = 17.33... (1) &nbsp; not a whole number (1) &nbsp; so <b>No</b> (1)', styles['ans']))
    s.append(Paragraph(
        'D3. d = 5 (1) &nbsp; a &minus; d = 9 &minus; 5 = 4 (1) &nbsp; nth term = <b>5n + 4</b> (1) &nbsp; '
        '20th term: 5(20) + 4 (1) &nbsp; = <b>104</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for correctly identifying the common difference or correctly '
        'substituting into a formula, even if the final answer contains an arithmetic error.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
