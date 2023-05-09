#!/usr/bin/python3
def uppercase(str):
    sentence = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            j = ord(i) - 32
            sentence += chr(j)
        else:
            sentence += i
    print("{}".format(sentence), end="\n")
