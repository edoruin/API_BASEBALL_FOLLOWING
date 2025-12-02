"""
    Docstring for ETL,
    Flujo de procesamiento 
    de los datos recibidor por la APIs

"""

import requests
import toml
import pandas as pd
import streamlit as st #para utilizar el cache 

#--- IMPORTAR EL APIKEY---
def API_detalles():
    """
    Contiene los datos relacionados a la API

    return:
        Api key y url base
    """
    try:
        with open("config.toml", "r") as f:
            config = toml.load(f)
    except FileNotFoundError:
        print("Error: Archivo de configuracion (config.toml) no encontrado.")
        exit()

    # 2. Acceder a la clave
    clave_api = config['api']['clave_secreta']

    base_url = config['api']['base_url']

    #encabezados de autenticacion
    headers = {
        "x-apisports-key": clave_api
    }

    return  headers, base_url #posicion 0 y 1

Headers,base_url = API_detalles() #almacenando 


def json_a_df(keys):
        """
        Docstring for json_a_df
        
        :param keys: 
            convierte archivos json a dataframes
        """
        leagues_list = keys['response']
        datos_df =  pd.json_normalize(leagues_list)
        return datos_df

        
# ---SOLICITANDO DATOS

# response = requests.get(f"{base_url}/leagues", headers=Headers) #datos de ligas

@st.cache_data(ttl=3600) #no vuelve a llamar la funcion si pides los mismos argumentos
def Obtener_juegos(temporada):

    """
    Docstring for Obtener_juegos:
        Extraccion de datos de los juegos
        que se han disputado por temporada
    
    :param temporada:  
        Escoge la temporada que quieres extraer
    """
    LINDOM_ID = 11
    SEASON = temporada
    params = {
        "league": LINDOM_ID,
        "season": SEASON
    }

    resp_games = requests.get(
        f"{base_url}/games",
        headers=Headers,
        params=params
    )

    resp_games.raise_for_status() #notificacion ante error http

    juegos = resp_games.json()

    juegos_df = json_a_df(juegos)

    return juegos_df
