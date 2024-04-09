#!/usr/bin/python3
""" This script return the top ten posts of a subreddit in Reddit API """


import requests


def top_ten(subreddit):
    """ This function retrieves top ten posts by subreddit name"""
    url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': 'API advanced project 0.1'}

    response = requests.get(f'{url}{subreddit}/hot.json?limit=10',
                            headers=headers)
    data = response.json()
    for post in data.get("data", {}).get("children", 0):

        sub = data.get("data", {}).get("title", 0)
    return sub
