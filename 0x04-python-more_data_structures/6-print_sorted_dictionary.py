#!/usr/bin/python3
# Sess254

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        print(i + ':', a_dictionary[i])
