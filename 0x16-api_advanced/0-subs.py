#!/usr/bin/python3
"""
function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    this fun is for num of suscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"user-agent":"ianmax"}
    try:
        requ = get(url,headers=header).json()
        num = requ["data"]["subscribers"]
        return num
    except Exception:
        return 0
