# -*- coding: utf-8 -*-
"""Check every answer in generate_pdfs.py numerically.

Each check compares the question's expression with the answer at several
values of x (and y), so a wrong sign or coefficient shows up at once.
Equation answers are checked by substituting the roots back in.
"""

from fractions import Fraction as F

XS = [F(-7, 3), F(-2), F(-1, 2), F(0), F(1), F(3), F(5, 2), F(11)]
YS = [F(-3), F(1, 3), F(2), F(7)]


def same(name, lhs, rhs, two_vars=False):
    pts = [(x, y) for x in XS for y in YS] if two_vars else [(x, None) for x in XS]
    for x, y in pts:
        try:
            a, b = (lhs(x, y), rhs(x, y)) if two_vars else (lhs(x), rhs(x))
        except ZeroDivisionError:
            continue
        assert a == b, f'{name}: differs at x={x}, y={y} ({a} vs {b})'


def roots(name, poly, rs):
    for r in rs:
        assert poly(r) == 0, f'{name}: {r} is not a root'


def num(name, value, expected):
    assert value == expected, f'{name}: {value} != {expected}'


# ---------------- Test 1
same('T1 A1', lambda x: (x + 4) * (x + 7), lambda x: x**2 + 11*x + 28)
same('T1 A2', lambda x: (x - 5) * (x + 3), lambda x: x**2 - 2*x - 15)
same('T1 A3', lambda x: (x - 6)**2, lambda x: x**2 - 12*x + 36)
same('T1 A4', lambda x: (3*x + 2) * (2*x - 5), lambda x: 6*x**2 - 11*x - 10)
same('T1 B1', lambda x: (x + 1) * (x + 2) * (x + 3), lambda x: x**3 + 6*x**2 + 11*x + 6)
same('T1 B2', lambda x: (x - 2) * (x + 4) * (2*x + 1), lambda x: 2*x**3 + 5*x**2 - 14*x - 8)
same('T1 C1', lambda x: x**2 + 9*x + 20, lambda x: (x + 4) * (x + 5))
same('T1 C2', lambda x: x**2 - 3*x - 28, lambda x: (x - 7) * (x + 4))
same('T1 C3', lambda x: x**2 - 49, lambda x: (x + 7) * (x - 7))
same('T1 C4', lambda x: 2*x**2 - 50, lambda x: 2 * (x + 5) * (x - 5))
same('T1 D1', lambda x: 2*x**2 + 7*x + 3, lambda x: (2*x + 1) * (x + 3))
same('T1 D2', lambda x: 3*x**2 - 10*x - 8, lambda x: (3*x + 2) * (x - 4))
same('T1 D3', lambda x: 4*x**2 + 10*x - 6, lambda x: 2 * (2*x - 1) * (x + 3))
roots('T1 E1', lambda x: x**2 - 5*x - 14, [7, -2])
same('T1 E2', lambda x: (x**2 + 5*x + 6) / (x**2 - 9), lambda x: (x + 2) / (x - 3))
same('T1 F1', lambda x: (x + 5)**2 - (x - 5)**2, lambda x: 20*x)
same('T1 F2a', lambda x: (x + 6) * (x - 2) - 33, lambda x: x**2 + 4*x - 45)
roots('T1 F2b', lambda x: x**2 + 4*x - 45, [5, -9])
num('T1 F2 width', 5 - 2, 3)
num('T1 F3', 53**2 - 47**2, 600)

