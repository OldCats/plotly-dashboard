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

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group",
            title="helo")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

## fig carrerhub start
df_carrerhub = pd.read_csv('https://library2.lincoln.ac.nz/dashboard/csvs/careerhub.csv', skiprows=6)

carrerhub_describe = f'{df_carrerhub.Appointments.sum()} people attended appointments with our Careers and Employment Advisors in the last 30 days. (Appointments may cover multiple topics.)'
title = 'Career advice'

fig_carrerhub = px.bar(df_carrerhub, x='Topic', y='Appointments', title=title)
fig_carrerhub.update_layout(xaxis={'categoryorder':'total descending'})

## fig cirulation stats start

df_circ_stats_by_desk = pd.read_csv('https://library2.lincoln.ac.nz/dashboard/csvs/circ_stats_by_desk.csv', 
                        skiprows=7,
                        skipfooter=1,
                        names=['Month', 'Circ desks', 'Self-checks'], engine='python')
df_circ_stats_by_desk = df_circ_stats_by_desk.iloc[::-1]
df_circ_stats_by_desk_desb = 'Which are used more: circulation desks or self-check machines?'

fig_cir_stat = px.line(df_circ_stats_by_desk, x='Month', y=['Circ desks','Self-checks'], title='Circulation Stats')
fig_cir_stat.update_xaxes(type='category')


app.layout = dbc.Container(
    [
       html.H1(
        children='Reports and Statistics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Te Kete Wānaka | Learning, Teaching and Library', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Hr(),

    dbc.Row(
            [
                dbc.Col([html.P(children=carrerhub_describe),
                         dcc.Graph(id="example-graph-1", figure=fig_carrerhub)],
                         md=6),
                dbc.Col([html.P(children=df_circ_stats_by_desk_desb),
                         dcc.Graph(id="example-graph-2", figure=fig_cir_stat)], 
                         md=6),
                dbc.Col(dcc.Graph(id="example-graph-3", figure=fig), 
                         md=4),
            ],
            align="center",
        ),
],
fluid=True,
)


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')
