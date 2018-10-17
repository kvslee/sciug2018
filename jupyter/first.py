# Step 1: import plotly library and chart objects
# Step 2: feed data
# Step 3: decorate layout

import plotly
from plotly.graph_objs import Bar, Pie, Scatter, Layout

# Need this when Jupyter is runnning on your local PC
plotly.offline.init_notebook_mode(connected=True)

# Pie Chart
pie_chart = plotly.offline.iplot({
    "data": [Pie(labels=["Leatherby", "Law", "Science", "Music", "Brandman"], values=[543, 365, 92, 61, 77])],
    "layout": Layout(title="Checkouts by Libraries")
})

