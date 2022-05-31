#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json"
    queries = requests.get(url.format(subreddit),
                           headers={"User-Agent": "holberton"},
                           allow_redirects=False)

    if queries.status_code == 200:  # if the request succeeded
        return queries.json()["data"]["subscribers"]

    return 0  # If not a valid subreddit
