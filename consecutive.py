from itertools import permutations, combinations
from string import digits


def compute():
    for r in range(2, 10):
        digit_tuples = set()
        for tup in combinations(digits, r):
            digits_sorted = sorted(tup)
            if "".join(digits_sorted) not in digits:
                continue
            for digit_tuple in permutations(digits_sorted, r):
                if digit_tuple[0] != "0":
                    digit_tuples.add(digit_tuple)
        yield sorted(digit_tuples)


def main(filename):
    index = 1
    with open(filename, "w") as f:
        for number_set in compute():
            for tup in number_set:
                f.write("{} {}\n".format(index, "".join(tup)))
                index += 1


if __name__ == "__main__":
    main("consecutive.txt")
