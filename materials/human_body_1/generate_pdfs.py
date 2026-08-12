# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Human Body Systems, Part 1: Breathing & Transport (AQA 8465 4.2.1, Foundation tier)."""

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
BIO = colors.HexColor('#2F8B57')
PAPER_LINE = colors.HexColor('#E4DDCE')
TABLE_HEAD_BG = colors.HexColor('#EAF2ED')

MARGIN = 18 * mm

styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=26,
                             textColor=INK, spaceAfter=4, leading=30),
    'subtitle': ParagraphStyle('subtitle', fontName='Helvetica', fontSize=10.5,
                                textColor=INK_SOFT, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=13.5,
                          textColor=BIO, spaceBefore=14, spaceAfter=7),
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
    doc = SimpleDocTemplate('human_body_1_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Human Body Systems: Breathing &amp; Transport',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('1. Respiration', styles['h2']))
    s.append(Paragraph('<b>Aerobic</b> (with oxygen): glucose + oxygen &rarr; carbon dioxide + water <i>(+ energy released)</i>', styles['body']))
    s.append(Paragraph('<b>Anaerobic</b> (no oxygen, e.g. sprinting): glucose &rarr; lactic acid <i>(+ energy released, but much less)</i>', styles['body']))
    s.append(Paragraph('Anaerobic respiration is fast to start but releases far less energy, and the lactic acid that builds up causes muscle fatigue/cramp.', styles['body']))

    s.append(Paragraph('2. Exchange surfaces &amp; the alveoli', styles['h2']))
    s.append(Paragraph('Every good exchange surface has: a <b>large surface area</b>, <b>thin walls</b> (short diffusion distance), a <b>good blood supply</b> (keeps the concentration gradient steep), and a <b>moist lining</b> (lets gases dissolve).', styles['body']))
    s.append(Paragraph('The alveoli in the lungs show all four: millions of them give a huge surface area; walls one cell thick give a short diffusion path; a network of capillaries gives a good blood supply; the lining is moist.', styles['body']))

    s.append(Paragraph('3. The heart &amp; double circulation', styles['h2']))
    s.append(table([
        [headcell('Chamber'), headcell('Receives / pumps to')],
        [cell('Right atrium'), cell('Receives deoxygenated blood from the body')],
        [cell('Right ventricle'), cell('Pumps deoxygenated blood to the lungs (pulmonary circuit)')],
        [cell('Left atrium'), cell('Receives oxygenated blood from the lungs')],
        [cell('Left ventricle'), cell('Pumps oxygenated blood to the body (systemic circuit) &mdash; thicker, more muscular wall than the right ventricle, since it must reach the whole body')],
    ], col_widths=[38 * mm, 105 * mm]))
    s.append(Paragraph('<b>Double circulation</b>: blood passes through the heart twice on each full circuit of the body &mdash; once via the lungs, once via the rest of the body.', styles['body']))

    s.append(Paragraph('4. Blood vessels', styles['h2']))
    s.append(table([
        [headcell('Vessel'), headcell('Wall &amp; lumen'), headcell('Job')],
        [cell('<b>Artery</b>'), cell('Thick, muscular &amp; elastic wall; narrow lumen'), cell('Carries blood at high pressure away from the heart')],
        [cell('<b>Vein</b>'), cell('Thin wall; wide lumen; has valves'), cell('Carries blood at low pressure back to the heart; valves stop backflow')],
        [cell('<b>Capillary</b>'), cell('Wall just one cell thick'), cell('Links arteries to veins; substances diffuse into/out of nearby cells')],
    ], col_widths=[24 * mm, 60 * mm, 59 * mm]))

    s.append(Paragraph('5. Blood components', styles['h2']))
    s.append(table([
        [headcell('Component'), headcell('Looks like'), headcell('Function')],
        [cell('<b>Red blood cell</b>'), cell('Biconcave disc, no nucleus, full of haemoglobin'), cell('Carries oxygen around the body')],
        [cell('<b>White blood cell</b>'), cell('Larger, has a nucleus'), cell('Fights infection (engulfs pathogens / makes antibodies)')],
        [cell('<b>Platelet</b>'), cell('Small cell fragment, no nucleus'), cell('Helps blood clot at a wound')],
        [cell('<b>Plasma</b>'), cell('Pale yellow liquid'), cell('Transports blood cells, dissolved food, CO&#8322;, urea &amp; hormones')],
    ], col_widths=[28 * mm, 55 * mm, 60 * mm]))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('human_body_1_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Human Body Systems: Breathing &amp; Transport', 'Test &middot; 38 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 38'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Respiration', styles['h2']))
    s += q('A1', 'Complete the word equation for aerobic respiration: glucose + oxygen &rarr; ______ + ______.', 2)
    s.append(Spacer(1, 8))
    s += q('A2', 'State two differences between aerobic and anaerobic respiration in muscle cells.', 2)
    s.append(Spacer(1, 8))
    s += q('A3', "During intense exercise, a sprinter's muscles cannot get enough oxygen. Name the type of respiration used, and describe one problem this causes.", 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Exchange surfaces', styles['h2']))
    s += q('B1', 'State three features that make a surface efficient for exchanging substances such as gases.', 3)
    s.append(Spacer(1, 8))
    s += q('B2', 'Explain how the structure of alveoli is adapted for efficient gas exchange.', 4)
    s.append(Spacer(1, 8))
    s += q('B3', 'Explain why capillary walls are only one cell thick.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; The heart &amp; circulation', styles['h2']))
    s += q('C1', 'Name the four chambers of the heart.', 4)
    s.append(Spacer(1, 8))
    s += q('C2', "What is meant by 'double circulation'?", 2)
    s.append(Spacer(1, 8))
    s += q('C3', 'Explain why the wall of the left ventricle is thicker (more muscular) than the wall of the right ventricle.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Blood vessels', styles['h2']))
    s += q('D1', 'State one structural difference between an artery and a vein, and explain why this difference is needed.', 2)
    s.append(Spacer(1, 8))
    s += q('D2', 'Veins contain valves. Explain why these are needed.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section E &mdash; Blood components', styles['h2']))
    s += q('E1', 'Name the four components of blood.', 4)
    s.append(Spacer(1, 8))
    s += q('E2', 'Explain how red blood cells are adapted to carry oxygen efficiently.', 3)
    s.append(Spacer(1, 8))
    s += q('E3', 'What is the function of platelets?', 1)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section F &mdash; Apply it', styles['h2']))
    s += q('F1', 'A patient has a low red blood cell count, a condition called anaemia. Suggest why they might feel tired all the time.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('human_body_1_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Human Body Systems: Breathing &amp; Transport', 'Answer sheet &middot; 38 marks total')

    s.append(Paragraph('Section A &mdash; Respiration', styles['h2']))
    s.append(Paragraph('<b>A1.</b> Carbon dioxide (1) + water (1).', styles['ans']))
    s.append(Paragraph('<b>A2.</b> Any two: aerobic needs oxygen, anaerobic does not (1); aerobic releases (much) more energy per glucose molecule (1); anaerobic produces lactic acid, aerobic produces carbon dioxide and water (1).', styles['ans']))
    s.append(Paragraph('<b>A3.</b> Anaerobic respiration (1); it produces lactic acid, which builds up and causes muscle fatigue/cramp (1).', styles['ans']))

    s.append(Paragraph('Section B &mdash; Exchange surfaces', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Any three: large surface area (1); thin walls/short diffusion distance (1); good blood supply (1); moist surface/lining (1).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> Millions of alveoli give a large surface area (1); walls are one cell thick, giving a short diffusion distance (1); surrounded by a network of capillaries, giving a good blood supply that maintains a steep concentration gradient (1); a moist lining lets gases dissolve (1).', styles['ans']))
    s.append(Paragraph('<b>B3.</b> This gives a short diffusion distance/pathway (1), so substances can diffuse quickly between the blood and body cells (1).', styles['ans']))

    s.append(Paragraph('Section C &mdash; The heart &amp; circulation', styles['h2']))
    s.append(Paragraph('<b>C1.</b> Right atrium (1), right ventricle (1), left atrium (1), left ventricle (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> Blood passes through the heart twice on each full circuit of the body (1): once to the lungs (pulmonary circuit) and once to the rest of the body (systemic circuit) (1).', styles['ans']))
    s.append(Paragraph('<b>C3.</b> The left ventricle pumps blood all the way around the body (systemic circuit) (1), while the right ventricle only pumps blood to the nearby lungs, so the left ventricle needs to generate much higher pressure (1).', styles['ans']))

    s.append(Paragraph('Section D &mdash; Blood vessels', styles['h2']))
    s.append(Paragraph('<b>D1.</b> E.g. arteries have thicker, more muscular/elastic walls (1) because they carry blood at high pressure away from the heart (1). <i>[or: veins have a wider lumen (1) to help blood flow at low pressure (1)]</i>', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Blood in veins is at low pressure (1); valves stop the blood from flowing backwards (1).', styles['ans']))

    s.append(Paragraph('Section E &mdash; Blood components', styles['h2']))
    s.append(Paragraph('<b>E1.</b> Red blood cells (1), white blood cells (1), platelets (1), plasma (1).', styles['ans']))
    s.append(Paragraph('<b>E2.</b> Biconcave disc shape gives a large surface area (1); no nucleus, giving more space to carry oxygen/haemoglobin (1); contains haemoglobin, which binds to oxygen (1).', styles['ans']))
    s.append(Paragraph('<b>E3.</b> They help the blood clot at a wound (1).', styles['ans']))

    s.append(Paragraph('Section F &mdash; Apply it', styles['h2']))
    s.append(Paragraph('<b>F1.</b> Fewer red blood cells means less haemoglobin to carry oxygen (1); so less oxygen is transported to (respiring) body cells (1); less oxygen means less energy released by (aerobic) respiration (1).', styles['ans']))

    s.append(Paragraph(
        'Marking note: accept any scientifically correct alternative answer with the same reasoning, even if '
        'different from the example shown &mdash; award marks for a correctly linked point, not for matching '
        'these exact words.',
        styles['note']))

    doc.build(s)


if __name__ == '__main__':
    build_reference()
    build_test()
    build_answers()
    print('done')
