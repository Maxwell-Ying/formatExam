import os
import sys
import random

import docx
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
# import divide
from docx.shared import Length
from load_new_words import load_new_words
from load_book import load_pages

day_in_week = "一二三四五六"

all_words = load_new_words(6)
all_letters = load_pages()

for index in all_words.keys():
    if index not in all_letters:
        continue
    doc_name = "六" + "年级第" + str(index) + "周课内巩固"
    document = docx.Document()
    document.styles['Normal'].font.name = u'宋体'
    document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    document.add_heading(doc_name, level=1)
    paragraph = document.add_paragraph("给下列词语注音并抄写\n")
    paragraph_format = paragraph.paragraph_format
    paragraph.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    paragraph_format.line_spacing = 1.5
    letter_count = 0
    line_count = 0
    for word in all_words[index]:
        if letter_count + len(word) > 16:
            paragraph.add_run("\n")
            letter_count = len(word)
            line_count += 1
            if line_count >= 2:
                break
        else:
            letter_count += len(word)
        paragraph.add_run(word + " ").bold = True
    paragraph.add_run("\n")

    paragraph2 = document.add_paragraph("生字组词\n")
    paragraph_format2 = paragraph.paragraph_format
    paragraph2.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    paragraph_format2.line_spacing = 1.5

    for x in range(6):
        run = paragraph2.add_run(all_letters[index][x] + "（   ）  （   ）  （   ） ")
        run.bold = True
        if x % 2 == 1:
            paragraph2.add_run("\n")

    document.save("11" + "-" + "1" + ".docx")
    break
