#!/usr/bin/python3
"""this is a module for 1-top_ten.py"""

import requests


def top_ten(subreddit):
    """
    returns the top 10 hot posts
    of the subreddit
    """
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 10}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    if 'data' not in data:
        print(None)
        return

    posts = data['data']['children']

    if not posts:
        print(None)
        return

    for post in posts:
        print(post['data']['title'])
