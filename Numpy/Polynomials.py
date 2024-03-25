"""
Title     : Polynomials
Subdomain : Numpy
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/np-polynomials/problem
"""
import numpy

p = numpy.array(list(map(float, input().split())), float)
x = float(input())
print(numpy.polyval(p, x))
