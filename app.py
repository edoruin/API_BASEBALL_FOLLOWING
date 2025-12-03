"""
    Codigo de Streamlit, 
    servidor para mostrar los datos extraidos de 
    las APIs.


    requerimientos: config.toml con Detalles de la API

"""
#Librerias
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np 
from datetime import date
import ETL #Modulo de extraccion de los datos de la API
import altair as alt

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="LIDOM Stats Dashboard",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Bienvenido a LIDOM Stats Dashboard")
st.markdown('¿Quien crees que ganara?')

st.header("Obtener Juegos por Año")
st.markdown("Introduce el año que quieres analizar")


# Argumento de juegos, del usuario
año_seleccionado = st.number_input(
    "Año de los juegos a buscar",
    min_value=0,
    max_value=3000,
    value=0, # Por defecto busca todos
    step=1
)


if st.button("Buscar"): # Logica para añadir el resultado que usuario introduzca
    if año_seleccionado > 0:
        # Aquí se usa el valor del input como argumento de la función
        st.subheader(f"Recopilando datos de Juegos para el año '({año_seleccionado})'")
        juegos = ETL.Obtener_juegos(temporada=int(año_seleccionado))
    else:
        # Ejecutar sin argumento
        st.subheader("Recopilando...")
        st.warning(f"No existe la temporada {año_seleccionado}.")


# ---VISUALIZACION

    st.markdown("---")
    st.success("¡Petición completada!")

    if not juegos.empty: #si existe informacion en el año solicitado

        st.dataframe(juegos, use_container_width=True)
        st.header('RANKINGS')
        st.markdown("---")
        col1, col2 = st.columns(2) # creando dos columnas
        with col1: 
            st.header("Bateos en casa")        
            hits_ranking_home = juegos['scores.home.hits'].groupby(juegos['teams.home.name']).sum().sort_values(ascending=False)
            st.dataframe(hits_ranking_home, height = 250)

            st.header("Carreras de casa")        
            Runs_ranking_home = juegos['scores.home.total'].groupby(juegos['teams.home.name']).sum().sort_values(ascending=False)
            st.dataframe(Runs_ranking_home, height = 250)

            st.header("Errores en casa")        
            Runs_ranking_home = juegos['scores.home.errors'].groupby(juegos['teams.home.name']).sum().sort_values(ascending=False)
            st.dataframe(Runs_ranking_home, height = 250)


        with col2:

            st.header("Bateos en visitante")        
            hits_ranking_away = juegos['scores.away.hits'].groupby(juegos['teams.away.name']).sum().sort_values(ascending=False)
            st.dataframe(hits_ranking_away, height = 250)

            st.header("Carreras de visitante")        
            Runs_ranking_home = juegos['scores.away.total'].groupby(juegos['teams.away.name']).sum().sort_values(ascending=False)
            st.dataframe(Runs_ranking_home, height = 250)

            st.header("Errores de visitante")        
            Runs_ranking_home = juegos['scores.away.errors'].groupby(juegos['teams.away.name']).sum().sort_values(ascending=False)
            st.dataframe(Runs_ranking_home, height = 250)

        
        
    else:
        st.warning(f"No se encontraron juegos para el año {año_seleccionado}.")

