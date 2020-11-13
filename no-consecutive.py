from string import digits
from itertools import product


def non_consecutive_number():
    consecutive_pairs = [digits[i:i+2] for i in range(9)]
    number_count, length = 1, 1
    while True:
        for number in product(digits, repeat=length):
            if number[0] == '0':
                continue
            for pair in consecutive_pairs:
                if all(digit in number for digit in pair):
                    break
            else:
                yield number_count, number
                number_count += 1
        length += 1


def main(filename, limit):
    with open(filename, "w") as f:
        for n, num in non_consecutive_number():
            f.write("{}\t\t{}\n".format(n, "".join(num)))
            if n == limit:
                return


if __name__ == "__main__":
    main("no-consecutive.txt", 20000)
