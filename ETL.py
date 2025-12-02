"""
    Docstring for ETL,
    Flujo de procesamiento 
    de los datos recibidor por la APIs

"""

import requests
import toml
import pandas as pd

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

def Obtener_juegos(temporada):

    """
    Docstring for Obtener_juegos
    
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

    juegos = resp_games.json()

    juegos_df = json_a_df(juegos)

    return juegos_df




