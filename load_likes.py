import os
import random
from typing import List

from docx.text.paragraph import Paragraph


def load_likes():
    ret = []
    with open(os.path.join("data", "形近字大全.txt"), encoding="gbk") as f:
        for line in f.readlines():
            line = line.strip()
            letters = line.split("：")
            if len(letters) > 1:
                letters = letters[1]
            else:
                letters = letters[0]
            letters = letters.split("，")
            letters = [i for i in letters if i]
            if letters:
                ret.append(letters)

    return ret


likes = load_likes()


def get_similar_letters(new_words: List[str]):
    ret = []
    for word in new_words:
        for letter in word:
            for like in likes:
                if letter in like:
                    ret.append(like)
    return ret


if __name__ == "__main__":
    print(get_similar_letters(["严厉", "股市"]))
