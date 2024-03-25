"""
Title     : Mutations
Subdomain : Strings
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 08 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/python-mutations/problem
"""


def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
