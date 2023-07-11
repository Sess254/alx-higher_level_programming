#!/usr/bin/python3
"""Defines an append to file function"""


def append_write(filename="", text=""):
    """Appends a string at end of text file and returns no of chars added"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
