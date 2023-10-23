#!/usr/bin/python3
""" 
script to for returning information about TODO list progress
of a given employee ID
"""

import json
import requests
import sys


if __name__ = "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])

    resp1 = requests.get(url1)
    resp2 = requests.get(url2)

    name = resp1.json()["name"]
    data = resp2.json()
    total = len(data)
    done = 0
    title = []

    for item in data:
        if item["completed"]:
            done += 1
            title.append(item["title"])

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for item in title:
        print("\t{}".format(item))
