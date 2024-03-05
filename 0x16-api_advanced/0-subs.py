#!/usr/bin/python3
"""
API Subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    nbr subs
    """
    link = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ALX aAPI task 0'}
    resp = requests.get(link, headers=headers, allow_redirects=False)

    if resp.status_code == 404:
        return 0

    return resp.json()['data']["subscribers"]
