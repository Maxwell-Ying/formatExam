from cnocr import CnOcr


def load_book(filename):
    ocr = CnOcr()
    res = ocr.ocr(filename)
    res = ["".join(i) for i in res]
    new_res = []
    new_word = []
    for line in res:
        if "|" not in line:
            new_res.append(line)
        else:
            new_word = line.split("|")
            new_word = [i for i in new_word if i]

    res = "".join(res)

    return res, new_word
