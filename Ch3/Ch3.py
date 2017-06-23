# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:48:48 2017

@author: nbrunner
"""

from matplotlib import pyplot as plt

years	=	[1950,	1960,	1970,	1980,	1990,	2000,	2010]
gdp	=	[300.2,	543.3,	1075.9,	2862.5,	5979.6,	10289.7,	14958.3]

plt.plot(years, gdp, color="green", marker='o',linestyle='solid')

movies	=	["Annie	Hall",	"Ben-Hur",	"Casablanca",	"Gandhi",	"West	Side	Story"]
num_oscars	=	[5,	11,	3,	8,	10]

xs = [i+0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
