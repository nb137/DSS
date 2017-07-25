# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 13:54:22 2017

@author: nbrunner
"""

'''
Check book repo for egrep.py which can grab stuff from cmd line
'''

# Using open, which I haven't done since LCO
file_to_write = open('TestFile.txt','w')
file_to_write.write("HELLO")
file_to_write.close()


import csv
data=[]
with open('tab_delimited_stock_prices.txt','rt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        data.append([date, symbol, closing_price])
        
data=[]
with open('colon_delimited_stock_prices.txt', 'rt') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        data.append([date, symbol, closing_price])

from bs4 import BeautifulSoup
import requests
site = "https://www.safaribooksonline.com/search/?query=data"
html = requests.get(site).text
soup = BeautifulSoup(html, 'lxml')

'''
None of this really works, the website is laid out completely
different than the book
'''

import	json
serialized	=	"""{	"title":"Data Science Book",
                 "author":"Joel Grus",
                 "publicationYear":2014,
                 "topics":["data","science","data science"]}"""
deserialized = json.loads(serialized)

import requests
endpoint = "https://api.github.com/users/nb137/repos"
repos = json.loads(requests.get(endpoint).text)
repoNames = [repo["name"] for repo in repos]

'''
Look at pandas and scrapy (web scraping)
'''