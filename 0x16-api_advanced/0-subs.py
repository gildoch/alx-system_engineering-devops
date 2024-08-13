#!/usr/bin/python3
"""Method to query the number of subscriber"""


def number_of_subscribers(subreddit):
    """Retrieves the number of subscriber on the subreddit"""
    import requests

    subs = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
    )

    if subs.status_code >= 300:
        return 0

    return subs.json().get("data").get("subscribers")
