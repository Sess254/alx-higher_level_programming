#!/usr/bin/python3
"""Defines a read file function"""


def read_file(filename=""):
    """Reads a text file and prints it stdout"""
    with open(filename, "r", encoding="utf") as file:
        for line in file:
            print(line, end="")
