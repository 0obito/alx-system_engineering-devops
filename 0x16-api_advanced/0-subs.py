#!/usr/bin/python3
"""
this is a 0-subs.py module
"""
import requests


if __name__ == "__main__":
    def number_of_subscribers(subreddit):
        """
        returns the total number of subscribers in a given subreddit
        """
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'API Practice'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0
        else:
            data = response.json()
            return data['data']['subscribers']