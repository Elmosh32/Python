def write_to_file(lst):
    f = open("file1", "w")
    for i in lst:
        f.write(str(i) + "\n")
    f.close()


def read_from_file():
    sum = 0
    f_r = open("file1", "r")
    f_w = open("file1", "a")
    for line in f_r:
        sum += int(line)
    f_w.write("the sum of numbers is: " + str(sum))
    f_r.close()
    f_w.close()


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    write_to_file(lst)
    read_from_file()
