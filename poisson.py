import matplotlib.pyplot as plt
import scipy.stats as stats
import math


class Poisson:
    def __init__(self, lamb, p, n, quantity, random_numbers):
        self.lamb = lamb
        self.p = p
        self.n = n
        self.quantity = quantity
        results = []
        results_frequency = []
        self.max_result_freq = 0

        self.results_frequency_without_tail = []
        self.count = []

        for x in range(n):
            results_frequency.insert(x, 0)

        iterator = 0
        for x in range(n):
            if iterator == quantity:
                break
            u = random_numbers[iterator]
            iterator += 1

            X = 0

            while u >= math.exp((-1) * lamb):
                if iterator == quantity:
                    break

                u = u * random_numbers[iterator]
                iterator += 1
                X += 1

            results.insert(x, X)
            results_frequency[X] += 1

            if self.max_result_freq < X:
                self.max_result_freq = X

        for x in range(self.max_result_freq):  # delete a tail of zeros
            self.count.insert(x, x)
            self.results_frequency_without_tail.insert(x, results_frequency[x])

    def print(self):
        plt.bar(self.count, self.results_frequency_without_tail)
        plt.suptitle('Rozkład Poissona')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()

    def chi_square(self):
        results_frequency_expected = []
        for k in range(self.max_result_freq):
            results_frequency_expected.insert(k, (math.pow(self.lamb, k) * math.exp((-1) * self.lamb)) / math.factorial(k) * self.n)

        chi_kwadrat = 0
        stopnie = 0
        for i in range(self.max_result_freq):
            if self.results_frequency_without_tail[i] > 10 and results_frequency_expected[i] > 10:
                chi_kwadrat += (self.results_frequency_without_tail[i] - results_frequency_expected[i]) ** 2 / results_frequency_expected[i]
                stopnie += 1

        alfa = 0.05

        crit = stats.chi2.ppf(q=1 - alfa, df=stopnie)

        if chi_kwadrat < crit:
            print('Rozkład jest zgodny z rozkładem Poissona')
        else:
            print('Rozkład nie jest zgodny z rozkładem Poissona')
