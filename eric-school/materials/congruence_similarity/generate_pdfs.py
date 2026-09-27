# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Congruence & Similarity (GCSE Maths, Geometry & Measures)."""

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


# NOTE: reportlab's Helvetica encoding does not support Unicode super/subscript
# glyphs. Where a super/subscript is needed, use the <super>/<sub> paragraph tags
# with plain characters (e.g. 'cm<super>2</super>') rather than literal Unicode
# super/subscript characters.

# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('congruence_similarity_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Congruence &amp; Similarity',
                 'Quick reference sheet &middot; GCSE Maths, Geometry &amp; Measures &middot; section 5 is Higher tier')

    s.append(Paragraph('1. Congruent vs similar', styles['h2']))
    s.append(Paragraph('<b>Congruent</b> = exactly the same shape <b>and</b> size (may be turned or flipped). All matching sides and angles are equal.', styles['bullet']))
    s.append(Paragraph('<b>Similar</b> = same shape, different size (one is an enlargement of the other). Matching angles are equal; matching sides are all in the same ratio.', styles['bullet']))

    s.append(Paragraph('2. Conditions for congruent triangles', styles['h2']))
    s.append(table([
        [headcell('Condition'), headcell('What must match')],
        [cell('<b>SSS</b>'), cell('All three pairs of sides equal')],
        [cell('<b>SAS</b>'), cell('Two sides and the angle <i>between</i> them (included angle)')],
        [cell('<b>ASA / AAS</b>'), cell('Two angles and a corresponding side')],
        [cell('<b>RHS</b>'), cell('Right angle, equal hypotenuses, and one other equal side')],
    ], col_widths=[35 * mm, 115 * mm]))
    s.append(Spacer(1, 6))
    s.append(Paragraph('AAA does <b>not</b> prove congruence (only similarity). SSA does <b>not</b> prove congruence either. '
                       'In a proof: state three facts, give a reason for each, then name the condition.', styles['body']))

    s.append(Paragraph('3. Similar shapes &mdash; missing lengths', styles['h2']))
    s.append(Paragraph('1) Find a pair of matching sides where both lengths are known. '
                       '2) Scale factor = new length &divide; original length. '
                       '3) Multiply by the SF to go from small to large; divide to go from large to small.', styles['body']))
    s.append(Paragraph('To test whether two shapes are similar, check that the ratio is the <b>same for every pair</b> of matching sides.', styles['body']))

    s.append(Paragraph('4. Similar triangles inside each other', styles['h2']))
    s.append(Paragraph('If DE is parallel to BC (D on AB, E on AC), triangles ADE and ABC are similar: angle A is shared and '
                       'the parallel lines make corresponding angles equal. Use the <b>whole</b> side AB = AD + DB for the large triangle. '
                       'Sketch the two triangles separately to match up sides.', styles['body']))

    s.append(Paragraph('5. Area &amp; volume scale factors (Higher)', styles['h2']))
    s.append(table([
        [headcell('Length SF'), headcell('Area SF (incl. surface area)'), headcell('Volume SF')],
        [cell('k'), cell('k<super>2</super>'), cell('k<super>3</super>')],
        [cell('2'), cell('4'), cell('8')],
        [cell('3'), cell('9'), cell('27')],
    ], col_widths=[40 * mm, 60 * mm, 50 * mm]))
    s.append(Spacer(1, 6))
    s.append(Paragraph('Given an area ratio? <b>Square-root</b> it to get the length SF. Given a volume ratio? <b>Cube-root</b> it. '
                       'Always get back to the length SF first, then square or cube as needed.', styles['body']))

    s.append(Paragraph('6. Common mistakes', styles['h2']))
    s.append(Paragraph('Using DB instead of the whole side AB in nested triangles.', styles['bullet']))
    s.append(Paragraph('Multiplying an area or volume by the length scale factor instead of k<super>2</super> or k<super>3</super>.', styles['bullet']))
    s.append(Paragraph('Pairing up the wrong sides &mdash; match sides using equal angles, not position on the page.', styles['bullet']))
    s.append(Paragraph('Writing a congruence proof with no reasons, or using AAA as a condition.', styles['bullet']))
    s.append(Paragraph('Dividing the wrong way round: SF = new &divide; original, and check the answer is bigger or smaller as expected.', styles['bullet']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('congruence_similarity_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Congruence &amp; Similarity', 'Test &middot; 36 marks total &middot; Section D is Higher-tier content')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 36'),
    ]], col_widths=[80 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 10))

    s.append(Paragraph('Section A &mdash; Congruence', styles['h2']))
    s += q('A1', 'Explain the difference between two shapes being <i>congruent</i> and two shapes being <i>similar</i>.', 2)
    s += q('A2', 'For each pair of triangles, state the condition (SSS, SAS, ASA or RHS) that proves they are congruent.<br/>'
                 '(a) Both have sides 6 cm, 9 cm and 11 cm.<br/>'
                 '(b) Both are right-angled, with hypotenuse 10 cm and one other side 6 cm.<br/>'
                 '(c) Both have sides 7 cm and 5 cm with an angle of 55&#176; between them.', 3)
    s += q('A3', 'Two triangles both have angles of 40&#176;, 60&#176; and 80&#176;. Explain why this does not prove they are congruent.', 1)
    s += q('A4', 'ABCD is a parallelogram with diagonal AC. Prove that triangles ABC and CDA are congruent.', 3)

    s.append(Paragraph('Section B &mdash; Similar shapes: missing lengths', styles['h2']))
    s += q('B1', 'A rectangle measures 4 cm by 6 cm. A similar rectangle has a shorter side of 10 cm. Find its longer side.', 2)
    s += q('B2', 'Triangles ABC and PQR are similar, with A matching P, B matching Q and C matching R. '
                 'AB = 5 cm, BC = 8 cm and AC = 7 cm. PQ = 12.5 cm. Find QR and PR.', 3)
    s += q('B3', 'Rectangle X is 3 cm by 5 cm. Rectangle Y is 6 cm by 9 cm. Are the rectangles similar? Show how you decide.', 2)
    s += q('B4', 'Two triangles are similar. A side of 18 cm on the larger triangle matches a side of 12 cm on the smaller one. '
                 'Another side of the larger triangle is 24 cm. Find the matching side on the smaller triangle.', 2)

    s.append(Paragraph('Section C &mdash; Similar triangles inside each other', styles['h2']))
    s.append(Paragraph('In triangle ABC, D lies on AB and E lies on AC, with DE parallel to BC.', styles['body']))
    s += q('C1', 'Explain why triangle ADE is similar to triangle ABC.', 1)
    s += q('C2', 'AD = 4 cm, DB = 6 cm and DE = 5 cm. Find the length of BC.', 3)
    s += q('C3', 'In a different triangle of the same type, AE = 6 cm, AC = 15 cm and BC = 20 cm. Find the length of DE.', 2)

    s.append(Paragraph('Section D &mdash; Area &amp; volume of similar shapes (Higher)', styles['h2']))
    s += q('D1', 'A shape is enlarged by length scale factor 3. By what scale factor is its area multiplied?', 1)
    s += q('D2', 'Two similar triangles have matching sides of 4 cm and 12 cm. The smaller triangle has area 10 cm<super>2</super>. '
                 'Find the area of the larger triangle.', 2)
    s += q('D3', 'Two similar cones have heights 6 cm and 9 cm. The smaller cone has volume 64 cm<super>3</super>. '
                 'Find the volume of the larger cone.', 3)
    s += q('D4', 'Two similar solids have surface areas 50 cm<super>2</super> and 200 cm<super>2</super>. '
                 'The smaller solid has volume 30 cm<super>3</super>. Find the volume of the larger solid.', 4)
    s += q('D5', 'The volumes of two similar jugs are in the ratio 8 : 27. Find the ratio of their heights.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('congruence_similarity_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Congruence &amp; Similarity', 'Answer sheet &middot; 36 marks total')

    s.append(Paragraph('Section A &mdash; Congruence', styles['h2']))
    s.append(Paragraph('A1. Congruent: same shape <b>and</b> same size (1) &nbsp; similar: same shape but different size / one is an enlargement of the other (1)', styles['ans']))
    s.append(Paragraph('A2. (a) <b>SSS</b> (1) &nbsp; (b) <b>RHS</b> (1) &nbsp; (c) <b>SAS</b> (1)', styles['ans']))
    s.append(Paragraph('A3. Equal angles only show the triangles are the same shape &mdash; one could be bigger than the other, so they are similar but not necessarily congruent (1)', styles['ans']))
    s.append(Paragraph('A4. AB = CD and BC = DA (opposite sides of a parallelogram are equal) (1) &nbsp; AC is common to both triangles (1) &nbsp; so congruent by <b>SSS</b> (1). '
                       'Also accept: AB = CD, angle BAC = angle DCA (alternate angles), AC common, so SAS.', styles['ans']))

    s.append(Paragraph('Section B &mdash; Similar shapes: missing lengths', styles['h2']))
    s.append(Paragraph('B1. SF = 10 &divide; 4 = 2.5 (1) &nbsp; 6 &times; 2.5 = <b>15 cm</b> (1)', styles['ans']))
    s.append(Paragraph('B2. SF = 12.5 &divide; 5 = 2.5 (1) &nbsp; QR = 8 &times; 2.5 = <b>20 cm</b> (1) &nbsp; PR = 7 &times; 2.5 = <b>17.5 cm</b> (1)', styles['ans']))
    s.append(Paragraph('B3. 6 &divide; 3 = 2 and 9 &divide; 5 = 1.8 (1) &nbsp; ratios are different, so <b>not similar</b> (1)', styles['ans']))
    s.append(Paragraph('B4. SF = 12 &divide; 18 = 2/3 (1) &nbsp; 24 &times; 2/3 = <b>16 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Similar triangles inside each other', styles['h2']))
    s.append(Paragraph('C1. Angle A is shared, and angle ADE = angle ABC (corresponding angles, as DE is parallel to BC), so all three angles are equal (1)', styles['ans']))
    s.append(Paragraph('C2. AB = 4 + 6 = 10 (1) &nbsp; SF = 10 &divide; 4 = 2.5 (1) &nbsp; BC = 5 &times; 2.5 = <b>12.5 cm</b> (1)', styles['ans']))
    s.append(Paragraph('C3. SF (large to small) = 6 &divide; 15 = 0.4 (1) &nbsp; DE = 20 &times; 0.4 = <b>8 cm</b> (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Area &amp; volume of similar shapes (Higher)', styles['h2']))
    s.append(Paragraph('D1. 3<super>2</super> = <b>9</b> (1)', styles['ans']))
    s.append(Paragraph('D2. Length SF = 3, area SF = 9 (1) &nbsp; 10 &times; 9 = <b>90 cm<super>2</super></b> (1)', styles['ans']))
    s.append(Paragraph('D3. Length SF = 9 &divide; 6 = 1.5 (1) &nbsp; volume SF = 1.5<super>3</super> = 3.375 (1) &nbsp; 64 &times; 3.375 = <b>216 cm<super>3</super></b> (1)', styles['ans']))
    s.append(Paragraph('D4. Area SF = 200 &divide; 50 = 4 (1) &nbsp; length SF = &radic;4 = 2 (1) &nbsp; volume SF = 2<super>3</super> = 8 (1) &nbsp; 30 &times; 8 = <b>240 cm<super>3</super></b> (1)', styles['ans']))
    s.append(Paragraph('D5. Cube root of each part: 2 and 3 (1) &nbsp; ratio of heights = <b>2 : 3</b> (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correct scale factor even if the final answer contains an arithmetic slip. '
        'In proofs, each fact needs a reason to earn its mark; accept any valid congruence condition with correct reasons. '
        'Missing units on an otherwise-correct numerical answer should lose the final accuracy mark, not the method mark.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
