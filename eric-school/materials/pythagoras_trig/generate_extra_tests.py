# -*- coding: utf-8 -*-
"""Generate three extra practice tests + answer sheets for
Pythagoras' Theorem & Trigonometry (GCSE Maths, Geometry & Measures).

Each test keeps the same 5-section, 27-mark shape as the original
pythagoras_trig_test.pdf, but the three tests deliberately use
DIFFERENT question styles from each other and from the original
(not just re-numbered clones of the same template):

- Test 2: converse of Pythagoras, elevation/depression word problems,
  an isosceles-triangle split, a combined Pythagoras+trig question.
- Test 3: Pythagoras applied to squares/equilateral triangles, true/false
  and calculator-comparison conceptual questions, a navigation word
  problem, a ladder-safety "does it meet the requirement" question.
- Test 4: surd-form answers, "which method/ratio would you use"
  identification questions, true/false, two combined (a)/(b) questions.
"""

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


def marking_note():
    return Paragraph(
        'Marking note: award method marks for a correctly set-up equation or calculation even if the final answer '
        'contains a rounding or arithmetic slip. Accept any correct rounding to 1 decimal place unless a different '
        'level of accuracy is specified. Missing units on an otherwise-correct numerical answer should lose the '
        'final accuracy mark, not the method mark.',
        styles['note'])


# ============================================================ TEST 2
# Flavour: converse of Pythagoras, angle of elevation/depression word
# problems, splitting an isosceles triangle, a combined ladder question.

def build_test2():
    doc = SimpleDocTemplate('pythagoras_trig_test2.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Extra practice test 2 &middot; 27 marks total')
    s.append(name_table())
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s += q('A1', 'Point A is 8 km east and 6 km north of point B. Find the direct distance from A to B.', 2)
    s += q('A2', 'A ship sails 24 km east, then 7 km south, from its starting point. Use Pythagoras&rsquo; theorem to find how far the ship now is from its starting point.', 3)
    s += q('A3', 'A triangle has sides of length 9 cm, 12 cm and 15 cm. Use Pythagoras&rsquo; theorem to show that this triangle is right-angled.', 2)

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s += q('B1', 'A student says: &ldquo;To find a missing angle, I should always use sin<sup>-1</sup>, no matter which two sides I know.&rdquo; Explain why this is incorrect.', 1)
    s += q('B2', 'In a right-angled triangle you know the adjacent side and want to find the opposite side. Which SOH CAH TOA ratio should you use, and write the rearranged formula for the opposite side.', 1)
    s += q('B3', 'True or False: cos 60&#176; = sin 30&#176;. Show a calculation to support your answer.', 1)

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s += q('C1', 'From a point on the ground 20 m from the base of a tower, the angle of elevation to the top of the tower is 34&#176;. Find the height of the tower, to 1 decimal place.', 3)
    s += q('C2', 'A plane is flying at a height of 1200 m. The angle of depression from the plane to a landmark on the ground is 8&#176;. Find the horizontal distance from the plane to the landmark, to the nearest metre.', 2)
    s += q('C3', 'A rope is attached to the top of a flagpole and anchored to the ground, making an angle of 63&#176; with the ground. If the rope is 10 m long, find the height of the flagpole, to 1 decimal place.', 2)

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s += q('D1', 'A ramp is 5 m long and rises to a height of 1.2 m. Find the angle the ramp makes with the ground, to 1 decimal place.', 2)
    s += q('D2', 'A surveyor stands 45 m from the base of a cliff. The top of the cliff is 62 m above the ground. Find the angle of elevation to the top of the cliff, to 1 decimal place.', 3)

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s += q('E1', 'An isosceles triangle has two equal sides of length 13 cm and a base of 10 cm. Find the perpendicular height of the triangle by splitting the base into two equal halves.', 2)
    s += q('E2', 'A ladder 6 m long leans against a wall, reaching 5.2 m up the wall. (a) Find the distance from the foot of the ladder to the wall. (b) Find the angle the ladder makes with the ground. Give both answers to 1 decimal place.', 3)

    doc.build(s)


