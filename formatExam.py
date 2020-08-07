import os
import sys
import docx
import divide

day_in_week = "一二三四五六"


def get_words(fin):
    ret = []
    for line in fin.readlines():
        line = line.strip()
        word = line.split("\t")[0]
        ret.append(word)
    return ret


words = []

for file in os.listdir("data"):
    with open(os.path.join("data", file)) as f:
        words += get_words(f)

words = [i for i in words if 2 <= len(i) <= 4]

for i in range(6):
    degree = i+1
    for j in range(20):
        doc_name = day_in_week[i] + "年级第" + str(j+1) + "周课内巩固"
        document = docx.Document()
        document.add_heading(doc_name, level=2)
        paragraph = document.add_paragraph("给下列词语注音并抄写")
        



