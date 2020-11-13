class Collatz:

    def __init__(self, filename, verbose=True):
        self.filename = filename
        self.verbose = verbose
        self.steps = {1: 1}

    def cycle_verbose(self, number):
        step = 0
        start = number
        while True:
            yield number, step
            if number == 1:
                self.steps[start] = step
                break
            elif number % 2:
                number = 3 * number + 1
            else:
                number //= 2
            step += 1

    def cycle_nonverbose(self, number):
        step = 0
        start = number
        while True:
            if number in self.steps:
                self.steps[start] = self.steps[number] + step
                return self.steps[start]
            elif number % 2:
                number = (3 * number + 1) // 2
                step += 2
            else:
                number //= 2
                step += 1

    def write(self, limit=1000):
        with open(self.filename, "w") as f:
            if self.verbose:
                for number in range(1, limit+1):
                    for a, step in self.cycle_verbose(number):
                        f.write("{}{}({}+{})\n".format(a, ' ' * (10 - len(str(a))), number, step))
                    f.write('-' * 40 + '\n')
            else:
                total = 0
                for number in range(1, limit+1):
                    total += self.cycle_nonverbose(number)
                    f.write("{}:{}{} steps          {} total steps\n".format(
                        number, ' ' * (11 - len(str(number))), self.steps[number], total))


foo = Collatz("collatz.txt", verbose=False)
foo.write()
bar = Collatz("collatz-verbose.txt", verbose=True)
bar.write()