# ---------------- Test 2
same('T2 A1', lambda x: (x + 3) * (x + 9), lambda x: x**2 + 12*x + 27)
same('T2 A2', lambda x: (x - 8) * (x - 2), lambda x: x**2 - 10*x + 16)
same('T2 A3', lambda x: (2*x + 5)**2, lambda x: 4*x**2 + 20*x + 25)
same('T2 A4', lambda x: (x + 4)**2, lambda x: x**2 + 8*x + 16)
same('T2 B1', lambda x: (x + 3) * (x - 1) * (x - 4), lambda x: x**3 - 2*x**2 - 11*x + 12)
same('T2 B2', lambda x: (x + 2)**3, lambda x: x**3 + 6*x**2 + 12*x + 8)
same('T2 C1', lambda x: x**2 + 2*x - 24, lambda x: (x + 6) * (x - 4))
same('T2 C2', lambda x: x**2 - 13*x + 36, lambda x: (x - 4) * (x - 9))
same('T2 C3', lambda x: 9*x**2 - 16, lambda x: (3*x + 4) * (3*x - 4))
same('T2 C4', lambda x: x**2 + 8*x + 15, lambda x: (x + 3) * (x + 5))
same('T2 D1', lambda x: 5*x**2 + 13*x - 6, lambda x: (5*x - 2) * (x + 3))
same('T2 D2', lambda x: 6*x**2 - 11*x + 4, lambda x: (2*x - 1) * (3*x - 4))
same('T2 D3', lambda x: 3*x**3 - 12*x, lambda x: 3*x * (x + 2) * (x - 2))
roots('T2 E1', lambda x: 2*x**2 + x - 15, [F(5, 2), -3])
same('T2 E2', lambda x: (2*x**2 - 7*x - 4) / (x**2 - 16), lambda x: (2*x + 1) / (x + 4))
same('T2 F1a', lambda x: x**2 + 8*x + 5, lambda x: (x + 4)**2 - 11)
num('T2 F1b', (-4)**2 + 8*(-4) + 5, -11)
same('T2 F2', lambda n: (2*n + 3)**2 - (2*n + 1)**2, lambda n: 8 * (n + 1))
num('T2 F3', 1001**2 - 999**2, 4000)

# ---------------- Test 3
same('T3 A1', lambda x: (x + 2) * (x + 11), lambda x: x**2 + 13*x + 22)
same('T3 A2', lambda x: (x - 7) * (x + 7), lambda x: x**2 - 49)
same('T3 A3', lambda x: (4*x - 3) * (x + 2), lambda x: 4*x**2 + 5*x - 6)
same('T3 A4', lambda x: (x + 3)**2 + (x - 1)**2, lambda x: 2*x**2 + 4*x + 10)
same('T3 B1', lambda x: (2*x - 1) * (x + 3) * (x - 2), lambda x: 2*x**3 + x**2 - 13*x + 6)
same('T3 B2', lambda x: (x - 1)**3, lambda x: x**3 - 3*x**2 + 3*x - 1)
same('T3 C1', lambda x: x**2 + 15*x + 56, lambda x: (x + 7) * (x + 8))
same('T3 C2', lambda x: x**2 + x - 30, lambda x: (x + 6) * (x - 5))
same('T3 C3', lambda x: 100 - x**2, lambda x: (10 + x) * (10 - x))
same('T3 C4', lambda x: 5*x**2 - 20*x - 60, lambda x: 5 * (x - 6) * (x + 2))
same('T3 D1', lambda x: 3*x**2 + 11*x + 10, lambda x: (3*x + 5) * (x + 2))
same('T3 D2', lambda x: 4*x**2 - 4*x - 15, lambda x: (2*x + 3) * (2*x - 5))
same('T3 D3', lambda x, y: 25*x**2 - 9*y**2, lambda x, y: (5*x + 3*y) * (5*x - 3*y), two_vars=True)
roots('T3 E1', lambda x: x**2 - (6*x - 8), [2, 4])
same('T3 E2', lambda x: (3*x**2 + 6*x) / (x**2 - x - 6), lambda x: 3*x / (x - 3))
same('T3 F1', lambda x: x**2 + 14*x + 49, lambda x: (x + 7)**2)
same('T3 F1 perimeter', lambda x: 4 * (x + 7), lambda x: 4*x + 28)
same('T3 F2', lambda x: x * (x + 2) * (x + 5), lambda x: x**3 + 7*x**2 + 10*x)
same('T3 F3', lambda n: n**2 + (n + 1)**2, lambda n: 2 * (n**2 + n) + 1)
num('T3 F4', F(15, 2)**2 - F(5, 2)**2, 50)

