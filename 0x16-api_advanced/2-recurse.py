#!/usr/bin/python3
"""
This method returns a list of titles of all hot arcticles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return hot list of articles using recursive aproach"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "MyRedditBot/0.1 (by u/GildoChauze;\
                learning purposes)"
    }

    params = {
        "limit": 100,
        "after": after,
    }

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]

            for post in posts:
                hot_list.append(post["data"]["title"])

            after = data["data"]["after"]

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
