# ⚾️ Streamlit Baseball Dashboard

Un proyecto de ejemplo que utiliza la **API de Béisbol** (`API-Baseball`) para obtener datos y los visualiza a través de un **Dashboard interactivo** creado con **Streamlit** en Python.


[LINK DE API-SPORTS(API-BASEBALL)](https://dashboard.api-football.com/register)

[API-BASEBALL DOCUMENTACIÓN](https://api-sports.io/documentation/baseball/v1#tag/Teams)

---

## 🛠️ Requisitos e Instalación

### Requisitos

Asegúrate de tener instalado **Python** (versión 3.8 o superior) y una **clave API** válida de $\text{API-Baseball}$.

### Instalación

1.  **Clonar el repositorio** (si aplica):
    ```bash
    git clone https://github.com/edoruin/API_BASEBALL_FOLLOWING
    cd API_BASEBALL_FOLLOWING
    ```

2.  **Crear y activar un entorno virtual** (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    .\venv\Scripts\activate   # En Windows
    ```

3.  **Instalar las dependencias de Python**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar la clave API**:
    * Crea un archivo llamado `secrets.toml` en el directorio raiz del proyecto y agrega tu clave API, dentro:

    * template de archivo .toml:
        ```python
        # config.toml

        # La clave API se guarda dentro de una sección [api]. 
        

        [api] #seccion de apis
        clave_secreta = "TU=SECRET"


        #URL base de la pagina(version1) MANTENER IGUAL
        base_url = "https://v1.baseball.api-sports.io"

        ```

---

## 🚀 Cómo Funciona

El proyecto consta de dos componentes principales:

### 1. Obtención de Datos (ETL.py)

* Utilizamos la librería **`requests`** para hacer llamadas $\text{HTTP}$ a los $\text{endpoints}$ de la $\text{API-Baseball}$.
* La $\text{API}$ proporciona datos en formato **$\text{JSON}$** sobre estadísticas de equipos, jugadores, partidos en vivo, etc.
* En este proyecto, un ejemplo de la lógica sería obtener las estadísticas de la temporada actual para un equipo seleccionado, utilizamos tres funciones principales apoyadas de dos secundarias:  Obtener_juegos y Comparar_equipo y Estadisticas.

### 2. Visualización (App.py)

* **Streamlit** es un framework de Python que convierte scripts de datos en **aplicaciones web interactivas** con solo unas pocas líneas de código.
* Los datos obtenidos de la $\text{API}$ se cargan en un $\text{DataFrame}$ de **Pandas** en ETL.py y son utilizados en app.py


---

## 💻 Uso

Para ejecutar la aplicación, navega hasta el directorio raíz del proyecto en la terminal y ejecuta el siguiente comando:

```bash
streamlit run app.py  
