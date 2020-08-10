from pypinyin import pinyin


def get_multi_pronounce(new_words):
    ret = []
    letters = "".join(new_words)
    for letter in letters:
        if len(pinyin(letter, heteronym=True)[0]) > 1:
            ret.append(letter)
    return ret


if __name__ == "__main__":
    print(get_multi_pronounce(["惊", "将军"]))
