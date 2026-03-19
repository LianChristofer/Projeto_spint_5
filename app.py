import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

st.header("Analise Exploratória dos valores de carros dos USA", text_alignment = 'center' )

hist_button = st.button('Criar um Histogram?')

if hist_button:

    #Criando uma msg
    st.write("Criando um Histograma...")

    #Criando um Histograma
    fig = px.histogram(car_data, x='odometer', nbins=100)

    #Plotando o histograma
    st.plotly_chart(fig, use_container_width=True)

