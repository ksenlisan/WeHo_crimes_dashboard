from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('2018-2022_timestamped.csv')
df = df.query('timestamp >= "2018-01-01 00:00:00"')
app = Dash(__name__)

fig = px.histogram(df, x="timestamp", nbins=54)
fig2 = px.histogram(df, x="hour", nbins=24)
fig3 = px.histogram(df, x="weekday", nbins=24)

app.layout = html.Div(children=[
    html.H1(children='Test'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='crimes per time of day',
        figure=fig2
    ),

    dcc.Graph(
        id='crimes per day of the week',
        figure=fig3
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)