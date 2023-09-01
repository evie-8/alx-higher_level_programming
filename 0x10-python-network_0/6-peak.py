#!/usr/bin/python3
"""Find peak of unsorted list of integers"""


def find_peak(list_of_integers):
    """Finding peak of unsorted list of integers"""
    if not list_of_integers:
        return None
    lists = list_of_integers
    list_len = len(lists)

    if list_len == 1:
        return lists[0]

    if list_len == 2:
        if lists[0] >= lists[1]:
            return lists[0]
        else:
            return lists[1]

    for i in range(0, list_len):
        peak = lists[i]
        if (i > 0 and i < list_len - 1 and
                lists[i + 1] <= peak and lists[i - 1] <= peak):
            return peak
        elif i == 0 and lists[i + 1] <= peak:
            return peak
        elif i == list_len - 1 and lists[i - 1] <= peak:
            return peak
    return None
