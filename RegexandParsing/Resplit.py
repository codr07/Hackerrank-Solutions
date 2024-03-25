"""
Title     : Re.split()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 3 januaryuaryruary 2024
Problem   : https://www.hackerrank.com/challenges/re-split/problem
"""

import re

regex_pattern = r"[.,]+"

print("\n".join(re.split(regex_pattern, input())))
