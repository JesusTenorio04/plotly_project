import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('Aplicación de análisis de vehículos')

# Cargamos los datos
vehicles_df = pd.read_csv('vehicles_us.csv') 

# Creamos una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    # Escribimos un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Creamos el histograma
    fig = px.histogram(vehicles_df, x="odometer")
    
    # Mostramos el histograma
    st.plotly_chart(fig, use_container_width=True)

# Creamos una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    # Escribimos un mensaje
    st.write('Creación de un gráfico de dispersión: Odómetro vs Precio')
    
    # Creamos el gráfico de dispersión
    fig2 = px.scatter(vehicles_df, x="odometer", y="price")
    
    # Mostramos el gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)