# -*- coding: utf-8 -*-
"""Generate eight practice tests + answer sheets for
Quadratics: Expanding & Factorising (GCSE Maths, AQA 8300, Higher tier).

Every test has the same six sections and 40 marks, in the order the
skills build on each other:

  A  Expanding double brackets (incl. squared brackets)        8 marks
  B  Expanding three brackets (Higher)                          6 marks
  C  Factorising x^2 + bx + c and the difference of two squares 7 marks
  D  Factorising ax^2 + bx + c (Higher)                         6 marks
  E  Using factorising: solving, algebraic fractions            6 marks
  F  Problem solving & proof (identities, completing the square) 7 marks

Each test uses fresh numbers and a slightly different question style
(error spotting, missing coefficients, area/volume contexts, proofs).
Run verify_answers.py after editing any question: it checks every
expansion, factorisation and solution numerically.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle

INK = colors.HexColor('#23201A')
INK_SOFT = colors.HexColor('#6B6355')
MATHS = colors.HexColor('#3A5E85')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#F1EAD9')

MARGIN = 20 * mm
TOTAL = 40
WORKING_SPACE_PER_MARK = 8 * mm  # blank space under each question for Eric's working
TITLE = 'Quadratics: Expanding &amp; Factorising'

styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=24,
                             textColor=INK, spaceAfter=4, leading=28),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=10.5,
                                textColor=INK_SOFT, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=14,
                          textColor=MATHS, spaceBefore=14, spaceAfter=8),
    'marks': ParagraphStyle('marks', fontName='Helvetica-Oblique', fontSize=9.5,
                             textColor=INK_SOFT, spaceAfter=12),
    'qtext': ParagraphStyle('qtext', fontName='Helvetica', fontSize=10.5,
                             textColor=INK, leading=15, spaceAfter=2),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=10.5,
                           textColor=INK, leading=15, spaceAfter=7),
    'note': ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=9.5,
                            textColor=INK_SOFT, leading=13, spaceBefore=14),
    'tablecell': ParagraphStyle('tablecell', fontName='Helvetica', fontSize=10,
                                 textColor=INK),
    'frac': ParagraphStyle('frac', fontName='Helvetica', fontSize=11,
                            textColor=INK, alignment=1, leading=14),
}

SECTIONS = {
    'A': 'Section A &mdash; Expanding double brackets',
    'B': 'Section B &mdash; Expanding three brackets',
    'C': 'Section C &mdash; Factorising x<sup>2</sup> + bx + c and the difference of two squares',
    'D': 'Section D &mdash; Factorising ax<sup>2</sup> + bx + c',
    'E': 'Section E &mdash; Using factorising',
    'F': 'Section F &mdash; Problem solving &amp; proof',
}


def hr():
    return HRFlowable(width='100%', thickness=1, color=PAPER_LINE,
                       spaceBefore=6, spaceAfter=14)


def header(subtitle):
    return [Paragraph(TITLE, styles['title']), Paragraph(subtitle, styles['subtitle']), hr()]


def name_table():
    t = Table([[
        Paragraph('Name: ________________________________', styles['tablecell']),
        Paragraph('Date: ______________', styles['tablecell']),
        Paragraph(f'Score: _____ / {TOTAL}', styles['tablecell']),
    ]], colWidths=[80 * mm, 45 * mm, 40 * mm], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEAD_BG),
        ('LINEBELOW', (0, 0), (-1, -1), 0.75, PAPER_LINE),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def frac(num, den):
    """A stacked algebraic fraction, indented under the question text."""
    t = Table([[Paragraph(num, styles['frac'])], [Paragraph(den, styles['frac'])]],
              colWidths=[40 * mm], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (0, 0), 0.9, INK),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    outer = Table([[t]], colWidths=[170 * mm], hAlign='LEFT')
    outer.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 24),
                               ('TOPPADDING', (0, 0), (-1, -1), 4),
                               ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    return outer


def marking_note():
    return Paragraph(
        'Marking note: the marks in brackets show where each mark is earned. Award method marks for a correct '
        'method even if there is a later slip. Accept answers in any equivalent form, e.g. terms in a different '
        'order, or brackets written the other way round: (x &minus; 7)(x + 4) is the same as (x + 4)(x &minus; 7). '
        '&ldquo;Factorise fully&rdquo; questions lose the last mark if a common factor is left inside a bracket.',
        styles['note'])


# Each question: (id, question text, marks, answer text, optional fraction (num, den))
# Use <sup>2</sup> for powers and &minus; for minus signs: reportlab's Helvetica
# can't draw Unicode superscript characters.

TESTS = {
    1: [
        ('A', [
            ('A1', 'Expand and simplify (x + 4)(x + 7)', 2,
             'x<sup>2</sup> + 7x + 4x + 28 (1) &nbsp; = <b>x<sup>2</sup> + 11x + 28</b> (1)'),
            ('A2', 'Expand and simplify (x &minus; 5)(x + 3)', 2,
             'x<sup>2</sup> + 3x &minus; 5x &minus; 15 (1) &nbsp; = <b>x<sup>2</sup> &minus; 2x &minus; 15</b> (1)'),
            ('A3', 'Expand and simplify (x &minus; 6)<sup>2</sup>', 2,
             '(x &minus; 6)(x &minus; 6) = x<sup>2</sup> &minus; 6x &minus; 6x + 36 (1) &nbsp; = <b>x<sup>2</sup> &minus; 12x + 36</b> (1)'),
            ('A4', 'Expand and simplify (3x + 2)(2x &minus; 5)', 2,
             '6x<sup>2</sup> &minus; 15x + 4x &minus; 10 (1) &nbsp; = <b>6x<sup>2</sup> &minus; 11x &minus; 10</b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (x + 1)(x + 2)(x + 3)', 3,
             '(x + 1)(x + 2) = x<sup>2</sup> + 3x + 2 (1) &nbsp; (x<sup>2</sup> + 3x + 2)(x + 3) = x<sup>3</sup> + 3x<sup>2</sup> + 3x<sup>2</sup> + 9x + 2x + 6 (1) '
             '&nbsp; = <b>x<sup>3</sup> + 6x<sup>2</sup> + 11x + 6</b> (1)'),
            ('B2', 'Expand and simplify (x &minus; 2)(x + 4)(2x + 1)', 3,
             '(x &minus; 2)(x + 4) = x<sup>2</sup> + 2x &minus; 8 (1) &nbsp; (x<sup>2</sup> + 2x &minus; 8)(2x + 1) = 2x<sup>3</sup> + x<sup>2</sup> + 4x<sup>2</sup> + 2x &minus; 16x &minus; 8 (1) '
             '&nbsp; = <b>2x<sup>3</sup> + 5x<sup>2</sup> &minus; 14x &minus; 8</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> + 9x + 20', 2,
             'Two numbers that multiply to 20 and add to 9: 4 and 5 (1) &nbsp; <b>(x + 4)(x + 5)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> &minus; 3x &minus; 28', 2,
             'Multiply to &minus;28, add to &minus;3: &minus;7 and 4 (1) &nbsp; <b>(x &minus; 7)(x + 4)</b> (1)'),
            ('C3', 'Factorise x<sup>2</sup> &minus; 49', 1,
             'Difference of two squares: <b>(x + 7)(x &minus; 7)</b> (1)'),
            ('C4', 'Factorise fully 2x<sup>2</sup> &minus; 50', 2,
             '2(x<sup>2</sup> &minus; 25) (1) &nbsp; = <b>2(x + 5)(x &minus; 5)</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 2x<sup>2</sup> + 7x + 3', 2,
             '2 &times; 3 = 6; numbers that multiply to 6 and add to 7: 6 and 1, so 2x<sup>2</sup> + 6x + x + 3 = 2x(x + 3) + 1(x + 3) (1) &nbsp; <b>(2x + 1)(x + 3)</b> (1)'),
            ('D2', 'Factorise 3x<sup>2</sup> &minus; 10x &minus; 8', 2,
             '3 &times; &minus;8 = &minus;24; numbers: &minus;12 and 2, so 3x<sup>2</sup> &minus; 12x + 2x &minus; 8 = 3x(x &minus; 4) + 2(x &minus; 4) (1) &nbsp; <b>(3x + 2)(x &minus; 4)</b> (1)'),
            ('D3', 'Factorise fully 4x<sup>2</sup> + 10x &minus; 6', 2,
             '2(2x<sup>2</sup> + 5x &minus; 3) (1) &nbsp; = <b>2(2x &minus; 1)(x + 3)</b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve x<sup>2</sup> &minus; 5x &minus; 14 = 0', 3,
             '(x &minus; 7)(x + 2) = 0 (1) &nbsp; x &minus; 7 = 0 or x + 2 = 0 (1) &nbsp; <b>x = 7 or x = &minus;2</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = (x + 2)(x + 3) (1) &nbsp; denominator = (x + 3)(x &minus; 3) (1) &nbsp; cancel (x + 3): <b>(x + 2) / (x &minus; 3)</b> (1)',
             ('x<sup>2</sup> + 5x + 6', 'x<sup>2</sup> &minus; 9')),
        ]),
        ('F', [
            ('F1', 'Show that (n + 5)<sup>2</sup> &minus; (n &minus; 5)<sup>2</sup> = 20n for every value of n', 2,
             '(n<sup>2</sup> + 10n + 25) &minus; (n<sup>2</sup> &minus; 10n + 25) (1) &nbsp; = n<sup>2</sup> + 10n + 25 &minus; n<sup>2</sup> + 10n &minus; 25 = <b>20n</b> (1)'),
            ('F2', 'A rectangle is (x + 6) cm long and (x &minus; 2) cm wide. Its area is 33 cm<sup>2</sup>.<br/>'
                   '(a) Show that x<sup>2</sup> + 4x &minus; 45 = 0. &nbsp; (b) Solve the equation to find the width of the rectangle.', 4,
             '(a) (x + 6)(x &minus; 2) = x<sup>2</sup> + 4x &minus; 12 (1) &nbsp; x<sup>2</sup> + 4x &minus; 12 = 33, so x<sup>2</sup> + 4x &minus; 45 = 0 (1)<br/>'
             '(b) (x + 9)(x &minus; 5) = 0 so x = 5 or x = &minus;9 (1) &nbsp; a length can&rsquo;t be negative, so x = 5 and the <b>width = 3 cm</b> (1)'),
            ('F3', 'Without a calculator, use the difference of two squares to work out 53<sup>2</sup> &minus; 47<sup>2</sup>', 1,
             '(53 + 47)(53 &minus; 47) = 100 &times; 6 = <b>600</b> (1)'),
        ]),
    ],
    2: [
        ('A', [
            ('A1', 'Expand and simplify (x + 3)(x + 9)', 2,
             'x<sup>2</sup> + 9x + 3x + 27 (1) &nbsp; = <b>x<sup>2</sup> + 12x + 27</b> (1)'),
            ('A2', 'Expand and simplify (x &minus; 8)(x &minus; 2)', 2,
             'x<sup>2</sup> &minus; 2x &minus; 8x + 16 (1) &nbsp; = <b>x<sup>2</sup> &minus; 10x + 16</b> (1)'),
            ('A3', 'Expand and simplify (2x + 5)<sup>2</sup>', 2,
             '(2x + 5)(2x + 5) = 4x<sup>2</sup> + 10x + 10x + 25 (1) &nbsp; = <b>4x<sup>2</sup> + 20x + 25</b> (1)'),
            ('A4', 'A student writes (x + 4)<sup>2</sup> = x<sup>2</sup> + 16. Explain the mistake and write the correct expansion.', 2,
             'They squared each term separately and missed the two middle terms: (x + 4)<sup>2</sup> means (x + 4)(x + 4) (1) &nbsp; <b>x<sup>2</sup> + 8x + 16</b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (x + 3)(x &minus; 1)(x &minus; 4)', 3,
             '(x + 3)(x &minus; 1) = x<sup>2</sup> + 2x &minus; 3 (1) &nbsp; (x<sup>2</sup> + 2x &minus; 3)(x &minus; 4) = x<sup>3</sup> &minus; 4x<sup>2</sup> + 2x<sup>2</sup> &minus; 8x &minus; 3x + 12 (1) '
             '&nbsp; = <b>x<sup>3</sup> &minus; 2x<sup>2</sup> &minus; 11x + 12</b> (1)'),
            ('B2', 'Expand and simplify (x + 2)<sup>3</sup>', 3,
             '(x + 2)<sup>2</sup> = x<sup>2</sup> + 4x + 4 (1) &nbsp; (x<sup>2</sup> + 4x + 4)(x + 2) = x<sup>3</sup> + 2x<sup>2</sup> + 4x<sup>2</sup> + 8x + 4x + 8 (1) '
             '&nbsp; = <b>x<sup>3</sup> + 6x<sup>2</sup> + 12x + 8</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> + 2x &minus; 24', 2,
             'Multiply to &minus;24, add to 2: 6 and &minus;4 (1) &nbsp; <b>(x + 6)(x &minus; 4)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> &minus; 13x + 36', 2,
             'Multiply to 36, add to &minus;13: &minus;4 and &minus;9 (1) &nbsp; <b>(x &minus; 4)(x &minus; 9)</b> (1)'),
            ('C3', 'Factorise 9x<sup>2</sup> &minus; 16', 1,
             '(3x)<sup>2</sup> &minus; 4<sup>2</sup> = <b>(3x + 4)(3x &minus; 4)</b> (1)'),
            ('C4', 'x<sup>2</sup> + bx + 15 factorises to (x + 3)(x + a). Find the values of a and b.', 2,
             '3 &times; a = 15 so <b>a = 5</b> (1) &nbsp; b = 3 + 5, so <b>b = 8</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 5x<sup>2</sup> + 13x &minus; 6', 2,
             '5 &times; &minus;6 = &minus;30; numbers: 15 and &minus;2, so 5x<sup>2</sup> + 15x &minus; 2x &minus; 6 = 5x(x + 3) &minus; 2(x + 3) (1) &nbsp; <b>(5x &minus; 2)(x + 3)</b> (1)'),
            ('D2', 'Factorise 6x<sup>2</sup> &minus; 11x + 4', 2,
             '6 &times; 4 = 24; numbers: &minus;8 and &minus;3, so 6x<sup>2</sup> &minus; 8x &minus; 3x + 4 = 2x(3x &minus; 4) &minus; 1(3x &minus; 4) (1) &nbsp; <b>(2x &minus; 1)(3x &minus; 4)</b> (1)'),
            ('D3', 'Factorise fully 3x<sup>3</sup> &minus; 12x', 2,
             '3x(x<sup>2</sup> &minus; 4) (1) &nbsp; = <b>3x(x + 2)(x &minus; 2)</b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve 2x<sup>2</sup> + x &minus; 15 = 0', 3,
             '(2x &minus; 5)(x + 3) = 0 (1) &nbsp; 2x &minus; 5 = 0 or x + 3 = 0 (1) &nbsp; <b>x = 2.5 or x = &minus;3</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = (2x + 1)(x &minus; 4) (1) &nbsp; denominator = (x + 4)(x &minus; 4) (1) &nbsp; cancel (x &minus; 4): <b>(2x + 1) / (x + 4)</b> (1)',
             ('2x<sup>2</sup> &minus; 7x &minus; 4', 'x<sup>2</sup> &minus; 16')),
        ]),
        ('F', [
            ('F1', '(a) Write x<sup>2</sup> + 8x + 5 in the form (x + a)<sup>2</sup> + b. &nbsp; '
                   '(b) Hence write down the coordinates of the turning point of y = x<sup>2</sup> + 8x + 5.', 3,
             '(a) (x + 4)<sup>2</sup> = x<sup>2</sup> + 8x + 16 (1) &nbsp; so x<sup>2</sup> + 8x + 5 = <b>(x + 4)<sup>2</sup> &minus; 11</b> (1)<br/>'
             '(b) <b>(&minus;4, &minus;11)</b> (1)'),
            ('F2', 'Prove that the difference between the squares of two consecutive odd numbers is always a multiple of 8.', 3,
             'Let the numbers be 2n + 1 and 2n + 3 (1) &nbsp; (2n + 3)<sup>2</sup> &minus; (2n + 1)<sup>2</sup> = (4n<sup>2</sup> + 12n + 9) &minus; (4n<sup>2</sup> + 4n + 1) = 8n + 8 (1) '
             '&nbsp; = 8(n + 1), which is <b>a multiple of 8</b> (1)'),
            ('F3', 'Without a calculator, work out 1001<sup>2</sup> &minus; 999<sup>2</sup>', 1,
             '(1001 + 999)(1001 &minus; 999) = 2000 &times; 2 = <b>4000</b> (1)'),
        ]),
    ],
    3: [
        ('A', [
            ('A1', 'Expand and simplify (x + 2)(x + 11)', 2,
             'x<sup>2</sup> + 11x + 2x + 22 (1) &nbsp; = <b>x<sup>2</sup> + 13x + 22</b> (1)'),
            ('A2', 'Expand and simplify (x &minus; 7)(x + 7). Explain why the answer has no x term.', 2,
             '<b>x<sup>2</sup> &minus; 49</b> (1) &nbsp; the middle terms +7x and &minus;7x cancel out (1)'),
            ('A3', 'Expand and simplify (4x &minus; 3)(x + 2)', 2,
             '4x<sup>2</sup> + 8x &minus; 3x &minus; 6 (1) &nbsp; = <b>4x<sup>2</sup> + 5x &minus; 6</b> (1)'),
            ('A4', 'Expand and simplify (x + 3)<sup>2</sup> + (x &minus; 1)<sup>2</sup>', 2,
             'x<sup>2</sup> + 6x + 9 + x<sup>2</sup> &minus; 2x + 1 (1) &nbsp; = <b>2x<sup>2</sup> + 4x + 10</b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (2x &minus; 1)(x + 3)(x &minus; 2)', 3,
             '(2x &minus; 1)(x + 3) = 2x<sup>2</sup> + 5x &minus; 3 (1) &nbsp; (2x<sup>2</sup> + 5x &minus; 3)(x &minus; 2) = 2x<sup>3</sup> &minus; 4x<sup>2</sup> + 5x<sup>2</sup> &minus; 10x &minus; 3x + 6 (1) '
             '&nbsp; = <b>2x<sup>3</sup> + x<sup>2</sup> &minus; 13x + 6</b> (1)'),
            ('B2', 'Show that (x &minus; 1)<sup>3</sup> = x<sup>3</sup> &minus; 3x<sup>2</sup> + 3x &minus; 1', 3,
             '(x &minus; 1)<sup>2</sup> = x<sup>2</sup> &minus; 2x + 1 (1) &nbsp; (x<sup>2</sup> &minus; 2x + 1)(x &minus; 1) = x<sup>3</sup> &minus; x<sup>2</sup> &minus; 2x<sup>2</sup> + 2x + x &minus; 1 (1) '
             '&nbsp; = <b>x<sup>3</sup> &minus; 3x<sup>2</sup> + 3x &minus; 1</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> + 15x + 56', 2,
             'Multiply to 56, add to 15: 7 and 8 (1) &nbsp; <b>(x + 7)(x + 8)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> + x &minus; 30', 2,
             'Multiply to &minus;30, add to 1: 6 and &minus;5 (1) &nbsp; <b>(x + 6)(x &minus; 5)</b> (1)'),
            ('C3', 'Factorise 100 &minus; x<sup>2</sup>', 1,
             '<b>(10 + x)(10 &minus; x)</b> (1)'),
            ('C4', 'Factorise fully 5x<sup>2</sup> &minus; 20x &minus; 60', 2,
             '5(x<sup>2</sup> &minus; 4x &minus; 12) (1) &nbsp; = <b>5(x &minus; 6)(x + 2)</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 3x<sup>2</sup> + 11x + 10', 2,
             '3 &times; 10 = 30; numbers: 6 and 5, so 3x<sup>2</sup> + 6x + 5x + 10 = 3x(x + 2) + 5(x + 2) (1) &nbsp; <b>(3x + 5)(x + 2)</b> (1)'),
            ('D2', 'Factorise 4x<sup>2</sup> &minus; 4x &minus; 15', 2,
             '4 &times; &minus;15 = &minus;60; numbers: &minus;10 and 6, so 4x<sup>2</sup> &minus; 10x + 6x &minus; 15 = 2x(2x &minus; 5) + 3(2x &minus; 5) (1) &nbsp; <b>(2x + 3)(2x &minus; 5)</b> (1)'),
            ('D3', 'Factorise 25x<sup>2</sup> &minus; 9y<sup>2</sup>', 2,
             '(5x)<sup>2</sup> &minus; (3y)<sup>2</sup> (1) &nbsp; = <b>(5x + 3y)(5x &minus; 3y)</b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve x<sup>2</sup> = 6x &minus; 8', 3,
             'x<sup>2</sup> &minus; 6x + 8 = 0 (1) &nbsp; (x &minus; 2)(x &minus; 4) = 0 (1) &nbsp; <b>x = 2 or x = 4</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = 3x(x + 2) (1) &nbsp; denominator = (x &minus; 3)(x + 2) (1) &nbsp; cancel (x + 2): <b>3x / (x &minus; 3)</b> (1)',
             ('3x<sup>2</sup> + 6x', 'x<sup>2</sup> &minus; x &minus; 6')),
        ]),
        ('F', [
            ('F1', 'The area of a square is (x<sup>2</sup> + 14x + 49) cm<sup>2</sup>. Find an expression for its perimeter.', 2,
             'x<sup>2</sup> + 14x + 49 = (x + 7)<sup>2</sup>, so each side is (x + 7) cm (1) &nbsp; perimeter = 4(x + 7) = <b>(4x + 28) cm</b> (1)'),
            ('F2', 'A cuboid measures x cm by (x + 2) cm by (x + 5) cm. Find an expression for its volume. Give your answer in expanded form.', 2,
             '(x + 2)(x + 5) = x<sup>2</sup> + 7x + 10 (1) &nbsp; x(x<sup>2</sup> + 7x + 10) = <b>(x<sup>3</sup> + 7x<sup>2</sup> + 10x) cm<sup>3</sup></b> (1)'),
            ('F3', 'Prove that the sum of the squares of two consecutive whole numbers is always odd.', 2,
             'n<sup>2</sup> + (n + 1)<sup>2</sup> = n<sup>2</sup> + n<sup>2</sup> + 2n + 1 = 2n<sup>2</sup> + 2n + 1 (1) &nbsp; = 2(n<sup>2</sup> + n) + 1, which is one more than an even number, so <b>always odd</b> (1)'),
            ('F4', 'Without a calculator, work out 7.5<sup>2</sup> &minus; 2.5<sup>2</sup>', 1,
             '(7.5 + 2.5)(7.5 &minus; 2.5) = 10 &times; 5 = <b>50</b> (1)'),
        ]),
    ],
    4: [
        ('A', [
            ('A1', 'Expand and simplify (x &minus; 9)(x &minus; 4)', 2,
             'x<sup>2</sup> &minus; 4x &minus; 9x + 36 (1) &nbsp; = <b>x<sup>2</sup> &minus; 13x + 36</b> (1)'),
            ('A2', 'Expand and simplify (5 &minus; x)(3 + x)', 2,
             '15 + 5x &minus; 3x &minus; x<sup>2</sup> (1) &nbsp; = <b>15 + 2x &minus; x<sup>2</sup></b> (1)'),
            ('A3', 'Expand and simplify (3x &minus; 2y)<sup>2</sup>', 2,
             '9x<sup>2</sup> &minus; 6xy &minus; 6xy + 4y<sup>2</sup> (1) &nbsp; = <b>9x<sup>2</sup> &minus; 12xy + 4y<sup>2</sup></b> (1)'),
            ('A4', 'Expand and simplify (2x + 1)(x &minus; 3) &minus; (x &minus; 2)<sup>2</sup>', 2,
             '(2x<sup>2</sup> &minus; 5x &minus; 3) &minus; (x<sup>2</sup> &minus; 4x + 4) (1) &nbsp; = <b>x<sup>2</sup> &minus; x &minus; 7</b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (x + 5)(x &minus; 5)(x + 2)', 3,
             '(x + 5)(x &minus; 5) = x<sup>2</sup> &minus; 25 (1) &nbsp; (x<sup>2</sup> &minus; 25)(x + 2), with at least 3 of the 4 terms correct (1) '
             '&nbsp; = <b>x<sup>3</sup> + 2x<sup>2</sup> &minus; 25x &minus; 50</b> (1)'),
            ('B2', 'Expand and simplify (3x &minus; 1)(x + 2)<sup>2</sup>', 3,
             '(x + 2)<sup>2</sup> = x<sup>2</sup> + 4x + 4 (1) &nbsp; (3x &minus; 1)(x<sup>2</sup> + 4x + 4) = 3x<sup>3</sup> + 12x<sup>2</sup> + 12x &minus; x<sup>2</sup> &minus; 4x &minus; 4 (1) '
             '&nbsp; = <b>3x<sup>3</sup> + 11x<sup>2</sup> + 8x &minus; 4</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> &minus; 16x + 63', 2,
             'Multiply to 63, add to &minus;16: &minus;7 and &minus;9 (1) &nbsp; <b>(x &minus; 7)(x &minus; 9)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> + 5x &minus; 84', 2,
             'Multiply to &minus;84, add to 5: 12 and &minus;7 (1) &nbsp; <b>(x + 12)(x &minus; 7)</b> (1)'),
            ('C3', 'Factorise 4x<sup>2</sup> &minus; 1', 1,
             '<b>(2x + 1)(2x &minus; 1)</b> (1)'),
            ('C4', 'Factorise fully x<sup>4</sup> &minus; 81', 2,
             '(x<sup>2</sup> + 9)(x<sup>2</sup> &minus; 9) (1) &nbsp; = <b>(x<sup>2</sup> + 9)(x + 3)(x &minus; 3)</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 6x<sup>2</sup> + x &minus; 2', 2,
             '6 &times; &minus;2 = &minus;12; numbers: 4 and &minus;3, so 6x<sup>2</sup> + 4x &minus; 3x &minus; 2 = 2x(3x + 2) &minus; 1(3x + 2) (1) &nbsp; <b>(2x &minus; 1)(3x + 2)</b> (1)'),
            ('D2', 'Factorise 10x<sup>2</sup> &minus; 17x + 3', 2,
             '10 &times; 3 = 30; numbers: &minus;15 and &minus;2, so 10x<sup>2</sup> &minus; 15x &minus; 2x + 3 = 5x(2x &minus; 3) &minus; 1(2x &minus; 3) (1) &nbsp; <b>(5x &minus; 1)(2x &minus; 3)</b> (1)'),
            ('D3', 'Factorise fully 8x<sup>2</sup> &minus; 2x &minus; 6', 2,
             '2(4x<sup>2</sup> &minus; x &minus; 3) (1) &nbsp; = <b>2(4x + 3)(x &minus; 1)</b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve 3x<sup>2</sup> &minus; 5x = 2', 3,
             '3x<sup>2</sup> &minus; 5x &minus; 2 = 0 (1) &nbsp; (3x + 1)(x &minus; 2) = 0 (1) &nbsp; <b>x = &minus;<super>1</super>&frasl;<sub>3</sub> or x = 2</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = (2x + 3)(2x &minus; 3) (1) &nbsp; denominator = (2x &minus; 3)(x + 2) (1) &nbsp; cancel (2x &minus; 3): <b>(2x + 3) / (x + 2)</b> (1)',
             ('4x<sup>2</sup> &minus; 9', '2x<sup>2</sup> + x &minus; 6')),
        ]),
        ('F', [
            ('F1', 'Write 2x<sup>2</sup> + 12x + 7 in the form a(x + b)<sup>2</sup> + c', 3,
             '2(x<sup>2</sup> + 6x) + 7 (1) &nbsp; = 2[(x + 3)<sup>2</sup> &minus; 9] + 7 (1) &nbsp; = <b>2(x + 3)<sup>2</sup> &minus; 11</b> (1)'),
            ('F2', 'n is an integer. Prove that (2n + 1)<sup>2</sup> &minus; (2n &minus; 1)<sup>2</sup> is always a multiple of 8.', 3,
             '(4n<sup>2</sup> + 4n + 1) (1) &nbsp; &minus; (4n<sup>2</sup> &minus; 4n + 1) (1) &nbsp; = 8n, which is <b>8 &times; an integer, so a multiple of 8</b> (1)'),
            ('F3', 'Without a calculator, work out 8.7<sup>2</sup> &minus; 1.3<sup>2</sup>', 1,
             '(8.7 + 1.3)(8.7 &minus; 1.3) = 10 &times; 7.4 = <b>74</b> (1)'),
        ]),
    ],
    5: [
        ('A', [
            ('A1', 'Expand and simplify (x + 6)(x + 8)', 2,
             'x<sup>2</sup> + 8x + 6x + 48 (1) &nbsp; = <b>x<sup>2</sup> + 14x + 48</b> (1)'),
            ('A2', 'Expand and simplify (x &minus; 10)(x + 4)', 2,
             'x<sup>2</sup> + 4x &minus; 10x &minus; 40 (1) &nbsp; = <b>x<sup>2</sup> &minus; 6x &minus; 40</b> (1)'),
            ('A3', 'Expand and simplify (x + 9)<sup>2</sup>', 2,
             '(x + 9)(x + 9) = x<sup>2</sup> + 9x + 9x + 81 (1) &nbsp; = <b>x<sup>2</sup> + 18x + 81</b> (1)'),
            ('A4', 'Expand and simplify (5x &minus; 2)(2x + 3)', 2,
             '10x<sup>2</sup> + 15x &minus; 4x &minus; 6 (1) &nbsp; = <b>10x<sup>2</sup> + 11x &minus; 6</b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (x + 4)(x &minus; 3)(x + 1)', 3,
             '(x + 4)(x &minus; 3) = x<sup>2</sup> + x &minus; 12 (1) &nbsp; (x<sup>2</sup> + x &minus; 12)(x + 1) = x<sup>3</sup> + x<sup>2</sup> + x<sup>2</sup> + x &minus; 12x &minus; 12 (1) '
             '&nbsp; = <b>x<sup>3</sup> + 2x<sup>2</sup> &minus; 11x &minus; 12</b> (1)'),
            ('B2', 'Expand and simplify (2x + 3)(x &minus; 1)(x + 5)', 3,
             '(2x + 3)(x &minus; 1) = 2x<sup>2</sup> + x &minus; 3 (1) &nbsp; (2x<sup>2</sup> + x &minus; 3)(x + 5) = 2x<sup>3</sup> + 10x<sup>2</sup> + x<sup>2</sup> + 5x &minus; 3x &minus; 15 (1) '
             '&nbsp; = <b>2x<sup>3</sup> + 11x<sup>2</sup> + 2x &minus; 15</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> + 11x + 24', 2,
             'Multiply to 24, add to 11: 3 and 8 (1) &nbsp; <b>(x + 3)(x + 8)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> &minus; 8x &minus; 33', 2,
             'Multiply to &minus;33, add to &minus;8: &minus;11 and 3 (1) &nbsp; <b>(x &minus; 11)(x + 3)</b> (1)'),
            ('C3', 'Factorise x<sup>2</sup> &minus; 121', 1,
             'Difference of two squares: <b>(x + 11)(x &minus; 11)</b> (1)'),
            ('C4', 'Factorise fully 3x<sup>2</sup> &minus; 27x + 60', 2,
             '3(x<sup>2</sup> &minus; 9x + 20) (1) &nbsp; = <b>3(x &minus; 4)(x &minus; 5)</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 2x<sup>2</sup> + 11x + 12', 2,
             '2 &times; 12 = 24; numbers: 8 and 3, so 2x<sup>2</sup> + 8x + 3x + 12 = 2x(x + 4) + 3(x + 4) (1) &nbsp; <b>(2x + 3)(x + 4)</b> (1)'),
            ('D2', 'Factorise 3x<sup>2</sup> &minus; 7x &minus; 6', 2,
             '3 &times; &minus;6 = &minus;18; numbers: &minus;9 and 2, so 3x<sup>2</sup> &minus; 9x + 2x &minus; 6 = 3x(x &minus; 3) + 2(x &minus; 3) (1) &nbsp; <b>(3x + 2)(x &minus; 3)</b> (1)'),
            ('D3', 'Factorise fully 6x<sup>2</sup> &minus; 3x &minus; 30', 2,
             '3(2x<sup>2</sup> &minus; x &minus; 10) (1) &nbsp; = <b>3(2x &minus; 5)(x + 2)</b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve x<sup>2</sup> + 3x &minus; 40 = 0', 3,
             '(x + 8)(x &minus; 5) = 0 (1) &nbsp; x + 8 = 0 or x &minus; 5 = 0 (1) &nbsp; <b>x = &minus;8 or x = 5</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = (x + 5)(x &minus; 5) (1) &nbsp; denominator = (x + 5)(x &minus; 3) (1) &nbsp; cancel (x + 5): <b>(x &minus; 5) / (x &minus; 3)</b> (1)',
             ('x<sup>2</sup> &minus; 25', 'x<sup>2</sup> + 2x &minus; 15')),
        ]),
        ('F', [
            ('F1', '(a) Write x<sup>2</sup> &minus; 10x + 18 in the form (x + a)<sup>2</sup> + b. &nbsp; '
                   '(b) Hence write down the coordinates of the turning point of y = x<sup>2</sup> &minus; 10x + 18.', 3,
             '(a) (x &minus; 5)<sup>2</sup> = x<sup>2</sup> &minus; 10x + 25 (1) &nbsp; so x<sup>2</sup> &minus; 10x + 18 = <b>(x &minus; 5)<sup>2</sup> &minus; 7</b> (1)<br/>'
             '(b) <b>(5, &minus;7)</b> (1)'),
            ('F2', 'n is an integer. Prove that (n + 3)<sup>2</sup> &minus; (n + 1)<sup>2</sup> is always a multiple of 4.', 3,
             '(n<sup>2</sup> + 6n + 9) &minus; (n<sup>2</sup> + 2n + 1) (1) &nbsp; = 4n + 8 (1) &nbsp; = 4(n + 2), which is <b>4 &times; an integer, so a multiple of 4</b> (1)'),
            ('F3', 'Without a calculator, work out 65<sup>2</sup> &minus; 35<sup>2</sup>', 1,
             '(65 + 35)(65 &minus; 35) = 100 &times; 30 = <b>3000</b> (1)'),
        ]),
    ],
    6: [
        ('A', [
            ('A1', 'Expand and simplify (x + 5)(x + 12)', 2,
             'x<sup>2</sup> + 12x + 5x + 60 (1) &nbsp; = <b>x<sup>2</sup> + 17x + 60</b> (1)'),
            ('A2', 'Expand and simplify (x &minus; 3)(x &minus; 11)', 2,
             'x<sup>2</sup> &minus; 11x &minus; 3x + 33 (1) &nbsp; = <b>x<sup>2</sup> &minus; 14x + 33</b> (1)'),
            ('A3', 'Expand and simplify (3x &minus; 4)<sup>2</sup>', 2,
             '(3x &minus; 4)(3x &minus; 4) = 9x<sup>2</sup> &minus; 12x &minus; 12x + 16 (1) &nbsp; = <b>9x<sup>2</sup> &minus; 24x + 16</b> (1)'),
            ('A4', 'Fill in the two missing numbers: (x + 7)(x &minus; ___ ) = x<sup>2</sup> + 2x &minus; ___', 2,
             '7 &minus; ? = 2, so the first missing number is <b>5</b> (1) &nbsp; 7 &times; 5 = 35, so the second is <b>35</b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (x &minus; 3)(x &minus; 2)(x + 6)', 3,
             '(x &minus; 3)(x &minus; 2) = x<sup>2</sup> &minus; 5x + 6 (1) &nbsp; (x<sup>2</sup> &minus; 5x + 6)(x + 6) = x<sup>3</sup> + 6x<sup>2</sup> &minus; 5x<sup>2</sup> &minus; 30x + 6x + 36 (1) '
             '&nbsp; = <b>x<sup>3</sup> + x<sup>2</sup> &minus; 24x + 36</b> (1)'),
            ('B2', 'Expand and simplify (x &minus; 3)<sup>3</sup>', 3,
             '(x &minus; 3)<sup>2</sup> = x<sup>2</sup> &minus; 6x + 9 (1) &nbsp; (x<sup>2</sup> &minus; 6x + 9)(x &minus; 3) = x<sup>3</sup> &minus; 3x<sup>2</sup> &minus; 6x<sup>2</sup> + 18x + 9x &minus; 27 (1) '
             '&nbsp; = <b>x<sup>3</sup> &minus; 9x<sup>2</sup> + 27x &minus; 27</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> + 3x &minus; 54', 2,
             'Multiply to &minus;54, add to 3: 9 and &minus;6 (1) &nbsp; <b>(x + 9)(x &minus; 6)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> &minus; 17x + 72', 2,
             'Multiply to 72, add to &minus;17: &minus;8 and &minus;9 (1) &nbsp; <b>(x &minus; 8)(x &minus; 9)</b> (1)'),
            ('C3', 'Factorise 16x<sup>2</sup> &minus; 25', 1,
             '(4x)<sup>2</sup> &minus; 5<sup>2</sup> = <b>(4x + 5)(4x &minus; 5)</b> (1)'),
            ('C4', 'Factorise fully 7x<sup>2</sup> &minus; 7', 2,
             '7(x<sup>2</sup> &minus; 1) (1) &nbsp; = <b>7(x + 1)(x &minus; 1)</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 2x<sup>2</sup> &minus; 9x + 10', 2,
             '2 &times; 10 = 20; numbers: &minus;4 and &minus;5, so 2x<sup>2</sup> &minus; 4x &minus; 5x + 10 = 2x(x &minus; 2) &minus; 5(x &minus; 2) (1) &nbsp; <b>(2x &minus; 5)(x &minus; 2)</b> (1)'),
            ('D2', 'Factorise 4x<sup>2</sup> + 4x &minus; 3', 2,
             '4 &times; &minus;3 = &minus;12; numbers: 6 and &minus;2, so 4x<sup>2</sup> + 6x &minus; 2x &minus; 3 = 2x(2x + 3) &minus; 1(2x + 3) (1) &nbsp; <b>(2x &minus; 1)(2x + 3)</b> (1)'),
            ('D3', 'Factorise 9x<sup>2</sup> &minus; 12x + 4', 2,
             '9 &times; 4 = 36; numbers: &minus;6 and &minus;6, so 9x<sup>2</sup> &minus; 6x &minus; 6x + 4 = 3x(3x &minus; 2) &minus; 2(3x &minus; 2) (1) &nbsp; <b>(3x &minus; 2)<sup>2</sup></b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve x<sup>2</sup> + 7x = 18', 3,
             'x<sup>2</sup> + 7x &minus; 18 = 0 (1) &nbsp; (x + 9)(x &minus; 2) = 0 (1) &nbsp; <b>x = &minus;9 or x = 2</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = (2x &minus; 1)(x + 3) (1) &nbsp; denominator = (2x + 1)(2x &minus; 1) (1) &nbsp; cancel (2x &minus; 1): <b>(x + 3) / (2x + 1)</b> (1)',
             ('2x<sup>2</sup> + 5x &minus; 3', '4x<sup>2</sup> &minus; 1')),
        ]),
        ('F', [
            ('F1', 'A rectangle is (2x + 3) cm long and (x &minus; 1) cm wide. Its area is 18 cm<sup>2</sup>.<br/>'
                   '(a) Show that 2x<sup>2</sup> + x &minus; 21 = 0. &nbsp; (b) Solve the equation and find the perimeter of the rectangle.', 4,
             '(a) (2x + 3)(x &minus; 1) = 2x<sup>2</sup> + x &minus; 3 (1) &nbsp; 2x<sup>2</sup> + x &minus; 3 = 18, so 2x<sup>2</sup> + x &minus; 21 = 0 (1)<br/>'
             '(b) (2x + 7)(x &minus; 3) = 0 so x = 3 or x = &minus;3.5; a length can&rsquo;t be negative, so x = 3 (1) &nbsp; '
             'the rectangle is 9 cm by 2 cm, so <b>perimeter = 22 cm</b> (1)'),
            ('F2', 'Show that (2x + 3)<sup>2</sup> &minus; (2x &minus; 3)<sup>2</sup> = 24x for every value of x', 2,
             '(4x<sup>2</sup> + 12x + 9) &minus; (4x<sup>2</sup> &minus; 12x + 9) (1) &nbsp; = 4x<sup>2</sup> + 12x + 9 &minus; 4x<sup>2</sup> + 12x &minus; 9 = <b>24x</b> (1)'),
            ('F3', 'Without a calculator, work out 9.6<sup>2</sup> &minus; 0.4<sup>2</sup>', 1,
             '(9.6 + 0.4)(9.6 &minus; 0.4) = 10 &times; 9.2 = <b>92</b> (1)'),
        ]),
    ],
    7: [
        ('A', [
            ('A1', 'Expand and simplify (x + 7)(x &minus; 2)', 2,
             'x<sup>2</sup> &minus; 2x + 7x &minus; 14 (1) &nbsp; = <b>x<sup>2</sup> + 5x &minus; 14</b> (1)'),
            ('A2', 'Expand and simplify (x &minus; 1)(x &minus; 12)', 2,
             'x<sup>2</sup> &minus; 12x &minus; x + 12 (1) &nbsp; = <b>x<sup>2</sup> &minus; 13x + 12</b> (1)'),
            ('A3', 'Expand and simplify (2x &minus; 7)(3x &minus; 1)', 2,
             '6x<sup>2</sup> &minus; 2x &minus; 21x + 7 (1) &nbsp; = <b>6x<sup>2</sup> &minus; 23x + 7</b> (1)'),
            ('A4', 'A square has sides of length (2x + 3) cm. Find an expression for its area. Give your answer in expanded form.', 2,
             '(2x + 3)(2x + 3) = 4x<sup>2</sup> + 6x + 6x + 9 (1) &nbsp; = <b>(4x<sup>2</sup> + 12x + 9) cm<sup>2</sup></b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (x + 1)(x + 4)(x &minus; 5)', 3,
             '(x + 1)(x + 4) = x<sup>2</sup> + 5x + 4 (1) &nbsp; (x<sup>2</sup> + 5x + 4)(x &minus; 5) = x<sup>3</sup> &minus; 5x<sup>2</sup> + 5x<sup>2</sup> &minus; 25x + 4x &minus; 20 (1) '
             '&nbsp; = <b>x<sup>3</sup> &minus; 21x &minus; 20</b> (1)'),
            ('B2', 'Expand and simplify (x + 3)(2x &minus; 1)<sup>2</sup>', 3,
             '(2x &minus; 1)<sup>2</sup> = 4x<sup>2</sup> &minus; 4x + 1 (1) &nbsp; (4x<sup>2</sup> &minus; 4x + 1)(x + 3) = 4x<sup>3</sup> + 12x<sup>2</sup> &minus; 4x<sup>2</sup> &minus; 12x + x + 3 (1) '
             '&nbsp; = <b>4x<sup>3</sup> + 8x<sup>2</sup> &minus; 11x + 3</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> + 14x + 45', 2,
             'Multiply to 45, add to 14: 5 and 9 (1) &nbsp; <b>(x + 5)(x + 9)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> &minus; 2x &minus; 63', 2,
             'Multiply to &minus;63, add to &minus;2: &minus;9 and 7 (1) &nbsp; <b>(x &minus; 9)(x + 7)</b> (1)'),
            ('C3', 'Factorise 49 &minus; 4x<sup>2</sup>', 1,
             '7<sup>2</sup> &minus; (2x)<sup>2</sup> = <b>(7 + 2x)(7 &minus; 2x)</b> (1)'),
            ('C4', 'x<sup>2</sup> + bx &minus; 20 factorises to (x &minus; 4)(x + a). Find the values of a and b.', 2,
             '&minus;4 &times; a = &minus;20 so <b>a = 5</b> (1) &nbsp; b = &minus;4 + 5, so <b>b = 1</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 3x<sup>2</sup> + 14x + 8', 2,
             '3 &times; 8 = 24; numbers: 12 and 2, so 3x<sup>2</sup> + 12x + 2x + 8 = 3x(x + 4) + 2(x + 4) (1) &nbsp; <b>(3x + 2)(x + 4)</b> (1)'),
            ('D2', 'Factorise 5x<sup>2</sup> &minus; 12x + 4', 2,
             '5 &times; 4 = 20; numbers: &minus;10 and &minus;2, so 5x<sup>2</sup> &minus; 10x &minus; 2x + 4 = 5x(x &minus; 2) &minus; 2(x &minus; 2) (1) &nbsp; <b>(5x &minus; 2)(x &minus; 2)</b> (1)'),
            ('D3', 'Factorise fully 12x<sup>2</sup> + 22x &minus; 4', 2,
             '2(6x<sup>2</sup> + 11x &minus; 2) (1) &nbsp; = <b>2(6x &minus; 1)(x + 2)</b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve 2x<sup>2</sup> &minus; 7x + 3 = 0', 3,
             '(2x &minus; 1)(x &minus; 3) = 0 (1) &nbsp; 2x &minus; 1 = 0 or x &minus; 3 = 0 (1) &nbsp; <b>x = 0.5 or x = 3</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = (x &minus; 5)(x + 2) (1) &nbsp; denominator = (x + 2)(x &minus; 2) (1) &nbsp; cancel (x + 2): <b>(x &minus; 5) / (x &minus; 2)</b> (1)',
             ('x<sup>2</sup> &minus; 3x &minus; 10', 'x<sup>2</sup> &minus; 4')),
        ]),
        ('F', [
            ('F1', '(a) Write x<sup>2</sup> + 6x &minus; 4 in the form (x + a)<sup>2</sup> + b. &nbsp; '
                   '(b) Hence write down the minimum value of x<sup>2</sup> + 6x &minus; 4.', 3,
             '(a) (x + 3)<sup>2</sup> = x<sup>2</sup> + 6x + 9 (1) &nbsp; so x<sup>2</sup> + 6x &minus; 4 = <b>(x + 3)<sup>2</sup> &minus; 13</b> (1)<br/>'
             '(b) a square can&rsquo;t be negative, so the <b>minimum value is &minus;13</b> (when x = &minus;3) (1)'),
            ('F2', 'Prove that if you multiply two consecutive even numbers and add 1, the answer is always a square number.', 3,
             'Let the numbers be 2n and 2n + 2 (1) &nbsp; 2n(2n + 2) + 1 = 4n<sup>2</sup> + 4n + 1 (1) &nbsp; = (2n + 1)<sup>2</sup>, which is <b>a square number</b> (1)'),
            ('F3', 'Without a calculator, work out 76<sup>2</sup> &minus; 24<sup>2</sup>', 1,
             '(76 + 24)(76 &minus; 24) = 100 &times; 52 = <b>5200</b> (1)'),
        ]),
    ],
    8: [
        ('A', [
            ('A1', 'Expand and simplify (x + 10)(x + 3)', 2,
             'x<sup>2</sup> + 3x + 10x + 30 (1) &nbsp; = <b>x<sup>2</sup> + 13x + 30</b> (1)'),
            ('A2', 'Expand and simplify (x &minus; 4)(x + 13)', 2,
             'x<sup>2</sup> + 13x &minus; 4x &minus; 52 (1) &nbsp; = <b>x<sup>2</sup> + 9x &minus; 52</b> (1)'),
            ('A3', 'Expand and simplify (x &minus; 2y)(x + 5y)', 2,
             'x<sup>2</sup> + 5xy &minus; 2xy &minus; 10y<sup>2</sup> (1) &nbsp; = <b>x<sup>2</sup> + 3xy &minus; 10y<sup>2</sup></b> (1)'),
            ('A4', 'Expand and simplify 3(x + 2)<sup>2</sup> &minus; (x + 4)(x &minus; 1)', 2,
             '(3x<sup>2</sup> + 12x + 12) &minus; (x<sup>2</sup> + 3x &minus; 4) (1) &nbsp; = <b>2x<sup>2</sup> + 9x + 16</b> (1)'),
        ]),
        ('B', [
            ('B1', 'Expand and simplify (x &minus; 4)(x + 1)(x + 3)', 3,
             '(x &minus; 4)(x + 1) = x<sup>2</sup> &minus; 3x &minus; 4 (1) &nbsp; (x<sup>2</sup> &minus; 3x &minus; 4)(x + 3) = x<sup>3</sup> + 3x<sup>2</sup> &minus; 3x<sup>2</sup> &minus; 9x &minus; 4x &minus; 12 (1) '
             '&nbsp; = <b>x<sup>3</sup> &minus; 13x &minus; 12</b> (1)'),
            ('B2', 'Expand and simplify (2x + 1)<sup>3</sup>', 3,
             '(2x + 1)<sup>2</sup> = 4x<sup>2</sup> + 4x + 1 (1) &nbsp; (4x<sup>2</sup> + 4x + 1)(2x + 1) = 8x<sup>3</sup> + 4x<sup>2</sup> + 8x<sup>2</sup> + 4x + 2x + 1 (1) '
             '&nbsp; = <b>8x<sup>3</sup> + 12x<sup>2</sup> + 6x + 1</b> (1)'),
        ]),
        ('C', [
            ('C1', 'Factorise x<sup>2</sup> + 10x + 21', 2,
             'Multiply to 21, add to 10: 3 and 7 (1) &nbsp; <b>(x + 3)(x + 7)</b> (1)'),
            ('C2', 'Factorise x<sup>2</sup> &minus; 9x &minus; 36', 2,
             'Multiply to &minus;36, add to &minus;9: &minus;12 and 3 (1) &nbsp; <b>(x &minus; 12)(x + 3)</b> (1)'),
            ('C3', 'Factorise 25x<sup>2</sup> &minus; 64', 1,
             '(5x)<sup>2</sup> &minus; 8<sup>2</sup> = <b>(5x + 8)(5x &minus; 8)</b> (1)'),
            ('C4', 'Factorise fully 2x<sup>3</sup> &minus; 18x', 2,
             '2x(x<sup>2</sup> &minus; 9) (1) &nbsp; = <b>2x(x + 3)(x &minus; 3)</b> (1)'),
        ]),
        ('D', [
            ('D1', 'Factorise 2x<sup>2</sup> + 3x &minus; 20', 2,
             '2 &times; &minus;20 = &minus;40; numbers: 8 and &minus;5, so 2x<sup>2</sup> + 8x &minus; 5x &minus; 20 = 2x(x + 4) &minus; 5(x + 4) (1) &nbsp; <b>(2x &minus; 5)(x + 4)</b> (1)'),
            ('D2', 'Factorise 3x<sup>2</sup> &minus; 17x + 10', 2,
             '3 &times; 10 = 30; numbers: &minus;15 and &minus;2, so 3x<sup>2</sup> &minus; 15x &minus; 2x + 10 = 3x(x &minus; 5) &minus; 2(x &minus; 5) (1) &nbsp; <b>(3x &minus; 2)(x &minus; 5)</b> (1)'),
            ('D3', 'Factorise 6x<sup>2</sup> &minus; 13x &minus; 5', 2,
             '6 &times; &minus;5 = &minus;30; numbers: &minus;15 and 2, so 6x<sup>2</sup> &minus; 15x + 2x &minus; 5 = 3x(2x &minus; 5) + 1(2x &minus; 5) (1) &nbsp; <b>(3x + 1)(2x &minus; 5)</b> (1)'),
        ]),
        ('E', [
            ('E1', 'Solve x(x + 4) = 21', 3,
             'x<sup>2</sup> + 4x &minus; 21 = 0 (1) &nbsp; (x + 7)(x &minus; 3) = 0 (1) &nbsp; <b>x = &minus;7 or x = 3</b> (1)'),
            ('E2', 'Simplify fully', 3,
             'Numerator = 3(x + 2)(x &minus; 2) (1) &nbsp; denominator = (x + 3)(x &minus; 2) (1) &nbsp; cancel (x &minus; 2): <b>3(x + 2) / (x + 3)</b> (1)',
             ('3x<sup>2</sup> &minus; 12', 'x<sup>2</sup> + x &minus; 6')),
        ]),
        ('F', [
            ('F1', 'Write 3x<sup>2</sup> &minus; 12x + 5 in the form a(x + b)<sup>2</sup> + c', 3,
             '3(x<sup>2</sup> &minus; 4x) + 5 (1) &nbsp; = 3[(x &minus; 2)<sup>2</sup> &minus; 4] + 5 (1) &nbsp; = <b>3(x &minus; 2)<sup>2</sup> &minus; 7</b> (1)'),
            ('F2', 'A square lawn has sides of x metres. A path 2 m wide goes all the way round the outside of the lawn. '
                   'Show that the area of the path is (8x + 16) m<sup>2</sup>.', 3,
             'The outer square has sides of (x + 4) m (1) &nbsp; (x + 4)<sup>2</sup> = x<sup>2</sup> + 8x + 16 (1) &nbsp; '
             'path = (x<sup>2</sup> + 8x + 16) &minus; x<sup>2</sup> = <b>(8x + 16) m<sup>2</sup></b> (1)'),
            ('F3', 'Without a calculator, work out 12.5<sup>2</sup> &minus; 7.5<sup>2</sup>', 1,
             '(12.5 + 7.5)(12.5 &minus; 7.5) = 20 &times; 5 = <b>100</b> (1)'),
        ]),
    ],
}


def check_marks():
    for n, sections in TESTS.items():
        total = sum(item[2] for _, qs in sections for item in qs)
        assert total == TOTAL, f'Test {n} adds up to {total}, not {TOTAL}'


def build_test(n):
    doc = SimpleDocTemplate(f'quadratics_test{n}.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = header(f'Practice test {n} &middot; {TOTAL} marks &middot; Higher tier &middot; non-calculator')
    s.append(name_table())
    s.append(Spacer(1, 8))
    for key, qs in TESTS[n]:
        s.append(Paragraph(SECTIONS[key], styles['h2']))
        for item in qs:
            qid, text, marks = item[0], item[1], item[2]
            block = [Paragraph(f'<b>{qid}.</b> {text}', styles['qtext'])]
            if len(item) > 4:
                block.append(frac(*item[4]))
            block.append(Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']))
            block.append(Spacer(1, WORKING_SPACE_PER_MARK * marks))
            s.append(KeepTogether(block))
    doc.build(s)


def build_answers(n):
    doc = SimpleDocTemplate(f'quadratics_test{n}_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = header(f'Practice test {n} &mdash; answer sheet &middot; {TOTAL} marks')
    for key, qs in TESTS[n]:
        s.append(Paragraph(SECTIONS[key], styles['h2']))
        for item in qs:
            s.append(Paragraph(f'<b>{item[0]}.</b> {item[3]}', styles['ans']))
    s.append(marking_note())
    doc.build(s)


if __name__ == '__main__':
    check_marks()
    for n in TESTS:
        build_test(n)
        build_answers(n)
    print('Built', len(TESTS) * 2, 'PDFs')
