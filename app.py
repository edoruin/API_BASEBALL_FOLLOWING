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

st.title("Bienvenido a LIDOM Stats Dashboard⚾️⚾️⚾️")


st.header("Obtener Juegos por Año")
st.markdown("Introduce el año que quieres analizar")


# Argumento de juegos, del usuario
año_seleccionado = st.number_input(
    "Año de los juegos a buscar",
    min_value=0,
    max_value=3000,
    value=None, # Por defecto busca todos
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

st.markdown("---")
st.markdown("---")

opciones_equipos = [ #para los menus desplegables
    '--seleccionar--',
    'Aguilas Cibaenas',
    'Estrellas Orientales',
    'Tigres del Licey',
    'Toros del Este',
    'Leones del Escogido',
    'Gigantes del Cibao'
]

st.header("Compara tus equipos")
st.markdown("Seleccione equipo y temporada")

col1, col2 = st.columns(2)


st.header("Datos del primer equipo")
año_seleccionado = st.number_input(
"temporada del equipo 1",
min_value=0,
max_value=3000,
value=None, # Por defecto busca todos
step=1)

equipo_box = st.selectbox(
    'seleccionar equipo1',
    opciones_equipos
)

st.header("Datos del segundo equipo")
año_seleccionado2 = st.number_input(
"temporada del equipo 2",
min_value=0,
max_value=3000,
value=None, # Por defecto busca todos
step=1)

equipo_box2 = st.selectbox(
    'Selecciona equipo2',
    opciones_equipos
)


if st.button("Comparar"): # Logica para añadir el resultado que usuario introduzca
    if (año_seleccionado > 0 and equipo_box is not None 
        and año_seleccionado2 > 0 and equipo_box2 is not None):
        st.success("¡Petición completada!")
        st.subheader(f"Buscando la temporada {año_seleccionado} del {equipo_box}")
        equipo_selected = ETL.Comparar_equipo(temporada=int(año_seleccionado),equipo=str(equipo_box))
        equipo_selected2 = ETL.Comparar_equipo(temporada=int(año_seleccionado2),equipo=str(equipo_box2))


        col1,col2 = st.columns(2)
        with col1:
            #equipo graficos comparativos
            logo = equipo_selected['teams.home.logo'].unique()            #equipo 1
            name = equipo_selected['teams.home.name'].unique()
            st.image(logo[0],caption=name,width=200)

            #grafico estrella
            Statistics = ETL.Estadisticas(equipo_selected)
            estadisticas = pd.DataFrame({
                    'Estadística': ['Hits','Carreras','Errores defensivos'],
                    'Valor': [Statistics[0],Statistics[1],Statistics[2]]
                })
            
            fig = px.line_polar(
                    estadisticas, 
                    r='Valor',
                    theta='Estadística',
                    line_close=True,
                    title=f"Rendimiento de {name[0]} en Estadísticas Clave",
                    # Configuración de apariencia y rango directamente aquí:
                    range_r=[0, 100]  # Configura el rango radial (equivalente a range=[0, 5])
            )

            # 2. Aplicar el estilo del polígono (fill y color)
            fig.update_traces(fill='toself', line_color='blue')

            # 3. Mostrar el gráfico en Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            logo2 = equipo_selected2['teams.home.logo'].unique()            #equipo 2
            name2 = equipo_selected2['teams.home.name'].unique()
            st.image(logo2[0],caption=name2,width=200)

    else:
        st.warning(f"En {name} no existe la temporada{año_seleccionado}")
        st.warning(f"En {name2} no existe la temporada{año_seleccionado2}")





