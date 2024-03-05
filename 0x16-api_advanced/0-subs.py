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


    return resp.json()['data']["subscribers"]
