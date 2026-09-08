# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Atomic Structure & the Periodic Table (AQA GCSE Chemistry 8462, 4.1)."""

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
CHEM = colors.HexColor('#C4571F')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#FBEADD')

MARGIN = 18 * mm

styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=26,
                             textColor=INK, spaceAfter=4, leading=30),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=10.5,
                                textColor=INK_SOFT, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=13.5,
                          textColor=CHEM, spaceBefore=14, spaceAfter=7),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10,
                            textColor=INK, leading=14, spaceAfter=7, alignment=TA_LEFT),
    'bodyb': ParagraphStyle('bodyb', fontName='Helvetica-Bold', fontSize=10,
                             textColor=INK, leading=14, spaceAfter=7),
    'marks': ParagraphStyle('marks', fontName='Helvetica-Oblique', fontSize=9,
                             textColor=INK_SOFT, spaceAfter=9),
    'qtext': ParagraphStyle('qtext', fontName='Helvetica', fontSize=10,
                             textColor=INK, leading=14, spaceAfter=2),
    'ans': ParagraphStyle('ans', fontName='Helvetica', fontSize=10,
                           textColor=INK, leading=14, spaceAfter=6),
    'note': ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=9,
                            textColor=INK_SOFT, leading=12, spaceBefore=12),
    'tablehead': ParagraphStyle('tablehead', fontName='Helvetica', fontSize=8.7,
                                 textColor=INK_SOFT),
    'tablecell': ParagraphStyle('tablecell', fontName='Helvetica', fontSize=9.3,
                                 textColor=INK, leading=12.5),
}


def hr():
    return HRFlowable(width='100%', thickness=1, color=PAPER_LINE,
                       spaceBefore=6, spaceAfter=12)


def header(title, subtitle):
    return [Paragraph(title, styles['title']), Paragraph(subtitle, styles['subtitle']), hr()]


def table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEAD_BG),
        ('LINEBELOW', (0, 0), (-1, -1), 0.75, PAPER_LINE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 8.7),
        ('TEXTCOLOR', (0, 0), (-1, 0), INK_SOFT),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def cell(text):
    return Paragraph(text, styles['tablecell'])


def headcell(text):
    return Paragraph(text, styles['tablehead'])


# ---------------------------------------------------------------- REFERENCE

