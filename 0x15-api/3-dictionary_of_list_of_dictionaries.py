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
    url2 = "https://jsonplaceholder.typicode.com/todos"

    resp1 = requests.get(url1)
    resp2 = requests.get(url2)

    name = resp1.json()
    data = resp2.json()

    tasks = []
    item = {}

    for element in data:
        item = {"task": element["title"], "completed": element["completed"],
                "username": name["username"]}
        tasks.append(item)

    inf = {name["id"]: tasks}
    with open("todo_all_employees.json", mode="w") as file:
        json.dump(inf, file)
