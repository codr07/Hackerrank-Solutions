"""
Title     : Input()
Subdomain : Built-Ins
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 3 januaryuaryruary 2024
Problem   : https://www.hackerrank.com/challenges/input/problem
"""

if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    equation = input().strip()
    print(eval(equation) == k)
