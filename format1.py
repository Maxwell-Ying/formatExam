import os
import sys
import random

import docx
from docx.enum.text import WD_LINE_SPACING
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
# import divide
from docx.shared import Length

from draw import draw_one_multi_pron, draw_two_multi_pron
from load_new_words import load_new_words
from load_book import load_pages
from load_likes import load_likes
from get_multi_pronouce import get_multi_pronounce

day_in_week = "一二三四五六"
brackets = "（   ）  （   ）  （   ）"

all_words = load_new_words(6)
all_letters = load_pages()
all_likes = load_likes()

for index in all_words.keys():
    if index not in all_letters:
        continue
    doc_name = "六" + "年级第" + str(index) + "周课内巩固"
    document = docx.Document()
    document.styles['Normal'].font.name = u'宋体'
    document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    heading = document.add_heading(doc_name, level=1)
    heading_format = heading.paragraph_format
    heading_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    paragraph = document.add_paragraph("一、给下列词语注音并抄写\n")
    paragraph_format = paragraph.paragraph_format
    paragraph.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    paragraph_format.line_spacing = 1.5
    letter_count = 0
    line_count = 0
    for word in all_words[index]:
        if len(word) > 4:
            continue
        if letter_count + len(word) > 16:
            paragraph.add_run("\n\n")
            letter_count = len(word)
            line_count += 1
            if line_count >= 2:
                break
        else:
            letter_count += len(word)
        paragraph.add_run(word + " ").bold = True
    paragraph.add_run("\n")

    paragraph2 = document.add_paragraph("二、生字组词\n")
    paragraph_format2 = paragraph.paragraph_format
    paragraph2.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    paragraph_format2.line_spacing = 1.5

    for x in range(6):
        run = paragraph2.add_run(all_letters[index][x] + brackets + "   ")
        run.bold = True
        if x % 2 == 1:
            paragraph2.add_run("\n")

    paragraph3 = document.add_paragraph("三、形近字辨析\n")
    paragraph_format3 = paragraph3.paragraph_format
    paragraph_format3.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE

    like1, like2 = all_likes[:2]
    for x in range(len(like1)):
        run = paragraph3.add_run(like1[x] + brackets + "   " + like2[x] + brackets + "\n")
        run.bold = True

    paragraph4 = document.add_paragraph("四、多音字辨析\n")
    paragraph_format4 = paragraph4.paragraph_format
    paragraph_format4.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE

    multi_pronounce = get_multi_pronounce(all_words[index])
    if len(multi_pronounce) == 0:
        print("第"+str(index)+"周生字中没有足够的多音字")
    elif len(multi_pronounce) == 1:
        draw_one_multi_pron(paragraph4, multi_pronounce[0])
    else:
        draw_two_multi_pron(paragraph4, multi_pronounce[0], multi_pronounce[1])

    document.save(os.path.join("result", "6" + "-" + str(index) + ".docx"))
    break