# ---------------- Test 4
same('T4 A1', lambda x: (x - 9) * (x - 4), lambda x: x**2 - 13*x + 36)
same('T4 A2', lambda x: (5 - x) * (3 + x), lambda x: 15 + 2*x - x**2)
same('T4 A3', lambda x, y: (3*x - 2*y)**2, lambda x, y: 9*x**2 - 12*x*y + 4*y**2, two_vars=True)
same('T4 A4', lambda x: (2*x + 1) * (x - 3) - (x - 2)**2, lambda x: x**2 - x - 7)
same('T4 B1', lambda x: (x + 5) * (x - 5) * (x + 2), lambda x: x**3 + 2*x**2 - 25*x - 50)
same('T4 B2', lambda x: (3*x - 1) * (x + 2)**2, lambda x: 3*x**3 + 11*x**2 + 8*x - 4)
same('T4 C1', lambda x: x**2 - 16*x + 63, lambda x: (x - 7) * (x - 9))
same('T4 C2', lambda x: x**2 + 5*x - 84, lambda x: (x + 12) * (x - 7))
same('T4 C3', lambda x: 4*x**2 - 1, lambda x: (2*x + 1) * (2*x - 1))
same('T4 C4', lambda x: x**4 - 81, lambda x: (x**2 + 9) * (x + 3) * (x - 3))
same('T4 D1', lambda x: 6*x**2 + x - 2, lambda x: (2*x - 1) * (3*x + 2))
same('T4 D2', lambda x: 10*x**2 - 17*x + 3, lambda x: (5*x - 1) * (2*x - 3))
same('T4 D3', lambda x: 8*x**2 - 2*x - 6, lambda x: 2 * (4*x + 3) * (x - 1))
roots('T4 E1', lambda x: 3*x**2 - 5*x - 2, [F(-1, 3), 2])
same('T4 E2', lambda x: (4*x**2 - 9) / (2*x**2 + x - 6), lambda x: (2*x + 3) / (x + 2))
same('T4 F1', lambda x: 2*x**2 + 12*x + 7, lambda x: 2 * (x + 3)**2 - 11)
same('T4 F2', lambda n: (2*n + 1)**2 - (2*n - 1)**2, lambda n: 8*n)
num('T4 F3', F(87, 10)**2 - F(13, 10)**2, 74)

# ---------------- Test 5
same('T5 A1', lambda x: (x + 6) * (x + 8), lambda x: x**2 + 14*x + 48)
same('T5 A2', lambda x: (x - 10) * (x + 4), lambda x: x**2 - 6*x - 40)
same('T5 A3', lambda x: (x + 9)**2, lambda x: x**2 + 18*x + 81)
same('T5 A4', lambda x: (5*x - 2) * (2*x + 3), lambda x: 10*x**2 + 11*x - 6)
same('T5 B1', lambda x: (x + 4) * (x - 3) * (x + 1), lambda x: x**3 + 2*x**2 - 11*x - 12)
same('T5 B2', lambda x: (2*x + 3) * (x - 1) * (x + 5), lambda x: 2*x**3 + 11*x**2 + 2*x - 15)
same('T5 C1', lambda x: x**2 + 11*x + 24, lambda x: (x + 3) * (x + 8))
same('T5 C2', lambda x: x**2 - 8*x - 33, lambda x: (x - 11) * (x + 3))
same('T5 C3', lambda x: x**2 - 121, lambda x: (x + 11) * (x - 11))
same('T5 C4', lambda x: 3*x**2 - 27*x + 60, lambda x: 3 * (x - 4) * (x - 5))
same('T5 D1', lambda x: 2*x**2 + 11*x + 12, lambda x: (2*x + 3) * (x + 4))
same('T5 D2', lambda x: 3*x**2 - 7*x - 6, lambda x: (3*x + 2) * (x - 3))
same('T5 D3', lambda x: 6*x**2 - 3*x - 30, lambda x: 3 * (2*x - 5) * (x + 2))
roots('T5 E1', lambda x: x**2 + 3*x - 40, [-8, 5])
same('T5 E2', lambda x: (x**2 - 25) / (x**2 + 2*x - 15), lambda x: (x - 5) / (x - 3))
same('T5 F1a', lambda x: x**2 - 10*x + 18, lambda x: (x - 5)**2 - 7)
num('T5 F1b', 5**2 - 10*5 + 18, -7)
same('T5 F2', lambda n: (n + 3)**2 - (n + 1)**2, lambda n: 4 * (n + 2))
num('T5 F3', 65**2 - 35**2, 3000)

