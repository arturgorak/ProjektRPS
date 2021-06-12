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
        names = ['Successes', 'Failures']
        plt.bar(names, self.distribution)
        plt.suptitle('Bernoulli distribution')
        plt.show()

    def chi_square(self):
        expected = []
        expected.insert(0, self.p * self.n)  # success
        expected.insert(1, (1 - self.p) * self.n)  # defeat

        chi = 0
        for i in range(2):
            if self.distribution[i] > 5 and expected[i] > 5:
                chi += (self.distribution[i] - expected[i]) ** 2 / expected[i]

        alfa = 0.05
        crit = stats.chi2.ppf(q=1 - alfa, df=1)

        if chi < crit:
            print("The distribution is consistent with the Bernoulli distribution ")
        else:
            print("The distribution is not consistent with the Bernoulli distribution ")

        names = ['Successes', 'Failures']
        plt.bar(names, expected)
        plt.suptitle('expected Bernoulli distribution')
        plt.show()