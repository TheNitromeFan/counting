def is_not_composite(n):
    if n <= 2:
        return True
    elif n % 2 == 0:
        return False
    for p in range(3, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            return False
    return True


def sum_is_not_composite(n):
    sum_of_digits = 0
    while n:
        sum_of_digits += n % 10
        n //= 10
    return is_not_composite(sum_of_digits)


def main(filename, limit):
    with open(filename, "w") as f:
        count = 1
        for n in range(limit+1):
            if sum_is_not_composite(n):
                f.write("{}\t\t{}\n".format(count, n))
                count += 1


if __name__ == "__main__":
    main("sum-not-composite.txt", 10000)
