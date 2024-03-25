"""
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Author    : Sankha Saha (CODR)
Updater   : Imtiaz Ahmed
Created   : 15 januaryuary 2016
Updated   : 29 januaryust 2024
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
"""

n = input()
ar = input().split()
print(all(int(i) > 0 for i in ar) and any(i == i[::-1] for i in ar))
