import matplotlib.pyplot as plt
import math
import scipy.stats as stats
MT = []
index = 0


def initialize_generator(seed):
    global MT
    MT.insert(0, seed)
    for i in range(1, 624):
        tmp = 1812433253 * (MT[i - 1] ^ (MT[i - 1] >> 30)) + i
        mask = ~(~0 << 32)
        MT.insert(i, tmp & mask)


def generate_numbers():
    mask = (1 << 31) - 1
    for i in range(624):
        tmp = mask & (MT[((i + 1) % 624)])

        y = (1 & (MT[i] >> (32 - 1))) + tmp

        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if y % 2 == 1:
            MT[i] = MT[i] ^ 2567483615


def extract_numbers():
    global index
    if index == 0:
        generate_numbers()

    y = MT[index]
    y = y ^ (y >> 11)
    y = y ^ ((y << 7) & 2636928640)  # 0x9d2c5680
    y = y ^ ((y << 15) & 4022730752)  # 0xefc60000
    y = y ^ (y >> 18)

    index = (index + 1) % 624
    return y


def blum_blum_shub(x0, q, p, n, array):
    m = q*p
    array.insert(0, x0)
    for i in range(1, n):
        array.insert(i, (array[i - 1] * array[i - 1]) % m)


if __name__ == '__main__':

    #
    # initialize_generator(seed=seed)
    #
    # random_numbers = []
    # for x in range(how_many_numbers):
    #     random_numbers.insert(x, (extract_numbers() % seed / seed))
    #
    # results = []
    # for x in range(seed):
    #     results.insert(x, 0)
    #
    # for x in random_numbers:
    #     results[int(x*seed)] += 1
    #
    #
    # maximum = 0
    # for x in results:
    #     if x > maximum:
    #         maximum = x
    #
    # plt.title('Ilość występowania danych MT')
    # plt.xlabel('Liczba')
    # plt.ylabel('Ilość')
    # plt.plot(count, results)
    # plt.axis([0, seed, 0, maximum + maximum/10])
    # plt.grid(True)
    # plt.show()

    #
    bbs_array = []
    seed = 1000
    how_many_numbers = 1000000
    blum_blum_shub(seed, 30000000091, 40000000003, n=how_many_numbers, array=bbs_array)

    count = []
    for x in range(0, seed):
        count.insert(x, x)

    results2 = []
    for x in range(seed):
        results2.insert(x, 0)

    for x in bbs_array:
        results2[x % seed] += 1

    maximum2 = 0
    for x in results2:
        if x > maximum2:
            maximum2 = x

    plt.title('Ilość występowania danych bbs')
    plt.xlabel('Liczba')
    plt.ylabel('Ilość')
    plt.plot(count, results2)
    plt.axis([0, seed, 0, maximum2 + maximum2 / 10])
    plt.grid(True)
    plt.show()

    random_numbers = []
    for x in range(len(bbs_array)):
        random_numbers.insert(x, (bbs_array[x] % seed)/seed)

    # Rozkład Bernouliego
    p = 0.3
    bernoulli_distribution = []
    bernoulli_distribution.insert(0, 0)  # success
    bernoulli_distribution.insert(1, 0)  # defeat

    for x in random_numbers:
        if x <= p:
            bernoulli_distribution[0] += 1
        else:
            bernoulli_distribution[1] += 1

    names = ['Sukcesy', 'Porażki']
    plt.bar(names, bernoulli_distribution)
    plt.suptitle('Rozkład Bernoulliego')
    plt.show()

    # Rozkład geometryczny

    p = 0.3
    n = 1000
    iterator = 0
    geometric_results = []
    geometric_results_frequency = []
    max_geo_result_freq = 0

    for x in range(how_many_numbers):
        geometric_results_frequency.insert(x, 0)

    for x in range(n):
        X = 1

        if iterator == how_many_numbers:
            break
        U = random_numbers[iterator]
        iterator += 1

        while U > p:
            X += 1
            if iterator == how_many_numbers:
                break
            U = random_numbers[iterator]
            iterator += 1

        geometric_results.insert(x, X)
        geometric_results_frequency[X] += 1

        if max_geo_result_freq < X:
            max_geo_result_freq = X

    geometric_results_frequency_without_tail = []
    geometric_count = []

    for x in range(max_geo_result_freq + int(max_geo_result_freq/10)):  # delete a tail of zeros
        geometric_count.insert(x, x)
        geometric_results_frequency_without_tail.insert(x, geometric_results_frequency[x])

    plt.bar(geometric_count, geometric_results_frequency_without_tail)
    plt.suptitle('Rozkład geometryczny')
    plt.xlabel('Results')
    plt.ylabel('Frequency')
    plt.show()

    # Rozkład Poissona

    lamb = 10
    poisson_results = []
    poisson_results_frequency = []
    poisson_results_frequency_without_tail = []
    poisson_count = []
    max_result_freq = 0
    poisson_n = 10000

    for x in range(poisson_n):
        poisson_results_frequency.insert(x, 0)

    iterator = 0
    pr_iterator = 0
    for x in range(poisson_n):
        if iterator == how_many_numbers:
            break
        U = random_numbers[iterator]
        iterator += 1

        X = 0

        while U >= math.exp((-1) * lamb):
            if iterator == how_many_numbers:
                break

            U = U * random_numbers[iterator]
            iterator += 1
            X += 1

        poisson_results.insert(x, X)
        poisson_results_frequency[X] += 1

        if max_result_freq < X:
            max_result_freq = X

    for x in range(max_result_freq):  # delete a tail of zeros
        poisson_count.insert(x, x)
        poisson_results_frequency_without_tail.insert(x, poisson_results_frequency[x]/poisson_n)

    poisson_results_frequency_expected = []

    for k in range(max_result_freq):
        poisson_results_frequency_expected.insert(k, (math.pow(lamb, k) * math.exp((-1) * lamb))/math.factorial(k))

    chi_kwadrat = 0
    for i in range(max_geo_result_freq):
        chi_kwadrat += (poisson_results_frequency_without_tail[i] - poisson_results_frequency_expected[i])**2/poisson_results_frequency_expected[i]

    alfa = 0.05
    p = 1  # only lambda
    k = max_result_freq
    df = k - p - 1

    crit = stats.chi2.ppf(q=alfa, df=df)
    if chi_kwadrat < crit:
        print("Rozkład jest zgodny z rozkładem Poissona")
    else:
        print("Rozkład nie jest zgodny z rozkładem Poissona")

    plt.bar(poisson_count, poisson_results_frequency_without_tail)
    plt.suptitle('Rozkład Poissona')
    plt.xlabel('Results')
    plt.ylabel('Frequency')
    plt.show()

    plt.bar(poisson_count, poisson_results_frequency_expected)
    plt.suptitle('Rozkład Poissona spodziewany')
    plt.xlabel('Results')
    plt.ylabel('Frequency')
    plt.show()


