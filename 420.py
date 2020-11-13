from string import digits
from itertools import product


def four_twenty_number():
    number_count, length = 1, 2
    while True:
        for number in product(digits, repeat=length):
            if number[0] == '0':
                continue
            number = "".join(number)
            if '420' in number:
                yield number_count, number
                number_count += 1
        length += 1


def main(filename, limit):
    with open(filename, "w") as f:
        for n, num in four_twenty_number():
            f.write("{}\t\t{}\n".format(n, num))
            if n == limit:
                return


if __name__ == "__main__":
    main("420.txt", 20000)
