"""
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 16 januaryuary 2016
Updated   : 08 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
"""


def swap_case(sentence):
    updated_s = ""
    for c in sentence:
        if c.isupper():
            updated_s += c.lower()
        elif c.islower():
            updated_s += c.upper()
        else:
            updated_s += c
    return updated_s


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
