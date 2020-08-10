import random
from typing import List

from docx.text.paragraph import Paragraph

space = "       "
bracket = "（    ）"


def draw_one_multi_pron(paragraph: Paragraph, letter: str):
    run1 = paragraph.add_run(space)
    # run1.bold = True
    run1.font.underline = True
    paragraph.add_run('\n')
    run2 = paragraph.add_run(letter)
    # run2.bold = True
    paragraph.add_run('\n')
    run3 = paragraph.add_run(bracket)
    # run3.bold = True
    paragraph.add_run('\n')


def draw_two_multi_pron(paragraph: Paragraph, letter1: str, letter2: str):
    draw_empty(paragraph)

    run6 = paragraph.add_run(letter1)
    # run6.bold = True
    run7 = paragraph.add_run(space*4)
    run8 = paragraph.add_run(letter2)
    # run8.bold = True
    paragraph.add_run('\n')

    draw_empty(paragraph)


def draw_empty(paragraph: Paragraph):
    run0 = paragraph.add_run(space)
    run1 = paragraph.add_run(space)
    run1.underline = True
    run2 = paragraph.add_run(bracket)
    # run2.bold = True
    run3 = paragraph.add_run(space + space)
    run4 = paragraph.add_run(space)
    run4.underline = True
    run5 = paragraph.add_run(bracket)
    # run5.bold = True
    paragraph.add_run('\n')


def draw_like(paragraph: Paragraph, words: List[str]):
    words = random.sample(words, 2)
    for word in words:
        run = paragraph.add_run(word)
        # run.bold = True
        run2 = paragraph.add_run(bracket*3)
        # run2.bold = True
        run3 = paragraph.add_run(space)

    paragraph.add_run('\n')


