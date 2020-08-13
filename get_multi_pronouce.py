import os

from pypinyin import pinyin


def get_multi_pronounce(new_words):
    ret = []
    letters = "".join(new_words)
    for letter in letters:
        if len(pinyin(letter, heteronym=True)[0]) > 1:
            ret.append(letter)
    return ret


def load_multi_pronounce(level):
    ret = []
    filename = os.path.join("book_data", "multi_pronounce_" + str(level) + ".txt")
    with open(filename) as f:
        for line in f:
            line = line.strip()
            for letter in line:
                ret.append(letter)
    return ret


if __name__ == "__main__":
    print(load_multi_pronounce(2))
