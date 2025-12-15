import requests
from dotenv import dotenv_values

def get_requests(endpoints, base_url, owner, repo, pat):
    for end_point in endpoints:
        full_endpoint = f'{base_url}/{owner}/{repo}/{end_point}'
        response = requests.get(full_endpoint, auth=(owner, pat))
        response.raise_for_status()
        data = response.json()
        
        print(f"\n--- {end_point.capitalize()} ---")
        
        if end_point == "releases":
            for i, item in enumerate(data, 1):
                print(f"{i}. Name: {item.get('name')}")
        
        elif end_point == "collaborators":
            for i, item in enumerate(data, 1):
                perms = item.get('permissions', {})
                print(f"{i}. User: {item.get('login')}, Permissions: {perms}")
        
        elif end_point == "branches":
            for i, item in enumerate(data, 1):
                print(f"{i}. Branch: {item.get('name')}")
        
        elif end_point == "commits":
            for i, item in enumerate(data[:5], 1):
                commit = item.get('commit', {})
                author = commit.get('author', {}).get('name')
                msg = commit.get('message')
                date = commit.get('author', {}).get('date')
                print(f"{i}. Author: {author}, Date: {date}, Message: {msg}")
        
        elif end_point == "pulls":
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



    end_points = ["releases", "collaborators", "branches", "commits", "pulls"]
    get_requests(end_points, base_url, owner, repo, pat)

if __name__ == "__main__":
    main()