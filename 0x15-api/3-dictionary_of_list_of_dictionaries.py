#!/usr/bin/python3
"""
script to for returning information about TODO list progress
a given id
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    url1 = "https://jsonplaceholder.typicode.com/users"

    resp1 = requests.get(url1)

    names = resp1.json()
    items = {}
    all = []
    for user in names:
        url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            names["id"])

        resp2 = requests.get(url2)
        data = repo2.json()
        for task in data:
            items = {"username": names["username"], "task": task["title"],
                     "completed": task["completed"]}
        all .append(items)
        inf = {names["id"]: all}

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(inf, file)
