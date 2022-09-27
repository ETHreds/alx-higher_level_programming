#!/usr/bin/python3
"""
    Append to file
"""


def append_write(filename="", text=""):
    """Appends to text file and returns number odf chars added"""
    with open(filename, mode='a', encoding='UTF8') as file:
        for char in text:
            file.write(char)
    return len(text)
