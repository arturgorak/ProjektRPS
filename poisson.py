import matplotlib.pyplot as plt
import scipy.stats as stats
import math


class Poisson:
    def __init__(self, lamb, n, quantity, random_numbers):
        self.lamb = lamb  # oczekiwana liczba zdarzen
        self.n = n  # liczba generacji w generatorze losowym
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
        plt.suptitle('Poisson distribution ')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()

    def chi_square(self):
        expected = []
        for k in range(self.max_result_freq):
            expected.insert(k, (math.pow(self.lamb, k) * math.exp((-1) * self.lamb)) / math.factorial(k) * self.n)

        plt.bar(self.count, expected)
        plt.suptitle('expected Poisson distribution ')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()


        chi = 0.
        degrees = 0
        for i in range(len(expected)):
            if self.results_frequency_without_tail[i] > 5 and expected[i] > 5:
                chi += ((self.results_frequency_without_tail[i] - expected[i]) ** 2) / expected[i]
                degrees += 1

        alfa = 0.05
        crit = stats.chi2.ppf(q=1 - alfa, df=degrees - 1)

        if chi < crit:
            print('The distribution is consistent with the Poisson distribution ')
        else:
            print('The distribution is not consistent with the Poisson distribution ')
