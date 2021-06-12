import matplotlib.pyplot as plt
import scipy.stats as stats


class Geometric:
    def __init__(self, p, n, quantity, random_numbers):
        self.p = p
        self.n = n
        self.quantity = quantity
        results = []
        results_frequency = []
        self.max_result_freq = 0
        iterator = 0

        for x in range(quantity):
            results_frequency.insert(x, 0)

        for x in range(n):
            X = 1

            if iterator == quantity:
                break

            u = random_numbers[iterator]
            iterator += 1

            while u > p:
                X += 1
                if iterator == quantity:
                    break
                u = random_numbers[iterator]
                iterator += 1

            results.insert(x, X)
            results_frequency[X] += 1

            if self.max_result_freq < X:
                self.max_result_freq = X

        self.results_frequency_without_tail = []
        self.count = []

        for x in range(self.max_result_freq):  # delete a tail of zeros
            self.count.insert(x, x)
            self.results_frequency_without_tail.insert(x, results_frequency[x])

    def print(self):
        plt.bar(self.count, self.results_frequency_without_tail)
        plt.suptitle('Rozkład geometryczny')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()

    def chi_square(self):

        frequency_exp = []
        frequency_exp.insert(0, 0)

        for k in range(1, self.max_result_freq):
            frequency_exp.insert(k, (1 - self.p) ** (k - 1) * self.p * self.n)

        degrees = 0
        chi = 0
        for i in range(1, self.max_result_freq):
            if self.results_frequency_without_tail[i] > 5 and frequency_exp[i] > 5:
                chi += (self.results_frequency_without_tail[i] - frequency_exp[i]) ** 2 / frequency_exp[i]
                degrees += 1

        alfa = 0.05
        crit = stats.chi2.ppf(q=(1 - alfa), df=degrees - 1)

        if chi < crit:
            print("Rozkład jest zgodny z rozkładem geometrycznym")
        else:
            print("Rozkład nie jest zgodny z rozkładem geometrycznym")

        # plt.bar(self.count, frequency_exp)
        # plt.suptitle('Rozkład geometryczny spodziewany')
        # plt.xlabel('Results')
        # plt.ylabel('Frequency')
        # plt.show()
