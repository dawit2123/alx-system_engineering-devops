#!/usr/bin/python3
""" function that queries a Reddit API """
import requests as req
import sys


def top_ten(subreddit):
    """ Returns: top ten post titles """

    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = req.get(url, headers=headers, allow_redirects=False,
                       params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
