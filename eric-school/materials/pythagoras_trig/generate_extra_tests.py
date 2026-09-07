# -*- coding: utf-8 -*-
"""Generate three extra practice tests + answer sheets for
Pythagoras' Theorem & Trigonometry (GCSE Maths, Geometry & Measures).

Same style/section structure as the original pythagoras_trig_test.pdf
(Sections A-E, 27 marks total) but with all new numbers, for extra
practice after doing well on the original test."""

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
    'marks': ParagraphStyle('marks', fontName='Helvetica-Oblique', fontSize=9.5,
                             textColor=INK_SOFT, spaceAfter=10),
    'qtext': ParagraphStyle('qtext', fontName='Helvetica', fontSize=10.5,
                             textColor=INK, leading=15, spaceAfter=2),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=10.5,
                           textColor=INK, leading=15, spaceAfter=6),
    'note': ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=9.5,
                            textColor=INK_SOFT, leading=13, spaceBefore=14),
    'tablecell': ParagraphStyle('tablecell', fontName='Helvetica', fontSize=10,
                                 textColor=INK),
}


def hr():
    return HRFlowable(width='100%', thickness=1, color=PAPER_LINE,
                       spaceBefore=6, spaceAfter=14)


def header(title, subtitle):
    return [Paragraph(title, styles['title']), Paragraph(subtitle, styles['subtitle']), hr()]


