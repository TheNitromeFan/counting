import math


class Egyptian(object):
    def __init__(self, filename, limit):
        self.filename = filename
        self.limit = limit
        self.count = 1
        self.up = True

    @staticmethod
    def denominators(numerator, denominator):
        if numerator == 1:
            return [denominator]
        quotient = denominator // numerator + 1
        numerator, denominator = numerator * quotient - denominator, denominator * quotient
        common = math.gcd(numerator, denominator)
        return [quotient] + Egyptian.denominators(numerator // common, denominator // common)

    def numerators(self):
        denominator = 3
        while True:
            if self.up:
                loop = range(2, denominator, 1)
            else:
                loop = range(denominator-1, 1, -1)
            for number in loop:
                if math.gcd(number, denominator) == 1:
                    yield number, denominator
            denominator += 1
            self.up = not self.up

    def decomposition(self):
        with open(self.filename, "w") as f:
            f.write("EGYPTIAN FRACTION DECOMPOSITIONS")
            for numerator, denominator in Egyptian.numerators(self):
                f.write("\n{:05}\t\t{}/{} = ".format(self.count, numerator, denominator))
                f.write(" + ".join("1/{}".format(d) for d in Egyptian.denominators(numerator, denominator)))
                self.count += 1
                if self.count > self.limit:
                    return


if __name__ == "__main__":
    Egyptian("egyptian.txt", 10000).decomposition()
