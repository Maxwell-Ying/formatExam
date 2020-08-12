import os


def load_new_words(level):
    ret = {}
    filename = os.path.join("book_data", "new_word_" + str(level) + ".txt")
    with open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            letters = line.strip().split(" ")
            letters = [i for i in letters if i]
            index = letters[0]
            others = letters[1:]
            ret[index] = others
    return ret


if __name__ == "__main__":
    res = load_new_words(level=2)
    print(res)
