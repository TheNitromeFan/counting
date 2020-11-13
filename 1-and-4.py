from string import digits
from itertools import product


def one_and_four_number():
    number_count, length = 1, 2
    while True:
        for number in product(digits, repeat=length):
            if number[0] == '0':
                continue
            if '1' in number and '4' in number:
                yield number_count, number
                number_count += 1
        length += 1


def main(filename, limit):
    with open(filename, "w") as f:
        for n, num in one_and_four_number():
            f.write("{}\t\t{}\n".format(n, "".join(num)))
            if n == limit:
                return


if __name__ == "__main__":
    main("1-and-4.txt", 20000)
