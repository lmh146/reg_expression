"""
    reg_expression1.py -- Builds a dictionary from a web server log that sums
                          up web server usage by user id.

    Author: Lindsay Hopewell (lmh539@nyu.edu)
    Last Revised: 8/12/2023
"""
import re

f = open('../access_log.txt')
f_lines = f.readlines()

bytes_dict = {}

for line in f_lines:
    pattern1 = re.search(r'/~([a-z]{2,3}\d{2,3})', line)
    pattern2 = re.search(r'\d{1,3}\s(\d+)', line)

    if not pattern1 or not pattern2:
        continue

    nyu_id = pattern1.group(1)
    byte = pattern2.group(1)

    if nyu_id not in bytes_dict:
        bytes_dict[nyu_id] = 0
    bytes_dict[nyu_id] = bytes_dict[nyu_id] + int(byte)

for id in sorted(bytes_dict, key=bytes_dict.get, reverse=True):
    if bytes_dict[id] > 1000000:
        print(f'{id}:  {bytes_dict[id]}')