def build_answers2():
    doc = SimpleDocTemplate('pythagoras_trig_test2_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Extra practice test 2 &mdash; answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s.append(Paragraph('A1. 8<sup>2</sup> + 6<sup>2</sup> = 64 + 36 = 100 (1) &nbsp; distance = &radic;100 = <b>10 km</b> (1)', styles['ans']))
    s.append(Paragraph('A2. 24<sup>2</sup> + 7<sup>2</sup> (1) &nbsp; = 576 + 49 = 625 (1) &nbsp; &radic;625 = <b>25 km</b> (1)', styles['ans']))
    s.append(Paragraph('A3. 9<sup>2</sup> + 12<sup>2</sup> = 81 + 144 = 225 (1) &nbsp; 15<sup>2</sup> = 225 &mdash; since these are equal, the triangle <b>is right-angled</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s.append(Paragraph('B1. The correct inverse function (sin<sup>-1</sup>, cos<sup>-1</sup> or tan<sup>-1</sup>) depends on which two sides are known &mdash; sin<sup>-1</sup> only works when the opposite and hypotenuse are known (1)', styles['ans']))
    s.append(Paragraph('B2. <b>TOA</b>: opposite = adjacent &times; tan &#952; (1)', styles['ans']))
    s.append(Paragraph('B3. <b>True</b> &mdash; cos 60&#176; = 0.5 and sin 30&#176; = 0.5 (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s.append(Paragraph('C1. tan 34&#176; = h &divide; 20 (1) &nbsp; h = 20 &times; tan 34&#176; (1) &nbsp; = <b>13.5 m</b> (1)', styles['ans']))
    s.append(Paragraph('C2. tan 8&#176; = 1200 &divide; d &rarr; d = 1200 &divide; tan 8&#176; (1) &nbsp; = <b>8538 m</b> (1)', styles['ans']))
    s.append(Paragraph('C3. sin 63&#176; = h &divide; 10 &rarr; h = 10 &times; sin 63&#176; (1) &nbsp; = <b>8.9 m</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s.append(Paragraph('D1. sin &#952; = 1.2 &divide; 5 = 0.24 &rarr; &#952; = sin<sup>-1</sup>(0.24) (1) &nbsp; = <b>13.9&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('D2. tan &#952; = 62 &divide; 45 = 1.3778 (1) &nbsp; &#952; = tan<sup>-1</sup>(1.3778) (1) &nbsp; = <b>54.0&#176;</b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s.append(Paragraph('E1. Half the base = 5 cm; height<sup>2</sup> = 13<sup>2</sup> &minus; 5<sup>2</sup> = 169 &minus; 25 = 144 (1) &nbsp; height = &radic;144 = <b>12 cm</b> (1)', styles['ans']))
    s.append(Paragraph('E2. (a) distance<sup>2</sup> = 6<sup>2</sup> &minus; 5.2<sup>2</sup> = 36 &minus; 27.04 = 8.96 &rarr; &radic;8.96 = <b>3.0 m</b> (1) &nbsp; (b) sin &#952; = 5.2 &divide; 6 (1) &nbsp; &#952; = sin<sup>-1</sup>(5.2&divide;6) = <b>60.1&#176;</b> (1)', styles['ans']))

    s.append(marking_note())
    doc.build(s)


# ============================================================ TEST 3
# Flavour: Pythagoras applied to squares/equilateral triangles, true/false
# and calculator-comparison conceptual questions, a navigation word
# problem, a ladder-safety "does it meet the requirement" question.

def build_test3():
    doc = SimpleDocTemplate('pythagoras_trig_test3.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Extra practice test 3 &middot; 27 marks total')
    s.append(name_table())
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s += q('A1', 'A square has a diagonal of 18 cm. Find the length of one side, to 1 decimal place.', 2)
    s += q('A2', 'An equilateral triangle has sides of length 16 cm. Find its perpendicular height, to 1 decimal place.', 3)
    s += q('A3', 'A triangle has sides of length 11 cm, 60 cm and 61 cm. Determine, showing your working, whether this triangle is right-angled.', 2)

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s += q('B1', 'True or False: in a right-angled triangle, increasing the angle &#952; (while keeping the hypotenuse fixed) increases the length of the side opposite &#952;. Explain your answer.', 1)
    s += q('B2', 'Without using a calculator, state whether tan 80&#176; is greater than or less than 1. Explain your reasoning.', 1)
    s += q('B3', 'Calculate sin 70&#176; and cos 70&#176; (to 2 decimal places) and state which is larger.', 1)

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s += q('C1', 'A right-angled triangle has a hypotenuse of 22 cm and an angle of 40&#176;. Find the length of the side adjacent to the 40&#176; angle, to 1 decimal place.', 3)
    s += q('C2', 'A vertical flagpole casts a shadow 9 m long when the sun&rsquo;s angle of elevation is 51&#176;. Find the height of the flagpole, to 1 decimal place.', 2)
    s += q('C3', 'A right-angled triangle has an angle of 24&#176; and an opposite side of 5 cm. Find the length of the adjacent side, to 1 decimal place.', 2)

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s += q('D1', 'A road climbs 18 m over a horizontal distance of 150 m. Find the angle of the slope, to 1 decimal place.', 2)
    s += q('D2', 'A right-angled triangle has a hypotenuse of 19 cm and one shorter side of 11 cm. Find the angle between the hypotenuse and the 11 cm side, to 1 decimal place.', 3)

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s += q('E1', 'A window cleaner&rsquo;s ladder must make an angle of at least 65&#176; with the ground to be considered safe. The ladder is 4 m long and its foot is placed 1.5 m from the wall. Calculate the angle the ladder makes with the ground and state whether it meets the safety requirement.', 2)
    s += q('E2', 'A ship sails from port P for 15 km due east to point Q, then turns and sails 9 km due north to point R. (a) Find the direct distance from P to R, to 1 decimal place. (b) Find the angle between the direct route PR and the initial direction PQ (due east), to 1 decimal place.', 3)

    doc.build(s)


def build_answers3():
    doc = SimpleDocTemplate('pythagoras_trig_test3_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Extra practice test 3 &mdash; answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s.append(Paragraph('A1. a<sup>2</sup> + a<sup>2</sup> = 18<sup>2</sup> &rarr; 2a<sup>2</sup> = 324 (1) &nbsp; a<sup>2</sup> = 162 &rarr; a = &radic;162 = <b>12.7 cm</b> (1)', styles['ans']))
    s.append(Paragraph('A2. Splitting the triangle in half gives a right-angled triangle with hypotenuse 16 cm and base 8 cm (1) &nbsp; height<sup>2</sup> = 16<sup>2</sup> &minus; 8<sup>2</sup> = 256 &minus; 64 = 192 (1) &nbsp; height = &radic;192 = <b>13.9 cm</b> (1)', styles['ans']))
    s.append(Paragraph('A3. 11<sup>2</sup> + 60<sup>2</sup> = 121 + 3600 = 3721 (1) &nbsp; 61<sup>2</sup> = 3721 &mdash; since these are equal, the triangle <b>is right-angled</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s.append(Paragraph('B1. <b>True</b> &mdash; opposite = hypotenuse &times; sin &#952;, and sin &#952; increases as &#952; increases from 0&#176; to 90&#176;, so a larger &#952; gives a larger opposite side (1)', styles['ans']))
    s.append(Paragraph('B2. <b>Greater than 1</b> &mdash; tan 45&#176; = 1, and tan &#952; keeps increasing as &#952; increases towards 90&#176;, so tan 80&#176; &gt; 1 (1)', styles['ans']))
    s.append(Paragraph('B3. sin 70&#176; = 0.94, cos 70&#176; = 0.34 &mdash; <b>sin 70&#176; is larger</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s.append(Paragraph('C1. cos 40&#176; = x &divide; 22 (1) &nbsp; x = 22 &times; cos 40&#176; (1) &nbsp; = <b>16.9 cm</b> (1)', styles['ans']))
    s.append(Paragraph('C2. tan 51&#176; = h &divide; 9 &rarr; h = 9 &times; tan 51&#176; (1) &nbsp; = <b>11.1 m</b> (1)', styles['ans']))
    s.append(Paragraph('C3. tan 24&#176; = 5 &divide; x &rarr; x = 5 &divide; tan 24&#176; (1) &nbsp; = <b>11.2 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s.append(Paragraph('D1. tan &#952; = 18 &divide; 150 = 0.12 (1) &nbsp; &#952; = tan<sup>-1</sup>(0.12) = <b>6.8&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('D2. cos &#952; = 11 &divide; 19 = 0.5789 (1) &nbsp; &#952; = cos<sup>-1</sup>(0.5789) (1) &nbsp; = <b>54.6&#176;</b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s.append(Paragraph('E1. cos &#952; = 1.5 &divide; 4 = 0.375 &rarr; &#952; = cos<sup>-1</sup>(0.375) = 68.0&#176; (1) &nbsp; since 68.0&#176; &gt; 65&#176;, the ladder <b>meets the safety requirement</b> (1)', styles['ans']))
    s.append(Paragraph('E2. (a) PR<sup>2</sup> = 15<sup>2</sup> + 9<sup>2</sup> = 225 + 81 = 306 &rarr; PR = &radic;306 = <b>17.5 km</b> (1) &nbsp; (b) tan &#952; = 9 &divide; 15 = 0.6 (1) &nbsp; &#952; = tan<sup>-1</sup>(0.6) = <b>31.0&#176;</b> (1)', styles['ans']))

    s.append(marking_note())
    doc.build(s)


# ============================================================ TEST 4
# Flavour: surd-form answers, "which method/ratio" identification
# questions, true/false, two combined (a)/(b) questions.

def build_test4():
    doc = SimpleDocTemplate('pythagoras_trig_test4.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Extra practice test 4 &middot; 27 marks total')
    s.append(name_table())
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s += q('A1', 'A right-angled triangle has two shorter sides both equal to 6 cm. Find the length of the hypotenuse, giving your answer both as a simplified surd and to 1 decimal place.', 2)
    s += q('A2', 'A right-angled triangle has a hypotenuse of 10 cm and one shorter side of 7 cm. Find the length of the other shorter side, to 1 decimal place.', 3)
    s += q('A3', 'A ladder reaches from the ground to a window 4.8 m up a wall. The foot of the ladder is 2.2 m from the wall. Find the length of the ladder, to 1 decimal place.', 2)

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s += q('B1', 'A right-angled triangle has a known hypotenuse and a known angle, and you need to find the side adjacent to that angle. Which method should you use &mdash; Pythagoras&rsquo; theorem or SOH CAH TOA &mdash; and which specific ratio?', 1)
    s += q('B2', 'A right-angled triangle has two known shorter sides and no known angles. Which method should you use to find the hypotenuse: Pythagoras&rsquo; theorem, or SOH CAH TOA?', 1)
    s += q('B3', 'True or False: Pythagoras&rsquo; theorem can be used on any triangle, not just right-angled ones.', 1)

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s += q('C1', 'A right-angled triangle has an angle of 22&#176; and an opposite side of 6 cm. Find the length of the hypotenuse, to 1 decimal place.', 3)
    s += q('C2', 'A right-angled triangle has an angle of 66&#176; and a hypotenuse of 9 cm. Find the length of the side adjacent to the angle, to 1 decimal place.', 2)
    s += q('C3', 'A right-angled triangle has an angle of 39&#176; and an opposite side of 7 cm. Find the length of the adjacent side, to 1 decimal place.', 2)

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s += q('D1', 'A right-angled triangle has a hypotenuse of 25 cm and an adjacent side of 7 cm. Find the angle between them, to 1 decimal place.', 2)
    s += q('D2', 'A zip-wire is fixed between two platforms. The horizontal distance between the platforms is 40 m and the vertical drop is 14 m. Find the angle the zip-wire makes with the horizontal, to 1 decimal place.', 3)

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s += q('E1', 'A right-angled triangle has an opposite side of 9 cm and an adjacent side of 12 cm. (a) Find the length of the hypotenuse. (b) Find the angle opposite the 9 cm side, to 1 decimal place.', 2)
    s += q('E2', 'A rectangular gate measures 1.8 m high and 3 m wide. A diagonal support strut is fitted. (a) Find the length of the strut, to 1 decimal place. (b) Find the angle the strut makes with the base of the gate, to 1 decimal place.', 3)

    doc.build(s)


def build_answers4():
    doc = SimpleDocTemplate('pythagoras_trig_test4_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Pythagoras&rsquo; Theorem &amp; Trigonometry', 'Extra practice test 4 &mdash; answer sheet &middot; 27 marks total')

    s.append(Paragraph('Section A &mdash; Pythagoras&rsquo; theorem', styles['h2']))
    s.append(Paragraph('A1. 6<sup>2</sup> + 6<sup>2</sup> = 36 + 36 = 72 (1) &nbsp; hypotenuse = &radic;72 = <b>6&radic;2 &asymp; 8.5 cm</b> (1)', styles['ans']))
    s.append(Paragraph('A2. a<sup>2</sup> = 10<sup>2</sup> &minus; 7<sup>2</sup> (1) &nbsp; = 100 &minus; 49 = 51 (1) &nbsp; a = &radic;51 = <b>7.1 cm</b> (1)', styles['ans']))
    s.append(Paragraph('A3. length<sup>2</sup> = 4.8<sup>2</sup> + 2.2<sup>2</sup> = 23.04 + 4.84 = 27.88 (1) &nbsp; length = &radic;27.88 = <b>5.3 m</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; SOH CAH TOA basics', styles['h2']))
    s.append(Paragraph('B1. SOH CAH TOA &mdash; specifically <b>CAH</b> (adjacent = hypotenuse &times; cos &#952;) (1)', styles['ans']))
    s.append(Paragraph('B2. <b>Pythagoras&rsquo; theorem</b> &mdash; no angle is known or needed (1)', styles['ans']))
    s.append(Paragraph('B3. <b>False</b> &mdash; Pythagoras&rsquo; theorem only applies to right-angled triangles (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Finding missing sides', styles['h2']))
    s.append(Paragraph('C1. sin 22&#176; = 6 &divide; h (1) &nbsp; h = 6 &divide; sin 22&#176; (1) &nbsp; = <b>16.0 cm</b> (1)', styles['ans']))
    s.append(Paragraph('C2. cos 66&#176; = x &divide; 9 &rarr; x = 9 &times; cos 66&#176; (1) &nbsp; = <b>3.7 cm</b> (1)', styles['ans']))
    s.append(Paragraph('C3. tan 39&#176; = 7 &divide; x &rarr; x = 7 &divide; tan 39&#176; (1) &nbsp; = <b>8.6 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Finding missing angles', styles['h2']))
    s.append(Paragraph('D1. cos &#952; = 7 &divide; 25 = 0.28 (1) &nbsp; &#952; = cos<sup>-1</sup>(0.28) = <b>73.7&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('D2. tan &#952; = 14 &divide; 40 = 0.35 (1) &nbsp; &#952; = tan<sup>-1</sup>(0.35) (1) &nbsp; = <b>19.3&#176;</b> (1)', styles['ans']))

    s.append(Paragraph('Section E &mdash; Applying Pythagoras &amp; trigonometry', styles['h2']))
    s.append(Paragraph('E1. (a) hyp<sup>2</sup> = 9<sup>2</sup> + 12<sup>2</sup> = 81 + 144 = 225 &rarr; hyp = <b>15 cm</b> (1) &nbsp; (b) sin &#952; = 9 &divide; 15 = 0.6 &rarr; &#952; = sin<sup>-1</sup>(0.6) = <b>36.9&#176;</b> (1)', styles['ans']))
    s.append(Paragraph('E2. (a) strut<sup>2</sup> = 1.8<sup>2</sup> + 3<sup>2</sup> = 3.24 + 9 = 12.24 &rarr; strut = &radic;12.24 = <b>3.5 m</b> (1) &nbsp; (b) tan &#952; = 1.8 &divide; 3 = 0.6 (1) &nbsp; &#952; = tan<sup>-1</sup>(0.6) = <b>31.0&#176;</b> (1)', styles['ans']))

    s.append(marking_note())
    doc.build(s)


if __name__ == '__main__':
    build_test2()
    build_answers2()
    build_test3()
    build_answers3()
    build_test4()
    build_answers4()
    print('done')
