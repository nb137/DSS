# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:36:51 2017

@author: nbrunner
"""

import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from functools import partial
import random
from linear_algebra import distance


def sum_of_squares(v):
    return sum(v_i**2 for v_i in v )
    
def difference_quotient(f,x,h):
    return (f(x+h) - f(x))/h
    
def square(x):
    return x**2

def derivative(x):
    return 2*x
    
'''Numpy has a derivative form that would look like this:
import sympy
x = sympy.Symbol('x')
y = x**2 +1
yprime = y.diff(x)
#yprime==2*x
f = sympy.lambdify(x,yprime,'numpy')
#f(2)==4
'''
derivative_estimate = partial(difference_quotient, square, h=0.00001)

x = range(-10,10)
# plt.plot(x, map(derivative,x),'rx', label='Actual')
# for some reason Python won't unpack the Map object (sees length 1)
plt.plot(x, [i for i in map(derivative,x)],'rx', label='Actual')
plt.plot(x,[i for i in map(derivative_estimate,x)], 'b+', label='Estimate')
plt.legend(loc=9)
plt.show()

def parital_difference_quotient(f, v, i, h):
    '''compute ith partial difference quotient of f at v'''
    w = [v_j + (h if j ==i else 0)
        for j, v_j in enumerate(v)]
    return (f(w) - f(v) / h)
    
def estimate_gradient(f, v, h=0.00001):
    return [parital_difference_quotient(f, v, i, h)
        for i, _ in enumerate(v)]
            
def step(v, direction, step_size):
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]
    
def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]
    
v = [random.randint(-10,10) for i in range(3)]  # rand starting point

tolerance = 0.00001
'''
while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v
'''
    
def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf') # return inf if funct errors
    return safe_f
    
step_sizes	=	[100,	10,	1,	0.1,	0.01,	0.001,	0.0001,	0.00001]

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    global sstep_sizes
    theta = theta_0
    target_fn = safe(target_fn)    
    value = target_fn(theta)
    
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta,gradient, -step_size for step_size in step_sizes)]
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

def negate(f):
    return lambda *args, **kwargs: -f(*args,**kwargs)
    
def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn), negate_all(gradient_fn),
                          theta_0, tolerance)

#I bet scikitlearn has something for all this
# stochastic gradient descent = pick one point at a time randomly and predict

