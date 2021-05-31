import matplotlib.pyplot as plt
MT = []
bbs = []
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


def blum_blum_shub(x0, q, p, n):
    global bbs
    m = q*p
    bbs.insert(0, x0)
    for i in range(1, n):
        bbs.insert(i, (bbs[i - 1] * bbs[i - 1]) % m)


if __name__ == '__main__':
    seed = 15

    initialize_generator(seed=seed)

    results = []
    for x in range(seed):
        results.insert(x, 0)

    count = []
    for x in range(0, seed):
        count.insert(x, x)

    # for x in MT:
    #     results[x % seed] += 1

    for x in range(10000):
        results[extract_numbers() % seed] += 1

    maximum = 0
    for x in results:
        if x > maximum:
            maximum = x

    plt.title('Ilość występowania danych MT')
    plt.xlabel('Liczba')
    plt.ylabel('Ilość')
    plt.plot(count, results)
    plt.axis([0, seed, 0, maximum + maximum/10])
    plt.grid(True)
    plt.show()

    blum_blum_shub(1234, 30000000091, 40000000003, 10000)

    results2 = []
    for x in range(seed):
        results2.insert(x, 0)

    for x in bbs:
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
