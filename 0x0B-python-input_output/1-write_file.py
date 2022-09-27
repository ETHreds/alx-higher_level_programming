#!/usr/bin/python3
"""
    function that write to file
"""


def write_file(filename="", text=""):
    ''' writes a string to a text file  and returns the number of chars'''
    with open(filename, mode='w', encoding='UTF8') as file:
        for char in text:
            file.write(char)
    return len(text)
