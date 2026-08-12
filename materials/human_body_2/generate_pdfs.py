# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Human Body Systems, Part 2: Digestion & Control (AQA 8465 4.2.1, Foundation tier)."""

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
    doc = SimpleDocTemplate('human_body_2_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Human Body Systems: Digestion &amp; Control',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('1. The digestive system', styles['h2']))
    s.append(Paragraph('Digestion breaks down large, insoluble food molecules into small, soluble molecules that can be absorbed into the blood.', styles['body']))
    s.append(table([
        [headcell('Organ'), headcell('What it does')],
        [cell('Mouth'), cell('Chews food; saliva contains amylase, which starts digesting starch')],
        [cell('Oesophagus'), cell('Muscular tube that pushes food down to the stomach')],
        [cell('Stomach'), cell('Churns food; produces acid (kills bacteria, right pH for protease) and protease')],
        [cell('Small intestine'), cell('Digestion completed here; digested food is absorbed into the blood')],
        [cell('Large intestine'), cell('Absorbs water; forms faeces')],
        [cell('Pancreas'), cell('Produces amylase, protease &amp; lipase, released into the small intestine')],
        [cell('Liver'), cell('Produces bile')],
    ], col_widths=[35 * mm, 108 * mm]))

    s.append(Paragraph('2. Enzymes &amp; bile', styles['h2']))
    s.append(Paragraph('Enzymes are <b>biological catalysts</b> &mdash; proteins that speed up reactions without being used up. Each has an active site shaped to fit one substrate (lock and key).', styles['body']))
    s.append(table([
        [headcell('Enzyme'), headcell('Breaks down'), headcell('Into')],
        [cell('Amylase'), cell('Starch'), cell('Sugars')],
        [cell('Protease'), cell('Protein'), cell('Amino acids')],
        [cell('Lipase'), cell('Lipids (fats)'), cell('Fatty acids + glycerol')],
    ], col_widths=[35 * mm, 50 * mm, 58 * mm]))
    s.append(Paragraph('<b>Bile</b> (made in the liver) is not an enzyme. It <b>neutralises</b> stomach acid, giving enzymes in the small intestine the right (alkaline) pH, and <b>emulsifies</b> fats into tiny droplets, increasing the surface area for lipase.', styles['body']))

    s.append(Paragraph('3. The nervous system &amp; reflexes', styles['h2']))
    s.append(Paragraph('A <b>reflex</b> is a fast, automatic response that does not involve conscious thought. Pathway:', styles['body']))
    s.append(Paragraph('<b>stimulus &rarr; receptor &rarr; sensory neuron &rarr; relay neuron (spinal cord) &rarr; motor neuron &rarr; effector &rarr; response</b>', styles['bodyb']))
    s.append(Paragraph('A <b>synapse</b> is the gap between two neurons; a chemical is released to carry the signal across it. Reflexes are fast because the signal is processed in the spinal cord, not the brain.', styles['body']))

    s.append(Paragraph('4. The endocrine system', styles['h2']))
    s.append(Paragraph('Hormones are chemical messengers released directly into the blood by glands, producing an effect at a target organ. Slower to start than nerves, but longer-lasting.', styles['body']))
    s.append(table([
        [headcell('Gland'), headcell('Hormone'), headcell('Effect')],
        [cell('Pituitary gland'), cell('Several'), cell('"Master gland" &mdash; controls other glands')],
        [cell('Pancreas'), cell('Insulin'), cell('Reduces blood glucose concentration')],
        [cell('Adrenal glands'), cell('Adrenaline'), cell('"Fight or flight" response')],
        [cell('Thyroid gland'), cell('Thyroxine'), cell('Regulates metabolic rate')],
    ], col_widths=[35 * mm, 30 * mm, 78 * mm]))
    s.append(Paragraph('<b>Nervous vs hormonal:</b> nervous signals are electrical, travel along neurons &mdash; fast, short-lived. Hormonal signals are chemical, travel in the blood &mdash; slower, longer-lasting.', styles['bodyb']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('human_body_2_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Human Body Systems: Digestion &amp; Control', 'Test &middot; 37 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 37'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Digestion &amp; enzymes', styles['h2']))
    s += q('A1', 'Name the organ that produces bile.', 1)
    s.append(Spacer(1, 8))
    s += q('A2', 'Complete: an enzyme is a __________ that speeds up a reaction without being used up.', 1)
    s.append(Spacer(1, 8))
    s += q('A3', 'Name the three digestive enzymes covered in this lesson, and state what each one breaks food down into.', 6)
    s.append(Spacer(1, 8))
    s += q('A4', 'Explain two roles of bile in digestion.', 4)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; The nervous system', styles['h2']))
    s += q('B1', 'A stimulus is detected by a receptor and a response is produced by an effector. Name, in order, the three types of neuron involved in a reflex arc between these two points.', 3)
    s.append(Spacer(1, 8))
    s += q('B2', 'What is a synapse?', 2)
    s.append(Spacer(1, 8))
    s += q('B3', 'Explain why reflexes are useful to the body.', 2)
    s.append(Spacer(1, 8))
    s += q('B4', 'Explain why reflex responses are faster than responses that involve conscious thought.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; The endocrine system', styles['h2']))
    s += q('C1', 'What is a hormone?', 2)
    s.append(Spacer(1, 8))
    s += q('C2', 'Name the gland often described as the "master gland".', 1)
    s.append(Spacer(1, 8))
    s += q('C3', 'Name the hormone that reduces blood glucose concentration, and the organ that produces it.', 2)
    s.append(Spacer(1, 8))
    s += q('C4', 'State two differences between nervous and hormonal communication.', 4)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Apply it', styles['h2']))
    s += q('D1', 'A person accidentally touches a hot iron and pulls their hand away before they feel any pain. Using your knowledge of the reflex arc, explain why this response happens so quickly.', 3)
    s.append(Spacer(1, 8))
    s += q('D2', "Explain why someone whose pancreas is damaged might have unusually high blood glucose levels after eating a meal.", 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('human_body_2_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Human Body Systems: Digestion &amp; Control', 'Answer sheet &middot; 37 marks total')

    s.append(Paragraph('Section A &mdash; Digestion &amp; enzymes', styles['h2']))
    s.append(Paragraph('<b>A1.</b> Liver (1).', styles['ans']))
    s.append(Paragraph('<b>A2.</b> Biological catalyst / protein (1).', styles['ans']))
    s.append(Paragraph('<b>A3.</b> Amylase &rarr; sugars (2); protease &rarr; amino acids (2); lipase &rarr; fatty acids + glycerol (2).', styles['ans']))
    s.append(Paragraph('<b>A4.</b> Any two, 2 marks each: neutralises stomach acid (1), giving the right/alkaline pH for enzymes in the small intestine (1); emulsifies fats into tiny droplets (1), increasing the surface area for lipase to act on (1).', styles['ans']))

    s.append(Paragraph('Section B &mdash; The nervous system', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Sensory neuron (1), relay neuron (1), motor neuron (1).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> The gap between two neurons (1); a chemical is released to carry the signal across it, triggering a new impulse in the next neuron (1).', styles['ans']))
    s.append(Paragraph('<b>B3.</b> They produce a very fast response (1), protecting the body from harm/damage before the brain has time to process the stimulus (1).', styles['ans']))
    s.append(Paragraph('<b>B4.</b> The impulse is processed by a relay neuron in the spinal cord (1) rather than travelling to the brain and back, so no conscious thought/decision-making is needed (1).', styles['ans']))

    s.append(Paragraph('Section C &mdash; The endocrine system', styles['h2']))
    s.append(Paragraph('<b>C1.</b> A chemical messenger (1), released directly into the blood by a gland, that produces an effect at a target organ (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> Pituitary gland (1).', styles['ans']))
    s.append(Paragraph('<b>C3.</b> Insulin (1); produced by the pancreas (1).', styles['ans']))
    s.append(Paragraph('<b>C4.</b> Any two, 2 marks each: nervous signals are electrical, hormonal signals are chemical (1) [explanation (1)]; nervous is fast-acting, hormonal is slower (1) [explanation (1)]; nervous effects are short-lived, hormonal effects last longer (1) [explanation (1)].', styles['ans']))

    s.append(Paragraph('Section D &mdash; Apply it', styles['h2']))
    s.append(Paragraph('<b>D1.</b> The stimulus (heat/pain) is detected by a receptor and passed along a sensory neuron to the spinal cord (1); a relay neuron passes the impulse straight to a motor neuron, without going via the brain (1); this means the muscle (effector) responds before the brain registers pain, because it is a reflex, not a conscious decision (1).', styles['ans']))
    s.append(Paragraph('<b>D2.</b> The pancreas normally produces insulin (1); insulin reduces blood glucose concentration, e.g. by causing glucose to be stored as glycogen (1); a damaged pancreas cannot produce enough insulin, so glucose is not removed from the blood effectively and levels stay high (1).', styles['ans']))

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
