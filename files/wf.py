def new_str(txt):
    chars = '''!?":;,()'`.*[]'''
    txt = txt.lower()
    for ele in txt:
        if ele in chars:
            txt = txt.replace(ele, "")
    return txt


def words_freq(txt):
    split_str = txt.split()
    my_dict = {}
    for word in split_str:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    print(sorted(my_dict.items(), key=lambda k: k[1]))


if __name__ == "__main__":
    f_r = open("txt", "r")
    lines = str(f_r.read())
    new_txt = new_str(lines)
    words_freq(new_txt)
    f_r.close()
