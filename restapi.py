import requests
from dotenv import dotenv_values

def get_requests(endpoints, name, owner, pat):
    url = endpoints[name]
    response = requests.get(url, auth=(owner, pat))
    response.raise_for_status()
    data = response.json()
    
    print(f"\n--- {name.capitalize()} ---")
    
    if name == "releases":
        for i, item in enumerate(data, 1):
            print(f"{i}. Name: {item.get('name')}")
    
    elif name == "collaborators":
        for i, item in enumerate(data, 1):
            perms = item.get('permissions', {})
            print(f"{i}. User: {item.get('login')}, Permissions: {perms}")
    
    elif name == "branches":
        for i, item in enumerate(data, 1):
            print(f"{i}. Branch: {item.get('name')}")
    
    elif name == "commits":
        for i, item in enumerate(data[:5], 1):
            commit = item.get('commit', {})
            author = commit.get('author', {}).get('name')
            msg = commit.get('message')
            date = commit.get('author', {}).get('date')
            print(f"{i}. Author: {author}, Date: {date}, Message: {msg}")
    
    elif name == "pulls":
        for i, item in enumerate(data, 1):
            user = item.get('user', {}).get('login')
            print(f"{i}. Title: {item.get('title')}, User: {user}")
    
    else:
        print(f"Count: {len(data)}")


def main():
    secrets = dotenv_values('.env')
    base_url = 'https://api.github.com/repos'
    owner = 'AbdalhameedMaree'
    repo = 'Optimization-Strategies-for-Local-Package-Delivery-Operations'
    pat = secrets.get('PAT')

    end_points = {
        "releases": f'{base_url}/{owner}/{repo}/releases',
        "collaborators": f'{base_url}/{owner}/{repo}/collaborators',
        "branches": f'{base_url}/{owner}/{repo}/branches',
        "commits": f'{base_url}/{owner}/{repo}/commits',
        "pulls": f'{base_url}/{owner}/{repo}/pulls'
    }
    get_requests(end_points, 'releases', owner, pat)
    get_requests(end_points, 'collaborators', owner, pat)
    get_requests(end_points, 'branches', owner, pat)
    get_requests(end_points, 'commits', owner, pat)
    get_requests(end_points, 'pulls', owner, pat)

if __name__ == "__main__":
    main()