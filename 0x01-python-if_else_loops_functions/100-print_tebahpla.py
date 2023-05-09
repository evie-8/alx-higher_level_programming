#!/usr/bin/python3
result = ""
for i in range(122, 64, -1):
    if (122 - i) % 2 == 0:
        result += chr(i)
    else:
        result += chr(i - 32)
print("{}".format(result[:-32]), end="")
