#!/usr/bin/python3
# Sess254

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else 'None'
    result = length, first_char
    return (result)
