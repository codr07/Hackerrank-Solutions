"""
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 08 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
"""
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
