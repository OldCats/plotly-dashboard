import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Reports and Statistics",
    layout="wide",
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


# streamlit layout
st.title('Reports and Statistics')
st.header('Te Kete Wānaka | Learning, Teaching and Library')


col1, col2 = st.columns(2)
with col1:
    st.write(carrerhub_describe)
    st.plotly_chart(fig_carrerhub)

with col2:
    st.write(df_circ_stats_by_desk_desb)
    st.plotly_chart(fig_cir_stat)
