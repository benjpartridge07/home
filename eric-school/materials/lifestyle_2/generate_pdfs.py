# -*- coding: utf-8 -*-
"""Generate reference sheet, test, and answer PDFs for
Lifestyle & Health, Part 2: Hormones (AQA 8465 4.3.1, Foundation tier)."""

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
    doc = SimpleDocTemplate('lifestyle_2_reference.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Lifestyle &amp; Health: Hormones',
                 'Quick reference sheet &middot; Biology &middot; keep handy for revision')

    s.append(Paragraph('1. The endocrine system', styles['h2']))
    s.append(Paragraph('The <b>endocrine system</b> is made up of glands that secrete <b>hormones</b> directly into the bloodstream. A hormone is a chemical messenger that travels in the blood to a <b>target organ</b>, where it produces an effect. Key glands: pituitary (the "master gland"), pancreas (insulin &amp; glucagon), adrenal glands (adrenaline), ovaries/testes (reproductive hormones).', styles['body']))

    s.append(Paragraph('2. Hormones vs nerves', styles['h2']))
    s.append(table([
        [headcell('Feature'), headcell('Nervous system'), headcell('Hormonal system')],
        [cell('Signal'), cell('Electrical impulses along neurons'), cell('Chemicals (hormones) in the blood')],
        [cell('Speed'), cell('Very fast'), cell('Slower')],
        [cell('Effect'), cell('Short-lived, precise area'), cell('Longer-lasting, wide area')],
    ], col_widths=[28 * mm, 57 * mm, 58 * mm]))

    s.append(Paragraph('3. Controlling blood glucose concentration', styles['h2']))
    s.append(Paragraph('Blood glucose is monitored and controlled by the <b>pancreas</b>. After eating carbohydrate, blood glucose rises &rarr; the pancreas releases <b>insulin</b> &rarr; insulin causes cells (liver/muscle) to take up glucose, converting excess into <b>glycogen</b> for storage &rarr; blood glucose falls back to normal. (Beyond Foundation: when blood glucose is too low, the pancreas releases <b>glucagon</b>, which converts glycogen back into glucose &mdash; together these keep blood glucose steady by negative feedback.)', styles['body']))

    s.append(Paragraph('4. Type 1 &amp; Type 2 diabetes', styles['h2']))
    s.append(table([
        [headcell(''), headcell('Type 1'), headcell('Type 2')],
        [cell('Cause'), cell('Pancreas produces little/no insulin'), cell('Cells stop responding properly to insulin')],
        [cell('Risk factors'), cell('Not strongly linked to lifestyle'), cell('Obesity, poor diet, lack of exercise')],
        [cell('Treatment'), cell('Insulin injections; monitor blood glucose'), cell('Lifestyle changes; medication; insulin if needed')],
    ], col_widths=[28 * mm, 57 * mm, 58 * mm]))
    s.append(Paragraph('<b>Lifestyle link:</b> obesity, poor diet and inactivity increase the risk of Type 2 diabetes &mdash; the same lifestyle changes that reduce cardiovascular disease risk also reduce this risk.', styles['bodyb']))

    doc.build(s)


# ---------------------------------------------------------------- TEST

def q(number, text, marks):
    return [
        Paragraph(f'<b>{number}.</b> {text}', styles['qtext']),
        Paragraph(f'[{marks} mark{"s" if marks != 1 else ""}]', styles['marks']),
    ]


def build_test():
    doc = SimpleDocTemplate('lifestyle_2_test.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Lifestyle &amp; Health: Hormones', 'Test &middot; 37 marks total')

    s.append(table([[
        cell('Name: ________________________________'),
        cell('Date: ______________'),
        cell('Score: _____ / 37'),
    ]], col_widths=[75 * mm, 45 * mm, 40 * mm]))
    s.append(Spacer(1, 8))

    s.append(Paragraph('Section A &mdash; The endocrine system &amp; hormones vs nerves', styles['h2']))
    s += q('A1', 'What is the endocrine system?', 2)
    s.append(Spacer(1, 8))
    s += q('A2', 'What is a hormone?', 2)
    s.append(Spacer(1, 8))
    s += q('A3', 'Give two differences between how the nervous system and the hormonal system send signals around the body.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section B &mdash; Blood glucose regulation', styles['h2']))
    s += q('B1', 'Name the gland that monitors and controls blood glucose concentration.', 1)
    s.append(Spacer(1, 8))
    s += q('B2', 'Describe how insulin causes blood glucose concentration to fall after a meal.', 3)
    s.append(Spacer(1, 8))
    s += q('B3', 'What happens to excess glucose that is not immediately needed by cells?', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section C &mdash; Type 1 &amp; Type 2 diabetes', styles['h2']))
    s += q('C1', 'What causes Type 1 diabetes?', 2)
    s.append(Spacer(1, 8))
    s += q('C2', 'What causes Type 2 diabetes?', 2)
    s.append(Spacer(1, 8))
    s += q('C3', 'Describe how Type 1 diabetes is usually treated.', 2)
    s.append(Spacer(1, 8))
    s += q('C4', 'Describe how Type 2 diabetes is usually treated.', 2)
    s.append(Spacer(1, 8))
    s += q('C5', 'Explain why uncontrolled diabetes can increase the risk of other diseases, such as cardiovascular disease.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section D &mdash; Hormones, lifestyle &amp; health risk', styles['h2']))
    s += q('D1', 'Explain why obesity is a risk factor for Type 2 diabetes.', 2)
    s.append(Spacer(1, 8))
    s += q('D2', 'State two lifestyle factors, other than obesity, linked to a higher risk of Type 2 diabetes.', 2)
    s.append(Spacer(1, 8))
    s += q('D3', 'Explain why Type 1 diabetes cannot be prevented by lifestyle changes, unlike Type 2 diabetes.', 2)
    s.append(Spacer(1, 12))

    s.append(Paragraph('Section E &mdash; Apply it', styles['h2']))
    s += q('E1', 'Two patients are newly diagnosed with diabetes: Patient X has Type 1, Patient Y has Type 2. Compare the advice and treatment each patient is likely to be given.', 4)
    s.append(Spacer(1, 8))
    s += q('E2', 'A student says "insulin causes blood glucose to rise." Explain why this statement is incorrect, and correct it.', 3)
    s.append(Spacer(1, 8))
    s += q('E3', 'Suggest why regularly monitoring blood glucose concentration is important for someone with diabetes.', 2)

    doc.build(s)


