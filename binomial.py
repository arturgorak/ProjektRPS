import matplotlib.pyplot as plt
import math
import scipy.stats as stats


class Binomial:
    def __init__(self, p, size, random_numbers):
        self.p = p
        self.size = size
        self.results = []
        self.frequency = []
        self.count = []
        self.rn_size = len(random_numbers)
        iterator = 0
        for x in range(int(self.rn_size / size)):
            successes = 0
            for i in range(size):
                if random_numbers[iterator] < p:
                    successes += 1
                iterator += 1

            self.results.insert(x, successes)

        for x in range(size + 1):
            self.frequency.insert(x, 0)
            self.count.insert(x, x)

        for x in self.results:
            self.frequency[x] += 1

    def print(self):
        plt.bar(self.count, self.frequency)
        plt.suptitle('Binomial distribution ')
        plt.show()

    def chi_square(self):
        expected = []
        for x in range(self.size + 1):
            expected.insert(x, (math.factorial(self.size)/(math.factorial(self.size - x) * math.factorial(x)) * math.pow(self.p, x) * math.pow(1 - self.p, self.size - x))*(self.rn_size / self.size))

        plt.bar(self.count, expected)
        plt.suptitle('Expected binomial distribution ')
        plt.show()

        chi = 0
        degrees = 0
        for i in range(self.size + 1):
            if self.frequency[i] > 5 and expected[i] > 5:
                chi += (self.frequency[i] - expected[i]) ** 2 / expected[i]
                degrees += 1

        alfa = 0.05
        crit = stats.chi2.ppf(q=1 - alfa, df=degrees - 1)
        if chi < crit:
            print('The distribution is consistent with the binomial distribution')
        else:
            print('The distribution is not consistent with the binomial distribution')