"""
Title     : String Formatting
Subdomain : Strings
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 08 januaryuaryruary 2024
Problem   : https://www.hackerrank.com/challenges/python-string-formatting/problem
"""


def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        o = oct(i)[2:]
        h = hex(i)[2:]
        h = h.upper()
        b = bin(i)[2:]
        d = str(i)
        print(f"{d:>{width}} {o:>{width}} {h:>{width}} {b:>{width}}")


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
