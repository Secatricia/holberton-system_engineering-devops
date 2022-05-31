#!/usr/bin/python3
"""count length of all posts"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    url = "https://www.reddit.com/r/{}/hot.json"
    queries = requests.get(url.format(subreddit),
                           headers={"User-Agent": "Holberton"},
                           allow_redirects=False,
                           params={"count": count, 'after': after})

    if queries.status_code == 404:
        return None

    if queries.status_code == 200:
        hot_lits = hot_list + [child.get("data").get("title")
                               for child in queries.json()
                               .get("data")
                               .get("children")]
        info = queries.json()
        if not info.get("data").get("after"):
            return hot_lits
        return recurse(subreddit, hot_lits,
                       info.get("data").get("count"),
                       info.get("data").get("after"))
    else:
        print(None)
