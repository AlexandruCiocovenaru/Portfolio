import requests # import requests module

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # store the API url in a variable
headers = {'Accept': 'application/vnd.github.v3+json'} # define headers to explicitly use the current Git API version
r = requests.get(url, headers=headers) # call the API by passing the url and headers as args
print(f"Status code: {r.status_code}") # print the status code that arrives from the API call

# Process the results.
response_dict = r.json() # convert the API JSON data into a Python dict

# Explore the information about the repositories.
repo_dicts = response_dict['items'] # store the value of key 'items', which is a list of dicts
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" # add an HTML anchor to generate a hyperlink
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}" # add HTML code within f string with Plotly (line breaker)
    labels.append(label)

# Make a visualization.
# Define a list of data to plot the bar chart
data = [{
    'type': 'bar', # select the type of chart
    'x': repo_links, # add repo_name and repo_url data to X (horizontal) axis
    'y': stars, # add stars data to Y (vertical) axis
    'hovertext': labels, # add tooltips
    'marker': {
        'color': 'rgb(60, 100, 150)', # define a blue color for the bars
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'} # set up the outline of the bars
        },
    'opacity': 0.6, # set the opacity of the bars
}]

# Define a layout for the data to plot the bar chart
my_layout = {
    'title': 'Most-Starred Python Projects on Github', # set up the title of the chart
    'title_x': 0.5, # align the title on the middle
    'titlefont': {'size': 28}, # enlarge the font of the chart title
    'xaxis': {
        'title': 'Repository', # define the title of the X axis
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars', # define the title of the Y axis
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

# Set up the plot for the bar chart
fig = {'data': data, 'layout': my_layout} # create a dict to contain the data and layout info.
offline.plot(fig, filename='python_repos.html') # pass the dict to plot() function and give it a name