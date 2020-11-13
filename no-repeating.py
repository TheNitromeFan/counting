from string import digits
from itertools import product


def no_repeating_number():
    number_count, length = 1, 2
    while True:
        for number in product(digits, repeat=length):
            if number[0] == '0':
                continue
            if all(number.count(c) == 1 for c in number):
                yield number_count, number
                number_count += 1
        length += 1


def main(filename, limit):
    with open(filename, "w") as f:
        for n, num in no_repeating_number():
            f.write("{}\t\t{}\n".format(n, "".join(num)))
            if n == limit:
                return


if __name__ == "__main__":
    main("no-repeating.txt", 100000)
