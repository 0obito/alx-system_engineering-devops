#!/usr/bin/python3
"""
this is a 0-subs.py module
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers in a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'RedditSubscriberCountBot/0.1 by YourUsername'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data['data']['subscribers']
    except (KeyError, ValueError):
        return 0
