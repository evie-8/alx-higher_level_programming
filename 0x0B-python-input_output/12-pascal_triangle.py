#!/usr/bin/python3
""" module for pascal triangle"""


def pascal_triangle(n):
    """creating a list of list of integers"""
    if n <= 0:
        return []
    result = [[] for row in range(n)]
    for i in range(n):
        for j in range(1 + i):
            if (j < i):
                if (j == 0):
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j] + result[i - 1][j - 1])
            elif (j == i):
                result[i].append(1)
    return result
