#!/usr/bin/python3
"""
this is a module that
returns the total number
of subscribers in a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'API Practice'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        return data['data']['subscribers']
