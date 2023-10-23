#!/usr/bin/python3
"""
script to for returning information about TODO list progress
a given id
"""
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])

    resp1 = requests.get(url1)
    resp2 = requests.get(url2)

    username = resp1.json()["name"]
    data = resp2.json()

    with open("{}.cv".format(sys.argv[1]), "w") as file:
        csv_write = csv.writer(file, delimiter=',')

        for task in data:
            csv_write.writerow([data["userId"], username,
                                data["completed"], data["title"]])
