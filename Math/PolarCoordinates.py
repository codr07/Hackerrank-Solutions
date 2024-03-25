"""
Title     : Polar Coordinates
Subdomain : Math
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/polar-coordinates/problem
"""
import cmath

z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])