# ---------------- Test 6
same('T6 A1', lambda x: (x + 5) * (x + 12), lambda x: x**2 + 17*x + 60)
same('T6 A2', lambda x: (x - 3) * (x - 11), lambda x: x**2 - 14*x + 33)
same('T6 A3', lambda x: (3*x - 4)**2, lambda x: 9*x**2 - 24*x + 16)
same('T6 A4', lambda x: (x + 7) * (x - 5), lambda x: x**2 + 2*x - 35)
same('T6 B1', lambda x: (x - 3) * (x - 2) * (x + 6), lambda x: x**3 + x**2 - 24*x + 36)
same('T6 B2', lambda x: (x - 3)**3, lambda x: x**3 - 9*x**2 + 27*x - 27)
same('T6 C1', lambda x: x**2 + 3*x - 54, lambda x: (x + 9) * (x - 6))
same('T6 C2', lambda x: x**2 - 17*x + 72, lambda x: (x - 8) * (x - 9))
same('T6 C3', lambda x: 16*x**2 - 25, lambda x: (4*x + 5) * (4*x - 5))
same('T6 C4', lambda x: 7*x**2 - 7, lambda x: 7 * (x + 1) * (x - 1))
same('T6 D1', lambda x: 2*x**2 - 9*x + 10, lambda x: (2*x - 5) * (x - 2))
same('T6 D2', lambda x: 4*x**2 + 4*x - 3, lambda x: (2*x - 1) * (2*x + 3))
same('T6 D3', lambda x: 9*x**2 - 12*x + 4, lambda x: (3*x - 2)**2)
roots('T6 E1', lambda x: x**2 + 7*x - 18, [-9, 2])
same('T6 E2', lambda x: (2*x**2 + 5*x - 3) / (4*x**2 - 1), lambda x: (x + 3) / (2*x + 1))
same('T6 F1a', lambda x: (2*x + 3) * (x - 1) - 18, lambda x: 2*x**2 + x - 21)
roots('T6 F1b', lambda x: 2*x**2 + x - 21, [3, F(-7, 2)])
num('T6 F1 sides', (2*3 + 3, 3 - 1), (9, 2))
num('T6 F1 area', 9 * 2, 18)
num('T6 F1 perimeter', 2 * (9 + 2), 22)
same('T6 F2', lambda x: (2*x + 3)**2 - (2*x - 3)**2, lambda x: 24*x)
num('T6 F3', F(96, 10)**2 - F(4, 10)**2, 92)

