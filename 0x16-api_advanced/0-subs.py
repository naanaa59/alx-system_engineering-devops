#!/usr/bin/python3
""" This script return the numbers of subscribers to Reddit API """


import requests
import sys


def number_of_subscribers(subreddit):
    """ This function retrieves subsribers by subreddit name"""
    url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': 'Oumaima'}

    response = requests.get(f'{url}{subreddit}/about.json',
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
