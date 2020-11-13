from string import digits
from itertools import permutations


def no_repeating_number():
    number_count = 1
    for length in range(2, 10):
        for number in permutations(digits[1:length]):
            yield number_count, number
            number_count += 1


def main(filename, limit):
    with open(filename, "w") as f:
        for n, num in no_repeating_number():
            f.write("{}\t\t{}\n".format(n, "".join(num)))
            if n == limit:
                return


if __name__ == "__main__":
    main("permutations.txt", 50000)
