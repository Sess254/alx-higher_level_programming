#!/usr/bin/python3
""" Write a Python script that takes in a URL,
    sends a request to the URL and displays the body of
    the response (decoded in utf-8)
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    if (sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as reaponse:
        body = response.read().decode('utf-8')

    print(body)
