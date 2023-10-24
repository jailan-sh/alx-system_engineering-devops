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

    name = resp1.json()
    data = resp2.json()

    with open("{}.csv".format(sys.argv[1]), mode="w") as file:
        csv_write = csv.writer(file, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)

        for item in data:
            csv_write.writerow([item["userId"], name["username"],
                                item['completed'], item['title']])