def build_reference():
    doc = SimpleDocTemplate('atomic_structure_periodic_table_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Atomic Structure &amp; the Periodic Table',
                 'Quick reference sheet &middot; Chemistry &middot; keep handy for revision')

    s.append(Paragraph('1. Subatomic particles', styles['h2']))
    s.append(table([
        [headcell('Particle'), headcell('Relative mass'), headcell('Relative charge'), headcell('Location')],
        [cell('Proton'), cell('1'), cell('+1'), cell('Nucleus')],
        [cell('Neutron'), cell('1'), cell('0'), cell('Nucleus')],
        [cell('Electron'), cell('very small'), cell('&minus;1'), cell('Shells around nucleus')],
    ], col_widths=[35 * mm, 35 * mm, 35 * mm, 37 * mm]))

    s.append(Paragraph('2. Atomic number, mass number &amp; isotopes', styles['h2']))
    s.append(Paragraph('<b>Atomic number</b> = number of protons = number of electrons. <b>Mass number</b> = protons + neutrons. So neutrons = mass number &minus; atomic number.', styles['body']))
    s.append(Paragraph('<b>Isotopes</b>: same element (same protons), different number of neutrons. Same chemical properties, different physical properties (mass, density; some radioactive).', styles['body']))
    s.append(Paragraph('<b>Relative atomic mass</b> = weighted mean of isotope masses, using % abundance: A<sub>r</sub> = &Sigma;(mass &times; %abundance) &divide; 100.', styles['body']))

    s.append(Paragraph('3. Electronic structure', styles['h2']))
    s.append(Paragraph('Electrons fill the lowest-energy shell first. Maximum per shell (first 20 elements): <b>1st = 2, 2nd = 8, 3rd = 8</b>. Example: sodium (11) = 2,8,1.', styles['body']))
    s.append(Paragraph('<b>Group number</b> = electrons in outer shell. <b>Period number</b> = number of occupied shells.', styles['body']))

    s.append(Paragraph('4. Development of the periodic table', styles['h2']))
    s.append(Paragraph('<b>Newlands (1864)</b>: ordered by atomic weight; "Law of Octaves" &mdash; every 8th element had similar properties. Rejected: forced dissimilar elements together, no gaps for undiscovered elements.', styles['body']))
    s.append(Paragraph('<b>Mendeleev (1869)</b>: ordered mostly by atomic weight but swapped some elements to group similar properties together; left gaps and predicted missing elements&rsquo; properties &mdash; later discoveries (e.g. germanium) matched, giving the table credibility.', styles['body']))
    s.append(Paragraph('<b>Modern table</b>: ordered by increasing atomic (proton) number. Same group = same outer electrons = similar properties. Same period = same number of shells.', styles['body']))

    s.append(Paragraph('5. Metals vs non-metals', styles['h2']))
    s.append(table([
        [headcell(''), headcell('Metals'), headcell('Non-metals')],
        [cell('Position'), cell('Left &amp; bottom-left'), cell('Top-right')],
        [cell('Properties'), cell('Shiny, malleable, good conductors, high m.p./b.p.'), cell('Dull, brittle, poor conductors, low m.p./b.p.')],
        [cell('Ion formed'), cell('Positive (lose electrons)'), cell('Negative (gain electrons) or covalent')],
    ], col_widths=[28 * mm, 71 * mm, 43 * mm]))

    s.append(Paragraph('6. Groups 0, 1 &amp; 7', styles['h2']))
    s.append(table([
        [headcell('Group'), headcell('Outer electrons'), headcell('Trend'), headcell('Key facts')],
        [cell('0 &mdash; Noble gases'), cell('Full shell'), cell('B.p. increases down group'), cell('Unreactive, monatomic gases')],
        [cell('1 &mdash; Alkali metals'), cell('1'), cell('Reactivity increases down group'), cell('Soft, low density, react vigorously with water')],
        [cell('7 &mdash; Halogens'), cell('7'), cell('Reactivity decreases down group'), cell('Diatomic molecules, can displace less reactive halogens')],
    ], col_widths=[35 * mm, 28 * mm, 45 * mm, 34 * mm]))
    s.append(Paragraph('Trend reason: going down a group, the outer shell is further from the nucleus and more shielded &mdash; easier to lose an electron (Group 1, reactivity up), harder to gain one (Group 7, reactivity down).', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('atomic_structure_periodic_table_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Atomic Structure &amp; the Periodic Table', 'Test &middot; 36 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 36'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Atoms, particles &amp; isotopes', styles['h2']))
    s += q('A1', 'State the relative charge of a proton, and the relative charge of an electron.', 2)
    s.append(Spacer(1, 8))
    s += q('A2', 'An atom of an element has 6 protons and 6 neutrons. State its atomic number and its mass number.', 2)
    s.append(Spacer(1, 8))
    s += q('A3', 'An atom of chlorine has atomic number 17 and mass number 35. Calculate its number of neutrons.', 1)
    s.append(Spacer(1, 8))
    s += q('A4', 'Explain what is meant by the term &ldquo;isotopes&rdquo;.', 2)
    s.append(Spacer(1, 8))
    s += q('A5', 'Bromine has two isotopes: bromine-79 (50.7% abundance) and bromine-81 (49.3% abundance). Calculate the relative atomic mass of bromine, to 1 decimal place.', 3)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Electronic structure', styles['h2']))
    s += q('B1', 'State the maximum number of electrons that can occupy the 1st shell, and the 2nd shell.', 2)
    s.append(Spacer(1, 8))
    s += q('B2', 'Give the electronic structure of a phosphorus atom (atomic number 15).', 2)
    s.append(Spacer(1, 8))
    s += q('B3', 'An atom has the electronic structure 2,8,7. State which group and which period this atom belongs to.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; Development of the periodic table', styles['h2']))
    s += q('C1', 'Describe Newlands&rsquo; &ldquo;Law of Octaves&rdquo;, and give one reason it was not widely accepted.', 2)
    s.append(Spacer(1, 8))
    s += q('C2', 'Explain how Mendeleev used gaps in his periodic table to gain scientific credibility for his arrangement of the elements.', 3)
    s.append(Spacer(1, 8))
    s += q('C3', 'State the property used to arrange elements in the modern periodic table.', 1)
    s.append(Spacer(1, 8))
    s += q('C4', 'State what elements in the same group of the periodic table have in common, in terms of electronic structure.', 1)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Metals, non-metals &amp; key groups', styles['h2']))
    s += q('D1', 'Give two physical properties of metals.', 2)
    s.append(Spacer(1, 8))
    s += q('D2', 'Give two physical properties of non-metals.', 2)
    s.append(Spacer(1, 8))
    s += q('D3', 'Explain why the noble gases (Group 0) are very unreactive.', 2)
    s.append(Spacer(1, 8))
    s += q('D4', 'Sodium reacts with water. (a) Write a word equation for this reaction. (b) Describe two observations you would make during the reaction.', 3)
    s.append(Spacer(1, 8))
    s += q('D5', 'Explain, in terms of electronic structure, why reactivity increases down Group 1.', 2)
    s.append(Spacer(1, 8))
    s += q('D6', 'Chlorine can displace bromine from a solution of potassium bromide. Write a word equation for this reaction, and state what type of reaction this is.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('atomic_structure_periodic_table_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Atomic Structure &amp; the Periodic Table', 'Answer sheet &middot; 36 marks total')

    s.append(Paragraph('Section A &mdash; Atoms, particles &amp; isotopes', styles['h2']))
    s.append(Paragraph('<b>A1.</b> Proton = <b>+1</b> (1); electron = <b>&minus;1</b> (1)', styles['ans']))
    s.append(Paragraph('<b>A2.</b> Atomic number = <b>6</b> (1); mass number = 6 + 6 = <b>12</b> (1)', styles['ans']))
    s.append(Paragraph('<b>A3.</b> Neutrons = 35 &minus; 17 = <b>18</b> (1)', styles['ans']))
    s.append(Paragraph('<b>A4.</b> Atoms of the same element (same number of protons) (1) with a different number of neutrons / different mass number (1)', styles['ans']))
    s.append(Paragraph('<b>A5.</b> A<sub>r</sub> = (79 &times; 50.7 + 81 &times; 49.3) &divide; 100 (1) &nbsp; = (4005.3 + 3993.3) &divide; 100 = 7998.6 &divide; 100 (1) &nbsp; = <b>80.0</b> (1)', styles['ans']))

    s.append(Paragraph('Section B &mdash; Electronic structure', styles['h2']))
    s.append(Paragraph('<b>B1.</b> 1st shell = <b>2</b> (1); 2nd shell = <b>8</b> (1)', styles['ans']))
    s.append(Paragraph('<b>B2.</b> <b>2, 8, 5</b> (2 &mdash; 1 mark if only one number is wrong)', styles['ans']))
    s.append(Paragraph('<b>B3.</b> Group <b>7</b>, since it has 7 outer electrons (1); Period <b>3</b>, since it has 3 occupied shells (1)', styles['ans']))

    s.append(Paragraph('Section C &mdash; Development of the periodic table', styles['h2']))
    s.append(Paragraph('<b>C1.</b> Elements were arranged in order of atomic weight, and every 8th element had similar properties (1). Not accepted because: it forced dissimilar elements into the same group / left no gaps for undiscovered elements (any one, 1)', styles['ans']))
    s.append(Paragraph('<b>C2.</b> He left gaps for elements not yet discovered (1); used the pattern to predict their properties (1); when later-discovered elements (e.g. germanium) matched these predictions, it gave scientists confidence his table reflected a real pattern (1)', styles['ans']))
    s.append(Paragraph('<b>C3.</b> Atomic (proton) number (1)', styles['ans']))
    s.append(Paragraph('<b>C4.</b> The same number of electrons in their outer shell (1)', styles['ans']))

    s.append(Paragraph('Section D &mdash; Metals, non-metals &amp; key groups', styles['h2']))
    s.append(Paragraph('<b>D1.</b> Any two of: shiny; malleable/ductile; good conductors of heat &amp; electricity; high melting/boiling points; high density (1 mark each, max 2)', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Any two of: dull; brittle; poor conductors of heat &amp; electricity (insulators); low melting/boiling points (1 mark each, max 2)', styles['ans']))
    s.append(Paragraph('<b>D3.</b> Noble gases have a full outer shell of electrons (1); this makes them very stable, so they do not easily gain, lose or share electrons (1)', styles['ans']))
    s.append(Paragraph('<b>D4.</b> (a) sodium + water &rarr; sodium hydroxide + hydrogen (1) &nbsp; (b) any two of: fizzing/bubbles of gas; sodium moves/floats/melts into a ball on the surface; sodium may catch fire; the solution becomes warm (1 mark each, max 2)', styles['ans']))
    s.append(Paragraph('<b>D5.</b> Going down Group 1, the outer electron is in a shell further from the nucleus (1); it is more shielded by inner shells, so it is lost more easily (1)', styles['ans']))
    s.append(Paragraph('<b>D6.</b> chlorine + potassium bromide &rarr; potassium chloride + bromine (1); this is a <b>displacement reaction</b>, since chlorine is more reactive than bromine and displaces it (1)', styles['ans']))

    s.append(Paragraph(
        'Marking note: award method marks for a correctly set-up equation or calculation even if the final answer '
        'contains a rounding or arithmetic slip. Accept any scientifically correct alternative property, observation, '
        'or reason not shown above.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
