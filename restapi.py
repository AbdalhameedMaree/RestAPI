import requests
from dotenv import dotenv_values

def get_response_data(url, owner, pat):
    response = requests.get(url, auth=(owner, pat))
    response.raise_for_status()
    return response.json()

def get_releases(url, owner, pat):
    data = get_response_data(url, owner, pat)
    print("\n--- Releases ---")
    for i, item in enumerate(data, 1):
        print(f"{i}. Name: {item.get('name')}")

def get_collaborators(url, owner, pat):
    data = get_response_data(url, owner, pat)
    print("\n--- Collaborators ---")
    for i, item in enumerate(data, 1):
        perms = item.get('permissions', {})
        print(f"{i}. User: {item.get('login')}, Permissions: {perms}")

def get_branches(url, owner, pat):
    data = get_response_data(url, owner, pat)
    print("\n--- Branches ---")
    for i, item in enumerate(data, 1):
        print(f"{i}. Branch: {item.get('name')}")

def get_commits(url, owner, pat):
    data = get_response_data(url, owner, pat)
    print("\n--- Commits ---")
    for i, item in enumerate(data[:5], 1):
        commit = item.get('commit', {})
        author = commit.get('author', {}).get('name')
        msg = commit.get('message')
        date = commit.get('author', {}).get('date')
        print(f"{i}. Author: {author}, Date: {date}, Message: {msg}")

def get_pulls(url, owner, pat):
    data = get_response_data(url, owner, pat)
    print("\n--- Pulls ---")
    for i, item in enumerate(data, 1):
        user = item.get('user', {}).get('login')
        print(f"{i}. Title: {item.get('title')}, User: {user}")

def main():
    secrets = dotenv_values('.env')
    base_url = 'https://api.github.com/repos'
    owner = 'AbdalhameedMaree'
    repo = 'Optimization-Strategies-for-Local-Package-Delivery-Operations'
    pat = secrets.get('PAT')

    endpoints = {
        "releases": f'{base_url}/{owner}/{repo}/releases',
        "collaborators": f'{base_url}/{owner}/{repo}/collaborators',
        "branches": f'{base_url}/{owner}/{repo}/branches',
        "commits": f'{base_url}/{owner}/{repo}/commits',
        "pulls": f'{base_url}/{owner}/{repo}/pulls'
    }
    
    get_releases(endpoints['releases'], owner, pat)
    get_collaborators(endpoints['collaborators'], owner, pat)
    get_branches(endpoints['branches'], owner, pat)
    get_commits(endpoints['commits'], owner, pat)
    get_pulls(endpoints['pulls'], owner, pat)

if __name__ == "__main__":
    main()