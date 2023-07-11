#!/usr/bin/python3
"""Defines a insert a line to text to file function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts, serches an updates"""
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
