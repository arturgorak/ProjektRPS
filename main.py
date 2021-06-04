from bernoulli import Bernoulli
from geometric import Geometric
from poisson import Poisson
from exponential import Exponential
from normal import Normal
from blum_blum_shub_generator import Bbs
from marsenne_twister import  Marsenne
import matplotlib.pyplot as plt
import math
import scipy.stats as stats


if __name__ == '__main__':
    seed = 3090176421
    how_many_numbers = 100000
    random_numbers = []
    bbs = Bbs(x0=seed, q=30000000091, p=40000000003, quantity=how_many_numbers)
    bbs.generate_random_numbers(random_numbers, 10000)
    # bbs.print_frequency(1000)
    # bbs.runs_test()


    # mar = Marsenne(seed)
    # mar.random_numbers(random_numbers, how_many_numbers, 1000)


    # Rozkład Bernouliego
    # p = 0.6
    # ber = Bernoulli(p=p, quantity=how_many_numbers, random_numbers=random_numbers)
    # ber.print()
    # ber.chi_square()

    # Rozkład geometryczny

    # p = 0.3
    # n = 10000
    # geo = Geometric(p=p, n=n, quantity=how_many_numbers, random_numbers=random_numbers)
    # geo.print()
    # geo.chi_square()

    # Rozkład Poissona
    # lamb = 4
    # p = 0.3
    # n = 10000
    # poi = Poisson(lamb=lamb, p=p, n=n, quantity=how_many_numbers, random_numbers=random_numbers)
    # poi.print()
    # poi.chi_square()
    #
    #
    # Rozkład wykładniczy
    # lamb = 1
    # n = 1000
    # expo = Exponential(lamb=lamb, n=n, accuracy=0.5, quantity=how_many_numbers, random_numbers=random_numbers)
    # expo.print()
    # expo.chi_square()

    # Rozkład Normalny
    # norm = Normal(quantity=how_many_numbers, random_numbers=random_numbers, accuracy=0.1)
    # norm.print()
    # norm.chi_square()

