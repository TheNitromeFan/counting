from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 0 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def CountButSkipIfSumComposite(length=1000):
    n = 0
    i = 1
    print(i, n)
    while i < length:
        i += 1
        n += 1
        while not isPrime(sum(map(int, str(n)))):
            n += 1
        print(i, n)


CountButSkipIfSumComposite()
