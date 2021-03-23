from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from eq_explore_data import mags, lons, lats, hover_texts

# Map the earthquakes.
# Define a list of data to plot the geo data
data = [{
    'type': 'scattergeo', # select the type of chart
    'lon': lons, # add the lon data
    'lat': lats, # add the lat data
    'text': hover_texts, # add the descriptive data (magnitude and location)
    'marker': { # add a marker to change how the scattered plot looks like
        'size': [5*mag for mag in mags], # define the size in a list comprehension
        'color': mags, # specify what values should be used to determine where each marker falls on the colorscale
        'colorscale': 'Viridis', # specify which range of colors to use (dark blue to bright yellow)
        'reversescale': True, # reverse the colors: for low values bright yellow and for high values dark blue)
        'colorbar': {'title': 'Magnitude'}, # the legend of the colorscale
        }
}]
my_layout = Layout(title='Global Earthquakes') # set up the chart title using a Layout object

fig = {'data': data, 'layout': my_layout} # create a dict to contain the data and layout info.
offline.plot(fig, filename='global_earthquakes.html') # pass the dict to plot() function and give it a name