# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:36:51 2017

@author: nbrunner
"""

import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

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
from functools import partial
derivative_estimate = partial(difference_quotient, square, h=0.00001)

x = range(-10,10)
plt.plot(x, map(derivative,x),'rx', label='Actual')     #WHY IS THIS SAYING X AND Y ARE NOT THE SAME DIMENSION?
plt.plot(x,map(derivative_estimate,x), 'b+', label='Estimate')
plt.legend(loc=9)
plt.show()
