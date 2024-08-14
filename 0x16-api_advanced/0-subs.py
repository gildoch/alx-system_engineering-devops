#!/usr/bin/python3
"""Method to query the number of subscriber"""

import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscriber on the subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/0.1 (by u/GildoChauze; \
               learning purposes)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.RequestException:
        return 0
