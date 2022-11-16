#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests


def number_of_subscribers(subreddit):
    """number of subscribers

    Args:
        subreddit (_type_): _description_

    Returns:
        _type_: _description_
    """
    user = {"User-Agent": "Ahmed_belhaj"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
