#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""


from requests import get


def recurse(subreddit, hot_list=[], key):
    """
    return a list of titles of hot articles
    """
    try:
        url = "https://www.reddit.com/r/{}/hot?after={}".format(subredit, key)
        header = {"user-agent": "ianmax"}
        req = get(url, headers=header, allow_redirects=False).json()
        topTen = req["data"]["children"]
        for a in topTen:
            hot_list.append(a["data"]["title"])
        key = req["data"]["after"]
        if key:
            recurse(subreddit, hot_list, key)
        return hot_list
    except Exception:
        print("None")
