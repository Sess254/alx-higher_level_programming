#!/usr/bin/python3
"""Defines a write to file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
