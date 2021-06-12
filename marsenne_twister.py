import matplotlib.pyplot as plt
import scipy.stats as stats
import math


class Marsenne:
    def __init__(self, seed):
        self.mt = []
        self.index = 0
        self.mt.insert(0, seed)
        self.rand_num_array = []
        for i in range(1, 624):
            tmp = 1812433253 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i
            mask = ~(~0 << 32)
            self.mt.insert(i, tmp & mask)

    def generate(self):
        mask = (1 << 31) - 1
        for i in range(624):
            tmp = mask & (self.mt[((i + 1) % 624)])

            y = (1 & (self.mt[i] >> (32 - 1))) + tmp

            self.mt[i] = self.mt[(i + 397) % 624] ^ (y >> 1)
            if y % 2 == 1:
                self.mt[i] = self.mt[i] ^ 2567483615

    def extract_numbers(self):
        if self.index == 0:
            self.generate()

        y = self.mt[self.index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 2636928640)  # 0x9d2c5680
        y = y ^ ((y << 15) & 4022730752)  # 0xefc60000
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        return y

    def random_numbers(self, array, quantity, limit):

        for x in range(quantity):
            self.rand_num_array.insert(x, self.extract_numbers() % limit)

        for x in range(len(self.rand_num_array)):
            array.insert(x, self.rand_num_array[x]/limit)

    def print_frequency(self, limit):
        frequency = []
        count = []
        for x in range(limit):
            frequency.insert(x, 0)
            count.insert(x, x)

        for x in self.rand_num_array:
            frequency[x % limit] += 1

        maximum = 0
        for x in frequency:
            if x > maximum:
                maximum = x

        plt.title('Amount of data present in Marsenne Twister generator')
        plt.xlabel('Numbers')
        plt.ylabel('Quantity')
        plt.plot(count, frequency)
        plt.axis([0, limit, 0, maximum + maximum / 10])
        plt.show()

    def chi_square(self, array):
        expected = []
        actual = []
        n = 6
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
            else:
                actual[5] += 1

        chi = 0
        iterator = 0
        for x in range(n):
            if actual[x] > 5 and expected[x] > 5:
                chi += (actual[x] - expected[x]) ** 2 / expected[x]
                iterator += 1

        alfa = 0.05
        crit = stats.chi2.ppf(q=1 - alfa, df=iterator-1)
        if chi < crit:
            print("The distribution is consistent with the uniform distribution")
        else:
            print("The distribution is not consistent with the uniform distribution")

    def runs_test(self, random_numbers):
        tmp = []
        length = len(random_numbers)
        for x in range(length):
            tmp.insert(x, random_numbers[x])

        tmp.sort()
        median = 0
        if length % 2 == 0:
            median = 0.5 * (random_numbers[int(length / 2)] + random_numbers[int((length - 1) / 2)])
        else:
            median = random_numbers[int(length / 2)]

        runs = 0
        a_freq = 0
        b_freq = 0

        series_array = []
        for x in range(length):
            if random_numbers[x] > median:
                series_array.insert(x, 'a')
            elif random_numbers[x] < median:
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

        ek = 2 * a_freq * b_freq / length + 1
        dk = math.sqrt((2 * a_freq * b_freq * (2 * a_freq * b_freq - length)) / ((length - 1) * length * length))

        z = (runs - ek) / dk
        z_for_005 = 1.96
        # alfa = 0.05
        # p_values_one = stats.norm.sf(abs(z))  # one-sided
        # p_values_two = stats.norm.sf(abs(z)) * 2  # twosided
        #
        # print('Runs Test')
        # print('Number of runs: ' + str(runs))
        # print('Number of a\'s: %s; Number of b\'s: %s ' % (a_freq, b_freq))
        # print('Z value: ' + str(z))
        # print('One tailed P value: %s; Two tailed P value: %s ' % (p_values_one, p_values_two))

        if abs(z) > z_for_005:
            print("We reject the null hypothesis, i.e. the postulate of sample randomness")
        else:
            print("We cannot reject the null hypothesis, i.e. the randomness of the sample")