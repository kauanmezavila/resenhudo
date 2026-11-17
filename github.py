import requests

def get_last_commit(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    response.raise_for_status()

    commit = response.json()[0]

    return {
        "sha": commit["sha"],
        "message": commit["commit"]["message"],
        "author": commit["commit"]["author"]["name"],
        "date": commit["commit"]["author"]["date"],
        "url": commit["html_url"]
    }
