import matplotlib.pyplot as plt
import scipy.stats as stats


class Bernoulli:
    def __init__(self, p, quantity, random_numbers):
        self.p = p
        self.n = quantity
        self.distribution = []
        self.distribution.insert(0, 0)
        self.distribution.insert(1, 0)
        for x in random_numbers:
            if x <= p:
                self.distribution[0] += 1
            else:
                self.distribution[1] += 1

    def print(self):
        names = ['Sukcesy', 'Porażki']
        plt.bar(names, self.distribution)
        plt.suptitle('Rozkład Bernoulliego')
        plt.show()

    def chi_square(self):
        expected = []
        expected.insert(0, self.p * self.n)  # success
        expected.insert(1, (1 - self.p) * self.n)  # defeat

        chi_square_value = 0
        for i in range(2):
            chi_square_value += (self.distribution[i] - expected[i]) ** 2 / expected[i]

        alfa = 0.05
        crit = stats.chi2.ppf(q=1 - alfa, df=1)

        if chi_square_value < crit:
            print("Rozkład jest zgodny z rozkładem Bernoulliego")
        else:
            print("Rozkład nie jest zgodny z rozkładem Bernoulliego")

        # names = ['Sukcesy', 'Porażki']
        # plt.bar(names, expected)
        # plt.suptitle('Rozkład Bernoulliego spodziewany')
        # plt.show()