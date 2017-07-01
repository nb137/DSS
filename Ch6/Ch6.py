# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 21:32:51 2017

@author: Nathan.Brunner
"""
import math
import matplotlib.pyplot as plt
from prob_dists import *    #I just started throwing them all in there
from collections import Counter
# Bayes Notes

P_D = 1/10000. # Prob of disease
P_T = 0.99  # Prob of test being accurate

# If you test positive we want P(D|T) or the prob that you have the disease given that you tested positive

# P(D|T) = P(T|D)*P(D) / [P(T|D)*P(D) + P(T|nD)*(P(nD)])

P_T_nD = 1 - P_T
P_T_D = P_T
P_nD = 1 - P_D

P_D_T = (P_T_D*P_D)/(P_T_D*P_D + P_T_nD*P_nD)

print("Prob of neg test if you are neg: %03f" % P_T)
print("Prob of pos test if you are neg: %03f" % P_D_T)

population = 1e6
# here we could calculate expected number of people with disease, number without, and who falsly tests positive
false_pos = population * P_D_T
true_pos = population * P_D
print("Number of people with false positives: %d" % false_pos)
print("Number of people with disease: %d" % true_pos)
print("Ratio of true pos/false pos: %03f" % (true_pos/false_pos))

def uniform_pdf(x):
    return 1 if x>=0 and x<1 else 0

def uniform_cdf(x):
    if x<0: return 0
    elif x < 1: return x
    else: return 1
    
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) **2 /2/sigma**2)/ (sqrt_two_pi * sigma))

xs = [x/10 for x in range(-50,50)]
'''
plt.plot(xs, [normal_pdf(x) for x in xs],'-',label="s=1")
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs],'-',label="s=2")
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs],'-',label="s=0.5")
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs],'-',label="s=1 mu=-1")
'''

def normal_cdf(x, mu=0, sigma=1):
    return (1+ math.erf((x-mu) / math.sqrt(2) / sigma))/2
'''
plt.plot(xs, [normal_cdf(x) for x in xs],'-',label="s=1")
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs],'-',label="s=2")
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs],'-',label="s=0.5")
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs],'-',label="s=1 mu=-1")
'''
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    '''find approx inverse using binary search'''
    if mu != 0 or sigma !=1:
        return mu + sigma * inverse_normal_cdf(p)
    low_z, low_p = -10, 0
    hi_z, hi_p = 10, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z+hi_z)/2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            #midpoint low, search above
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            #midpoint high, search above
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

def make_hist(p,n, num_points):
    data = [binomial(n,p) for _ in range(num_points)]
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
             [v / num_points for v in histogram.values()],
              0.8,
              color='0.75')
    mu = p*n
    sigma = math.sqrt(n*p*(1-p))
    xs = range(min(data),max(data)+1)
    ys = [normal_cdf(i+0.5, mu,sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs,ys)
    plt.show()
    
    