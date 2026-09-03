# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Pythagoras' Theorem & Trigonometry (GCSE Maths, Geometry & Measures)."""

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


# NOTE: Helvetica's base encoding does not render Unicode superscript/subscript
# glyphs (e.g. U+00B2 for the "²" character can show as a black box in some
# viewers). Use reportlab's <sup>/<sub> paragraph tags with plain digits instead,
# e.g. 'a<sup>2</sup>' rather than a literal superscript-2 character.

# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('pythagoras_trig_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry',
                 'Quick reference sheet &middot; GCSE Maths, Geometry &amp; Measures &middot; keep handy for revision')

    s.append(Paragraph('1. Pythagoras&rsquo; theorem', styles['h2']))
    s.append(Paragraph('For any right-angled triangle, with hypotenuse c (the longest side, opposite the right angle) and shorter sides a and b:', styles['body']))
    s.append(Paragraph('a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>', styles['bodyb']))
    s.append(Paragraph('Finding the <b>hypotenuse</b>: c = &radic;(a<sup>2</sup> + b<sup>2</sup>) &mdash; add the squares, then square root. Example: a = 6, b = 8 &rarr; c = &radic;(36+64) = &radic;100 = <b>10</b>.', styles['body']))
    s.append(Paragraph('Finding a <b>shorter side</b>: a = &radic;(c<sup>2</sup> &minus; b<sup>2</sup>) &mdash; subtract the squares, then square root. Example: c = 13, b = 5 &rarr; a = &radic;(169&minus;25) = &radic;144 = <b>12</b>.', styles['body']))

    s.append(Paragraph('2. Right-angled trigonometry: SOH CAH TOA', styles['h2']))
    s.append(Paragraph('Relative to an angle &#952; in a right-angled triangle: the <b>hypotenuse</b> is the longest side (opposite the right angle); the <b>opposite</b> side is across from &#952;; the <b>adjacent</b> side is next to &#952; (not the hypotenuse).', styles['body']))
    s.append(table([
        [headcell('Rule'), headcell('Ratio'), headcell('Use when you know/want&hellip;')],
        [cell('SOH'), cell('sin &#952; = opp &divide; hyp'), cell('opposite &amp; hypotenuse')],
        [cell('CAH'), cell('cos &#952; = adj &divide; hyp'), cell('adjacent &amp; hypotenuse')],
        [cell('TOA'), cell('tan &#952; = opp &divide; adj'), cell('opposite &amp; adjacent')],
    ], col_widths=[25 * mm, 60 * mm, 65 * mm]))

    s.append(Paragraph('3. Finding a missing side', styles['h2']))
    s.append(Paragraph('Rearrange the ratio to make the unknown side the subject. If the unknown is on top (opp or adj), <b>multiply</b> by the trig ratio. If the unknown is on the bottom (hyp, or adj in TOA), <b>divide</b>.', styles['body']))
    s.append(Paragraph('Example: angle 35&#176;, hypotenuse 9 cm, find the opposite x. sin 35&#176; = x &divide; 9 &rarr; x = 9 &times; sin 35&#176; = <b>5.2 cm</b> (1 d.p.).', styles['body']))

    s.append(Paragraph('4. Finding a missing angle', styles['h2']))
    s.append(Paragraph('Use the inverse trig function (sin<sup>-1</sup>, cos<sup>-1</sup>, tan<sup>-1</sup>) to find &#952; from a ratio of two known sides.', styles['body']))
    s.append(table([
        [headcell('Known sides'), headcell('Formula')],
        [cell('opposite &amp; hypotenuse'), cell('&#952; = sin<sup>-1</sup>(opp &divide; hyp)')],
        [cell('adjacent &amp; hypotenuse'), cell('&#952; = cos<sup>-1</sup>(adj &divide; hyp)')],
        [cell('opposite &amp; adjacent'), cell('&#952; = tan<sup>-1</sup>(opp &divide; adj)')],
    ], col_widths=[65 * mm, 85 * mm]))
    s.append(Paragraph('Example: opposite 7 cm, hypotenuse 11 cm. sin &#952; = 7 &divide; 11 = 0.6364 &rarr; &#952; = sin<sup>-1</sup>(0.6364) = <b>39.5&#176;</b> (1 d.p.).', styles['body']))

    s.append(Paragraph('5. Common mistakes', styles['h2']))
    s.append(Paragraph('Mixing up which side is the hypotenuse &mdash; it is always the longest side, opposite the right angle, never adjacent to it.', styles['bullet']))
    s.append(Paragraph('Labelling opposite/adjacent relative to the wrong angle &mdash; always check which angle is &#952; first.', styles['bullet']))
    s.append(Paragraph('Forgetting to use the inverse function (sin<sup>-1</sup> etc.) when finding an angle, rather than a side.', styles['bullet']))
    s.append(Paragraph('Calculator left in radian mode instead of degree mode &mdash; always check before using sin/cos/tan.', styles['bullet']))
    s.append(Paragraph('Adding instead of subtracting (or vice versa) when rearranging a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup> to find a shorter side.', styles['bullet']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('pythagoras_trig_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Test &middot; 27 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 27'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s += q('A1', 'A right-angled triangle has shorter sides of 5 cm and 12 cm. Find the length of the hypotenuse.', 2)
    s += q('A2', 'A right-angled triangle has a hypotenuse of 15 cm and one shorter side of 9 cm. Find the length of the other shorter side.', 3)
    s += q('A3', 'A rectangle measures 7 cm by 24 cm. Find the length of its diagonal.', 2)

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s += q('B1', 'In a right-angled triangle, which side is always the hypotenuse?', 1)
    s += q('B2', 'Write down the SOH CAH TOA formula you would use to find the opposite side if you know the hypotenuse and the angle.', 1)
    s += q('B3', 'Write down the SOH CAH TOA formula you would use to find an angle if you know the opposite and adjacent sides.', 1)

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s += q('C1', 'A right-angled triangle has an angle of 42&#176; and a hypotenuse of 10 cm. Find the length of the side opposite the angle, to 1 decimal place.', 3)
    s += q('C2', 'A right-angled triangle has an angle of 55&#176; and an adjacent side of 8 cm. Find the length of the hypotenuse, to 1 decimal place.', 2)
    s += q('C3', 'A right-angled triangle has an angle of 33&#176; and an adjacent side of 6 cm. Find the length of the side opposite the angle, to 1 decimal place.', 2)

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s += q('D1', 'A right-angled triangle has an opposite side of 6 cm and a hypotenuse of 13 cm. Find the angle, to 1 decimal place.', 2)
    s += q('D2', 'A right-angled triangle has an adjacent side of 5 cm and an opposite side of 9 cm. Find the angle, to 1 decimal place.', 3)

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s += q('E1', 'A ladder rests against a vertical wall. The foot of the ladder is 1.8 m from the wall and the ladder is 4.5 m long. Calculate how far up the wall the ladder reaches, to 1 decimal place.', 2)
    s += q('E2', 'A flagpole casts a shadow. A wire from the top of the flagpole to a point on the ground 6 m from its base makes an angle of 58&#176; with the ground. Calculate the height of the flagpole, to 1 decimal place.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('pythagoras_trig_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s.append(Paragraph('A1. c<sup>2</sup> = 5<sup>2</sup> + 12<sup>2</sup> = 25 + 144 = 169 (1) &nbsp; c = &radic;169 = <b>13 cm</b> (1)', styles['ans']))
    s.append(Paragraph('A2. a<sup>2</sup> = 15<sup>2</sup> &minus; 9<sup>2</sup> (1) &nbsp; = 225 &minus; 81 = 144 (1) &nbsp; a = &radic;144 = <b>12 cm</b> (1)', styles['ans']))
    s.append(Paragraph('A3. diagonal<sup>2</sup> = 7<sup>2</sup> + 24<sup>2</sup> = 49 + 576 = 625 (1) &nbsp; diagonal = &radic;625 = <b>25 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s.append(Paragraph('B1. The <b>longest side</b>, opposite the right angle (1)', styles['ans']))
    s.append(Paragraph('B2. <b>SOH</b>: opposite = hypotenuse &times; sin &#952; (1)', styles['ans']))
    s.append(Paragraph('B3. <b>TOA</b>: &#952; = tan<sup>-1</sup>(opposite &divide; adjacent) (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s.append(Paragraph('C1. sin 42&#176; = x &divide; 10 (1) &nbsp; x = 10 &times; sin 42&#176; (1) &nbsp; = <b>6.7 cm</b> (1)', styles['ans']))
    s.append(Paragraph('C2. cos 55&#176; = 8 &divide; h &rarr; h = 8 &divide; cos 55&#176; (1) &nbsp; = <b>13.9 cm</b> (1)', styles['ans']))
    s.append(Paragraph('C3. tan 33&#176; = x &divide; 6 &rarr; x = 6 &times; tan 33&#176; (1) &nbsp; = <b>3.9 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s.append(Paragraph('D1. sin &#952; = 6 &divide; 13 = 0.4615 &rarr; &#952; = sin<sup>-1</sup>(0.4615) (1) &nbsp; = <b>27.5&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('D2. tan &#952; = 9 &divide; 5 = 1.8 (1) &nbsp; &#952; = tan<sup>-1</sup>(1.8) (1) &nbsp; = <b>60.9&#176;</b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s.append(Paragraph('E1. Use Pythagoras: height<sup>2</sup> = 4.5<sup>2</sup> &minus; 1.8<sup>2</sup> = 20.25 &minus; 3.24 = 17.01 (1) &nbsp; &radic;17.01 = <b>4.1 m</b> (1)', styles['ans']))
    s.append(Paragraph('E2. tan 58&#176; = h &divide; 6 (1) &nbsp; h = 6 &times; tan 58&#176; (1) &nbsp; = <b>9.6 m</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly set-up equation or calculation even if the final answer '
        'contains a rounding or arithmetic slip. Accept any correct rounding to 1 decimal place unless a different '
        'level of accuracy is specified. Missing units on an otherwise-correct numerical answer should lose the '
        'final accuracy mark, not the method mark.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
