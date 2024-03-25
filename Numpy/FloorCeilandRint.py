"""
Title     : Floor, Ceil and Rint
Subdomain : Numpy
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 17 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
"""
import numpy as np

np.set_printoptions(legacy="1.13")
A = np.array(input().split(), float)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))

# Alternate solution
# print(*(f(A) for f in [np.floor, np.ceil, np.rint]), sep='\n')
