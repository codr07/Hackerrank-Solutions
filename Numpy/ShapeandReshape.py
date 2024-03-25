"""
Title     : Shape and Reshape
Subdomain : Numpy
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""
import numpy

ar = list(map(int, input().split()))
np_ar = numpy.array(ar)
print(numpy.reshape(np_ar, (3, 3)))
