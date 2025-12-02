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
import requests
import toml
from datetime import date



#--- IMPORTAR EL APIKEY---
try:
    with open("config.toml", "r") as f:
        config = toml.load(f)
except FileNotFoundError:
    print("Error: Archivo de configuracion (config.toml) no encontrado.")
    exit()

# 2. Acceder a la clave
clave_api = config['api']['clave_secreta']

#encabezados de autenticacion
headers = {
    "x-apisports-key": clave_api
}


### ---EXTRAYENDO DATA DE JUEGOS

# equipos = pd.read_csv('data/stats_equipos_39_2023.csv') # variables 
# jugadores = pd.read_csv('data/ligas_futbol.csv')
# equipos.describe(include='all')
# jugadores.describe(include='all')



# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="LIDOM Stats Dashboard",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded"
)
