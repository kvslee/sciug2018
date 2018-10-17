# Step 1: import plotly library and chart objects
# Step 2: Use offline plot function
# Step 3: feed data
# Step 4: decorate layout
# Step 5: pass optional arguments

import plotly
from plotly.graph_objs import Bar, Pie, Scatter, Layout

# Bar Chart
plotly.offline.plot({
    "data": [Bar(x=["Leatherby", "Law", "Science", "Music", "Brandman"], y=[543, 365, 92, 61, 77])],
    "layout": Layout(title="SCIUG Conference")
}, filename='output/first_offline_bar.html')


# Pie Chart
plotly.offline.plot({
    "data": [Pie(labels=["Leatherby", "Law", "Science", "Music", "Brandman"], values=[543, 365, 92, 61, 77])],
    "layout": Layout(title="SCIUG Conference")
}, filename='output/first_offline_pie.html', show_link=False)