# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 19:26:26 2017

@author: nbrunner
"""

def apply_to_one(f):
    return f(1)
    
y = apply_to_one(lambda x: x + 4)

# Default Dics - useful for creating a dict that will create
# a default entry if the entry doesn't exist already

from collections import defaultdict

dd_dict = defaultdict(dict) #the dict creates an empty dict
dd_dict["Joel"]["City"] = "Seattle"  # {"Joel": {"city":"Seattle"}}


# Counter creates a dict that counts the instances of entries
from collections import Counter
c = Counter([0,1,2,0])
print(c)

# a set will only contain unique values
s = set()
s.add(1)
s.add(2)    # (1,2)
s.add(2)    #still (1,2)
''' in is a very fast operation on sets'''
print(2 in s)

def double(x):
    return 2 * x

#map
xs = [1,2,3,4]
'''LIST COMPREHENSION'''
twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)

#filter
def is_even(x):
    return x % 2 == 0
    
x_evens = [x for x in xs if is_even(x)]
x_evens = filter(is_even, xs)
#using partial
from functools import partial
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)

#zip unzip
list1 = ["a",'b','c']
list2 = [1,2,3]
zipped = zip(list1, list2)
unz1, unz2 = zip(*zipped)

# args
def magic(*args, **kwargs):
    print ("unnamed args:",args)
    print("keyword args:",kwargs)
