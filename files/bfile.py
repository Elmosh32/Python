import struct


def write_to_file(ls):
    f = open("file", "wb")
    f.write(struct.pack('c', "\n".encode()))
    for i in range(len(ls) - 1):
        leng = str(len(str(ls[i])) + 1) + 's'
        f.write(struct.pack(leng, (str(ls[i]) + "\n").encode()))
    f.write(struct.pack('c', (str(ls[len(ls) - 1]).encode())))

    f.close()


def read_from_file():
    sumf = 0
    txt = "the sum of numbers is: "
    f_w = open("file", "ab")
    f_r = open("file", "rb")
    for line in f_r:
        sumf += int(struct.unpack('s', f_r.read(1))[0].decode("UTF-8"))

    txt += str(sumf)
    n = len(txt)
    leng = str(n) + 's'
    f_w.write(struct.pack(leng, (txt).encode()))

    f_r.close()
    f_w.close()
    f_r = open("file", "rb")
    for line in f_r:
        num = len(line)
        print(struct.unpack('{}s'.format(num), line)[0].decode("UTF-8"))
    f_r.close()


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    write_to_file(lst)
    read_from_file()
