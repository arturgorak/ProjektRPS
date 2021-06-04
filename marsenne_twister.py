import matplotlib.pyplot as plt

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

        plt.title('Ilość występowania danych w generatorze Marsenne Twister')
        plt.xlabel('Liczba')
        plt.ylabel('Ilość')
        plt.plot(count, frequency)
        plt.axis([0, limit, 0, maximum + maximum / 10])
        plt.show()

