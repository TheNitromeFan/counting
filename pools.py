def prime_factorize(n):
    factors = []
    if n % 2 == 0:
        count = 0
        while n % 2 == 0:
            count += 1
            n //= 2
        factors.append((2, count))
    prime = 3
    while prime ** 2 <= n:
        if n % prime == 0:
            count = 0
            while n % prime == 0:
                count += 1
                n //= prime
            factors.append((prime, count))
        prime += 2
    if n > 1:
        factors.append((n, 1))
    return factors


def stack_heights(n):
    return [base ** exponent for base, exponent in prime_factorize(n)]


def is_pool(n):
    heights = stack_heights(n)
    i, j = 0, len(heights)-1
    while i < j and heights[i] <= heights[i+1]:
        i += 1
    while j > i and heights[j] <= heights[j-1]:
        j -= 1
    return i != j


def main():
    f = open("no-pool.txt", "w")
    g = open("pool.txt", "w")
    f.write("1\t1\n")
    f_index, g_index = 2, 1
    for n in range(2, 1000000):
        if is_pool(n):
            g.write("{}\t{}\n".format(g_index, n))
            g_index += 1
        else:
            f.write("{}\t{}\n".format(f_index, n))
            f_index += 1
    f.close()
    g.close()


if __name__ == "__main__":
    main()
