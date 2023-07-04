#!/usr/bin/python3

"""Prints square with the char #."""


def print_square(size):
    """Prints a square with # char.

    Args:
       int for size

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
