import requests
from datetime import datetime, timezone, timedelta


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
        "url": commit["html_url"],
    }


def get_trending():
    yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")

    url = "https://api.github.com/search/repositories"

    params = {
        "q": f"pushed:>{yesterday} stars:>5",
        "sort": "stars",
        "order": "desc",
        "per_page": 10,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    result = f"**⭐ Melhores repos {yesterday}!**\n\n"

    i = 0
    for repo in data.get("items", []):
        i += 1
        result += (f"**#{i}.** {repo['full_name']} \n- ⭐ {repo['stargazers_count']} \n- 🔗 [Acesse]({"https://github.com/" + repo['full_name']})\n\n")
    return result
