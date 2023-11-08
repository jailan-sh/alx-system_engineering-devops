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

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']['subscribers']
    else:
        return 0
