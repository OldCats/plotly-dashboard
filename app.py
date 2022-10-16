# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'background': 'white',
    'text': 'black'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = dbc.Container(
    [
       html.H1(
        children='Reports and Statistics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dbc.Row(
            [
                dbc.Col(dcc.Graph(id="example-graph-1", figure=fig), md=4),
                dbc.Col(dcc.Graph(id="example-graph-2", figure=fig), md=4),
                dbc.Col(dcc.Graph(id="example-graph-3", figure=fig), md=4),
            ],
            align="center",
        ),
],
fluid=True,
)


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')
