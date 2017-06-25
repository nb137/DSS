# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:48:48 2017

@author: nbrunner
"""

from matplotlib import pyplot as plt
from collections import Counter

years	=	[1950,	1960,	1970,	1980,	1990,	2000,	2010]
gdp	=	[300.2,	543.3,	1075.9,	2862.5,	5979.6,	10289.7,	14958.3]

#plt.plot(years, gdp, color="green", marker='o',linestyle='solid')

movies	=	["Annie Hall",	"Ben-Hur",	"Casablanca",	"Gandhi",	"West	Side	Story"]
num_oscars	=	[5,	11,	3,	8,	10]

'''
xs = [i+0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.xticks([i+0.5 for i, _ in enumerate(movies)], movies)
plt.show()
'''

grades	=	[83,95,91,87,70,0,85,82,100,67,73,77,0]
'''
create bins of ten for grades
'''
decile = lambda grade: grade//10*10
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x-4 for x in histogram.keys()],    # shift bars left by 4 for alignment
         histogram.values(),                # hist values are bar heights
        8)          # width 8 for our bins of 10 leaves 1 between each side
plt.axis([-5,105,0,5])  #x, y. -5 and 105 to fit width of bars
plt.xticks([10*i for i in range(11)])
# can also do
#plt.xticks(list(range(0,110,10))
plt.clf()
'''Line Charts'''
variance = [1,	2,	4,	8,	16,	32,	64,	128,	256]
bias_squared = [256,	128,	64,	32,	16,	8,	4,	2,	1]
total_error = [x+y for x,y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')

plt.clf()

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                xy=(friend_count,minute_count),
                xytext=(5,-5),
                textcoords='offset points')