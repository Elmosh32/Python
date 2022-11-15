def wc(file):
    new_word = True
    num_of_lines, num_of_words, num_of_chars = 0, 0, 0
    while True:
        ch = file.read(1)
        if not ch:
            break
        if ch == '\n':
            num_of_lines += 1
            num_of_chars += 1
            new_word = True
        elif ch.isspace():
            num_of_chars += 1
            new_word = True
        elif new_word and not ch.isspace():
            num_of_words += 1
            num_of_chars += 1
            new_word = False
        else:
            num_of_chars += 1
    print(num_of_words, num_of_chars, num_of_lines)


if __name__ == "__main__":
    f_r = open("alice", "r")
    wc(f_r)
    f_r.close()
