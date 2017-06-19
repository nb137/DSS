# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:49:10 2017

@author: nathan.brunner
"""

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]

#insert a plot where you split the data here

from collections import defaultdict

salary_by_tenure = defaultdict(list)

# key is years, value is avg salary for that tenure
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
    
average_salary_by_tenure = {
        tenure : sum(salaries)/len(salaries)
        for tenure, salaries in salary_by_tenure.items()
        }

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than 2"
    elif tenure < 5:
        return "2-5"
    else:
        return "more than five"
    
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
#average_salary_by_bucket = {
#        tenure_bucket : sum(salaries)/len(salaries)
#        for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
#        }

from collections import Counter

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print((word, count))