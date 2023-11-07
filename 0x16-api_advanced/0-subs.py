#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
"""

import requests
import json


def number_of_subscribers(subreddit):
    """function to get subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'jailan'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
