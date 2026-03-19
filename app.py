import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

st.header("Analise Exploratória dos valores de carros dos USA", text_alignment = 'center' )

question_box = st.multiselect('Gostaria de analiser estatisticas de carro?', ["sim", "não"])

if "sim" in question_box:
    #Dando as escolhas possiveis
    choices = st.multiselect("Quais gráficos quer ver?", ["hist", "scatter", "both"])

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
    print("Obrigado pela visita, tenha um bom dia")


    

