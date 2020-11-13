two_square_map = {0: (0, 0), 1: (1, 0), 2: (1, 1)}
four_square_map = {0: (0, 0, 0, 0), 1: (1, 0, 0, 0), 2: (1, 1, 0, 0)}


def get_primes():
    with open("primes.txt", "r") as p:
        return [int(x.rstrip("\n")) for x in p]


def is_fermat(n, primes):
    for prime in primes:
        prime_count = 0
        while n % prime == 0:
            n //= prime
            prime_count += 1
        if prime % 4 == 3 and prime_count % 2 == 1:
            return False
        elif n == 1:
            return True


def two_square(n):
    m = int(n ** 0.5)
    while True:
        diff = n - m ** 2
        k = int(diff ** 0.5)
        if k * k + m * m == n:
            return m, k
        m -= 1


def is_legendre(n):
    while n % 4 == 0:
        n //= 4
    return n % 8 != 7


def three_square(n, primes):
    m = int(n ** 0.5)
    while True:
        diff = n - m ** 2
        if diff == 0:
            return m, 0, 0
        elif is_fermat(diff, primes):
            a, b = two_square(diff)
            return m, a, b
        m -= 1


def four_square_prime(n, primes):
    m = int(n ** 0.5)
    while True:
        diff = n - m ** 2
        if diff == 0:
            return m, 0, 0, 0
        elif is_legendre(diff):
            a, b, c = three_square(diff, primes)
            return m, a, b, c
        m -= 1


def four_square(limit):
    primes = get_primes()
    for n in range(3, limit+1):
        for prime in primes:
            if prime >= n:
                four_square_map[n] = four_square_prime(n, primes)
                break
            elif n % prime == 0:
                n1, n2 = prime, n // prime
                a, b = four_square_map[n1], four_square_map[n2]
                c1 = a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
                c2 = a[0] * b[1] + a[1] * b[0] + a[2] * b[3] - a[3] * b[2]
                c3 = a[0] * b[2] - a[1] * b[3] + a[2] * b[0] + a[3] * b[1]
                c4 = a[0] * b[3] + a[1] * b[2] - a[2] * b[1] + a[3] * b[0]
                c = sorted([abs(c1), abs(c2), abs(c3), abs(c4)], reverse=True)
                four_square_map[n] = tuple(c)
                break


def main(limit=10**5):
    four_square(limit)
    with open("four-squares.txt", "w") as f:
        for ind in range(limit+1):
            f.write("{0} = {1}^2 + {2}^2 + {3}^2 + {4}^2\n".format(ind, *four_square_map[ind]))


if __name__ == "__main__":
    main(limit=10**5)
