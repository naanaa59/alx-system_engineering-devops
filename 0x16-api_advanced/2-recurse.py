#!/usr/bin/python3
""" This script returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'project API advanced'}
    params = {'limit': 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            if 'after' in data['data'] and data['data']['after'] is not None:
                after = data['data']['after']
                return recurse(subreddit, hot_list, after)
        return hot_list if hot_list else None
    else:
        return None
