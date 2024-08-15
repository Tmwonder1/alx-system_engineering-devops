#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers (not active users, total subscribers)"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers of a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit, or 0 if invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {"User-Agent": "python:myapp:v1.0 (by /u/your_username)"}

    try:
        response = requests.get(url, headers=user_agent, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0

def main():
    """Main function to interact with the user."""
    subreddit = input("Enter the name of the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    if subscribers == 0:
        print(f"Failed to retrieve data or nonexisting subreddit: {subreddit}")
    else:
        print(f"Number of subscribers in r/{subreddit}: {subscribers}")

if __name__ == "__main__":
    main()
