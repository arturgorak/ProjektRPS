import matplotlib.pyplot as plt
import scipy.stats as stats
import math
from scipy.integrate import quad


def integrand(x, lamb):
    return lamb * math.exp((-1) * lamb * x)


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
        maximum = results[quantity - 1]
        maximum = round(maximum) + 1

        self.iterator = 0
        i = 0
        while i <= maximum:
            self.count.insert(self.iterator, i)
            i += accuracy
            self.iterator += 1

        for x in range(self.iterator):
            self.results_frequency.insert(x, 0)

        for x in results:
            for j in range(self.iterator):
                if x < self.count[j]:
                    self.results_frequency[j - 1] += 1
                    break

    def print(self):
        plt.plot(self.count, self.results_frequency)
        plt.suptitle('Rozkład wykładniczy')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()
        return 0

    def chi_square(self):

        expected = []
        for x in range(0, self.iterator - 1):
            I = quad(integrand, self.count[x], self.count[x + 1], args=self.lamb)
            expected.insert(x, I[0] * self.quantity)

        expected.insert(self.iterator - 1, 0)

        plt.plot(self.count, expected)
        plt.suptitle('Rozkład wykładniczy spodziewany')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()

        chi_kwadrat = 0
        for i in range(len(expected)):
            if self.results_frequency[i] > 10 and expected[i] > 10:
                chi_kwadrat += (self.results_frequency[i] - expected[i]) ** 2 / expected[i]

        alfa = 0.5
        crit = stats.chi2.ppf(q=1 - alfa, df=self.iterator)
        if chi_kwadrat < crit:
            print("Rozkład jest zgodny z rozkładem wykładniczym")
        else:
            print("Rozkład nie jest zgodny z rozkładem wykładniczym")
