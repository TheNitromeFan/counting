import math


class LowerRadix(object):
    def __init__(self, filename, limit):
        self.filename = filename
        self.limit = limit
        self.primes = {2, 3, 5, 7}
        self.indices = \
            {(False, True, False, False): [3, 6, 9], (True, True, False, False): [6], (False, False, False, True): [7]}
        self.count = 1

    @staticmethod
    def prime_factors(number):
        primes = []
        while number % 2 == 0:
            primes.append(2)
            number //= 2
        prime = 3
        while number > 1:
            if number % prime == 0:
                primes.append(prime)
                number //= prime
            else:
                prime += 2
        return primes

    def denominators(self):
        denominator = 1
        while True:
            factors = LowerRadix.prime_factors(denominator)
            prime_count = (2 in factors, 3 in factors, 5 in factors, 7 in factors)
            if set(factors).issubset(self.primes) and prime_count in self.indices:
                print(denominator)
                yield denominator, self.indices[prime_count]
            denominator += 1

    @staticmethod
    def coprimes(number):
        for candidate in range(1, number):
            if math.gcd(candidate, number) == 1:
                yield candidate

    def fractions(self):
        with open(self.filename, "w") as f:
            f.write("COUNT\t\tFRACTION\n")
            for denominator, indices in LowerRadix.denominators(self):
                for numerator in LowerRadix.coprimes(denominator):
                    f.write("{:05}\t\t{}/{}\n".format(self.count, numerator, denominator))
                    self.count += len(indices)
                    if self.count > self.limit:
                        return

if __name__ == "__main__":
    LowerRadix("lowerradix.txt", 10000).fractions()
