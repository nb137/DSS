# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:36:59 2017

@author: Nathan.Brunner
"""

#start piling up libraries that are used in chapters
import matplotlib.pyplot as plt
from collections import Counter
from numpy import random, mean, median
import statistics
import math
import random
from prob_dists import * # we wrote this to contian probability distributions


normal_probability_below = normal_cdf

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
normal_two_sided_bounds(0.95, mu_0, sigma_0)

lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability

hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1-type_2_probability

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * normal_probability_above(x,mu,sigma)
    else:
        return 2 * normal_probability_below(x,mu,sigma)
'''
# computationally heavy loop
extreme_value_count = 0
for _ in range(10000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000))
    if num_heads >=530 or num_heads <=470:
        extreme_value_count+=1

print(extreme_value_count/10000)
'''

p_hat = 525/1000
mu=p_hat
sigma = math.sqrt(p_hat * (1-p_hat)/1000)

def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p*(1-p)/N)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    ''' 
    AB Test Stat returns a z-test of A and B
    Returns the Z value, which can be used in a Z distribution
    to find P, the probability of them being the same
    As he says, a T test should be used unless sigma is known
    '''
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B**2)

def B(alpha, beta):
    return math.gamma(alpha) * math.gamma(beta)/math.gamma(alpha+beta)

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:
        return 0
    return x** (alpha-1)*(1-x)**(beta-1) / B(alpha, beta)

# I should look more into Bayesian inference since I don't quite understand it here
