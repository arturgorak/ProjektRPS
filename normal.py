import matplotlib.pyplot as plt
import scipy.stats as stats
import math
from scipy.integrate import quad


def integrand(x):
    return (1/(math.sqrt(2*math.pi)))*math.exp((-0.5) * x * x)


class Normal:
    def __init__(self, quantity, random_numbers, accuracy):
        self.n = quantity
        self.accuracy = accuracy
        self.x = []
        self.y = []
        i = 0
        iterator = 0
        while i < quantity:
            while random_numbers[i] == 0:
                i += 1
                if i == quantity:
                    break

            if i == quantity:
                break
            theta = 2 * math.pi * random_numbers[i]
            i += 1
            if i == quantity:
                break

            while random_numbers[i] == 0:
                i += 1
                if i == quantity:
                    break
            if i == quantity:
                break
            r = math.sqrt((-2) * math.log(random_numbers[i]))

            i += 1
            self.x.insert(iterator, r * math.cos(theta))
            self.y.insert(iterator, r * math.sin(theta))
            iterator += 1

        self.frequency_x = []
        self.frequency_y = []

        self.count = []
        self.x.sort()
        self.y.sort()

        minimum = round(self.x[0])
        maksimum = (-1) * minimum
        iterator = 0
        i = minimum
        while i <= maksimum:
            self.count.insert(iterator, i)
            i += accuracy
            iterator += 1

        for x in range(iterator):
            self.frequency_x.insert(x, 0)
            self.frequency_y.insert(x, 0)

        for x in self.x:
            for j in range(iterator):
                if x < self.count[j]:
                    self.frequency_x[j - 1] += 1
                    break

        for x in self.y:
            for j in range(iterator):
                if x < self.count[j]:
                    self.frequency_y[j - 1] += 1
                    break

    def print(self):
        # plt.scatter(x=self.x, y=self.y, s=0.0001, marker='o', c='r', edgecolors='purple')
        # plt.suptitle('Rozkład Normalny')
        # plt.show()

        plt.plot(self.count, self.frequency_x)
        plt.suptitle('Rozkład Normalny wedle osi X')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()

        plt.plot(self.count, self.frequency_y)
        plt.suptitle('Rozkład Normalny wedle osi Y')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()


    def chi_square(self):
        expected = []
        iterator = 0
        for x in self.count:
            I = quad(integrand, x, x + self.accuracy)
            expected.insert(iterator, I[0] * self.n/2)
            iterator += 1

        chi = 0
        iterator = 0
        for x in range(len(expected)):
            if expected[x] > 10 and self.frequency_x[x] > 10:
                chi += (self.frequency_x[x] - expected[x]) ** 2 / expected[x]
                iterator += 1

        alfa = 0.5
        crit = stats.chi2.ppf(q=1 - alfa, df=iterator)
        print(str(chi) + " " + str(crit))
        if chi < crit:
            print("Rozkład X jest zgodny z rozkładem naturalnym")
        else:
            print("Rozkład X nie jest zgodny z rozkładem naturalnym")

        chi = 0
        iterator = 0
        for x in range(len(expected)):
            if expected[x] > 10 and self.frequency_y[x] > 10:
                chi += (self.frequency_y[x] - expected[x]) ** 2 / expected[x]
                iterator += 1


        crit = stats.chi2.ppf(q=1 - alfa, df=iterator)
        print(str(chi) + " " + str(crit))
        if chi < crit:
            print("Rozkład Y jest zgodny z rozkładem naturalnym")
        else:
            print("Rozkład Y nie jest zgodny z rozkładem naturalnym")

        plt.plot(self.count, expected)
        plt.suptitle('Rozkład Normalny spodziewany')
        plt.xlabel('Results')
        plt.ylabel('Frequency')
        plt.show()