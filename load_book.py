from cnocr import CnOcr


def load_book(filename):
    ocr = CnOcr()
    res = ocr.ocr(filename)
    res = ["".join(i) for i in res]
    # print(res)
    # print()
    res = "".join(res)
    # print(res)
    return res
