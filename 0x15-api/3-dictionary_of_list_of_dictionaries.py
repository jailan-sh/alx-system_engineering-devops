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
    inf = {}
    for user in names:
        all = []
        items = {}
        url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user["id"])

        resp2 = requests.get(url2)
        data = resp2.json()
        for task in data:
            if task["userId"] == user["id"]:
                items = {"username": user["username"], "task": task["title"],
                         "completed": task["completed"]}
                all .append(items)
        inf[user["id"]] = all

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(inf, file)
