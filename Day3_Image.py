import gmaps
import gmaps.datasets
gmaps.configure(api_key='AIzaSyCaLk5pUopaL025Ink1AuCSaTIRitdTM40')
import pandas as pd

locations = []
my_filtered_csv = pd.read_csv("tweet_input.csv", usecols = ['latitude', 'longitude'])

fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(my_filtered_csv))
fig