# ---------------- Test 7
same('T7 A1', lambda x: (x + 7) * (x - 2), lambda x: x**2 + 5*x - 14)
same('T7 A2', lambda x: (x - 1) * (x - 12), lambda x: x**2 - 13*x + 12)
same('T7 A3', lambda x: (2*x - 7) * (3*x - 1), lambda x: 6*x**2 - 23*x + 7)
same('T7 A4', lambda x: (2*x + 3)**2, lambda x: 4*x**2 + 12*x + 9)
same('T7 B1', lambda x: (x + 1) * (x + 4) * (x - 5), lambda x: x**3 - 21*x - 20)
same('T7 B2', lambda x: (x + 3) * (2*x - 1)**2, lambda x: 4*x**3 + 8*x**2 - 11*x + 3)
same('T7 C1', lambda x: x**2 + 14*x + 45, lambda x: (x + 5) * (x + 9))
same('T7 C2', lambda x: x**2 - 2*x - 63, lambda x: (x - 9) * (x + 7))
same('T7 C3', lambda x: 49 - 4*x**2, lambda x: (7 + 2*x) * (7 - 2*x))
same('T7 C4', lambda x: x**2 + 1*x - 20, lambda x: (x - 4) * (x + 5))
same('T7 D1', lambda x: 3*x**2 + 14*x + 8, lambda x: (3*x + 2) * (x + 4))
same('T7 D2', lambda x: 5*x**2 - 12*x + 4, lambda x: (5*x - 2) * (x - 2))
same('T7 D3', lambda x: 12*x**2 + 22*x - 4, lambda x: 2 * (6*x - 1) * (x + 2))
roots('T7 E1', lambda x: 2*x**2 - 7*x + 3, [F(1, 2), 3])
same('T7 E2', lambda x: (x**2 - 3*x - 10) / (x**2 - 4), lambda x: (x - 5) / (x - 2))
same('T7 F1a', lambda x: x**2 + 6*x - 4, lambda x: (x + 3)**2 - 13)
num('T7 F1b', (-3)**2 + 6*(-3) - 4, -13)
same('T7 F2', lambda n: 2*n * (2*n + 2) + 1, lambda n: (2*n + 1)**2)
num('T7 F3', 76**2 - 24**2, 5200)

# ---------------- Test 8
same('T8 A1', lambda x: (x + 10) * (x + 3), lambda x: x**2 + 13*x + 30)
same('T8 A2', lambda x: (x - 4) * (x + 13), lambda x: x**2 + 9*x - 52)
same('T8 A3', lambda x, y: (x - 2*y) * (x + 5*y), lambda x, y: x**2 + 3*x*y - 10*y**2, two_vars=True)
same('T8 A4', lambda x: 3 * (x + 2)**2 - (x + 4) * (x - 1), lambda x: 2*x**2 + 9*x + 16)
same('T8 B1', lambda x: (x - 4) * (x + 1) * (x + 3), lambda x: x**3 - 13*x - 12)
same('T8 B2', lambda x: (2*x + 1)**3, lambda x: 8*x**3 + 12*x**2 + 6*x + 1)
same('T8 C1', lambda x: x**2 + 10*x + 21, lambda x: (x + 3) * (x + 7))
same('T8 C2', lambda x: x**2 - 9*x - 36, lambda x: (x - 12) * (x + 3))
same('T8 C3', lambda x: 25*x**2 - 64, lambda x: (5*x + 8) * (5*x - 8))
same('T8 C4', lambda x: 2*x**3 - 18*x, lambda x: 2*x * (x + 3) * (x - 3))
same('T8 D1', lambda x: 2*x**2 + 3*x - 20, lambda x: (2*x - 5) * (x + 4))
same('T8 D2', lambda x: 3*x**2 - 17*x + 10, lambda x: (3*x - 2) * (x - 5))
same('T8 D3', lambda x: 6*x**2 - 13*x - 5, lambda x: (3*x + 1) * (2*x - 5))
roots('T8 E1', lambda x: x * (x + 4) - 21, [-7, 3])
same('T8 E2', lambda x: (3*x**2 - 12) / (x**2 + x - 6), lambda x: 3 * (x + 2) / (x + 3))
same('T8 F1', lambda x: 3*x**2 - 12*x + 5, lambda x: 3 * (x - 2)**2 - 7)
same('T8 F2', lambda x: (x + 4)**2 - x**2, lambda x: 8*x + 16)
num('T8 F3', F(25, 2)**2 - F(15, 2)**2, 100)

print('All answers check out.')
