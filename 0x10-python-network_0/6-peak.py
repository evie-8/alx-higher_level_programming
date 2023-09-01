#!/usr/bin/python3
"""Find peak of unsorted list of integers"""


def find_peak(list_of_integers):
    """Finding peak of unsorted list of integers"""
    if not list_of_integers:
        return None
    lists = list_of_integers
    for i in range(len(lists)):
        if ((i == 0 or lists[i] >= lists[i - 1])
        and (i == len(lists) - 1 or lists[i] >= lists[i + 1])):
            return lists[i]
    return None
