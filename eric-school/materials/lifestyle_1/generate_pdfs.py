# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Lifestyle & Health, Part 1: Disease Risk (AQA 8465 4.3.1, Foundation tier)."""

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
    doc = SimpleDocTemplate('lifestyle_1_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Lifestyle &amp; Health: Disease Risk',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('1. Communicable vs non-communicable disease', styles['h2']))
    s.append(Paragraph('A <b>communicable</b> disease is caused by a pathogen and can spread between people. A <b>non-communicable</b> disease cannot spread between people &mdash; it develops from genetic, lifestyle and/or environmental factors, often over a long time (e.g. cardiovascular disease, type 2 diabetes, some cancers, chronic lung disease).', styles['body']))

    s.append(Paragraph('2. Risk factors for non-communicable disease', styles['h2']))
    s.append(Paragraph('A <b>risk factor</b> increases the probability of developing a disease &mdash; it does not guarantee it.', styles['body']))
    s.append(table([
        [headcell('Risk factor'), headcell('Linked to')],
        [cell('Smoking'), cell('Lung disease, lung cancer, cardiovascular disease')],
        [cell('Poor diet (fat/salt/sugar)'), cell('Obesity, type 2 diabetes, cardiovascular disease')],
        [cell('Excess alcohol'), cell('Liver disease, some cancers')],
        [cell('Lack of exercise'), cell('Obesity, cardiovascular disease, type 2 diabetes')],
        [cell('Obesity'), cell('Type 2 diabetes, cardiovascular disease, some cancers')],
    ], col_widths=[50 * mm, 93 * mm]))
    s.append(Paragraph('<b>Correlation is not cause:</b> a link between a factor and a disease doesn’t prove the factor causes it &mdash; look for a plausible mechanism and repeated studies.', styles['bodyb']))

    s.append(Paragraph('3. Cardiovascular disease &amp; treatments', styles['h2']))
    s.append(Paragraph('In coronary heart disease, fatty deposits (atheroma) narrow the coronary arteries, restricting blood flow to the heart muscle.', styles['body']))
    s.append(table([
        [headcell('Treatment'), headcell('What it does')],
        [cell('Statins'), cell('Drugs that reduce blood cholesterol, slowing fatty deposit build-up')],
        [cell('Stents'), cell('Mesh tubes that hold a narrowed artery open')],
        [cell('Bypass surgery'), cell('A healthy vessel bypasses the blocked section of a coronary artery')],
        [cell('Artificial hearts/valves'), cell('Mechanical devices that pump blood or replace a faulty valve')],
        [cell('Heart transplant'), cell('A diseased heart is replaced with a healthy donor heart')],
    ], col_widths=[50 * mm, 93 * mm]))
    s.append(Paragraph('<b>Evaluate:</b> drugs/stents are less invasive but ongoing or can narrow again; surgery/transplant is more direct but carries surgical risk and donor hearts are scarce.', styles['bodyb']))

    s.append(Paragraph('4. Homeostasis &mdash; the big idea', styles['h2']))
    s.append(Paragraph('<b>Homeostasis</b> is the maintenance of a constant internal environment (e.g. body temperature, blood glucose, water content). Pattern: receptor detects a change &rarr; coordination system (nerves/hormones) &rarr; effector responds to restore the normal level. Detailed hormone control (e.g. insulin) is covered in Part 2.', styles['body']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('lifestyle_1_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Lifestyle &amp; Health: Disease Risk', 'Test &middot; 37 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 37'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; Communicable &amp; non-communicable disease', styles['h2']))
    s += q('A1', 'What is a communicable disease?', 2)
    s.append(Spacer(1, 8))
    s += q('A2', 'What is a non-communicable disease? Give one example.', 3)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Risk factors', styles['h2']))
    s += q('B1', 'State three lifestyle risk factors linked to non-communicable disease.', 3)
    s.append(Spacer(1, 8))
    s += q('B2', 'Name two diseases that smoking is a risk factor for.', 2)
    s.append(Spacer(1, 8))
    s += q('B3', 'A study finds that people who eat more processed food are more likely to develop type 2 diabetes. Explain why this does not prove that processed food causes type 2 diabetes.', 3)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; Cardiovascular disease &amp; treatment', styles['h2']))
    s += q('C1', 'Describe what happens in the arteries in coronary heart disease.', 2)
    s.append(Spacer(1, 8))
    s += q('C2', 'Describe how a stent treats coronary heart disease.', 2)
    s.append(Spacer(1, 8))
    s += q('C3', 'Explain how statins help to treat cardiovascular disease.', 2)
    s.append(Spacer(1, 8))
    s += q('C4', 'Evaluate the use of a heart transplant compared with an artificial heart for a patient with severe heart failure.', 4)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Homeostasis', styles['h2']))
    s += q('D1', 'What is homeostasis?', 2)
    s.append(Spacer(1, 8))
    s += q('D2', 'Give two examples of conditions the body keeps constant inside itself.', 2)
    s.append(Spacer(1, 8))
    s += q('D3', 'Describe the general pattern by which the body responds to a change and restores the normal level.', 3)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section E &mdash; Apply it', styles['h2']))
    s += q('E1', 'A patient with narrowed coronary arteries is offered either statins or a stent. Suggest one advantage and one disadvantage of each option.', 4)
    s.append(Spacer(1, 8))
    s += q('E2', 'Explain why someone who smokes, eats a poor diet, and does little exercise is at greater risk of cardiovascular disease than someone who does none of these things.', 3)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('lifestyle_1_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Lifestyle &amp; Health: Disease Risk', 'Answer sheet &middot; 37 marks total')

    s.append(Paragraph('Section A &mdash; Communicable &amp; non-communicable disease', styles['h2']))
    s.append(Paragraph('<b>A1.</b> A disease caused by a pathogen (1) that can be spread from person to person (1).', styles['ans']))
    s.append(Paragraph('<b>A2.</b> A disease that cannot be spread between people (1), caused by genetic/lifestyle/environmental factors (1); e.g. cardiovascular disease / type 2 diabetes / cancer / chronic lung disease (1).', styles['ans']))

    s.append(Paragraph('Section B &mdash; Risk factors', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Any three: smoking (1); poor diet (1); excess alcohol (1); lack of exercise (1); obesity (1).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> Any two: lung disease (1); lung cancer (1); cardiovascular disease (1).', styles['ans']))
    s.append(Paragraph('<b>B3.</b> This only shows a correlation between the two things (1); it does not show a mechanism/cause (1); another linked factor could explain both (e.g. those who eat more processed food may also exercise less) (1).', styles['ans']))

    s.append(Paragraph('Section C &mdash; Cardiovascular disease &amp; treatment', styles['h2']))
    s.append(Paragraph('<b>C1.</b> Fatty deposits (atheroma) build up in the artery walls (1), narrowing them and restricting blood flow to the heart muscle (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> A stent (mesh tube) is inserted into the narrowed artery (1) and holds it open, restoring blood flow (1).', styles['ans']))
    s.append(Paragraph('<b>C3.</b> Statins reduce blood cholesterol level (1), slowing the rate at which fatty deposits build up in the arteries (1).', styles['ans']))
    s.append(Paragraph('<b>C4.</b> Any two points each, up to 4: heart transplant &mdash; can fully restore normal heart function (1) but carries major surgical risk and donor hearts are scarce/there may be a long wait (1); artificial heart &mdash; can be fitted more quickly / used as a bridge to transplant (1) but is mechanical and may wear out, fail, or increase risk of blood clots (1).', styles['ans']))

    s.append(Paragraph('Section D &mdash; Homeostasis', styles['h2']))
    s.append(Paragraph('<b>D1.</b> The maintenance of a constant internal environment (1), despite changes inside or outside the body (1).', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Any two: body temperature (1); blood glucose concentration (1); water content (1).', styles['ans']))
    s.append(Paragraph('<b>D3.</b> A receptor detects a change away from the normal level (1); a coordination system (nerves or hormones) processes this (1); an effector responds to bring the level back to normal (1).', styles['ans']))

    s.append(Paragraph('Section E &mdash; Apply it', styles['h2']))
    s.append(Paragraph('<b>E1.</b> Statins: advantage &mdash; no surgery needed (1); disadvantage &mdash; must be taken long-term and can cause side effects (1). Stent: advantage &mdash; restores blood flow directly/quickly (1); disadvantage &mdash; involves a surgical procedure with associated risks (1).', styles['ans']))
    s.append(Paragraph('<b>E2.</b> Each of these is a separate risk factor for cardiovascular disease (1); having multiple risk factors at once increases the overall probability of developing the disease (1), because each one adds an additional way the heart/blood vessels can be damaged, e.g. narrowed arteries plus increased strain from obesity (1).', styles['ans']))

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
