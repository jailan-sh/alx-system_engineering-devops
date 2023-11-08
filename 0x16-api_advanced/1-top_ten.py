#!/usr/bin/python3
"""
Querries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit
"""

import requests
import json


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'jailan'}
    params = {"limit": 10, }
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None")
    else:
        print("None")
