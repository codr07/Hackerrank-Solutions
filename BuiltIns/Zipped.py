"""
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Author    : Sankha Saha (CODR)
Updater   : Imtiaz Ahmed
Created   : 15 januaryuary 2016
Updated   : 30 januaryust 2024
Problem   : https://www.hackerrank.com/challenges/zipped/problem
"""

N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))
