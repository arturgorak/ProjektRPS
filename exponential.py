import matplotlib.pyplot as plt
import scipy.stats as stats
import math


class Exponential:
    def __init__(self, lamb, n, accuracy, quantity, random_numbers):
        self.lamb = lamb
        self.n = n
        self.quantity = quantity
        self.accuracy = accuracy
        results = []
        self.results_frequency = []
        self.max_result_freq = 0
        self.count = []

        for x in range(quantity):
            results.insert(x, (-1) * math.log(1 - random_numbers[x]) / lamb)

        results.sort()

        self.results_frequency.insert(0, 0)
        self.iterator = 0
        for x in range(1, quantity):
            if results[x] < (self.iterator + 1) * accuracy:
                self.results_frequency[self.iterator] += 1
            else:
                self.iterator += 1
                self.results_frequency.insert(self.iterator, 1)

        for x in range(0, self.iterator + 1):
            self.count.insert(x, self.accuracy * (x + 1))


    def print(self):
        # plt.plot(self.count, self.results_frequency)
        # plt.suptitle('Rozkład wykładniczy')
        # plt.xlabel('Results')
        # plt.ylabel('Frequency')
        # plt.show()
        return 0



    def chi_square(self):

        expected = []
        for x in range(0, self.iterator + 1):
            expected.insert(x, self.lamb * math.exp((-1) * self.lamb * x * self.accuracy))

        skalowanie = 1

        for x in range(len(expected)):
            expected[x] = expected[x] * 10000

        chi_kwadrat = 0
        for i in range(len(expected)):
            if self.results_frequency[i] > 10 and expected[i] > 10:
                chi_kwadrat += (self.results_frequency[i] - expected[i]) ** 2 / expected[i]

        alfa = 0.5
        crit = stats.chi2.ppf(q=1 - alfa, df=self.iterator + 1)
        if chi_kwadrat < crit:
            print("Rozkład jest zgodny z rozkładem wykładniczym")
        else:
            print("Rozkład nie jest zgodny z rozkładem wykładniczym")
