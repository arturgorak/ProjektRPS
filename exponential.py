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
        self.results = []
        self.results_frequency = []
        self.max_result_freq = 0
        self.count = []

        for x in range(quantity):
            self.results.insert(x, (-1) * math.log(1 - random_numbers[x]) / lamb)

        self.results.sort()
        self.maximum = self.results[quantity - 1]
        self.maximum = round(self.maximum) + 1

        self.iterator = 0
        i = 0
        while i <= self.maximum:
            self.count.insert(self.iterator, i)
            i += self.accuracy
            self.iterator += 1

        for x in range(self.iterator):
            self.results_frequency.insert(x, 0)

        for x in self.results:
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
        compartments = []
        real = []
        expected = []
        width_comp = self.maximum / 7
        i = 0
        tmp = 0
        while i <= self.maximum:
            compartments.insert(tmp, i)
            i += width_comp
            tmp += 1

        for x in range(tmp):
            real.insert(x, 0)

        for x in self.results:
            for j in range(tmp):
                if x < compartments[j]:
                    real[j - 1] += 1
                    break

        for x in range(0, tmp - 1):
            I = quad(integrand, compartments[x], compartments[x + 1], args=self.lamb)
            expected.insert(x, I[0] * self.quantity)

        expected.insert(tmp - 1, 0)

        # plt.plot(compartments, expected)
        # plt.suptitle('Rozkład wykładniczy spodziewany')
        # plt.xlabel('Results')
        # plt.ylabel('Frequency')
        # plt.show()

        chi = 0
        degrees = 0
        for i in range(len(expected)):
            if real[i] > 5 and expected[i] > 5:
                chi += ((real[i] - expected[i]) ** 2) / expected[i]
                degrees += 1

        alfa = 0.05
        crit = stats.chi2.ppf(q=1 - alfa, df=degrees - 1)
        if chi < crit:
            print("Rozkład jest zgodny z rozkładem wykładniczym")
        else:
            print("Rozkład nie jest zgodny z rozkładem wykładniczym")