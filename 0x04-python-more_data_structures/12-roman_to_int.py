#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for j in range(len(roman_string)):
        if ans > 0 and val[roman_string[j]] > val[roman_string[j - 1]]:
            ans += val[roman_string[j]] - 2 * val[roman_string[j - 1]]
        else:
            ans += val[roman_string[j]]
    return ans
