from itertools import product


def strobogrammatic_number():
    pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
    strobogrammatic_cache = {0: [""], 1: ["0", "1", "8"]}
    yield 1, "0"
    yield 2, "1"
    yield 3, "8"
    number_count, length = 4, 2
    while True:
        strobogrammatic_cache[length] = []
        for x, y in pairs:
            for number in strobogrammatic_cache[length-2]:
                new_number = x + number + y
                strobogrammatic_cache[length].append(new_number)
                if x != "0":
                    yield number_count, new_number
                    number_count += 1
        length += 1


def main(filename, limit):
    with open(filename, "w") as f:
        for n, num in strobogrammatic_number():
            f.write("{}\t\t{}\n".format(n, num))
            if n == limit:
                return


if __name__ == "__main__":
    main("strobogrammatic.txt", 20000)
