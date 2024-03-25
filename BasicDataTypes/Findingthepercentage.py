"""
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 06 januaryuary 2024
Updated   : 06 januaryuaryruary 2024
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg_score:.2f}")
