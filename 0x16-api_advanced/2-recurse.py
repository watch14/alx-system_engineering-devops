#!/usr/bin/python3
""" API Subreddit """
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    top 10 posts
    """
    link = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'ALX aAPI task 2'}
    params = {"count": count, "after": after}
    resp = requests.get(link,
                        params=params,
                        headers=headers,
                        allow_redirects=False)

    if resp.status_code >= 400:
        return None

    results = resp.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list


result = recurse("programming")
print(len(result))
