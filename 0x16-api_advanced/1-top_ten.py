#!/usr/bin/python3
"""Fetch the top 10 hot posts from reddit"""


def top_ten(subreddit):
    """Method that retrieves the hot 10 post for a givem subreddit"""
    import requests

    subs = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
    )

    posts = subs.json().get("data").get("children")

    if subs.status_code >= 300:
        return "None"
    else:
        for post in posts:
            print(post.get("data").get("title"))