# ---------------------------------------------------------------- ANSWERS

def build_answers():
    doc = SimpleDocTemplate('lifestyle_2_test_answers.pdf', pagesize=A4,
                             leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    s = []
    s += header('Lifestyle &amp; Health: Hormones', 'Answer sheet &middot; 37 marks total')

    s.append(Paragraph('Section A &mdash; The endocrine system &amp; hormones vs nerves', styles['h2']))
    s.append(Paragraph('<b>A1.</b> The system of glands that secrete hormones (1) directly into the bloodstream (1).', styles['ans']))
    s.append(Paragraph('<b>A2.</b> A chemical messenger (1) carried in the blood to a target organ, where it produces an effect (1).', styles['ans']))
    s.append(Paragraph('<b>A3.</b> Any two: nervous system uses electrical impulses along neurons, hormonal system uses chemicals in the blood (1); nervous responses are fast, hormonal responses are slower (1); nervous effects are short-lived/precise, hormonal effects are longer-lasting/widespread (1).', styles['ans']))

    s.append(Paragraph('Section B &mdash; Blood glucose regulation', styles['h2']))
    s.append(Paragraph('<b>B1.</b> Pancreas (1).', styles['ans']))
    s.append(Paragraph('<b>B2.</b> The pancreas detects the rise and releases insulin (1); insulin causes cells (e.g. liver/muscle) to take up glucose from the blood (1); blood glucose concentration falls back to normal (1).', styles['ans']))
    s.append(Paragraph('<b>B3.</b> It is converted into glycogen (1) and stored, e.g. in the liver/muscles (1).', styles['ans']))

    s.append(Paragraph('Section C &mdash; Type 1 &amp; Type 2 diabetes', styles['h2']))
    s.append(Paragraph('<b>C1.</b> The pancreas produces little or no insulin (1), so blood glucose cannot be properly controlled (1).', styles['ans']))
    s.append(Paragraph('<b>C2.</b> Body cells stop responding properly to insulin/become resistant to it (1), or the pancreas does not produce enough insulin (1).', styles['ans']))
    s.append(Paragraph('<b>C3.</b> Regular insulin injections (1), matched to diet and activity level, with blood glucose monitoring (1).', styles['ans']))
    s.append(Paragraph('<b>C4.</b> Lifestyle changes such as a healthier diet, more exercise and weight loss (1); medication and/or insulin injections if needed (1).', styles['ans']))
    s.append(Paragraph('<b>C5.</b> Blood glucose concentration stays too high for long periods (1); this can damage blood vessels and nerves, increasing the risk of further disease, e.g. cardiovascular disease (1).', styles['ans']))

    s.append(Paragraph('Section D &mdash; Hormones, lifestyle &amp; health risk', styles['h2']))
    s.append(Paragraph('<b>D1.</b> Carrying excess body fat makes cells less responsive to insulin/causes insulin resistance (1), so blood glucose is not controlled properly, increasing the risk of Type 2 diabetes (1).', styles['ans']))
    s.append(Paragraph('<b>D2.</b> Any two: poor diet, e.g. high in fat/sugar (1); lack of exercise (1); (accept family history/genetics with justification) (1).', styles['ans']))
    s.append(Paragraph('<b>D3.</b> Type 1 diabetes is caused by the pancreas producing little or no insulin (often an autoimmune response), not by lifestyle factors (1); Type 2 diabetes is strongly linked to lifestyle factors such as obesity, poor diet and inactivity, so lifestyle changes reduce the risk (1).', styles['ans']))

    s.append(Paragraph('Section E &mdash; Apply it', styles['h2']))
    s.append(Paragraph('<b>E1.</b> Patient X (Type 1): will likely need regular insulin injections (1) alongside monitoring blood glucose and matching insulin to diet/activity (1). Patient Y (Type 2): will likely be advised to make lifestyle changes first, e.g. improved diet, more exercise, weight loss (1), with medication and/or insulin added later if these are not enough to control blood glucose (1).', styles['ans']))
    s.append(Paragraph('<b>E2.</b> The statement is incorrect because insulin causes blood glucose concentration to fall, not rise (1); insulin does this by causing cells to take up glucose from the blood and by increasing conversion of glucose to glycogen for storage (1); it is glucagon, not insulin, that causes blood glucose to rise (1).', styles['ans']))
    s.append(Paragraph('<b>E3.</b> It shows whether blood glucose is being kept within a safe range (1), allowing insulin dose, diet or activity to be adjusted to avoid blood glucose being too high or too low (1).', styles['ans']))

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
