#!/usr/bin/python3
# Sess254

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = max(a_dictionary.values())
    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
