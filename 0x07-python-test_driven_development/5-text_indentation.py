#!/usr/bin/python3
"""indentation of text.
"""


def text_indentation(text):
    """checking for identation.
    Args:
        text (str): text
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punct = ['.', '?', ':']
    i = 0
    r = ""
    while i < len(text):
        r += text[i]
        for j in punct:
            if text[i] == j:
                if r[0] == ' ':
                    r = r[1:]
                print(r, end="\n\n")
                r = ""
        i += 1
    if r[0] == ' ':
        r = r[1:]
    print(r, end="")
