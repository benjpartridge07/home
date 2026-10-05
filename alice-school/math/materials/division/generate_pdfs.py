"""Builds Alice's Year 6 division PDFs: a reference sheet, 3 practice tests and their answers.

Run:  python generate_pdfs.py
Every answer is worked out by the code (and checked with asserts), so the answer sheets can't
contain arithmetic slips. Follows the Year 6 National Curriculum / White Rose order: short division,
dividing by 2-digit numbers, division using factors, long division, and remainders in context.
"""
from fractions import Fraction
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = A4
TEAL = HexColor('#0e9488')
TEAL_SOFT = HexColor('#e3f7f4')
AMBER = HexColor('#b45309')
AMBER_SOFT = HexColor('#fef3c7')
GREY = HexColor('#5b616e')
GRID = HexColor('#d6e4e2')
M = 42  # page margin


def fmt(n):
    return f'{n:,}'


# ---------------------------------------------------------------- drawing helpers

def header(c, title, sub=None, name_line=False):
    c.setFillColor(TEAL)
    c.rect(0, H - 78, W, 78, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 22)
    c.drawString(M, H - 42, title)
    if sub:
        c.setFont('Helvetica', 11)
        c.drawString(M, H - 62, sub)
    if name_line:
        c.setFont('Helvetica', 11)
        c.drawRightString(W - M, H - 42, 'Name: ____________________')
        c.drawRightString(W - M, H - 62, 'Date: ______________')
    c.setFillColor(black)


def footer(c, text):
    c.setFont('Helvetica', 8)
    c.setFillColor(GREY)
    c.drawString(M, 22, text)
    c.drawRightString(W - M, 22, f'Page {c.getPageNumber()}')
    c.setFillColor(black)


