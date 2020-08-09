import os

from cnocr import CnOcr


digits = "1234567890"

ocr = CnOcr()


def load_page(filename, prefix=0):
    filename = os.path.join("book_data", filename)

    lines = ocr.ocr(filename)
    index_letter = {}
    for line in lines:
        # print(line)
        index = ""
        others = []
        for item in line:
            if item in digits:
                index += item
            else:
                others.append(item)
        if not index:
            continue
        if len(index) > 1:
            index = "".join(index)
        index_letter[str(int(index)+prefix)] = others

    return index_letter


def load_pages():
    map1 = load_page("61.png")
    map2 = load_page("62.png")
    map3 = load_page("63.png", 25)
    map_all = {**map1, **map2, **map3}
    # print(map_all)
    return map_all


if __name__ == "__main__":
    m = load_pages()
    print(m)
