"""
Title     : Tuples
Subdomain : Data Types
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 06 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/python-tuples/problem
"""
if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
