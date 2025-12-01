
import requests
from dotenv import dotenv_values
secrets = dotenv_values('.env')

BaseURL = secrets['BaseURL']
Repo = secrets['Repo']
Owner = secrets['Owner']
PAT = secrets['PAT']
API_Schema = f'{BaseURL}/{Owner}/{Repo}'


def get_data(API_url):
    response = requests.get(API_url, auth=(Owner, PAT))
    if response.status_code == 200:
        return response.json()
    else:
        return None


def print_data(data):
    if data is not None:
        for item in data:
            print(len(item))
    else:
        print("No data found or error in API request.")


def main():
    Releases_API = f'{API_Schema}/releases'
    Collaborators_API = f'{API_Schema}/collaborators'
    Branches_API = f'{API_Schema}/branches'
    Commits_API = f'{API_Schema}/commits'
    Pull_Requests_API = f'{API_Schema}/pulls'

    print("Number of Releases:")
    releases = get_data(Releases_API)
    print(len(releases))

    print("\nNumber of Collaborators:")
    collaborators = get_data(Collaborators_API)
    print(len(collaborators))

    print("\nNumber of Branches:")
    branches = get_data(Branches_API)
    print(len(branches))

    print("\nNumber of Commits:")
    commits = get_data(Commits_API)
    print(len(commits))

    print("\nNumber of Pull Requests:")
    pull_requests = get_data(Pull_Requests_API)
    print(len(pull_requests))



if __name__ == "__main__":
    main()