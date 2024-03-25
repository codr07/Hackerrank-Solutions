"""
Title     : Eye and Identity
Subdomain : Numpy
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 17 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
"""
import numpy as np

np.set_printoptions(legacy="1.13")
n, m = map(int, input().split())
print(np.eye(n, m, k=0))
