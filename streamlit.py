import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import time
import matplotlib
import numpy as np
import pydeck as pdk
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import plotly.express as px
import folium
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Warszawskie restauracje ze strony pyszne.pl")
    
data = ("~/Desktop/PAD_PROJEKT/df_cleaned.csv")


df = pd.read_csv("~/Desktop/PAD/PAD_PROJEKT/df_cleaned.csv").iloc[:,1:]
restaurants_dummies_nolunch = pd.read_csv("~/Desktop/PAD_PROJEKT/restaurants_dummies_nolunch.csv").iloc[:,1:]
restaurants_dummies_nolunch_withscore_row_norm = pd.read_csv("~/Desktop/PAD_PROJEKT/restaurants_dummies_nolunch_withscore_row_norm.csv").iloc[:,1:]
restaurants_dummies_by_score = pd.read_csv("~/Desktop/PAD_PROJEKT/restaurants_dummies_by_score.csv").iloc[:,1:]

st.dataframe(df)
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("### Mapa warszawskich restauracji")
    midpoint = (np.average(df['latitude']), np.average(df['longitude']))
    map2 = folium.Map(location = midpoint, tiles='Stamen Terrain', zoom_start = 10, control_scale=True)
    for index, loc in df.iterrows():
        if loc['score']>=4.3:
            color = 'red'
        elif loc['score']>3.8 and loc['score']<4.3:
            color = 'blue'
        elif loc['score']<3.8:
            color = 'darkgreen'
        else:
            color = 'black'
    #folium.RegularPolygonMarker([loc['latitude'], loc['longtitude']], popup = loc['name'], color=color, fill_color=color, number_of_sides=5, radius=6, rotation=30).add_to(map2)
        folium.CircleMarker([loc['latitude'], loc['longitude']], popup = loc['name'], color=color, fill_color=color, number_of_sides=3, radius=3, weight=5).add_to(map2)
    folium.LayerControl().add_to(map2)
    folium_static(map2, width = 600)
   
with fig_col2:
    st.markdown("### Top 15 rated restaurants")
    dfg = df.sort_values(by=['score'], ascending=False).head(15)
    dfg = dfg[['name', 'score']]
    fig2 = px.bar(dfg, y='name', x='score', orientation = 'h')
    st.write(fig2)

fig_col3, fig_col4 = st.columns(2)

with fig_col3:
    st.markdown("### Rozklad przedzialowy ocen naszych restauracji")
    labels = df.score_range.value_counts().index
    values = df.score_range.value_counts().values
    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(
        data=[
            go.Pie(labels=labels, values=values, hole=0.4)
    ])
    st.plotly_chart(fig)

with fig_col4:
    st.markdown("### Rodzaje kuchni pod wzgledem liczebnosci na stronie")
    fig2 = px.bar(restaurants_dummies_nolunch.sum(), labels={"index": "Restaurants"}, title="Count of restaurants")
    fig2.update_layout(showlegend=False, xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig2)

selected = st.selectbox(
     'Wybierz, w jakiej postaci wolisz miec przedstawiony udzial poszczegolnych kuchni w danym przedziale ocen',
     ('calkowity', 'procentowy'))

restaurants_nolunch_withscore = restaurants_dummies_nolunch_withscore_row_norm.columns.tolist()
if selected == "calkowity":
    st.balloons()
    fig4 = make_subplots(2, 2, subplot_titles=restaurants_dummies_by_score.index)
    for index, age_range in enumerate(restaurants_dummies_by_score.index):
        row = (index // 2) + 1
        col = (index % 2) + 1
        fig4.add_trace(
            go.Bar(x=restaurants_nolunch_withscore, y=restaurants_dummies_by_score.iloc[index]),
            row=row, col=col
        )
        fig4.update_layout(showlegend=False, height=1000, width=1000, xaxis={'categoryorder':'total descending'}, title="Number of restaurants cuisine types per score")
    st.plotly_chart(fig4)

if selected == "procentowy":
    st.balloons()
    fig5 = make_subplots(2, 2, subplot_titles=restaurants_dummies_nolunch_withscore_row_norm.index)
    for index, age_range in enumerate(restaurants_dummies_nolunch_withscore_row_norm.index):
        row = (index // 2) + 1
        col = (index % 2) + 1
        fig5.add_trace(
            go.Bar(x=restaurants_nolunch_withscore, y=restaurants_dummies_nolunch_withscore_row_norm.iloc[index]),
            row=row, col=col
        )
    fig5.update_layout(showlegend=False, height=1000, width=1000, xaxis={'categoryorder':'total descending'}, title="Percent of restaurants cuisine types per score")
    fig5.update_yaxes(tickformat="%")
    st.plotly_chart(fig5)

fig_col5, fig_col6 = st.columns(2)

with fig_col5:
    st.markdown("### Zaleznosc votes i popularity oraz score")
    st.markdown('Mozna zauwazyc zaleznosc, im wiecej oddanych glosow i wieksza popularnosc, tym wyzsza ocena restauracji**.')
    fig3 = px.scatter(df,x='popularity',y='votes',color='score')
    st.plotly_chart(fig3)

with fig_col6:
    zmienne = df[['votes', 'popularity', 'delivery_time_min', 'delivery_time_max']]
    zmienne = zmienne.columns.to_list()
    selected_column_names = st.selectbox("Wybierz zmienne do porownania ze zmienna score", zmienne)
    df2 = df[selected_column_names]
    fig6 = px.scatter(x=df['score'], y=df2)
    st.plotly_chart(fig6)

fig7 = px.imshow(df.corr(), title="Correlation heatmap")
fig7.update_layout(height=800)
st.plotly_chart(fig7)