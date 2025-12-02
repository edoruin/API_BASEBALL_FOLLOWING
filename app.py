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


# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="LIDOM Stats Dashboard",
    page_icon="⚾️",
    layout="wide",
    initial_sidebar_state="expanded"
)
