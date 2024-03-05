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

    if not resp.ok:
        if len(hot_list) == 0:
            return None
        else:
            return hot_list

    data = resp.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    
    after = data['after']
    dist = data['dist']
    if (after):
        recurse(subreddit, hot_list, count + dist, after)

    if len(hot_list) == 0:
        return None
    else:
        return hot_list


result = recurse("programming")
print(len(result))
