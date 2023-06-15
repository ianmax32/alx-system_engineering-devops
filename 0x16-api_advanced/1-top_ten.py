#!/usr/bin/python3
"""
function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given
subreddit.
"""


from requests import get


def top_ten(subreddit):
    """
    top 10 posts
    """
    try:
        url = "https://www.reddit.com/r/{}/hot?limit=10".format(subredit)
        header = {"user-agent": "ianmax"}
        req = get(url, headers=header, allo-redirects=false).json()
        topTen = req["data"]["children"]
        for a in topTen:
            print(a["data"]["title"])
    except Exception:
        print("None")
