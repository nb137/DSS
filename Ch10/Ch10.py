# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:47:28 2017

@author: nbrunner
"""
import math
from collections import Counter
import matplotlib.pyplot as plt
import random
from prob_dists import inverse_normal_cdf
import numpy as np

def bucketize(point, bucket_size):
    return bucket_size * math.floor(point/bucket_size)

def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)
    
def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()
    
random.seed(0)
uniform = [200 * random.random() - 100 for _ in range(10000)]

normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]
# you can do this within the random library, too

def random_normal():
    return inverse_normal_cdf(random.random())
    
xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() /2 for x in xs]
ys2 = [-x + random_normal() /2 for x in xs]

plt.scatter(xs,ys1, marker='.',color="black",label="ys1")
plt.scatter(xs,ys2, marker='.',color="gray",label="ys2")

np.correlate(xs,ys1)
np.correlate(xs,ys2)

'''
Now we're going to do a multivariate scatter plot matrix from scratch
but you can really just look into
pandas.plotting.scatter_matrix
'''
from scipy.stats import correlation, standard_deviation, mean
from linear_algebra import shape, get_row, get_column, make_matrix, \
    vector_mean, vector_sum, dot, magnitude, vector_subtract, scalar_multiply

def correlation_matrix(data):
    _,num_columns = shape(data)
    def matrix_entry(i,j):
        return correlation(get_column(data,i), get_column(data,j))
    return make_matrix(num_columns, num_columns, matrix_entry)

# Just skipping the plot here because pandas does it all
import pandas as pd
from pandas.tools.plotting import scatter_matrix
tit = pd.read_csv("C://Users/nathan.brunner/Desktop/titanic.csv")
tit["Sex"] = [int(i) for i in tit["Sex"]=="male"]
scatter_matrix(tit[["Survived","Pclass","Sex","Age","SibSp","Fare"]])
# look, we did it

