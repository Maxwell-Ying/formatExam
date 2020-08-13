import os


def load_similar_letters(level):
    ret = []
    filename = os.path.join("book_data", "similar_letter_" + str(level) + ".txt")
    with open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            letters = line.strip()
            ret.append(letters)
    return ret


if __name__ == "__main__":
    res = load_similar_letters(2)
    print(res)
