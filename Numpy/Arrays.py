"""
Title     : Arrays
Subdomain : Numpy
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/np-arrays/problem
"""
import numpy

ar = list(map(float, input().split()))
np_ar = numpy.array(ar, float)
print(np_ar[::-1])
