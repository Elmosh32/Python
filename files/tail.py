def tail(file, num_of_lines):
    count = 1
    ls = []
    while num_of_lines != 0:
        file.seek(0, 2)
        file.seek((file.tell() - count), 0)
        ch = file.read(1)
        if ch == '\n':
            num_of_lines -= 1
            ls.append(str(file.readline()))
        count += 1

    for line in range(len(ls) - 1, -1, -1):
        print(ls[line], end="")


if __name__ == "__main__":
    f_r = open("alice", "r")
    tail(f_r, 10)
    f_r.close()

"""def tail(num_of_lines):
    f_r = open("alice", "r")
    f_r.seek(0, 2)

    lines = f_r.readlines()
    lines = lines[-num_of_lines:]
    for line in lines:
        print(line, end="")
    f_r.close()
"""
