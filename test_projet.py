import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

velib_mois= pd.read_csv('velib_mois.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(x=velib_mois['Date de comptage'],y=velib_mois['Comptage horaire 2018'],name='2018'))
fig.add_trace(go.Scatter(x=velib_mois['Date de comptage'],y=velib_mois['Comptage horaire 2019'],name='2019'))
fig.add_trace(go.Scatter(x=velib_mois['Date de comptage'],y=velib_mois['Comptage horaire 2020'],name='2020'))
fig.add_trace(go.Scatter(x=velib_mois['Date de comptage'],y=velib_mois['Comptage horaire 2021'], name='2021'))

fig.update_layout(
    title="Utilisation des vélibs depuis 2018 (comptage horaire moyen)",
    xaxis_title="Par mois",
    yaxis_title="Comptage horaire moyen",
    legend_title="Année",
    font=dict(
        family="Courier New, monospace",
        size=18))

fig.show()
