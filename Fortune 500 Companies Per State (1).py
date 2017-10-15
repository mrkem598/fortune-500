# Get this figure: fig = py.get_figure("https://plot.ly/~stacyannj/368/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~stacyannj/368/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Fortune 500 Companies Per State (1)", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~stacyannj/368/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "x": ["States", "Finance", "Food & Beverage", "Health", "Housing & Construction", "Manufacturing", "Media & Entertainment", "Retail", "Tech & Services", "Transportation", "Utilities"], 
  "y": ["AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "MI", "MN", "MO", "NC", "NE", "NJ", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "TN", "TX", "UT", "VA", "WA", "WI"], 
  "z": [
    ["AL", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], ["AR", 0, 1, 0, 0, 1, 0, 3, 1, 1, 0], ["AZ", 0, 0, 0, 0, 1, 0, 3, 1, 0, 0], ["CA", 6, 0, 5, 3, 12, 2, 10, 12, 0, 3], ["CO", 1, 0, 1, 1, 1, 0, 1, 3, 1, 0], ["CT", 3, 0, 2, 3, 2, 1, 0, 5, 1, 0], ["DC", 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], ["DE", 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], ["FL", 2, 1, 1, 2, 1, 0, 4, 0, 3, 1], ["GA", 3, 2, 0, 4, 0, 0, 3, 2, 4, 2], ["IA", 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], ["ID", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], ["IL", 4, 5, 3, 3, 2, 1, 7, 2, 5, 2], ["IN", 0, 0, 2, 1, 2, 0, 0, 0, 0, 1], ["KS", 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], ["KY", 0, 1, 2, 0, 2, 0, 0, 0, 0, 0], ["LA", 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], ["MA", 3, 0, 2, 0, 1, 0, 3, 1, 1, 1], ["MD", 0, 0, 0, 1, 0, 2, 0, 0, 1, 0], ["MI", 2, 1, 1, 1, 2, 0, 1, 1, 9, 2], ["MN", 3, 4, 2, 0, 3, 0, 3, 0, 1, 1], ["MO", 2, 0, 2, 0, 3, 0, 2, 0, 0, 1], ["NC", 2, 1, 2, 0, 3, 0, 3, 0, 2, 1], ["NE", 2, 1, 0, 1, 0, 0, 0, 0, 1, 0], ["NJ", 2, 1, 5, 1, 2, 1, 2, 2, 1, 2], ["NV", 0, 0, 0, 0, 0, 4, 0, 0, 0, 0], ["NY", 23, 3, 2, 0, 5, 7, 7, 5, 2, 1], ["OH", 5, 1, 1, 1, 4, 0, 6, 0, 3, 2], ["OK", 0, 0, 0, 1, 2, 0, 1, 0, 0, 1], ["OR", 0, 0, 0, 0, 1, 0, 0, 0, 2, 0], ["PA", 3, 2, 1, 0, 3, 0, 4, 2, 1, 2], ["RI", 0, 0, 0, 0, 0, 0, 2, 0, 1, 0], ["SC", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], ["TN", 1, 0, 3, 0, 2, 0, 3, 0, 2, 0], ["TX", 2, 2, 1, 11, 16, 1, 6, 2, 4, 9], ["UT", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], ["VA", 3, 1, 0, 0, 0, 2, 3, 2, 6, 2], ["WA", 0, 1, 0, 0, 1, 0, 2, 3, 3, 0], ["WI", 2, 0, 0, 0, 1, 0, 1, 1, 3, ], 
  "autocolorscale": False, 
  "colorscale": [
    [0, "rgb(12,51,131)"], [0.25, "rgb(10,136,186)"], [0.5, "rgb(242,211,56)"], [0.75, "rgb(242,143,56)"], [1, "rgb(217,30,30)], 
  "name": "States", 
  "opacity": 1, 
  "reversescale": False, 
  "showscale": False, 
  "type": "heatmap", 
  "uid": "bfd9c2", 
  "xsrc": "stacyannj:354:?names", 
  "ysrc": "stacyannj:354:KJ113WD807EC95Z5O2LE4J6NLB0XP35Q", 
  "zauto": False, 
  "zmax": 10, 
  "zmin": 0, 
  "zsmooth": False, 
  "zsrc": "stacyannj:354:"
}
data = Data([trace1])
layout = {
  "autosize": False, 
  "dragmode": "zoom", 
  "font": {
    "color": "#444", 
    "family": "PT Sans Narrow, sans-serif", 
    "size": 12
  }, 
  "height": 750, 
  "hidesources": False, 
  "hovermode": "x", 
  "margin": {
    "t": 80, 
    "b": 110
  }, 
  "paper_bgcolor": "#fff", 
  "plot_bgcolor": "#fff", 
  "separators": ".,", 
  "showlegend": False, 
  "title": "Fortune 500 Companies Per State", 
  "titlefont": {
    "color": "#444", 
    "family": "PT Sans Narrow, sans-serif", 
    "size": 28
  }, 
  "width": 545, 
  "xaxis": {
    "autorange": False, 
    "fixedrange": True, 
    "gridcolor": "#eee", 
    "gridwidth": 1, 
    "mirror": False, 
    "nticks": 0, 
    "range": [0.510017238417, 10.5], 
    "showgrid": True, 
    "showline": False, 
    "showticklabels": True, 
    "tickangle": -30, 
    "tickcolor": "#444", 
    "tickfont": {
      "color": "#444", 
      "family": "PT Sans Narrow, sans-serif", 
      "size": 14
    }, 
    "ticklen": 5, 
    "tickmode": "auto", 
    "ticks": "outside", 
    "tickwidth": 1, 
    "title": "Source: <a href=\"http://www.fortune.com\">Fortune</a>", 
    "titlefont": {
      "color": "#444", 
      "family": "PT Sans Narrow, sans-serif", 
      "size": 12
    }, 
    "type": "category", 
    "zeroline": True, 
    "zerolinecolor": "#444", 
    "zerolinewidth": 1
  }, 
  "yaxis": {
    "autorange": True, 
    "dtick": 1, 
    "fixedrange": True, 
    "linecolor": "#444", 
    "linewidth": 1, 
    "mirror": False, 
    "range": [38.5, -0.5], 
    "rangemode": "normal", 
    "showgrid": False, 
    "showline": True, 
    "showticklabels": True, 
    "tick0": 0, 
    "tickangle": "auto", 
    "tickcolor": "#444", 
    "tickfont": {
      "color": "#444", 
      "family": "PT Sans Narrow, sans-serif", 
      "size": 14
    }, 
    "ticklen": 5, 
    "tickmode": "linear", 
    "ticks": "outside", 
    "tickwidth": 1, 
    "titlefont": {
      "color": "#444", 
      "family": "PT Sans Narrow, sans-serif", 
      "size": 14
    }, 
    "type": "category", 
    "zeroline": True, 
    "zerolinecolor": "#444", 
    "zerolinewidth": 1
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)