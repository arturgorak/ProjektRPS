import math

import matplotlib.pyplot as plt


class Bbs:
    def __init__(self, x0, q, p, quantity):
        self.x0 = x0
        self.random_numbers = []
        m = q * p
        self.random_numbers.insert(0, x0)
        for x in range(1, quantity):
            self.random_numbers.insert(x, (self.random_numbers[x - 1] * self.random_numbers[x - 1]) % m)

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

        plt.title('Ilość występowania danych w generatorze Blum Blum Shub')
        plt.xlabel('Liczba')
        plt.ylabel('Ilość')
        plt.plot(count, frequency)
        plt.axis([0, limit, 0, maximum + maximum / 10])
        plt.show()

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

        a = 0  # when Xi > median
        b = 0  # when Xi < median
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
            a += 1
            a_freq += 1
        elif series_array[0] == 'b':
            b += 1
            b_freq += 1

        for x in range(1, length):
            if series_array[x] == 'a' and series_array[x-1] == 'b':
                a += 1
            elif series_array[x] == 'b' and series_array[x-1] == 'a':
                b += 1
            elif series_array[x] == 'b' and series_array[x-1] == 'c' and series_array[x-2] == 'a':
                b += 1
            elif series_array[x] == 'a' and series_array[x-1] == 'c' and series_array[x-2] == 'b':
                a += 1

            if series_array[x] == 'a':
                a_freq += 1
            elif series_array[x] == 'b':
                b_freq += 1

        # EK = 2*a_freq*b_freq/length + 1
        # DK = math.sqrt((2*a_freq*b_freq*(2*a_freq*b_freq - length))/((length - 1) * length * length))
        #
        # u = ((a + b) - EK) / DK
        # print("yo " + str(u))
