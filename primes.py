def is_prime(n, primes):
    for prime in primes:
        if n % prime == 0:
            return False
    return True


def main(limit=10**5):
    primes = [2]
    for n in range(3, limit, 2):
        if is_prime(n, primes):
            primes.append(n)
    with open("primes.txt", "w") as f:
        for prime in primes:
            f.write("{}\n".format(prime))


if __name__ == "__main__":
    main(limit=10**5)
