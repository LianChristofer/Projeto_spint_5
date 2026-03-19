import streamlit as st
import pandas as pd
import plotly.express as px
from time import sleep

car_data = pd.read_csv('vehicles.csv')

st.header("Analise Exploratória dos valores de carros dos USA", text_alignment = 'center' )

question_box = st.selectbox("Gostaria de analisar estatísticas de carro?", [" ","sim", "não"])

if " " in question_box:
    sleep(99999999999999999999999999999999999999)

if "sim" in question_box:
    #Dando as escolhas possiveis
    choices = st.selectbox("Quais gráficos quer ver?", ["hist", "scatter", "both"])

    #SE escolher his, plora um hist, e se escolher both tabm
    if "hist" in choices or "both" in choices:
        st.write("Criando um Histograma...")
        fig = px.histogram(car_data, x="odometer", y="price", nbins=100)
        st.plotly_chart(fig, use_container_width=True)

    #SE escolher scatter, plota o sctter, e se esocolher both tbm
    if "scatter" in choices or "both" in choices:
        st.write("Criando um gráfico de dispersão...")
        fig1 = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig1, use_container_width=True)

if "não" in question_box:
    st.write("Obrigado pela visita, tenha um bom dia")


    