def name_table():
    t = Table([[
        Paragraph('Name: ________________________________', styles['tablecell']),
        Paragraph('Date: ______________', styles['tablecell']),
        Paragraph('Score: _____ / 27', styles['tablecell']),
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


def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


# Each test: (A1, A2, A3, B1, B2, B3, C1, C2, C3, D1, D2, E1, E2) questions + answers
TESTS = {
    2: dict(
        a1=('A right-angled triangle has shorter sides of 9 cm and 12 cm. Find the length of the hypotenuse.', 2,
            'a<sup>2</sup> + b<sup>2</sup> = 9<sup>2</sup> + 12<sup>2</sup> = 81 + 144 = 225 (1) &nbsp; c = &radic;225 = <b>15 cm</b> (1)'),
        a2=('A right-angled triangle has a hypotenuse of 17 cm and one shorter side of 8 cm. Find the length of the other shorter side.', 3,
            'a<sup>2</sup> = 17<sup>2</sup> &minus; 8<sup>2</sup> (1) &nbsp; = 289 &minus; 64 = 225 (1) &nbsp; a = &radic;225 = <b>15 cm</b> (1)'),
        a3=('A rectangle measures 9 cm by 40 cm. Find the length of its diagonal.', 2,
            'diagonal<sup>2</sup> = 9<sup>2</sup> + 40<sup>2</sup> = 81 + 1600 = 1681 (1) &nbsp; diagonal = &radic;1681 = <b>41 cm</b> (1)'),
        b1=('In a right-angled triangle, what is the name of the side opposite the right angle?', 1,
            'The <b>hypotenuse</b> (1)'),
        b2=('Write down the SOH CAH TOA formula you would use to find the adjacent side if you know the hypotenuse and the angle.', 1,
            '<b>CAH</b>: adjacent = hypotenuse &times; cos &#952; (1)'),
        b3=('Write down the SOH CAH TOA formula you would use to find an angle if you know the opposite and hypotenuse.', 1,
            '<b>SOH</b>: &#952; = sin<sup>-1</sup>(opposite &divide; hypotenuse) (1)'),
        c1=('A right-angled triangle has an angle of 37&#176; and a hypotenuse of 12 cm. Find the length of the side opposite the angle, to 1 decimal place.', 3,
            'sin 37&#176; = x &divide; 12 (1) &nbsp; x = 12 &times; sin 37&#176; (1) &nbsp; = <b>7.2 cm</b> (1)'),
        c2=('A right-angled triangle has an angle of 62&#176; and an adjacent side of 5 cm. Find the length of the hypotenuse, to 1 decimal place.', 2,
            'cos 62&#176; = 5 &divide; h &rarr; h = 5 &divide; cos 62&#176; (1) &nbsp; = <b>10.7 cm</b> (1)'),
        c3=('A right-angled triangle has an angle of 27&#176; and an adjacent side of 9 cm. Find the length of the side opposite the angle, to 1 decimal place.', 2,
            'tan 27&#176; = x &divide; 9 &rarr; x = 9 &times; tan 27&#176; (1) &nbsp; = <b>4.6 cm</b> (1)'),
        d1=('A right-angled triangle has an opposite side of 8 cm and a hypotenuse of 17 cm. Find the angle, to 1 decimal place.', 2,
            'sin &#952; = 8 &divide; 17 = 0.4706 &rarr; &#952; = sin<sup>-1</sup>(0.4706) (1) &nbsp; = <b>28.1&#176;</b> (1)'),
        d2=('A right-angled triangle has an adjacent side of 7 cm and an opposite side of 11 cm. Find the angle, to 1 decimal place.', 3,
            'tan &#952; = 11 &divide; 7 = 1.5714 (1) &nbsp; &#952; = tan<sup>-1</sup>(1.5714) (1) &nbsp; = <b>57.5&#176;</b> (1)'),
        e1=('A ladder rests against a vertical wall. The foot of the ladder is 2.1 m from the wall and the ladder is 5.8 m long. Calculate how far up the wall the ladder reaches, to 1 decimal place.', 2,
            'Use Pythagoras: height<sup>2</sup> = 5.8<sup>2</sup> &minus; 2.1<sup>2</sup> = 33.64 &minus; 4.41 = 29.23 (1) &nbsp; &radic;29.23 = <b>5.4 m</b> (1)'),
        e2=('A wire runs from the top of a vertical pole to a point on the ground 8 m from its base, making an angle of 50&#176; with the ground. Calculate the height of the pole, to 1 decimal place.', 3,
            'tan 50&#176; = h &divide; 8 (1) &nbsp; h = 8 &times; tan 50&#176; (1) &nbsp; = <b>9.5 m</b> (1)'),
    ),
    3: dict(
        a1=('A right-angled triangle has shorter sides of 8 cm and 15 cm. Find the length of the hypotenuse.', 2,
            'a<sup>2</sup> + b<sup>2</sup> = 8<sup>2</sup> + 15<sup>2</sup> = 64 + 225 = 289 (1) &nbsp; c = &radic;289 = <b>17 cm</b> (1)'),
        a2=('A right-angled triangle has a hypotenuse of 25 cm and one shorter side of 7 cm. Find the length of the other shorter side.', 3,
            'a<sup>2</sup> = 25<sup>2</sup> &minus; 7<sup>2</sup> (1) &nbsp; = 625 &minus; 49 = 576 (1) &nbsp; a = &radic;576 = <b>24 cm</b> (1)'),
        a3=('A rectangle measures 20 cm by 21 cm. Find the length of its diagonal.', 2,
            'diagonal<sup>2</sup> = 20<sup>2</sup> + 21<sup>2</sup> = 400 + 441 = 841 (1) &nbsp; diagonal = &radic;841 = <b>29 cm</b> (1)'),
        b1=('Which SOH CAH TOA ratio links the opposite and adjacent sides (not the hypotenuse)?', 1,
            '<b>TOA</b> (1)'),
        b2=('Write down the SOH CAH TOA formula you would use to find the hypotenuse if you know the opposite side and the angle.', 1,
            '<b>SOH</b>: hypotenuse = opposite &divide; sin &#952; (1)'),
        b3=('Write down the SOH CAH TOA formula you would use to find an angle if you know the adjacent and hypotenuse.', 1,
            '<b>CAH</b>: &#952; = cos<sup>-1</sup>(adjacent &divide; hypotenuse) (1)'),
        c1=('A right-angled triangle has an angle of 48&#176; and a hypotenuse of 14 cm. Find the length of the side opposite the angle, to 1 decimal place.', 3,
            'sin 48&#176; = x &divide; 14 (1) &nbsp; x = 14 &times; sin 48&#176; (1) &nbsp; = <b>10.4 cm</b> (1)'),
        c2=('A right-angled triangle has an angle of 29&#176; and an adjacent side of 11 cm. Find the length of the hypotenuse, to 1 decimal place.', 2,
            'cos 29&#176; = 11 &divide; h &rarr; h = 11 &divide; cos 29&#176; (1) &nbsp; = <b>12.6 cm</b> (1)'),
        c3=('A right-angled triangle has an angle of 51&#176; and an adjacent side of 4 cm. Find the length of the side opposite the angle, to 1 decimal place.', 2,
            'tan 51&#176; = x &divide; 4 &rarr; x = 4 &times; tan 51&#176; (1) &nbsp; = <b>4.9 cm</b> (1)'),
        d1=('A right-angled triangle has an opposite side of 5 cm and a hypotenuse of 12 cm. Find the angle, to 1 decimal place.', 2,
            'sin &#952; = 5 &divide; 12 = 0.4167 &rarr; &#952; = sin<sup>-1</sup>(0.4167) (1) &nbsp; = <b>24.6&#176;</b> (1)'),
        d2=('A right-angled triangle has an adjacent side of 8 cm and an opposite side of 6 cm. Find the angle, to 1 decimal place.', 3,
            'tan &#952; = 6 &divide; 8 = 0.75 (1) &nbsp; &#952; = tan<sup>-1</sup>(0.75) (1) &nbsp; = <b>36.9&#176;</b> (1)'),
        e1=('A ladder rests against a vertical wall. The foot of the ladder is 1.5 m from the wall and the ladder is 4 m long. Calculate how far up the wall the ladder reaches, to 1 decimal place.', 2,
            'Use Pythagoras: height<sup>2</sup> = 4<sup>2</sup> &minus; 1.5<sup>2</sup> = 16 &minus; 2.25 = 13.75 (1) &nbsp; &radic;13.75 = <b>3.7 m</b> (1)'),
        e2=('A kite is flying on a taut string 25 m long, which makes an angle of 40&#176; with the ground. Calculate the height of the kite above the ground, to 1 decimal place.', 3,
            'sin 40&#176; = h &divide; 25 (1) &nbsp; h = 25 &times; sin 40&#176; (1) &nbsp; = <b>16.1 m</b> (1)'),
    ),
    4: dict(
        a1=('A right-angled triangle has shorter sides of 10 cm and 24 cm. Find the length of the hypotenuse.', 2,
            'a<sup>2</sup> + b<sup>2</sup> = 10<sup>2</sup> + 24<sup>2</sup> = 100 + 576 = 676 (1) &nbsp; c = &radic;676 = <b>26 cm</b> (1)'),
        a2=('A right-angled triangle has a hypotenuse of 20 cm and one shorter side of 12 cm. Find the length of the other shorter side.', 3,
            'a<sup>2</sup> = 20<sup>2</sup> &minus; 12<sup>2</sup> (1) &nbsp; = 400 &minus; 144 = 256 (1) &nbsp; a = &radic;256 = <b>16 cm</b> (1)'),
        a3=('A rectangle measures 18 cm by 24 cm. Find the length of its diagonal.', 2,
            'diagonal<sup>2</sup> = 18<sup>2</sup> + 24<sup>2</sup> = 324 + 576 = 900 (1) &nbsp; diagonal = &radic;900 = <b>30 cm</b> (1)'),
        b1=('In a right-angled triangle, what do we call the side next to angle &#952; that is not the hypotenuse?', 1,
            'The <b>adjacent</b> side (1)'),
        b2=('Write down the SOH CAH TOA formula you would use to find the opposite side if you know the adjacent side and the angle.', 1,
            '<b>TOA</b>: opposite = adjacent &times; tan &#952; (1)'),
        b3=('Write down the SOH CAH TOA formula you would use to find an angle if you know the adjacent and hypotenuse.', 1,
            '<b>CAH</b>: &#952; = cos<sup>-1</sup>(adjacent &divide; hypotenuse) (1)'),
        c1=('A right-angled triangle has an angle of 33&#176; and a hypotenuse of 16 cm. Find the length of the side opposite the angle, to 1 decimal place.', 3,
            'sin 33&#176; = x &divide; 16 (1) &nbsp; x = 16 &times; sin 33&#176; (1) &nbsp; = <b>8.7 cm</b> (1)'),
        c2=('A right-angled triangle has an angle of 47&#176; and an adjacent side of 6 cm. Find the length of the hypotenuse, to 1 decimal place.', 2,
            'cos 47&#176; = 6 &divide; h &rarr; h = 6 &divide; cos 47&#176; (1) &nbsp; = <b>8.8 cm</b> (1)'),
        c3=('A right-angled triangle has an angle of 58&#176; and an adjacent side of 3 cm. Find the length of the side opposite the angle, to 1 decimal place.', 2,
            'tan 58&#176; = x &divide; 3 &rarr; x = 3 &times; tan 58&#176; (1) &nbsp; = <b>4.8 cm</b> (1)'),
        d1=('A right-angled triangle has an opposite side of 9 cm and a hypotenuse of 15 cm. Find the angle, to 1 decimal place.', 2,
            'sin &#952; = 9 &divide; 15 = 0.6 &rarr; &#952; = sin<sup>-1</sup>(0.6) (1) &nbsp; = <b>36.9&#176;</b> (1)'),
        d2=('A right-angled triangle has an adjacent side of 6 cm and an opposite side of 13 cm. Find the angle, to 1 decimal place.', 3,
            'tan &#952; = 13 &divide; 6 = 2.1667 (1) &nbsp; &#952; = tan<sup>-1</sup>(2.1667) (1) &nbsp; = <b>65.2&#176;</b> (1)'),
        e1=('A ladder rests against a vertical wall. The foot of the ladder is 2.4 m from the wall and the ladder is 6.5 m long. Calculate how far up the wall the ladder reaches, to 1 decimal place.', 2,
            'Use Pythagoras: height<sup>2</sup> = 6.5<sup>2</sup> &minus; 2.4<sup>2</sup> = 42.25 &minus; 5.76 = 36.49 (1) &nbsp; &radic;36.49 = <b>6.0 m</b> (1)'),
        e2=('A ramp rises at an angle of 15&#176; to the horizontal over a horizontal distance of 12 m. Calculate the height gained by the ramp, to 1 decimal place.', 3,
            'tan 15&#176; = h &divide; 12 (1) &nbsp; h = 12 &times; tan 15&#176; (1) &nbsp; = <b>3.2 m</b> (1)'),
    ),
}


def build_test(n, t):
    doc = SimpleDocTemplate(f'pythagoras_trig_test{n}.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry',
                 f'Extra practice test {n} &middot; 27 marks total')
    s.append(name_table())
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s += q('A1', t['a1'][0], t['a1'][1])
    s += q('A2', t['a2'][0], t['a2'][1])
    s += q('A3', t['a3'][0], t['a3'][1])

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s += q('B1', t['b1'][0], t['b1'][1])
    s += q('B2', t['b2'][0], t['b2'][1])
    s += q('B3', t['b3'][0], t['b3'][1])

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s += q('C1', t['c1'][0], t['c1'][1])
    s += q('C2', t['c2'][0], t['c2'][1])
    s += q('C3', t['c3'][0], t['c3'][1])

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s += q('D1', t['d1'][0], t['d1'][1])
    s += q('D2', t['d2'][0], t['d2'][1])

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s += q('E1', t['e1'][0], t['e1'][1])
    s += q('E2', t['e2'][0], t['e2'][1])

    doc.build(s)


def build_answers(n, t):
    doc = SimpleDocTemplate(f'pythagoras_trig_test{n}_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry',
                 f'Extra practice test {n} &mdash; answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s.append(Paragraph(f'A1. {t["a1"][2]}', styles['ans']))
    s.append(Paragraph(f'A2. {t["a2"][2]}', styles['ans']))
    s.append(Paragraph(f'A3. {t["a3"][2]}', styles['ans']))

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s.append(Paragraph(f'B1. {t["b1"][2]}', styles['ans']))
    s.append(Paragraph(f'B2. {t["b2"][2]}', styles['ans']))
    s.append(Paragraph(f'B3. {t["b3"][2]}', styles['ans']))

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s.append(Paragraph(f'C1. {t["c1"][2]}', styles['ans']))
    s.append(Paragraph(f'C2. {t["c2"][2]}', styles['ans']))
    s.append(Paragraph(f'C3. {t["c3"][2]}', styles['ans']))

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s.append(Paragraph(f'D1. {t["d1"][2]}', styles['ans']))
    s.append(Paragraph(f'D2. {t["d2"][2]}', styles['ans']))

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s.append(Paragraph(f'E1. {t["e1"][2]}', styles['ans']))
    s.append(Paragraph(f'E2. {t["e2"][2]}', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly set-up equation or calculation even if the final answer '
        'contains a rounding or arithmetic slip. Accept any correct rounding to 1 decimal place unless a different '
        'level of accuracy is specified. Missing units on an otherwise-correct numerical answer should lose the '
        'final accuracy mark, not the method mark.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    for n, t in TESTS.items():
        build_test(n, t)
        build_answers(n, t)
    print('done')
