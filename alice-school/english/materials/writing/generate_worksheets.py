# -*- coding: utf-8 -*-
"""Generate printable joined-up (cursive) handwriting practice worksheets
for Alice, using the "Homemade Apple" font (Google Fonts, SIL Open Font
License) — a genuinely connected script font that renders correctly with
plain PDF text placement (no OpenType ligature/shaping engine needed,
unlike proper school-cursive fonts such as Playwrite, whose letter-joining
ligatures don't get applied by reportlab)."""

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

pdfmetrics.registerFont(TTFont('Handwriting', 'fonts/HomemadeApple.ttf'))

PAGE_W, PAGE_H = A4
MARGIN = 45
LINE_COLOR = colors.HexColor('#B9BEC7')
TRACE_GRAY = 0.72
WORD_SIZE = 34
ROW_HEIGHT = 58
TOP_START = PAGE_H - 130


class Sheet:
    def __init__(self, filename, title, subtitle):
        self.c = canvas.Canvas(filename, pagesize=A4)
        self.title = title
        self.subtitle = subtitle
        self.y = TOP_START
        self._draw_header()

    def _draw_header(self):
        self.c.setFont('Helvetica-Bold', 22)
        self.c.setFillColor(colors.HexColor('#23201A'))
        self.c.drawString(MARGIN, PAGE_H - 60, self.title)
        self.c.setFont('Helvetica', 11)
        self.c.setFillColor(colors.HexColor('#6B6355'))
        self.c.drawString(MARGIN, PAGE_H - 80, self.subtitle)
        self.c.setFont('Helvetica-Oblique', 10)
        self.c.drawString(MARGIN, PAGE_H - 100, 'Trace over the grey words, then have a go all by yourself on the blank lines.')
        self.c.setStrokeColor(colors.HexColor('#E4DDCE'))
        self.c.line(MARGIN, PAGE_H - 110, PAGE_W - MARGIN, PAGE_H - 110)

    def _new_page(self):
        self.c.showPage()
        self.y = PAGE_H - 60

    def _ensure_space(self, needed):
        if self.y - needed < MARGIN:
            self._new_page()

    def section_label(self, text):
        self._ensure_space(30)
        self.c.setFont('Helvetica-Bold', 12.5)
        self.c.setFillColor(colors.HexColor('#0E9488'))
        self.c.drawString(MARGIN, self.y, text)
        self.y -= 26

    def ruled_row(self, text=None, gray=None):
        """Draw one ruled baseline; if text given, print it sitting on the line."""
        self._ensure_space(ROW_HEIGHT)
        self.y -= ROW_HEIGHT
        baseline = self.y + 14
        self.c.setStrokeColor(LINE_COLOR)
        self.c.setLineWidth(0.75)
        self.c.line(MARGIN, baseline, PAGE_W - MARGIN, baseline)
        if text:
            self.c.setFont('Handwriting', WORD_SIZE)
            if gray is not None:
                self.c.setFillColorRGB(gray, gray, gray)
            else:
                self.c.setFillColor(colors.HexColor('#23201A'))
            self.c.drawString(MARGIN + 4, baseline + 3, text)

    def word_block(self, word, blanks=2):
        """One model row (solid, black) + 2 trace rows (grey) + N blank rows."""
        self.ruled_row(word, gray=None)
        self.ruled_row(word, gray=TRACE_GRAY)
        self.ruled_row(word, gray=TRACE_GRAY)
        for _ in range(blanks):
            self.ruled_row()
        self.y -= 8

    def save(self):
        self.c.save()


# ---------------------------------------------------------------- WORDS

def build_words_sheet():
    s = Sheet('words_practice.pdf',
              'Joined-Up Writing: My Name & Words',
              'Alice — Handwriting practice')

    s.section_label('My name')
    s.word_block('Alice')

    s.section_label('Simple words')
    for word in ['cat', 'dog', 'sun', 'hop', 'big', 'run', 'play', 'jump']:
        s.word_block(word)

    s.save()


# ---------------------------------------------------------------- SENTENCES

def build_sentences_sheet():
    s = Sheet('sentences_practice.pdf',
              'Joined-Up Writing: Simple Sentences',
              'Alice — Handwriting practice')

    s.section_label('Short sentences')
    for sentence in [
        'I like to play.',
        'The cat sat in the sun.',
        'My name is Alice.',
        'The dog can run fast.',
    ]:
        s.word_block(sentence)

    s.save()


if __name__ == '__main__':
    build_words_sheet()
    build_sentences_sheet()
    print('done')
