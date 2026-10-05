# -*- coding: utf-8 -*-
"""Practice sheet + answers for 'Equation of a line from its intercepts' (GCSE Maths, Higher).

Each question gives where a straight line crosses the y-axis (0, c) and the x-axis (a, 0);
Eric writes the equation. Every answer is computed (and asserted) here, not typed by hand.
Run:  python generate_pdfs.py
"""
from fractions import Fraction
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = A4
PURPLE = HexColor('#7c3aed')
PURPLE_SOFT = HexColor('#f1eafe')
GREY = HexColor('#5b616e')
GRID = HexColor('#e3e4ea')
M = 42

# (a, c): x-intercept (a, 0), y-intercept (0, c).  form 'y' = y = mx + c, 'int' = ax + by = c
SHEET_1 = {
    'A': [(3, 6, 'y'), (-2, 4, 'y'), (4, -8, 'y'), (5, 5, 'y'), (-3, -9, 'y'), (2, -8, 'y')],
    'B': [(6, 4, 'y'), (-4, 2, 'y'), (10, -4, 'y'), (-6, -9, 'y'), (9, 6, 'int'), (-8, 6, 'int')],
}


def gradient(a, c):
    return Fraction(-c, a)


def int_coeffs(a, c):
    """y = (p/q)x + c  ->  -p x + q y = q c, scaled so the x coefficient is positive."""
    m = gradient(a, c)
    A, B, C = -m.numerator, m.denominator, m.denominator * c
    if A < 0:
        A, B, C = -A, -B, -C
    assert A * a + B * 0 == C and A * 0 + B * c == C  # both intercepts lie on the line
    return A, B, C


def n(v):
    return f'-{abs(v)}' if v < 0 else str(v)


# ---------------------------------------------------------------- drawing helpers

def header(c, title, sub, name_line=False):
    c.setFillColor(PURPLE)
    c.rect(0, H - 78, W, 78, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 22)
    c.drawString(M, H - 42, title)
    c.setFont('Helvetica', 11)
    c.drawString(M, H - 62, sub)
    if name_line:
        c.drawRightString(W - M, H - 42, 'Name: ____________________')
        c.drawRightString(W - M, H - 62, 'Date: ______________')
    c.setFillColor(black)


def footer(c, text):
    c.setFont('Helvetica', 8)
    c.setFillColor(GREY)
    c.drawString(M, 22, text)
    c.drawRightString(W - M, 22, f'Page {c.getPageNumber()}')
    c.setFillColor(black)


