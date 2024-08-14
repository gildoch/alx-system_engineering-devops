#!/usr/bin/python3
"""Fetch the top 10 hot posts from reddit"""

import requests


def top_ten(subreddit):
    """Method that retrieves the hot 10 post for a givem subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "MyRedditBot/0.1 (by u/GildoChauze;\
              learning purposes)"
    }

    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]

            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
