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

    user = resp1.json()
    todo = resp2.json()

    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for item in todo:
            writer.writerow([user['id'], user['username'], item['completed'],
                             item['title']])
