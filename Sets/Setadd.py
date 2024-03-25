"""
Title     : Set .add()
Subdomain : Sets
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 19 januaryuaryruary 2024
problem   : https://www.hackerrank.com/challenges/py-set-add/problem
"""

n = int(input())
country_set = set()
for _ in range(n):
    country_name = input()
    country_set.add(country_name)
print(len(country_set))
