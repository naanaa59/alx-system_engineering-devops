#!/usr/bin/python3
""" This script return the numbers of subscribers to Reddit API """


import requests


def number_of_subscribers(subreddit):
    """ This function retrieves subsribers by subreddit name"""
    url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': 'API advanced project 0.1'}

    response = requests.get(f'{url}{subreddit}/about.json',
                            headers=headers)
    data = response.json()
    sub = data.get("data", {}).get("subscribers", 0)
    return sub
