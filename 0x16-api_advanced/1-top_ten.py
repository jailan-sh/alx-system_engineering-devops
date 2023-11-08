#!/usr/bin/python3
"""
Querries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit
"""

import requests
import json


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    headers = {"user-agent": "jailan"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    data = json.loads(response.text).get('data').get('children')
    if not data:
        print("None")
        return
    for item in data[0:10]:
        print(item.get('data').get('title'))
