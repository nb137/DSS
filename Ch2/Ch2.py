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