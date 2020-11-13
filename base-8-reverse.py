def is_valid(number):
    s = str(number)
    if "8" in s or "9" in s:
        return False
    octal = oct(number)
    return octal[2:][::-1] == s


def base_eight_reverse_start():
    ind, current = 1, 0
    while current <= 1527465:
        if is_valid(current):
            yield ind, current
            ind += 1
        current += 1
        if current % 10000000 == 0:
            print(current)


def base_eight_reverse():
    ind, current = 1, 110000000
    while True:
        if is_valid(current):
            yield ind, current
            ind += 1
        current += 1
        if current % 10000000 == 0:
            print(current)


def main(filename, limit):
    '''
    with open(filename, "w") as f:
        for n, num in base_eight_reverse_start():
            f.write("{}\t\t{}\n".format(n, num))
            if num == limit:
                return
    '''
    for i, c in base_eight_reverse():
        print("{} {}\n".format(i, c))


if __name__ == "__main__":
    main("base-8-reverse.txt", 10**10 + 3)
