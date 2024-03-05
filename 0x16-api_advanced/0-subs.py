#!/usr/bin/python3
""" API Subreddit """
import requests


def number_of_subscribers(subreddit):
    """ nbr subs """
    link = f"https://www.reddit.com/r/{subreddit}/about.json"
    resp = requests.get(link, allow_redirects=False)

    if resp.status_code == 404:
        return 0

    data = resp.json()

    return data['data']["subscribers"]
