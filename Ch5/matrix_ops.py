# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:07:14 2017

@author: Nathan.Brunner
"""

''' define vector math for 1xN 'matrices'''

# the book is awful at telling us what we need to import
from functools import partial, reduce
import math

def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v,w)]
    
def vector_subtract(v, w):
    return [v_i - w_i
            for v_i, w_i in zip(v,w)]
 
def vector_sum(vectors):
    return reduce(vector_add, vectors)

#vector_sum = partial(reduce, vector_add)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n=len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v,w):
    return sum(v_i*w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v, w))

#def distance(v,w):
#    return math.sqrt(squared_distance(v,w))

def distance(v,w):
    return magnitude(vector_subtract(v,w))

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
            for A_i in A]
    
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j)
            for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal(i,j):
    return 1 if i==j else 0

        