#!/usr/bin/python3
"""
Uses GitHub API to list 10 most recent commits from a repository by a user.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        # Get the 10 most recent commits
        commits = response.json()[:10]

        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print("Failed to fetch commits.")
