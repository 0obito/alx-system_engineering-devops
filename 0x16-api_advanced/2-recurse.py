#!/usr/bin/python3
""" this is the module for 2-recurse.py """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles
    of all hot articles for a given subreddit
    """
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'after': after} if after else {}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if 'data' not in data:
        return None

    posts = data['data']['children']

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
