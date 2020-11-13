from string import digits
from itertools import product


def has_consecutive(number, digit):
    if number.count(digit) > 1:
        return True
    if digit == '0':
        return '1' in number
    elif digit == '9':
        return '8' in number
    else:
        return str(int(digit) - 1) in number or str(int(digit) + 1) in number


def only_consecutive_number():
    number_count, length = 1, 2
    while True:
        for number in product(digits, repeat=length):
            if number[0] == '0':
                continue
            if all(has_consecutive(number, digit) for digit in number):
                yield number_count, number
                number_count += 1
        length += 1


def main(filename, limit):
    with open(filename, "w") as f:
        for n, num in only_consecutive_number():
            f.write("{}\t\t{}\n".format(n, "".join(num)))
            if n == limit:
                return


if __name__ == "__main__":
    main("only-consecutive.txt", 100000)
