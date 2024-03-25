"""
Title     : String Split and Join
Subdomain : Strings
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 08 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
"""


def split_and_join(sentence):
    return "-".join(sentence.split())


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
