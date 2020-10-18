import os


def load_new_letters(level):
    filename = os.path.join("book_data", "new_letter_" + str(level) + ".txt")
    ret = {}
    with open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            index, letters = line.split()
            letters = [i for i in letters]
            ret[index] = letters
    return ret


if __name__ == "__main__":
    print(load_new_letters(2))
