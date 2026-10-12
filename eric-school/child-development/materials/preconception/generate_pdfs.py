"""Builds the pre-conception health homework help sheet (OCR J809, R057 Topic 1.1).

Run:  python generate_pdfs.py
Output: preconception_homework_help.pdf
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether, PageBreak)

PINK = colors.HexColor('#db2777')
PINK_SOFT = colors.HexColor('#fce7f3')
BLUE_SOFT = colors.HexColor('#e8f0fe')
BLUE = colors.HexColor('#1d4ed8')
GREEN_SOFT = colors.HexColor('#e7f6ec')
GREEN = colors.HexColor('#15803d')
AMBER_SOFT = colors.HexColor('#fef3e2')
AMBER = colors.HexColor('#b45309')
DIM = colors.HexColor('#5b616e')

TITLE = ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=PINK)
SUB = ParagraphStyle('sub', fontName='Helvetica', fontSize=10, leading=13, textColor=DIM)
H1 = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=PINK,
                    spaceBefore=10, spaceAfter=4)
H2 = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=12, leading=15, spaceBefore=8, spaceAfter=3)
BODY = ParagraphStyle('body', fontName='Helvetica', fontSize=10.5, leading=14.5, spaceAfter=4)
SMALL = ParagraphStyle('small', fontName='Helvetica', fontSize=9.5, leading=12.5)
CELL = ParagraphStyle('cell', fontName='Helvetica', fontSize=9.5, leading=12.5)
CELLB = ParagraphStyle('cellb', fontName='Helvetica-Bold', fontSize=10, leading=13)


def box(paras, bg, edge, title=None, title_color=None):
    """A coloured call-out box holding a list of flowables."""
    inner = []
    if title:
        inner.append(Paragraph(title, ParagraphStyle('bt', parent=CELLB, textColor=title_color or edge)))
        inner.append(Spacer(1, 2))
    inner += paras
    t = Table([[inner]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LINEBEFORE', (0, 0), (0, -1), 3, edge),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def p(text, style=BODY):
    return Paragraph(text, style)


def model(text):
    return box([p(text, SMALL)], GREEN_SOFT, GREEN, 'Model answer')


def explain(text):
    return box([p(text, SMALL)], BLUE_SOFT, BLUE, 'What this really means')


def tip(text):
    return box([p(text, SMALL)], AMBER_SOFT, AMBER, 'Exam tip')


# Task 2: one row per factor -> (factor, women, men, remember)
FACTORS = [
    ('Weight',
     'Being <b>overweight</b> or <b>underweight</b> can upset the hormones that control '
     '<b>ovulation</b> (releasing an egg each month), so periods can become irregular and '
     'it is harder to get pregnant. Obesity also raises the risk of <b>miscarriage</b> and '
     '<b>gestational diabetes</b>. A healthy BMI is 18.5 to 24.9.',
     'Being overweight can <b>lower testosterone</b> and reduce the <b>number and quality of '
     'sperm</b>, so there is less chance of a sperm reaching and fertilising the egg.',
     'Weight affects <b>hormones</b>. Hormones control eggs and sperm.'),
    ('Smoking',
     'The chemicals in cigarettes <b>damage eggs</b> and the fallopian tubes, so it can take '
     'longer to conceive. It raises the risk of <b>miscarriage</b> and <b>ectopic pregnancy</b> '
     '(the baby growing outside the womb) and can bring on the menopause earlier.',
     'Smoking <b>lowers sperm count</b>, makes sperm swim less well (poor <b>motility</b>) and '
     'can <b>damage the DNA</b> inside sperm. It can also cause erection problems.',
     'Smoking damages <b>both</b> the egg and the sperm. Second-hand smoke counts too.'),
    ('Drinking alcohol',
     'Alcohol can <b>disrupt the menstrual cycle</b> and reduce fertility. A woman may not know '
     'she is pregnant for several weeks, and alcohol in that time can harm the baby and cause '
     '<b>Fetal Alcohol Spectrum Disorder (FASD)</b>. The NHS advice is <b>no alcohol</b> when '
     'trying for a baby.',
     'Heavy drinking can <b>lower testosterone</b>, reduce <b>sperm quality and count</b> and '
     'cause impotence (problems having sex). Men are advised to stay within <b>14 units a week</b>.',
     'For women the safest amount is <b>none</b>. For men, keep it low.'),
    ('Taking recreational drugs',
     'Drugs such as cannabis and cocaine can <b>stop or disrupt ovulation</b>. If she becomes '
     'pregnant, drugs pass to the baby and can cause <b>low birth weight</b>, '
     '<b>premature birth</b> and <b>withdrawal symptoms</b> in the newborn.',
     'Cannabis can <b>reduce sperm count and quality</b>. <b>Anabolic steroids</b> (used for '
     'bodybuilding) can stop sperm production altogether. Cocaine also damages sperm.',
     'Drugs can <b>switch off</b> egg release and sperm production.'),
    ('Parental age',
     'A woman is born with all her eggs, and they get <b>fewer and lower quality</b> with age. '
     'Fertility starts to fall in the early 30s and <b>faster after 35</b>. Older mothers have '
     'a higher risk of miscarriage and of conditions such as <b>Down\'s syndrome</b>. Very young '
     'mothers (teenagers) have higher risks too, such as premature birth.',
     'Men make new sperm all their lives, so fertility falls <b>more slowly</b>. From about '
     '<b>40</b>, sperm quality drops, it can take longer to conceive, and there is a slightly '
     'higher risk of miscarriage and of some conditions in the baby.',
     'Age is the <b>only</b> factor here you <b>cannot change</b>.'),
]


def task2_table():
    head = [p('<b>Factor</b>', CELL), p('<b>Effect on women</b>', CELL), p('<b>Effect on men</b>', CELL)]
    rows = [head]
    for name, women, men, remember in FACTORS:
        rows.append([
            [p('<b>%s</b>' % name, CELL), Spacer(1, 4),
             p('<font color="#b45309"><b>Remember:</b></font> %s' % remember, SMALL)],
            p(women, CELL), p(men, CELL)])
    t = Table(rows, colWidths=[38 * mm, 66 * mm, 66 * mm], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PINK_SOFT),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d6d9e0')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t


def rank_table():
    rows = [[p('<b>Rank</b>', CELL), p('<b>Factor</b>', CELL), p('<b>Why it goes here</b>', CELL)],
            [p('1', CELLB), p('<b>Smoking</b>', CELL),
             p('It harms <b>both</b> partners at once (eggs <b>and</b> sperm), it is very common, and '
               'it also raises the risk of miscarriage and ectopic pregnancy.', CELL)],
            [p('2', CELLB), p('<b>Taking recreational drugs</b>', CELL),
             p('Some drugs can <b>stop</b> ovulation or sperm production completely (for example '
               'steroids), which is a bigger effect than just lowering it.', CELL)],
            [p('3', CELLB), p('<b>Weight</b>', CELL),
             p('It affects hormones in both partners and is very common, but the effect builds up '
               'gradually and can be improved by changing diet and exercise.', CELL)],
            [p('4', CELLB), p('<b>Drinking alcohol</b>', CELL),
             p('Heavy drinking harms fertility, but light drinking has a smaller effect on '
               '<i>conceiving</i>. Its biggest danger is to the baby once pregnant.', CELL)]]
    t = Table(rows, colWidths=[14 * mm, 42 * mm, 114 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PINK_SOFT),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d6d9e0')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(DIM)
    canvas.drawString(20 * mm, 10 * mm, 'Child Development (OCR J809) - R057 Topic 1.1 Pre-conception health - homework help')
    canvas.drawRightString(190 * mm, 10 * mm, 'Page %d' % doc.page)
    canvas.restoreState()


def build_help():
    doc = SimpleDocTemplate('preconception_homework_help.pdf', pagesize=A4,
                            leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=16 * mm, bottomMargin=16 * mm,
                            title='Pre-conception Health - Homework Help')
    s = []
    s.append(p('Pre-conception Health: Homework Help', TITLE))
    s.append(p('Year 10 Child Development &middot; Topic 1.1: Factors affecting pre-conception health '
               'for women and men', SUB))
    s.append(Spacer(1, 6))
    s.append(box([p('Read each <b>explanation</b> first so you understand it, then write the answer on '
                    'your sheet <b>in your own words</b>. Your teacher wants to see that <i>you</i> '
                    'understand it, and putting it in your own words is how it sticks in your memory '
                    'for the exam. Then try the quiz on the Child Development page.', SMALL)],
                 PINK_SOFT, PINK, 'How to use this sheet'))

    # ---------------- Task 1 ----------------
    s.append(p('Task 1: Why does pre-conception health matter?', H1))
    s.append(p('a) What is meant by the term "pre-conception health"?', H2))
    s.append(explain(
        'Break the word up. <b>Pre</b> means <i>before</i>. <b>Conception</b> is the moment a sperm '
        'fertilises an egg and a baby starts to grow. So <b>pre-conception health</b> is how healthy '
        'the mum <b>and</b> dad are <b>before</b> the baby is made. It is about their bodies '
        '(weight, diet, illnesses) and their lifestyle choices (smoking, drinking, drugs).'))
    s.append(Spacer(1, 4))
    s.append(model(
        'Pre-conception health is the physical and mental health of <b>both the man and the woman</b> '
        'in the months <b>before they try to conceive</b> a baby. It includes their lifestyle choices, '
        'such as diet, weight, exercise, smoking, alcohol and drug use, and steps like taking '
        '<b>folic acid</b> and checking vaccinations, to give them the best chance of getting '
        'pregnant and having a healthy baby.'))

    s.append(p('b) Why is good pre-conception health important? (4 marks)', H2))
    s.append(explain(
        'It is worth <b>4 marks</b>, so give <b>4 separate reasons</b>. Each one needs a short '
        '<b>"because"</b> explaining it. The big idea is that the baby\'s body starts forming '
        '<b>very early</b>, often before anyone knows a baby is on the way. And sperm take '
        '<b>about 2 to 3 months</b> to grow, so the dad\'s health months earlier matters too.'))
    s.append(Spacer(1, 4))
    s.append(model(
        '1. It <b>increases fertility</b>, so the couple are more likely to conceive, because healthy '
        'eggs and sperm are more likely to meet and fertilise.<br/>'
        '2. It <b>reduces the risk of miscarriage, premature birth and low birth weight</b>, because '
        'the mother\'s body is in the best condition to support a pregnancy.<br/>'
        '3. It <b>reduces the risk of birth defects</b>, because the baby\'s brain, spine and heart '
        'form in the first few weeks, often <b>before the woman knows she is pregnant</b>. For example, '
        'taking <b>folic acid</b> lowers the risk of <b>spina bifida</b>.<br/>'
        '4. The <b>man\'s health matters too</b>, because sperm take about <b>3 months</b> to develop, '
        'so smoking, alcohol or drugs in that time can damage the sperm that make the baby.'))
    s.append(Spacer(1, 4))
    s.append(tip('Mentioning the <b>man</b> as well as the woman is an easy way to pick up marks, '
                 'because lots of students forget about him.'))

    # ---------------- Task 2 ----------------
    s.append(PageBreak())
    s.append(p('Task 2: Lifestyle factors and fertility (10 marks)', H1))
    s.append(p('There are 5 factors and 2 columns, so 10 boxes and probably <b>1 mark per box</b>. '
               'For each box, say <b>what happens in the body</b> and <b>how that makes conceiving '
               'harder</b>. Key words are in <b>bold</b>. Try to use them in your answers.', BODY))
    s.append(task2_table())
    s.append(Spacer(1, 6))
    s.append(box([p('<b>Fertility</b> = being able to get pregnant (women) or get someone pregnant '
                    '(men).<br/><b>Ovulation</b> = when an ovary releases an egg, about once a month.<br/>'
                    '<b>Sperm count</b> = how many sperm there are. <b>Motility</b> = how well they swim.<br/>'
                    '<b>Miscarriage</b> = losing a baby before 24 weeks of pregnancy.<br/>'
                    '<b>Ectopic pregnancy</b> = the baby starts growing outside the womb, usually in a '
                    'fallopian tube. It is dangerous and the pregnancy cannot continue.', SMALL)],
                 BLUE_SOFT, BLUE, 'Key words explained'))

    # ---------------- Task 3 ----------------
    s.append(PageBreak())
    s.append(p('Task 3: Ranking activity', H1))
    s.append(p('Which factor has the greatest effect on a couple\'s ability to conceive?', H2))
    s.append(explain(
        'This is an <b>opinion</b> question, so there is <b>no single right answer</b>. Your teacher '
        'is marking your <b>reasons</b>, not just the order. To decide, ask three questions about each '
        'factor:<br/>'
        '&bull; Does it affect <b>both</b> the man and the woman, or just one?<br/>'
        '&bull; Does it <b>stop</b> fertility completely, or just <b>lower</b> it?<br/>'
        '&bull; How <b>common</b> is it?<br/>'
        'The sheet lists 4 factors in the ranking table. Age is not in it, probably because it is '
        'the one factor nobody can change.'))
    s.append(Spacer(1, 6))
    s.append(p('Here is <b>one sensible ranking</b> with reasons. You can disagree, as long as you '
               'explain why.', BODY))
    s.append(rank_table())
    s.append(Spacer(1, 6))
    s.append(box([p('Write one sentence for your number 1, like this:<br/>'
                    '<i>"I think <b>smoking</b> has the greatest effect because it damages <b>both</b> '
                    'the woman\'s eggs and the man\'s sperm, so it lowers the fertility of both '
                    'partners at the same time."</i>', SMALL)],
                 AMBER_SOFT, AMBER, 'How to write your answer'))

    s.append(Spacer(1, 10))
    s.append(p('Sources: NHS (nhs.uk: "Trying to get pregnant" and "Infertility"), Tommy\'s '
               '(tommys.org: "Planning for pregnancy"), OCR Cambridge Nationals Child Development '
               'J809 specification.', SMALL))

    doc.build(s, onFirstPage=footer, onLaterPages=footer)


if __name__ == '__main__':
    build_help()
    print('Built preconception_homework_help.pdf')
