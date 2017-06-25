# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:23:25 2017

@author: Nathan.Brunner
"""

import matplotlib.pyplot as plt
from collections import Counter
from numpy import random, mean, median
import statistics
import numpy
from matrix_ops import dot

'''Grab data sets num_friends and daily_minutes from DSfS github'''

num_friends = [100,49,41,40,25] #"and lots more"
# this doesnt do anything interesting, so lets make a random list
# of length 204 since that is referenced
num_friends = [int(random.random_sample()*100) for _ in range(204)]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys) # this looks really stupid without num_friends data
num_points = len(num_friends)
largest_value = max(num_friends)

print(mean(num_friends))
print(median(num_friends))

def quantile(x, p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

'''HEY LOOK HOW EASY THIS IS'''
q=statistics.mode(num_friends)
r=statistics.mean(num_friends)
s=statistics.median(num_friends)

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

# def variance
x=statistics.variance(num_friends)
y=numpy.var(num_friends)

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x), de_mean(y))/(n-1)

def correlation(x,y):
    stdev_x = statistics.stdev(x)
    stdev_y = statistics.stdev(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x,y) / stdev_x / stdev_y
    else:
        return 0

#correlation(num_friends, daily_minutes)