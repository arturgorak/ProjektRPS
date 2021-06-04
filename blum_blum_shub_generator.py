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