def section(c, y, text, colour=TEAL):
    c.setFillColor(colour)
    c.roundRect(M, y - 6, W - 2 * M, 24, 6, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(M + 10, y + 1, text)
    c.setFillColor(black)
    return y - 26


def para(c, x, y, text, size=11, width=None, font='Helvetica', leading=None, colour=black):
    """Simple word-wrapping text. Supports **bold** segments. Returns the y below the text."""
    width = width or (W - M - x)
    leading = leading or size * 1.35
    bold_font = font + '-Bold' if font == 'Helvetica' else font
    # Words are lists of (text, bold) runs, so "**0**2" or "**remainder**." stay joined with no gap
    words, cur, bold = [], [], False
    for ch in text.replace('**', '\x00'):
        if ch == '\x00':
            bold = not bold
        elif ch == ' ':
            if cur:
                words.append(cur)
            cur = []
        elif cur and cur[-1][1] == bold:
            cur[-1] = (cur[-1][0] + ch, bold)
        else:
            cur.append((ch, bold))
    if cur:
        words.append(cur)
    space = c.stringWidth(' ', font, size)

    def word_w(wd):
        return sum(c.stringWidth(t, bold_font if b else font, size) for t, b in wd)

    def flush(line, y):
        xx = x
        c.setFillColor(colour)
        for wd in line:
            for t, b in wd:
                f = bold_font if b else font
                c.setFont(f, size)
                c.drawString(xx, y, t)
                xx += c.stringWidth(t, f, size)
            xx += space
        c.setFillColor(black)

    line, line_w = [], 0
    for wd in words:
        ww = word_w(wd)
        if line and line_w + ww > width:
            flush(line, y)
            y -= leading
            line, line_w = [], 0
        line.append(wd)
        line_w += ww + space
    if line:
        flush(line, y)
        y -= leading
    return y


def frac(c, x, y, num, den, size=12, whole=None):
    """Draws an optional whole number and a stacked fraction with its baseline at y. Returns end x."""
    if whole is not None:
        c.setFont('Helvetica-Bold', size + 2)
        c.drawString(x, y, str(whole))
        x += c.stringWidth(str(whole), 'Helvetica-Bold', size + 2) + 3
    c.setFont('Helvetica-Bold', size)
    wn, wd = c.stringWidth(str(num), 'Helvetica-Bold', size), c.stringWidth(str(den), 'Helvetica-Bold', size)
    fw = max(wn, wd) + 4
    c.drawCentredString(x + fw / 2, y + size * 0.55, str(num))
    c.setLineWidth(1)
    c.line(x, y + size * 0.38, x + fw, y + size * 0.38)
    c.drawCentredString(x + fw / 2, y - size * 0.62, str(den))
    return x + fw


def bus_stop_frame(c, x, y, divisor, ndigits, cw, size):
    """Divisor outside, line over the dividend. x,y = baseline of the dividend's first digit column."""
    c.setFont('Helvetica-Bold', size)
    c.drawRightString(x - 8, y, str(divisor))
    c.setLineWidth(1.6)
    top = y + size * 1.05
    c.line(x - 4, top, x + ndigits * cw, top)
    c.line(x - 4, top, x - 4, y - size * 0.35)


def short_division(c, x, y, dividend, divisor, cw=22, size=17, show_answer=True):
    """Bus stop layout with small carried digits. Returns (quotient, remainder)."""
    digits = str(dividend)
    bus_stop_frame(c, x, y, divisor, len(digits), cw, size)
    carry, started, q_str = 0, False, ''
    for i, d in enumerate(digits):
        cx = x + i * cw + cw / 2
        if carry:
            c.setFont('Helvetica', size * 0.55)
            c.setFillColor(AMBER)
            c.drawRightString(cx - c.stringWidth(d, 'Helvetica-Bold', size) / 2 - 1, y + size * 0.45, str(carry))
            c.setFillColor(black)
        c.setFont('Helvetica-Bold', size)
        c.drawCentredString(cx, y, d)
        cur = carry * 10 + int(d)
        q = cur // divisor
        carry = cur - q * divisor
        if q or started:
            started = True
            q_str += str(q)
            if show_answer:
                c.setFillColor(TEAL)
                c.drawCentredString(cx, y + size * 1.35, str(q))
                c.setFillColor(black)
    if carry and show_answer:
        c.setFillColor(TEAL)
        c.setFont('Helvetica-Bold', size * 0.8)
        c.drawString(x + len(digits) * cw + 4, y + size * 1.35, f'r {carry}')
        c.setFillColor(black)
    return int(q_str or 0), carry


def long_division(c, x, y, dividend, divisor, cw=22, size=16):
    """Full long division layout: subtract, then bring the next digit down (brought-down digit in amber)."""
    digits = str(dividend)
    n = len(digits)
    bus_stop_frame(c, x, y, divisor, n, cw, size)
    c.setFont('Helvetica-Bold', size)
    for i, d in enumerate(digits):
        c.drawCentredString(x + i * cw + cw / 2, y, d)
    row_h = size * 1.45
    ry = y
    cur, started = 0, False
    for i, d in enumerate(digits):
        cur = cur * 10 + int(d) if started else cur * 10 + int(d)
        if not started and cur < divisor and i < n - 1:
            continue
        started = True
        q = cur // divisor
        c.setFillColor(TEAL)
        c.setFont('Helvetica-Bold', size)
        c.drawCentredString(x + i * cw + cw / 2, y + size * 1.35, str(q))
        c.setFillColor(black)
        sub = q * divisor
        rem = cur - sub
        # subtraction row
        ry -= row_h
        s = str(sub)
        c.setFont('Helvetica-Bold', size)
        for k, ch in enumerate(s):
            c.drawCentredString(x + (i - len(s) + 1 + k) * cw + cw / 2, ry, ch)
        c.drawCentredString(x + (i - max(len(s), len(str(cur))) ) * cw + cw / 2, ry, '-')
        c.setLineWidth(1)
        width_digits = max(len(s), len(str(cur)))
        c.line(x + (i - width_digits + 1) * cw + 2, ry - size * 0.35, x + (i + 1) * cw - 2, ry - size * 0.35)
        # remainder row (with the next digit brought down)
        ry -= row_h
        if i < n - 1:
            nxt = digits[i + 1]
            shown = str(rem) if rem else ''
            for k, ch in enumerate(shown):
                c.drawCentredString(x + (i - len(shown) + 1 + k) * cw + cw / 2, ry, ch)
            c.setFillColor(AMBER)
            c.drawCentredString(x + (i + 1) * cw + cw / 2, ry, nxt)
            c.setFillColor(black)
            cur = rem
        else:
            c.drawCentredString(x + i * cw + cw / 2, ry, str(rem))
            if rem:
                c.setFillColor(TEAL)
                c.setFont('Helvetica-Bold', size * 0.8)
                c.drawString(x + n * cw + 4, y + size * 1.35, f'r {rem}')
                c.setFillColor(black)
    return ry


def work_box(c, x, y, w, h):
    """Squared paper working space (helps line digits up). y is the top edge."""
    c.setStrokeColor(GRID)
    c.setLineWidth(0.5)
    step = 14
    xx = x
    while xx <= x + w + 0.1:
        c.line(xx, y - h, xx, y)
        xx += step
    yy = y
    while yy >= y - h - 0.1:
        c.line(x, yy, x + w, yy)
        yy -= step
    c.setStrokeColor(black)


def answer_line(c, x, y, label='Answer:', width=150):
    c.setFont('Helvetica', 11)
    c.drawString(x, y, label)
    lw = c.stringWidth(label, 'Helvetica', 11)
    c.setLineWidth(0.8)
    c.line(x + lw + 4, y - 2, x + lw + 4 + width, y - 2)


def marks(c, y, m):
    c.setFont('Helvetica', 9)
    c.setFillColor(GREY)
    c.drawRightString(W - M, y, f'({m} mark{"s" if m > 1 else ""})')
    c.setFillColor(black)


# ---------------------------------------------------------------- reference sheet

def build_reference():
    path = os.path.join(HERE, 'division_reference.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle('Dividing Large Numbers - Reference Sheet')

    # ---- Page 1
    header(c, 'Dividing Large Numbers', 'Year 6 reference sheet  -  short division, factors, long division & remainders')
    y = H - 104
    y = section(c, y, '1. The key words')
    c.setFont('Helvetica-Bold', 20)
    c.drawCentredString(W / 2, y - 14, '4,536   ÷   7   =   648')
    c.setFont('Helvetica', 10)
    c.setFillColor(GREY)
    for xx, t in ((W / 2 - 92, 'dividend'), (W / 2 - 14, 'divisor'), (W / 2 + 78, 'quotient')):
        c.drawCentredString(xx, y - 30, t)
    c.setFillColor(black)
    y = para(c, M, y - 50, 'The **dividend** is the number being shared or grouped. The **divisor** is what you divide by. '
             'The **quotient** is the answer. Anything left over is the **remainder**.')
    y = para(c, M, y - 2, '**Always estimate first:** 6,182 ÷ 29 is about 6,000 ÷ 30 = **200**. '
             '**Always check after:** multiply your answer by the divisor (then add any remainder) and you should get the dividend back.')

    y = section(c, y - 14, '2. Short division ("bus stop") - you know this from Year 5')
    short_division(c, M + 70, y - 52, 4536, 7)
    tx = M + 230
    yy = para(c, tx, y - 14, 'Work from **left to right**, one digit at a time:', width=W - M - tx)
    yy = para(c, tx, yy, '• 4 ÷ 7 = 0, so carry the 4 to make **45**', width=W - M - tx)
    yy = para(c, tx, yy, '• 45 ÷ 7 = **6** r 3. Write 6 on top, carry the 3', width=W - M - tx)
    yy = para(c, tx, yy, '• 33 ÷ 7 = **4** r 5. Write 4, carry the 5', width=W - M - tx)
    yy = para(c, tx, yy, '• 56 ÷ 7 = **8**. Answer: **648**', width=W - M - tx)
    c.setFont('Helvetica', 9)
    c.setFillColor(AMBER)
    c.drawString(M + 20, y - 76, 'small orange numbers = carried remainders')
    c.setFillColor(black)
    y = min(yy, y - 84) - 22

    y = section(c, y, '3. Dividing by a 2-digit number: write the multiples first')
    # multiples table for 24
    bx, by = M, y - 6
    c.setFillColor(TEAL_SOFT)
    c.roundRect(bx, by - 132, 108, 132, 6, stroke=0, fill=1)
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(bx + 8, by - 14, 'Multiples of 24')
    c.setFont('Helvetica', 10)
    for k in range(1, 10):
        c.drawString(bx + 12, by - 14 - k * 12.5, f'{k} × 24 = {24 * k}')
    short_division(c, M + 190, y - 58, 7248, 24, cw=24)
    tx = M + 330
    yy = para(c, tx, y - 14, '**7,248 ÷ 24**', width=W - M - tx)
    yy = para(c, tx, yy, '• 7 ÷ 24 = 0, so use **72**: 72 ÷ 24 = **3**', width=W - M - tx)
    yy = para(c, tx, yy, '• 4 ÷ 24 = **0** r 4. Write the 0!', width=W - M - tx)
    yy = para(c, tx, yy, '• 48 ÷ 24 = **2**', width=W - M - tx)
    yy = para(c, tx, yy, 'Answer: **302**. Check: 302 × 24 = 7,248', width=W - M - tx)
    y = min(yy, by - 132) - 22

    y = section(c, y, '4. Division using factors (split the divisor into two easy steps)')
    y = para(c, M, y - 14, 'If the divisor has a factor pair you know well, divide by one factor, then the other.')
    c.setFont('Helvetica-Bold', 14)
    c.drawString(M + 10, y - 8, '2,688 ÷ 24')
    c.setFont('Helvetica', 12)
    c.drawString(M + 100, y - 8, '24 = 4 × 6, so ÷ 4 then ÷ 6')
    c.drawString(M + 10, y - 30, '2,688 ÷ 4 = 672')
    c.drawString(M + 150, y - 30, '672 ÷ 6 = 112')
    c.setFont('Helvetica-Bold', 12)
    c.drawString(M + 280, y - 30, 'So 2,688 ÷ 24 = 112')
    y = para(c, M, y - 52, 'Good factor pairs: 12 = 3 × 4, 15 = 3 × 5, 16 = 4 × 4, 18 = 2 × 9, 24 = 4 × 6, 25 = 5 × 5, 36 = 4 × 9.', size=10, colour=GREY)
    footer(c, "Alice's Maths  -  Dividing Large Numbers  -  Reference sheet")
    c.showPage()

    # ---- Page 2
    header(c, 'Dividing Large Numbers', 'Long division & remainders')
    y = H - 104
    y = section(c, y, '5. Long division: Divide, Multiply, Subtract, Bring down')
    q = 8736 // 24
    assert q * 24 == 8736
    bottom = long_division(c, M + 60, y - 44, 8736, 24, cw=24)
    tx = M + 230
    yy = para(c, tx, y - 14, '**8,736 ÷ 24** (written out in full, so nothing is kept in your head)', width=W - M - tx)
    steps = [
        '**Divide:** 8 ÷ 24 won\'t go, so use 87. 87 ÷ 24 = **3** (3 × 24 = 72)',
        '**Multiply & Subtract:** 87 - 72 = 15',
        '**Bring down** the next digit (3) to make **153**',
        '153 ÷ 24 = **6** (6 × 24 = 144). 153 - 144 = 9',
        'Bring down the 6 to make **96**. 96 ÷ 24 = **4**, remainder 0',
        'Answer: **364**. Check: 364 × 24 = 8,736',
    ]
    for s in steps:
        yy = para(c, tx, yy, '• ' + s, width=W - M - tx, size=10.5)
    yy = para(c, tx, yy - 4, 'Remember it with: **D**oes **M**cDonald\'s **S**ell **B**urgers? (Divide, Multiply, Subtract, Bring down - then repeat.)', width=W - M - tx, size=10, colour=AMBER)
    y = min(bottom, yy) - 34

    y = section(c, y, '6. Remainders: four ways to write them')
    assert 3754 // 16 == 234 and 3754 % 16 == 10
    y = para(c, M, y - 14, '**3,754 ÷ 16** = 234 with **10** left over. Depending on the question, write it as:')
    rows = [('As a remainder', '234 r 10'), ('As a fraction', None), ('As a decimal', '234.625  (10 ÷ 16 = 0.625)'), ('Rounded', 'see the stories below')]
    for i, (label, val) in enumerate(rows):
        yy = y - 8 - i * 26
        c.setFont('Helvetica-Bold', 11)
        c.drawString(M + 10, yy, label)
        if val:
            c.setFont('Helvetica', 12)
            c.drawString(M + 140, yy, val)
        else:
            end = frac(c, M + 140, yy, 10, 16, whole=234)
            c.setFont('Helvetica', 12)
            c.drawString(end + 8, yy, '=')
            end = frac(c, end + 22, yy, 5, 8, whole=234)
            c.setFont('Helvetica', 10)
            c.setFillColor(GREY)
            c.drawString(end + 10, yy, '(the remainder goes over the divisor, then simplify)')
            c.setFillColor(black)
    y = y - 8 - 4 * 26

    y = section(c, y - 4, '7. Remainders in real life: read the question!')
    assert 437 // 52 == 8 and 437 % 52 == 21 and 1000 // 12 == 83 and 1000 % 12 == 4
    c.setFillColor(TEAL_SOFT)
    c.roundRect(M, y - 74, (W - 2 * M) / 2 - 6, 70, 6, stroke=0, fill=1)
    c.setFillColor(AMBER_SOFT)
    c.roundRect(M + (W - 2 * M) / 2 + 6, y - 74, (W - 2 * M) / 2 - 6, 70, 6, stroke=0, fill=1)
    c.setFillColor(black)
    colw = (W - 2 * M) / 2 - 22
    para(c, M + 8, y - 18, '**Round UP** when everyone or everything must fit. 437 people, coaches seat 52: 437 ÷ 52 = 8 r 21, so you need **9 coaches**.', width=colw, size=10.5)
    para(c, M + (W - 2 * M) / 2 + 14, y - 18, '**Round DOWN** when only full groups count. 1,000 eggs in boxes of 12: 1,000 ÷ 12 = 83 r 4, so **83 full boxes**.', width=colw, size=10.5)
    y -= 96

    y = section(c, y, '8. Top tips', AMBER)
    tips = [
        'Write the **multiples of the divisor** down the side before you start. It saves lots of time.',
        'If a step won\'t go, write a **0** in the answer (7,248 ÷ 24 = 3**0**2, not 32).',
        'Your remainder must always be **smaller than the divisor**. If not, the digit above can go up by 1.',
        'Use **squared paper** so each digit has its own box and the columns line up.',
        'Short division and long division give the **same answer**. Long division just writes the subtractions down.',
    ]
    y -= 12
    for t in tips:
        y = para(c, M + 6, y, '• ' + t, size=10.5)
    footer(c, "Alice's Maths  -  Dividing Large Numbers  -  Reference sheet")
    c.showPage()
    c.save()
    return path


# ---------------------------------------------------------------- tests

TESTS = {
    1: dict(
        key=(5544, 22), estimate=(4827, 19, '5,000 ÷ 20 = 250'),
        short=[(3465, 5), (6104, 8), (2793, 7), (5976, 9)],
        two=[(7452, 18), (9821, 23), (6435, 15), (8364, 41)],
        factors=[(3360, 15, 3, 5), (5184, 24, 4, 6)],
        rem_r=(4975, 32), rem_frac=(2350, 12), rem_dec=(3021, 25),
        problems=[
            ('A theatre trip has **1,138** people. Each coach seats **48**. How many coaches are needed?', 1138, 48, 'up', 'coaches'),
            ('A factory has **2,350** biscuits. They pack them in packets of **24**. How many **full** packets can they make?', 2350, 24, 'down', 'full packets'),
            ('A school raised **£3,960**. It is shared equally between **18** classes. How much does each class get?', 3960, 18, 'exact', '£'),
        ]),
    2: dict(
        key=(6936, 24), estimate=(7912, 41, '8,000 ÷ 40 = 200'),
        short=[(2916, 4), (4557, 7), (8253, 9), (3618, 6)],
        two=[(5712, 16), (8526, 29), (7830, 27), (9632, 43)],
        factors=[(4320, 18, 2, 9), (6272, 28, 4, 7)],
        rem_r=(5483, 27), rem_frac=(3290, 15), rem_dec=(4374, 40),
        problems=[
            ('**2,450** pupils are going on a trip. Each minibus holds **16** pupils. How many minibuses are needed?', 2450, 16, 'up', 'minibuses'),
            ('A roll of ribbon is **1,000 cm** long. It is cut into pieces **35 cm** long. How many whole pieces can be cut?', 1000, 35, 'down', 'pieces'),
            ('A farmer packs **4,368** apples into crates of **24**. How many crates does she fill?', 4368, 24, 'exact', 'crates'),
        ]),
    3: dict(
        key=(7068, 31), estimate=(5876, 32, '6,000 ÷ 30 = 200'),
        short=[(4872, 6), (7236, 9), (1995, 5), (6328, 8)],
        two=[(9078, 34), (4896, 17), (7511, 37), (6624, 48)],
        factors=[(2940, 35, 5, 7), (7056, 36, 4, 9)],
        rem_r=(6215, 19), rem_frac=(4100, 18), rem_dec=(5358, 20),
        problems=[
            ('**3,100** people are coming to a concert. Each row seats **45** people. How many rows are needed?', 3100, 45, 'up', 'rows'),
            ('Cinema tickets cost **£14** each. How many tickets can you buy with **£1,000**?', 1000, 14, 'down', 'tickets'),
            ('A lorry drives **2,592 km** over **18** days, the same distance each day. How far does it drive each day?', 2592, 18, 'exact', 'km'),
        ]),
}
TOTAL = 31


def check_test(t):
    """Make sure every question behaves the way its section says it should."""
    a, b = t['key']
    assert a % b == 0
    for a, b in t['short'] + t['two']:
        assert a % b == 0 and 1000 <= a <= 9999, (a, b)
    for a, b, f1, f2 in t['factors']:
        assert f1 * f2 == b and a % f1 == 0 and (a // f1) % f2 == 0
    for key in ('rem_r', 'rem_frac', 'rem_dec'):
        a, b = t[key]
        assert a % b != 0, key
    a, b = t['rem_dec']
    d = Fraction(a, b)
    assert all(p in (2, 5) for p in prime_factors(d.denominator)), 'decimal must terminate'
    for _, a, b, kind, _ in t['problems']:
        assert (a % b == 0) == (kind == 'exact'), (a, b)


def prime_factors(n):
    out, p = [], 2
    while n > 1:
        while n % p == 0:
            out.append(p)
            n //= p
        p += 1
    return out


def dec_str(a, b):
    d = Fraction(a, b)
    whole = d.numerator // d.denominator
    rest = d - whole
    s = ''
    while rest:
        rest *= 10
        dig = rest.numerator // rest.denominator
        s += str(dig)
        rest -= dig
    return f'{fmt(whole)}.{s}'


def q_label(c, x, y, label):
    c.setFillColor(TEAL)
    c.circle(x + 9, y + 4, 10, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 9)
    c.drawCentredString(x + 9, y + 1, label)
    c.setFillColor(black)


def build_test(n):
    t = TESTS[n]
    check_test(t)
    path = os.path.join(HERE, f'division_test{n}.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle(f'Dividing Large Numbers - Practice Test {n}')
    foot = f"Alice's Maths  -  Dividing Large Numbers  -  Practice Test {n}"

    def new_page():
        footer(c, foot)
        c.showPage()
        header(c, f'Practice Test {n}', 'Dividing Large Numbers', name_line=True)
        return H - 100

    header(c, f'Practice Test {n}', 'Dividing Large Numbers  -  Year 6', name_line=True)
    y = H - 100
    c.setFont('Helvetica', 11)
    y = para(c, M, y, 'No calculator. Show your working in the squared boxes - the squares help keep your digits in columns. '
             'Use whichever method you like (short division, long division or factors) unless the question says otherwise.', size=10.5)
    c.setFont('Helvetica-Bold', 12)
    c.drawRightString(W - M, y - 6, f'Score:  ______ / {TOTAL}')
    y -= 34

    # A: key words and estimating
    y = section(c, y, 'Section A: Key words and estimating')
    a, b = t['key']
    q_label(c, M, y - 16, 'A1')
    para(c, M + 26, y - 14, f'Look at this calculation:  **{fmt(a)} ÷ {b} = {fmt(a // b)}**')
    answer_line(c, M + 26, y - 38, 'Which number is the divisor?', 80)
    answer_line(c, M + 290, y - 38, 'Which is the quotient?', 80)
    marks(c, y - 14, 2)
    y -= 62
    ea, eb, _ = t['estimate']
    q_label(c, M, y - 2, 'A2')
    para(c, M + 26, y, f'**Estimate** the answer to {fmt(ea)} ÷ {eb} by rounding both numbers. Show what you rounded to.')
    answer_line(c, M + 26, y - 24, 'Estimate:', 200)
    marks(c, y, 1)
    y -= 58

    # B: short division by 1 digit
    y = section(c, y, 'Section B: Short division (1 mark each)')
    bw = (W - 2 * M - 30) / 4
    for i, (a, b) in enumerate(t['short']):
        x = M + i * (bw + 10)
        q_label(c, x, y - 16, f'B{i + 1}')
        c.setFont('Helvetica-Bold', 13)
        c.drawString(x + 24, y - 14, f'{fmt(a)} ÷ {b}')
        work_box(c, x, y - 26, bw, 70)
        answer_line(c, x, y - 112, '=', bw - 20)
    y -= 144

    # C: dividing by 2-digit numbers
    y = section(c, y, 'Section C: Dividing by a 2-digit number (2 marks each)')
    for i, (a, b) in enumerate(t['two']):
        col = i % 2
        if col == 0 and i:
            y -= 148
        x = M + col * ((W - 2 * M) / 2 + 6)
        bw2 = (W - 2 * M) / 2 - 6
        q_label(c, x, y - 16, f'C{i + 1}')
        c.setFont('Helvetica-Bold', 13)
        c.drawString(x + 24, y - 14, f'{fmt(a)} ÷ {b}')
        work_box(c, x, y - 26, bw2, 84)
        answer_line(c, x, y - 128, 'Answer:', 100)
    y -= 168
    y = new_page()

    # D: factors
    y = section(c, y, 'Section D: Division using factors (2 marks each)')
    for i, (a, b, f1, f2) in enumerate(t['factors']):
        x = M + i * ((W - 2 * M) / 2 + 6)
        bw2 = (W - 2 * M) / 2 - 6
        q_label(c, x, y - 16, f'D{i + 1}')
        para(c, x + 24, y - 14, f'Work out **{fmt(a)} ÷ {b}** by dividing by **{f1}**, then by **{f2}**.', width=bw2 - 24, size=10.5)
        work_box(c, x, y - 44, bw2, 56)
        answer_line(c, x, y - 118, 'Answer:', 100)
    y -= 152

    # E: remainders
    y = section(c, y, 'Section E: Remainders (2 marks each)')
    items = [('E1', t['rem_r'], 'Give your answer **with a remainder** (r).'),
             ('E2', t['rem_frac'], 'Give your answer as a **mixed number** (remainder as a fraction, simplified).'),
             ('E3', t['rem_dec'], 'Give your answer as a **decimal**.')]
    bw3 = (W - 2 * M - 20) / 3
    for i, (lab, (a, b), instr) in enumerate(items):
        x = M + i * (bw3 + 10)
        q_label(c, x, y - 16, lab)
        c.setFont('Helvetica-Bold', 13)
        c.drawString(x + 24, y - 14, f'{fmt(a)} ÷ {b}')
        para(c, x, y - 34, instr, width=bw3, size=9.5)
        work_box(c, x, y - 62, bw3, 70)
        answer_line(c, x, y - 150, '=', bw3 - 20)
    y -= 184

    # F: problems
    y = section(c, y, 'Section F: Problems - think about the remainder! (2 marks each)')
    for i, (text, a, b, kind, unit) in enumerate(t['problems']):
        q_label(c, M, y - 16, f'F{i + 1}')
        yy = para(c, M + 26, y - 14, text, size=10.5, width=W - 2 * M - 80)
        marks(c, y - 14, 2)
        work_box(c, M + 26, yy - 2, W - 2 * M - 200, 42)
        answer_line(c, W - M - 160, yy - 40, 'Answer:', 100)
        y = yy - 58
    footer(c, foot)
    c.showPage()
    c.save()
    return path


def build_answers(n):
    t = TESTS[n]
    path = os.path.join(HERE, f'division_test{n}_answers.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle(f'Dividing Large Numbers - Practice Test {n} Answers')
    header(c, f'Practice Test {n}: Answers', f'Dividing Large Numbers  -  total {TOTAL} marks')
    y = H - 104
    lines = []

    def row(label, text, mark):
        nonlocal y
        if y < 70:
            footer(c, f"Alice's Maths  -  Practice Test {n} answers")
            c.showPage()
            header(c, f'Practice Test {n}: Answers', 'continued')
            y = H - 104
        q_label(c, M, y - 2, label)
        yy = para(c, M + 28, y, text, size=10.5, width=W - 2 * M - 90)
        c.setFont('Helvetica', 9)
        c.setFillColor(GREY)
        c.drawRightString(W - M, y, mark)
        c.setFillColor(black)
        y = yy - 3

    y = section(c, y, 'Section A')
    a, b = t['key']
    y -= 12
    row('A1', f'Divisor = **{b}** (1 mark). Quotient = **{fmt(a // b)}** (1 mark).', '2 marks')
    ea, eb, est = t['estimate']
    row('A2', f'About **{est.split("= ")[1]}**: {est}. Accept any sensible rounding (actual answer is about {round(ea / eb)}).', '1 mark')

    y = section(c, y - 14, 'Section B (1 mark each)')
    y -= 12
    for i, (a, b) in enumerate(t['short']):
        row(f'B{i + 1}', f'{fmt(a)} ÷ {b} = **{fmt(a // b)}**', '1 mark')

    y = section(c, y - 14, 'Section C (1 mark for a correct method, 1 for the answer)')
    y -= 12
    for i, (a, b) in enumerate(t['two']):
        q = a // b
        extra = '  (the 0 must be there!)' if '0' in str(q) else ''
        row(f'C{i + 1}', f'{fmt(a)} ÷ {b} = **{fmt(q)}**{extra}. Check: {fmt(q)} × {b} = {fmt(a)}', '2 marks')

    y = section(c, y - 14, 'Section D (1 mark for each correct step)')
    y -= 12
    for i, (a, b, f1, f2) in enumerate(t['factors']):
        mid = a // f1
        row(f'D{i + 1}', f'{fmt(a)} ÷ {f1} = {fmt(mid)}, then {fmt(mid)} ÷ {f2} = **{fmt(mid // f2)}**', '2 marks')

    y = section(c, y - 14, 'Section E (1 mark for the whole number, 1 for the remainder part)')
    y -= 12
    a, b = t['rem_r']
    row('E1', f'{fmt(a)} ÷ {b} = **{fmt(a // b)} r {a % b}**. Check: {fmt(a // b)} × {b} + {a % b} = {fmt(a)}', '2 marks')
    a, b = t['rem_frac']
    fr = Fraction(a % b, b)
    simp = f' = **{fmt(a // b)} {fr.numerator}/{fr.denominator}**' if fr.denominator != b else ''
    row('E2', f'{fmt(a)} ÷ {b} = {fmt(a // b)} r {a % b} = {fmt(a // b)} {a % b}/{b}{simp}' + ('' if simp else ' (already simplest)'), '2 marks')
    a, b = t['rem_dec']
    row('E3', f'{fmt(a)} ÷ {b} = {fmt(a // b)} r {a % b}. {a % b} ÷ {b} = {dec_str(a % b, b)} so the answer is **{dec_str(a, b)}**', '2 marks')

    y = section(c, y - 14, 'Section F (1 mark for the division, 1 for using the remainder correctly)')
    y -= 12
    for i, (text, a, b, kind, unit) in enumerate(t['problems']):
        q, r = divmod(a, b)
        if kind == 'up':
            txt = f'{fmt(a)} ÷ {b} = {q} r {r}. The {r} left over still need a place, so round **up**: **{q + 1} {unit}**.'
        elif kind == 'down':
            txt = f'{fmt(a)} ÷ {b} = {q} r {r}. The {r} left over is not enough for another one, so round **down**: **{q} {unit}**.'
        else:
            ans = f'£{fmt(q)}' if unit == '£' else f'{fmt(q)} {unit}'
            txt = f'{fmt(a)} ÷ {b} = **{ans}** (no remainder).'
        row(f'F{i + 1}', txt, '2 marks')

    y -= 6
    if y - 56 < 40:
        footer(c, f"Alice's Maths  -  Practice Test {n} answers")
        c.showPage()
        header(c, f'Practice Test {n}: Answers', 'continued')
        y = H - 104
    c.setFillColor(TEAL_SOFT)
    c.roundRect(M, y - 52, W - 2 * M, 50, 6, stroke=0, fill=1)
    c.setFillColor(black)
    para(c, M + 10, y - 18, '**Marking tip:** if the method is right but there is one small slip (e.g. a times-table fact), give the method mark. '
         'Look at any wrong answers together: was it a missing 0, a remainder bigger than the divisor, or a digit in the wrong column?', size=10, width=W - 2 * M - 20)
    footer(c, f"Alice's Maths  -  Practice Test {n} answers")
    c.showPage()
    c.save()
    return path


# ---------------------------------------------------------------- single practice sheets (Sections B and C only)

SHEETS = {
    1: dict(short=[(5838, 7), (4536, 8), (7281, 9), (6342, 6)],
            two=[(6273, 17), (9504, 24), (9792, 32), (7616, 34)]),
}
SHEET_TOTAL = 12


def build_sheet(n):
    t = SHEETS[n]
    used = {q for tt in TESTS.values() for q in tt['short'] + tt['two']}
    for a, b in t['short'] + t['two']:
        assert a % b == 0 and 1000 <= a <= 9999 and (a, b) not in used, (a, b)
    path = os.path.join(HERE, f'division_sheet{n}.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle(f'Dividing Large Numbers - Practice Sheet {n}')
    header(c, f'Practice Sheet {n}', 'Dividing Large Numbers  -  Year 6', name_line=True)
    y = H - 100
    y = para(c, M, y, 'No calculator. Show your working in the squared boxes. Use short division or long division, '
             'and write the multiples of the divisor down the side if it helps.', size=10.5)
    c.setFont('Helvetica-Bold', 12)
    c.drawRightString(W - M, y - 6, f'Score:  ______ / {SHEET_TOTAL}')
    y -= 34

    y = section(c, y, 'Section B: Short division (1 mark each)')
    bw = (W - 2 * M - 30) / 4
    for i, (a, b) in enumerate(t['short']):
        x = M + i * (bw + 10)
        q_label(c, x, y - 16, f'B{i + 1}')
        c.setFont('Helvetica-Bold', 13)
        c.drawString(x + 24, y - 14, f'{fmt(a)} ÷ {b}')
        work_box(c, x, y - 26, bw, 92)
        answer_line(c, x, y - 134, '=', bw - 20)
    y -= 166

    y = section(c, y, 'Section C: Dividing by a 2-digit number (2 marks each)')
    bw2 = (W - 2 * M) / 2 - 6
    for i, (a, b) in enumerate(t['two']):
        col = i % 2
        if col == 0 and i:
            y -= 214
        x = M + col * (bw2 + 12)
        q_label(c, x, y - 16, f'C{i + 1}')
        c.setFont('Helvetica-Bold', 13)
        c.drawString(x + 24, y - 14, f'{fmt(a)} ÷ {b}')
        work_box(c, x, y - 26, bw2, 150)
        answer_line(c, x, y - 194, 'Answer:', 100)
    footer(c, f"Alice's Maths  -  Dividing Large Numbers  -  Practice Sheet {n}")
    c.showPage()
    c.save()
    return path


def build_sheet_answers(n):
    t = SHEETS[n]
    path = os.path.join(HERE, f'division_sheet{n}_answers.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle(f'Dividing Large Numbers - Practice Sheet {n} Answers')
    header(c, f'Practice Sheet {n}: Answers', f'Dividing Large Numbers  -  total {SHEET_TOTAL} marks')
    y = H - 104

    def row(label, text, mark):
        nonlocal y
        q_label(c, M, y - 2, label)
        yy = para(c, M + 28, y, text, size=10.5, width=W - 2 * M - 90)
        c.setFont('Helvetica', 9)
        c.setFillColor(GREY)
        c.drawRightString(W - M, y, mark)
        c.setFillColor(black)
        y = yy - 3

    y = section(c, y, 'Section B (1 mark each)')
    y -= 12
    for i, (a, b) in enumerate(t['short']):
        q = a // b
        extra = '  (the 0 must be there!)' if '0' in str(q) else ''
        row(f'B{i + 1}', f'{fmt(a)} ÷ {b} = **{fmt(q)}**{extra}', '1 mark')

    y = section(c, y - 14, 'Section C (1 mark for a correct method, 1 for the answer)')
    y -= 12
    for i, (a, b) in enumerate(t['two']):
        q = a // b
        extra = '  (the 0 must be there!)' if '0' in str(q) else ''
        row(f'C{i + 1}', f'{fmt(a)} ÷ {b} = **{fmt(q)}**{extra}. Check: {fmt(q)} × {b} = {fmt(a)}', '2 marks')

    y -= 6
    c.setFillColor(TEAL_SOFT)
    c.roundRect(M, y - 52, W - 2 * M, 50, 6, stroke=0, fill=1)
    c.setFillColor(black)
    para(c, M + 10, y - 18, '**Marking tip:** if the method is right but there is one small slip (e.g. a times-table fact), give the method mark. '
         'Any times-table slips are worth practising on the Times Tables page.', size=10, width=W - 2 * M - 20)
    footer(c, f"Alice's Maths  -  Practice Sheet {n} answers")
    c.showPage()
    c.save()
    return path


if __name__ == '__main__':
    print(build_reference())
    for n in TESTS:
        print(build_test(n))
        print(build_answers(n))
    for n in SHEETS:
        print(build_sheet(n))
        print(build_sheet_answers(n))
