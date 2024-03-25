"""
Title     : Compress the String!
Subdomain : Itertools
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/compress-the-string/problem
"""

import itertools

s = input().strip()
s_unique_element = list(set(s))
group = []
key = []
for k, g in itertools.groupby(s):
    group.append(list(g))
    key.append(k)
for i in range(len(group)):
    group_length = len(group[i])
    k = int(key[i])
    print((group_length, k), end=" ")
