#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10"
    queries = requests.get(url
                           .format(subreddit),
                           headers={"User-Agent": "Holberton"},
                           allow_redirects=False)

    if queries.status_code == 200:
        for k in queries.json().get("data").get("children"):
            print(k.get("data").get("title"))
    else:
        print(None)
