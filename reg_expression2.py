"""
    reg_expression2.py -- Extracts all mentions of stock symbols and price
                          changes from a news article.

    Author: Lindsay Hopewell (lmh539@nyu.edu)
    Last Revised: 8/12/2023
"""
import re

f = open('../market_discussion.txt')
f_lines = f.read()

stocks = re.findall(r'[A-Z]+\,\s[+-]\d+\.\d+', f_lines)

for stock in sorted(stocks):
    print(stock)
