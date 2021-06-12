from bernoulli import Bernoulli
from binomial import Binomial
from geometric import Geometric
from poisson import Poisson
from exponential import Exponential
from normal import Normal
from blum_blum_shub_generator import Bbs
from marsenne_twister import Marsenne
from multiplicative_generator import Multiplicative
import matplotlib.pyplot as plt
import math
import scipy.stats as stats


if __name__ == '__main__':

    seed = 1619
    how_many_numbers = 100000
    random_numbers = []

    # bbs = Bbs(x0=seed, q=30000000091, p=40000000003, quantity=how_many_numbers)
    # bbs.generate_random_numbers(random_numbers, 10000)
    # bbs.print_frequency(1000)
    # bbs.runs_test()
    # bbs.chi_square(random_numbers)

    # mar = Marsenne(seed)
    # mar.random_numbers(random_numbers, how_many_numbers, 1000)
    # mar.chi_square(random_numbers)
    # mar.print_frequency(100)
    # mar.runs_test(random_numbers)
    #
    multi = Multiplicative(seed, how_many_numbers)
    multi.generate_random_numbers(random_numbers, 1000)
    multi.print_frequency(1000)
    multi.chi_square(random_numbers)
    multi.runs_test()


    # Rozkład Bernoulliego
    p = 0.6
    ber = Bernoulli(p=p, quantity=how_many_numbers, random_numbers=random_numbers)
    ber.print()
    ber.chi_square()
    #
    # Rozkład dwumianowy
    p = 0.11
    bino = Binomial(p=p, size=10, random_numbers=random_numbers)
    bino.print()
    bino.chi_square()


    # Rozkład geometryczny
    p = 0.3
    n = 10000
    geo = Geometric(p=p, n=n, quantity=how_many_numbers, random_numbers=random_numbers)
    geo.print()
    geo.chi_square()

    # Rozkład Poissona
    lamb = 10
    n = 1000
    poi = Poisson(lamb=lamb, n=n, quantity=how_many_numbers, random_numbers=random_numbers)
    poi.print()
    poi.chi_square()
    #

    # Rozkład wykładniczy
    lamb = 1.5
    n = 1000
    expo = Exponential(lamb=lamb, n=n, accuracy=0.3, quantity=how_many_numbers, random_numbers=random_numbers)
    expo.print()
    expo.chi_square()

    # Rozkład Normalny
    norm = Normal(quantity=how_many_numbers, random_numbers=random_numbers, accuracy=0.1)
    norm.print()
    norm.chi_square()

