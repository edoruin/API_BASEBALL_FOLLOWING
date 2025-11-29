"""
    Codigo de Streamlit, 
    servidor para mostrar los datos extraidos de 
    las APIs.

"""
#Librerias
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np 
import requests

equipos = pd.read_csv('data/stats_equipos_39_2023.csv')
jugadores = pd.read_csv('data/ligas_futbol.csv')
equipos.describe(include='all')
jugadores.describe(include='all')


# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Dashboard Fútbol", layout="wide")

# --- TÍTULO Y ENCABEZADO ---
st.title("Dashboard de Crecimiento de la Premier League")
st.markdown("Explora las estadísticas de los mejores equipos y jugadores de la temporada.")

# --- 1. FUNCIÓN DE CARGA DE DATOS ---
# Usamos @st.cache_data para que no llame a la API cada vez que cambias un filtro
@st.cache_data
def cargar_datos():
    # --- MODO DEMO (DATOS FALSOS PARA PROBAR AHORA) ---
    data = {
        'Jugador': ['Haaland', 'Salah', 'Son', 'Watkins', 'Saka', 'Isak', 'Foden', 'Palmer', 'Darwin'],
        'Equipo': ['Man City', 'Liverpool', 'Tottenham', 'Aston Villa', 'Arsenal', 'Newcastle', 'Man City', 'Chelsea', 'Liverpool'],
        'Goles': [27, 18, 17, 19, 16, 21, 19, 22, 11],
        'Asistencias': [5, 10, 10, 13, 9, 2, 8, 11, 8],
        'Partidos': [31, 32, 34, 37, 35, 30, 34, 33, 29]
    }
    df = pd.DataFrame(data)

    # --- MODO REAL (TU CÓDIGO DE API) ---
   

    return df

# Cargamos los datos
df = cargar_datos()


# --- 2. BARRA LATERAL (SIDEBAR) - FILTROS ---
st.sidebar.header("Filtros")

# Filtro por Equipo
equipos_disponibles = df['Equipo'].unique()
seleccion_equipos = st.sidebar.multiselect(
    "Selecciona Equipos:",
    options=equipos_disponibles,
    default=equipos_disponibles # Por defecto selecciona todos
)

# Filtro por Goles (Slider)
min_goles = st.sidebar.slider("Goles Mínimos:", 0, 30, 10)

# --- 3. APLICAR FILTROS AL DATAFRAME ---
# Filtramos el DF base según lo que eligió el usuario
df_filtrado = df[
    (df['Equipo'].isin(seleccion_equipos)) &
    (df['Goles'] >= min_goles)
]

# --- 4. MÉTRICAS PRINCIPALES (KPIs) ---
# Mostramos números grandes arriba
col1, col2, col3 = st.columns(3)
col1.metric("Jugadores Mostrados", len(df_filtrado))
col2.metric("Total Goles", df_filtrado['Goles'].sum())
col3.metric("Promedio Goles", round(df_filtrado['Goles'].mean(), 2))

st.divider() # Línea separadora

# --- 5. GRÁFICOS INTERACTIVOS ---
c1, c2 = st.columns((2, 1)) # La columna 1 es el doble de ancha que la 2

with c1:
    st.subheader("Goles vs Asistencias")
    fig_scatter = px.scatter(
        df_filtrado,
        x="Asistencias",
        y="Goles",
        color="Equipo",
        size="Partidos",
        hover_name="Jugador",
        text="Jugador",
        size_max=40
    )
    fig_scatter.update_traces(textposition='top center')
    st.plotly_chart(fig_scatter, use_container_width=True)

with c2:
    st.subheader("Goleadores por Equipo")
    # Agrupamos para ver qué equipo tiene más goles en total (de los filtrados)
    df_agrupado = df_filtrado.groupby('Equipo')['Goles'].sum().reset_index()
    fig_bar = px.bar(df_agrupado, x='Equipo', y='Goles', color='Equipo')
    st.plotly_chart(fig_bar, use_container_width=True)

# --- 6. TABLA DE DATOS ---
st.subheader("Datos Detallados")
st.dataframe(df_filtrado.set_index('Jugador'), use_container_width=True)