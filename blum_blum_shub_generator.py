import math
import scipy.stats as stats
import matplotlib.pyplot as plt


class Bbs:
    def __init__(self, x0, q, p, quantity):
        self.x0 = x0
        self.random_numbers = []
        m = q * p
        self.random_numbers.insert(0, x0)
        for x in range(1, quantity):
            self.random_numbers.insert(x, (self.random_numbers[x - 1] * self.random_numbers[x - 1]) % m)

        # f = open("results.txt", "a")

        # f.write('#==================================================================\n')
        # f.write('# generator mt19937  seed = 3090176421\n')
        # f.write('#==================================================================\n')
        # f.write('type: d\n')
        # f.write('count: 1000000000\n')
        # f.write('numbit: 10\n')
        # print("yo")
        #
        # tmp = x0
        # f.write(str(tmp % 1000) + '\n')
        # for x in range(1, quantity):
        #     tmp = ((tmp * tmp) % m)
        #     # self.random_numbers.insert(x, (self.random_numbers[x - 1] * self.random_numbers[x - 1]) % m)
        #     f.write(str(tmp % 1000) + "\n")
        #
        # f.close()

    def generate_random_numbers(self, array, accuracy):
        for x in range(len(self.random_numbers)):
            array.insert(x, self.random_numbers[x] % accuracy / accuracy)

    def print_frequency(self, limit):
        frequency = []
        count = []
        for x in range(limit):
            frequency.insert(x, 0)
            count.insert(x, x)

        for x in self.random_numbers:
            frequency[x % limit] += 1

        maximum = 0
        for x in frequency:
            if x > maximum:
                maximum = x

        plt.title('Amount of data present in Blum Blum Shub generator')
        plt.xlabel('Numbers')
        plt.ylabel('Quantity')
        plt.plot(count, frequency)
        plt.axis([0, limit, 0, maximum + maximum / 10])
        plt.show()

    def chi_square(self, array):
        expected = []
        actual = []
        n = 7
        for x in range(n):
            expected.insert(x, int(len(array)/n))
            actual.insert(x, 0)

        for x in array:
            if x < 1/n:
                actual[0] += 1
            elif x < 2/n:
                actual[1] += 1
            elif x < 3/n:
                actual[2] += 1
            elif x < 4/n:
                actual[3] += 1
            elif x < 5/n:
                actual[4] += 1
            elif x < 6/n:
                actual[5] += 1
            else:
                actual[6] += 1

        chi = 0
        degrees = 0
        for x in range(n):
            if actual[x] > 5 and expected[x] > 5:
                chi += (actual[x] - expected[x]) ** 2 / expected[x]
                degrees += 1

        alfa = 0.05
        crit = stats.chi2.ppf(q=1 - alfa, df=degrees-1)
        if chi < crit:
            print("The distribution is consistent with the uniform distribution ")
        else:
            print("The distribution is not consistent with the uniform distribution ")


    def runs_test(self):
        tmp = []
        length = len(self.random_numbers)
        for x in range(length):
            tmp.insert(x, self.random_numbers[x])

        tmp.sort()
        median = 0
        if length % 2 == 0:
            median = 0.5 * (self.random_numbers[int(length / 2)] + self.random_numbers[int((length - 1) / 2)])
        else:
            median = self.random_numbers[int(length / 2)]

        runs = 0
        a_freq = 0
        b_freq = 0

        series_array = []
        for x in range(length):
            if self.random_numbers[x] > median:
                series_array.insert(x, 'a')
            elif self.random_numbers[x] < median:
                series_array.insert(x, 'b')
            else:
                series_array.insert(x, 'c')

        if series_array[0] == 'a':
            runs += 1
            a_freq += 1
        elif series_array[0] == 'b':
            runs += 1
            b_freq += 1

        for x in range(1, length):
            if series_array[x] == 'a' and series_array[x-1] == 'b':
                runs += 1
            elif series_array[x] == 'b' and series_array[x-1] == 'a':
                runs += 1
            elif series_array[x] == 'b' and series_array[x-1] == 'c' and series_array[x-2] == 'a':
                runs += 1
            elif series_array[x] == 'a' and series_array[x-1] == 'c' and series_array[x-2] == 'b':
                runs += 1

            if series_array[x] == 'a':
                a_freq += 1
            elif series_array[x] == 'b':
                b_freq += 1

        ek = 2*a_freq*b_freq/length + 1
        dk = math.sqrt((2*a_freq*b_freq*(2*a_freq*b_freq - length))/((length - 1) * length * length))

        z = (runs - ek) / dk
        z_for_005 = 1.96
        # alfa = 0.05
        # p_values_one = stats.norm.sf(abs(z))  # one-sided
        # p_values_two = stats.norm.sf(abs(z)) * 2  # twosided
        #

        if abs(z) > z_for_005:
            print("We reject the null hypothesis, i.e. the postulate of sample randomness")
        else:
            print("We cannot reject the null hypothesis, i.e. the randomness of the sample")