def section(c, y, text):
    c.setFillColor(PURPLE)
    c.roundRect(M, y - 6, W - 2 * M, 24, 6, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(M + 10, y + 1, text)
    c.setFillColor(black)
    return y - 26


def q_label(c, x, y, label):
    c.setFillColor(PURPLE)
    c.circle(x + 10, y + 4, 11, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 9)
    c.drawCentredString(x + 10, y + 1, label)
    c.setFillColor(black)


def frac(c, x, y, num, den, size=11):
    """Draw a stacked fraction with its baseline-centre at y; returns its width."""
    c.setFont('Helvetica', size - 2)
    w = max(c.stringWidth(str(num), 'Helvetica', size - 2), c.stringWidth(str(den), 'Helvetica', size - 2)) + 3
    c.drawCentredString(x + w / 2, y + 5, str(num))
    c.drawCentredString(x + w / 2, y - 6, str(den))
    c.setLineWidth(0.8)
    c.line(x, y + 2.5, x + w, y + 2.5)
    return w


def draw_eq(c, x, y, parts, size=11, bold=False):
    """parts: strings, or ('f', num, den) for a stacked fraction."""
    font = 'Helvetica-Bold' if bold else 'Helvetica'
    for p in parts:
        if isinstance(p, tuple):
            x += frac(c, x, y, p[1], p[2], size) + 1
        else:
            c.setFont(font, size)
            c.drawString(x, y, p)
            x += c.stringWidth(p, font, size)
    return x


def y_form_parts(a, cc):
    m = gradient(a, cc)
    parts = ['y = ']
    if m.denominator == 1:
        parts.append({1: 'x', -1: '-x'}.get(m.numerator, f'{m.numerator}x'))
    else:
        if m < 0:
            parts.append('-')
        parts += [('f', abs(m.numerator), m.denominator), 'x']
    parts.append(f' + {cc}' if cc > 0 else f' - {abs(cc)}')
    return parts


def int_form_text(a, cc):
    A, B, C = int_coeffs(a, cc)
    ax = 'x' if A == 1 else f'{A}x'
    by = (' - ' if B < 0 else ' + ') + ('' if abs(B) == 1 else str(abs(B))) + 'y'
    return f'{ax}{by} = {n(C)}'


def mini_graph(c, x0, y0, size, a, cc):
    """Small axes with the two intercepts marked and the line drawn. (x0, y0) = bottom-left."""
    R = max(abs(a), abs(cc), 5) + 1
    k = size / (2 * R)
    cx, cy = x0 + size / 2, y0 + size / 2
    X = lambda v: cx + v * k
    Y = lambda v: cy + v * k
    c.setStrokeColor(GRID)
    c.setLineWidth(0.4)
    for i in range(-R, R + 1):
        c.line(X(i), Y(-R), X(i), Y(R))
        c.line(X(-R), Y(i), X(R), Y(i))
    c.setStrokeColor(black)
    c.setLineWidth(0.9)
    c.line(X(-R), cy, X(R), cy)
    c.line(cx, Y(-R), cx, Y(R))
    c.setFont('Helvetica-Oblique', 8)
    c.drawString(X(R) - 5, cy + 3, 'x')
    c.drawString(cx + 3, Y(R) - 7, 'y')
    m = float(gradient(a, cc))
    xs = sorted([(-R - cc) / m, (R - cc) / m])
    x1, x2 = max(-R, xs[0]), min(R, xs[1])
    c.setStrokeColor(PURPLE)
    c.setLineWidth(1.6)
    c.line(X(x1), Y(m * x1 + cc), X(x2), Y(m * x2 + cc))
    c.setFont('Helvetica-Bold', 8.5)

    def label(x, y, text, align):
        w = c.stringWidth(text, 'Helvetica-Bold', 8.5)
        left = {'r': x - w, 'l': x, 'c': x - w / 2}[align]
        c.setFillColor(white)
        c.rect(left - 1.5, y - 2.5, w + 3, 10.5, stroke=0, fill=1)
        c.setFillColor(black)
        c.drawString(left, y, text)

    lab_y, lab_x = f'(0, {n(cc)})', f'({n(a)}, 0)'
    if m > 0:
        label(X(0) - 5, Y(cc) - 3, lab_y, 'r')
    else:
        label(X(0) + 5, Y(cc) - 3, lab_y, 'l')
    above = (m > 0) == (a > 0)
    ly = Y(0) + (6 if above else -12)
    if abs(a) >= R - 2:  # near the edge: keep the label inside the grid
        label(X(a) + (4 if a > 0 else -4), ly, lab_x, 'r' if a > 0 else 'l')
    else:
        label(X(a), ly, lab_x, 'c')
    c.setFillColor(PURPLE)
    c.circle(X(0), Y(cc), 2.6, stroke=0, fill=1)
    c.circle(X(a), Y(0), 2.6, stroke=0, fill=1)
    c.setFillColor(black)
    c.setStrokeColor(black)


# ---------------------------------------------------------------- sheet

def build_sheet():
    path = os.path.join(HERE, 'line_from_intercepts_sheet1.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle('Equation from Intercepts - Practice Sheet 1')
    foot = "Eric's Maths  -  Equation of a line from its intercepts  -  Practice Sheet 1"
    titles = {'A': 'Section A: Whole-number gradients (2 marks each)',
              'B': 'Section B: Fraction gradients - Higher (2 marks each)'}
    total = 2 * sum(len(v) for v in SHEET_1.values())
    for sec, qs in SHEET_1.items():
        header(c, 'Equation from Intercepts', 'Practice Sheet 1  -  GCSE Maths (Higher)', name_line=True)
        y = H - 102
        c.setFont('Helvetica', 10.5)
        if sec == 'A':
            c.drawString(M, y, 'Each line crosses the axes at the two points shown. Write its equation in the form y = mx + c.')
            c.drawString(M, y - 15, 'Remember: c is where it crosses the y-axis, and m = change in y / change in x.')
            c.setFont('Helvetica-Bold', 12)
            c.drawRightString(W - M, y - 36, f'Score:  ______ / {total}')
        else:
            c.drawString(M, y, 'Leave fractions as fractions (not decimals). Q5 and Q6 want the form ax + by = c, where a, b, c are integers.')
        y -= 66 if sec == 'A' else 52
        y = section(c, y, titles[sec])
        colw = (W - 2 * M) / 3
        for i, (a, cc, form) in enumerate(qs):
            col, row = i % 3, i // 3
            x = M + col * colw
            top = y - 8 - row * 318
            q_label(c, x, top - 6, f'{sec}{i + 1}')
            c.setFont('Helvetica', 9.5)
            c.drawString(x + 26, top - 3, f'Crosses at (0, {n(cc)}) and ({n(a)}, 0)')
            mini_graph(c, x + 8, top - 168, colw - 26, a, cc)
            c.setFont('Helvetica', 8.5)
            c.setFillColor(GREY)
            c.drawString(x + 4, top - 184, 'Working:')
            c.setFillColor(black)
            c.setStrokeColor(GRID)
            for j in range(3):
                c.line(x + 4, top - 204 - j * 20, x + colw - 14, top - 204 - j * 20)
            c.setStrokeColor(black)
            c.setFont('Helvetica-Bold', 10)
            label = 'ax + by = c:' if form == 'int' else 'y ='
            c.drawString(x + 4, top - 278, label)
            c.setLineWidth(0.8)
            c.line(x + 4 + c.stringWidth(label, 'Helvetica-Bold', 10) + 4, top - 280, x + colw - 14, top - 280)
        footer(c, foot)
        c.showPage()
    c.save()
    return path


def build_answers():
    path = os.path.join(HERE, 'line_from_intercepts_sheet1_answers.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle('Equation from Intercepts - Practice Sheet 1 Answers')
    header(c, 'Practice Sheet 1: Answers', 'Equation from Intercepts  -  1 mark for the gradient, 1 for the full equation')
    y = H - 104
    for sec, qs in SHEET_1.items():
        y = section(c, y, f'Section {sec}') - 14
        for i, (a, cc, form) in enumerate(qs):
            m = gradient(a, cc)
            assert m * a + cc == 0  # (a, 0) is on y = mx + c
            q_label(c, M, y - 2, f'{sec}{i + 1}')
            xx = draw_eq(c, M + 30, y, [f'c = {n(cc)}.   m = {n(-cc)} / {n(a)} = '])
            if m.denominator == 1:
                xx = draw_eq(c, xx, y, [n(m.numerator)])
            else:
                xx = draw_eq(c, xx, y, ['-' if m < 0 else '', ('f', abs(m.numerator), m.denominator)])
            xx = draw_eq(c, xx + 12, y, ['So  '])
            xx = draw_eq(c, xx, y, y_form_parts(a, cc), bold=(form == 'y'))
            if form == 'int':
                A, B, C = int_coeffs(a, cc)
                q = m.denominator
                draw_eq(c, M + 30, y - 22, [f'x {q}:  {q}y = {n(m.numerator)}x + {n(q * cc)}   ->   '])
                draw_eq(c, M + 230, y - 22, [int_form_text(a, cc)], bold=True)
                y -= 22
            c.setFont('Helvetica', 9)
            c.setFillColor(GREY)
            c.drawRightString(W - M, y, '2 marks')
            c.setFillColor(black)
            y -= 30
        y -= 8
    c.setFillColor(PURPLE_SOFT)
    c.roundRect(M, y - 60, W - 2 * M, 58, 6, stroke=0, fill=1)
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(M + 10, y - 20, 'Quick check:')
    c.setFont('Helvetica', 10)
    c.drawString(M + 80, y - 20, 'put the x-intercept into your equation. You should get y = 0.')
    c.drawString(M + 10, y - 38, 'Common slips: the sign of m (does the line go up or down?), and m upside down (it is up / along, not along / up).')
    footer(c, "Eric's Maths  -  Equation from Intercepts  -  Practice Sheet 1 answers")
    c.showPage()
    c.save()
    return path


if __name__ == '__main__':
    print(build_sheet())
    print(build_answers())
