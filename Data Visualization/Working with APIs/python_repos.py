import requests # import requests module

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # store the API url in a variable
headers = {'Accept': 'application/vnd.github.v3+json'} # define headers to explicitly use the current Git API version
r = requests.get(url, headers=headers) # call the API by passing the url and headers as args
print(f"Status code: {r.status_code}") # print the status code that arrives from the API call

# Store API response in a variable.
response_dict = r.json() # convert the API JSON data into a Python dict
print(f"Total repositories: {response_dict['total_count']}") # print value from the API dict key 'total count'

# Explore the information about the repositories.
repo_dicts = response_dict['items'] # store the value of key 'items', which is a list of dicts
print(f"Repositories returned: {len(repo_dicts)}") # print the length to see how may repos dicts are in the list

# Examine the first repository.
# repo_dict = repo_dicts[0] # select the first dict in the repo dicts list
# print(f"\nKeys: {len(repo_dict)}") # print how many keys are in the first dict
# for key in sorted(repo_dict.keys()): # sort the keys and loop through them
#     print(key) # print the keys

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
