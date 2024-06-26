"""
Title     : Exceptions
Subdomain : Errors and Exceptions
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/exceptions/problem
"""

n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as e:
        print(f"Error Code: {e}")
