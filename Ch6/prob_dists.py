# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:23:52 2017

@author: Nathan.Brunner
"""
import math
import random


def uniform_pdf(x):
    return 1 if x>=0 and x<1 else 0

def uniform_cdf(x):
    if x<0: return 0
    elif x < 1: return x
    else: return 1
    
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) **2 /2/sigma**2)/ (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0, sigma=1):
    return (1+ math.erf((x-mu) / math.sqrt(2) / sigma))/2

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

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))