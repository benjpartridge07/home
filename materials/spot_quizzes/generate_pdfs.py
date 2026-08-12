# -*- coding: utf-8 -*-
"""Generate the Spot Quizzes PDFs: short standalone practice quizzes.
Standard form and order of magnitude (AQA Synergy 8465, Foundation tier,
maths-skills strand used across several Biology topics), plus a targeted
Fractions/Decimals/Percentages retest built from Eric's actual wrong
answers on the FDP topic test."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK = colors.HexColor('#23201A')
INK_SOFT = colors.HexColor('#6B6355')
BIO = colors.HexColor('#2F8B57')
MATHS = colors.HexColor('#3A5E85')

MARGIN = 18 * mm

styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=26,
                             textColor=INK, spaceAfter=4, leading=30),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=10.5,
                                textColor=INK_SOFT, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=13.5,
                          textColor=BIO, spaceBefore=14, spaceAfter=7),
    'h2m': ParagraphStyle('h2m', fontName='Helvetica-Bold', fontSize=13.5,
                           textColor=MATHS, spaceBefore=14, spaceAfter=7),
    'qtext': ParagraphStyle('qtext', fontName='Helvetica', fontSize=10,
                             textColor=INK, leading=14, spaceAfter=2, alignment=TA_LEFT),
    'marks': ParagraphStyle('marks', fontName='Helvetica-Oblique', fontSize=9,
                             textColor=INK_SOFT, spaceAfter=9),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=10,
                           textColor=INK, leading=14, spaceAfter=6),
    'note': ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=9,
                            textColor=INK_SOFT, leading=12, spaceBefore=12),
    'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=9.3,
                            textColor=INK, leading=12.5),
}


def hr():
    return HRFlowable(width='100%', thickness=1, color=colors.HexColor('#E4DDCE'),
                       spaceBefore=6, spaceAfter=12)


def header(title, subtitle):
    return [Paragraph(title, styles['title']), Paragraph(subtitle, styles['subtitle']), hr()]


def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def name_row():
    t = Table([[
        Paragraph('Name: ________________________________', styles['cell']),
        Paragraph('Date: ______________', styles['cell']),
    ]], colWidths=[100 * mm, 60 * mm], hAlign='LEFT')
    return t


# ---------------------------------------------------------------- STANDARD FORM

def build_standard_form_quiz():
    doc = SimpleDocTemplate('standard_form_quiz.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form', 'Spot quiz &middot; 11 marks total')
    s.append(name_row())
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Writing numbers in standard form', styles['h2']))
    s += q(1, 'A red blood cell is 8 &micro;m across. Write this in metres, using standard form.', 2)
    s.append(Spacer(1, 8))
    s += q(2, 'A virus is 30 nm across. Write this in metres, using standard form.', 2)
    s.append(Spacer(1, 8))
    s += q(3, 'A bacterium is 0.000004 m wide. Write this in standard form.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Converting standard form back', styles['h2']))
    s += q(4, 'Convert 6 &times; 10<sup>-6</sup> m to micrometres.', 2)
    s.append(Spacer(1, 8))
    s += q(5, 'Convert 1.5 &times; 10<sup>-4</sup> m to millimetres.', 2)
    s.append(Spacer(1, 8))
    s += q(6, 'Write 9 &times; 10<sup>-5</sup> m as an ordinary number, in metres.', 1)

    doc.build(s)


def build_standard_form_answers():
    doc = SimpleDocTemplate('standard_form_quiz_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Standard Form', 'Answer key &middot; 11 marks total')

    s.append(Paragraph('Section A &mdash; Writing numbers in standard form', styles['h2']))
    s.append(Paragraph('<b>1.</b> 8 &micro;m = 0.000008 m (1) &nbsp; = <b>8 &times; 10<sup>-6</sup> m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>2.</b> 30 nm = 0.00000003 m (1) &nbsp; = <b>3 &times; 10<sup>-8</sup> m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>3.</b> 0.000004 m (1) &nbsp; = <b>4 &times; 10<sup>-6</sup> m</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Converting standard form back', styles['h2']))
    s.append(Paragraph('<b>4.</b> 6 &times; 10<sup>-6</sup> m = 0.000006 m (1) &nbsp; = <b>6 &micro;m</b> (1)', styles['ans']))
    s.append(Paragraph('<b>5.</b> 1.5 &times; 10<sup>-4</sup> m = 0.00015 m (1) &nbsp; = <b>0.15 mm</b> (1)', styles['ans']))
    s.append(Paragraph('<b>6.</b> <b>0.00009 m</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for correctly counting decimal places even if the final answer '
        'contains an arithmetic slip.', styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- ORDER OF MAGNITUDE

def build_order_of_magnitude_quiz():
    doc = SimpleDocTemplate('order_of_magnitude_quiz.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Order of Magnitude', 'Spot quiz &middot; 10 marks total')
    s.append(name_row())
    s.append(Spacer(1, 10))

    s += q(1, 'A bacterium is about 3 &micro;m across and a red blood cell is about 30 &micro;m across. Calculate how many times bigger the red blood cell is, and state this as an order of magnitude.', 2)
    s.append(Spacer(1, 10))
    s += q(2, 'A plant cell is 5 &times; 10<sup>-5</sup> m wide and a bacterium is 5 &times; 10<sup>-6</sup> m wide. Calculate how many times wider the plant cell is.', 2)
    s.append(Spacer(1, 10))
    s += q(3, 'A virus is 2 &times; 10<sup>-8</sup> m across and a bacterium is 2 &times; 10<sup>-6</sup> m across. Calculate how many times bigger the bacterium is than the virus, and state this as an order of magnitude.', 2)
    s.append(Spacer(1, 10))
    s += q(4, 'An animal cell is 40 &micro;m across and a mitochondrion inside it is 4 &micro;m across. Calculate how many times bigger the animal cell is.', 2)
    s.append(Spacer(1, 10))
    s += q(5, 'A cell nucleus is 1 &times; 10<sup>-5</sup> m across and a ribosome is 1 &times; 10<sup>-7</sup> m across. Calculate how many orders of magnitude bigger the nucleus is.', 2)

    doc.build(s)


def build_order_of_magnitude_answers():
    doc = SimpleDocTemplate('order_of_magnitude_quiz_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Order of Magnitude', 'Answer key &middot; 10 marks total')

    s.append(Paragraph('<b>1.</b> 30 &divide; 3 = 10 (1) &nbsp; <b>one order of magnitude</b> bigger (1)', styles['ans']))
    s.append(Paragraph('<b>2.</b> (5 &times; 10<sup>-5</sup>) &divide; (5 &times; 10<sup>-6</sup>) = 10 (1) &nbsp; <b>10 times wider</b> (1)', styles['ans']))
    s.append(Paragraph('<b>3.</b> (2 &times; 10<sup>-6</sup>) &divide; (2 &times; 10<sup>-8</sup>) = 100 (1) &nbsp; <b>two orders of magnitude</b> bigger (1)', styles['ans']))
    s.append(Paragraph('<b>4.</b> 40 &divide; 4 = <b>10 times bigger</b> (1) &mdash; award both marks for correct division and answer (1)', styles['ans']))
    s.append(Paragraph('<b>5.</b> (1 &times; 10<sup>-5</sup>) &divide; (1 &times; 10<sup>-7</sup>) = 100 (1) &nbsp; <b>two orders of magnitude</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: "order of magnitude" &mdash; a ratio of 10 is one order of magnitude, a ratio of 100 is '
        'two orders of magnitude, and so on. Award method marks for correct division even if the order-of-'
        'magnitude wording is missing.', styles['note']))

    doc.build(s)


# ---------------------------------------------------------------- FDP WEAK SPOTS (MATHS)

def build_fdp_weak_spots_quiz():
    doc = SimpleDocTemplate('fdp_weak_spots_quiz.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Fractions, Decimals &amp; Percentages: Weak Spots',
                 'Spot quiz &middot; 14 marks total &middot; targeted retest after A1, A6, A8, C2, C3, D4')
    s.append(name_row())
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Converting fractions and decimals', styles['h2m']))
    s += q(1, 'Convert 5/8 to a decimal.', 1)
    s.append(Spacer(1, 8))
    s += q(2, 'Convert 7/25 to a decimal.', 1)
    s.append(Spacer(1, 8))
    s += q(3, 'Convert 0.65 to a fraction in its simplest form.', 1)
    s.append(Spacer(1, 8))
    s += q(4, 'Convert 0.8 to a fraction in its simplest form.', 1)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Fraction of an amount', styles['h2m']))
    s += q(5, 'Calculate 3/8 of 96.', 2)
    s.append(Spacer(1, 8))
    s += q(6, 'Calculate 7/10 of 150.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; Percentage of an amount (no calculator)', styles['h2m']))
    s += q(7, 'Calculate 30% of &pound;70 without a calculator. Show your method.', 2)
    s.append(Spacer(1, 8))
    s += q(8, 'Calculate 15% of &pound;48 without a calculator. Show your method.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Comparing fractions and percentages', styles['h2m']))
    s += q(9, 'Which is bigger: 3/5 or 55%? Show your working.', 1)
    s.append(Spacer(1, 8))
    s += q(10, 'Which is bigger: 9/20 or 47%? Show your working.', 1)

    doc.build(s)


def build_fdp_weak_spots_answers():
    doc = SimpleDocTemplate('fdp_weak_spots_quiz_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Fractions, Decimals &amp; Percentages: Weak Spots', 'Answer key &middot; 14 marks total')

    s.append(Paragraph('Section A &mdash; Converting fractions and decimals', styles['h2m']))
    s.append(Paragraph('<b>1.</b> 5 &divide; 8 = <b>0.625</b> (1)', styles['ans']))
    s.append(Paragraph('<b>2.</b> 7 &divide; 25 = <b>0.28</b> (1)', styles['ans']))
    s.append(Paragraph('<b>3.</b> 0.65 = 65/100 = <b>13/20</b> (1)', styles['ans']))
    s.append(Paragraph('<b>4.</b> 0.8 = 8/10 = <b>4/5</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Fraction of an amount', styles['h2m']))
    s.append(Paragraph('<b>5.</b> 96 &divide; 8 = 12 (1) &nbsp; 12 &times; 3 = <b>36</b> (1)', styles['ans']))
    s.append(Paragraph('<b>6.</b> 150 &divide; 10 = 15 (1) &nbsp; 15 &times; 7 = <b>105</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Percentage of an amount (no calculator)', styles['h2m']))
    s.append(Paragraph('<b>7.</b> 10% = &pound;7 (1) &nbsp; 30% = 7 &times; 3 = <b>&pound;21</b> (1)', styles['ans']))
    s.append(Paragraph('<b>8.</b> 10% = &pound;4.80, 5% = &pound;2.40 (1) &nbsp; 15% = 4.80 + 2.40 = <b>&pound;7.20</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Comparing fractions and percentages', styles['h2m']))
    s.append(Paragraph('<b>9.</b> 3/5 = 60% (1) &nbsp; <b>3/5 is bigger</b> than 55%', styles['ans']))
    s.append(Paragraph('<b>10.</b> 9/20 = 45% (1) &nbsp; <b>47% is bigger</b> than 9/20', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for finding 10% (and 1% or 5%) first, even if the final answer '
        'contains an arithmetic slip. For comparison questions, accept working the other way (converting the '
        'percentage to a fraction) provided the comparison is correct.', styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_standard_form_quiz()
    build_standard_form_answers()
    build_order_of_magnitude_quiz()
    build_order_of_magnitude_answers()
    build_fdp_weak_spots_quiz()
    build_fdp_weak_spots_answers()
    print('done')
