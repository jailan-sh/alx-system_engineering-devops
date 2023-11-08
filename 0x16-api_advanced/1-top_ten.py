#!/usr/bin/python3
"""
Querries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit
"""

import requests
import json

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    headers = {"User-Agent": "jailan"}  # Changed user-agent header
    params = {"limit": 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return
    data = response.json().get('data', {}).get('children', [])

    if not data:
        print("No posts found.")
        return
    for item in data:
        print(item.get('data', {}).get('title'))
