import jieba
import load_book


def get_words():
    paragraph = load_book.load_book("语文课本.jpg")

    ret = jieba.lcut(paragraph)

    ret = [i for i in ret if len(i) > 1]
    return ret

# print(ret)
