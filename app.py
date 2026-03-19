import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

st.header("Analise Exploratória dos valores de carros dos USA", text_alignment = 'center' )

hist_button = st.button('Gostaria de analiser estatisticas de carro?')

if hist_button:

    question_box = st.checkbox(["his", "scatter", "both"])

    if "his" in question_box:
        #Criando uma msg
        st.write("Criando um Histograma...")

        #Criando um Histograma
        fig = px.histogram(car_data, x='odometer', y="price", nbins=100)

        #Plotando o histograma
        st.plotly_chart(fig, use_container_width=True)

    if "scatter" in question_box:
        #Criando uma msg
        st.write("Criando um grafico de dispeção...")

        #Criando um Histograma
        fig1 = px.scatter(car_data, x='odometer', y="price")

        #Plotando o histograma
        st.plotly_chart(fig1, use_container_width=True)

    if "both" in question_box:
        #Criando uma msg
        st.write("Criando os gráficos...")

        #Criando um Histograma
        fig = px.histogram(car_data, x='odometer', y="price", nbins=100)

        #Plotando o histograma
        st.plotly_chart(fig, use_container_width=True)

        #Criando um grafico de disperção
        fig1 = px.scatter(car_data, x='odometer', y="price")

        #Plotando o grafico
        st.plotly_chart(fig1, use_container_width=True)

    

