# ⚾️ Streamlit Baseball Dashboard

Un proyecto de ejemplo que utiliza la **API de Béisbol** (`API-Baseball`) para obtener datos y los visualiza a través de un **Dashboard interactivo** creado con **Streamlit** en Python.

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
    * Crea un archivo llamado `.streamlit/secrets.toml` y agrega tu clave API.
    * **Alternativa simple (para pruebas)**: Exporta tu clave API como una variable de entorno llamada $\text{API\_KEY}$.

---

## 🚀 Cómo Funciona

El proyecto consta de dos componentes principales:

### 1. Obtención de Datos (API-Baseball)

* Utilizamos la librería **`requests`** para hacer llamadas $\text{HTTP}$ a los $\text{endpoints}$ de la $\text{API-Baseball}$.
* La $\text{API}$ proporciona datos en formato **$\text{JSON}$** sobre estadísticas de equipos, jugadores, partidos en vivo, etc.
* En este proyecto, un ejemplo de la lógica sería obtener las estadísticas de la temporada actual para un equipo seleccionado.

### 2. Visualización (Streamlit)

* **Streamlit** es un framework de Python que convierte scripts de datos en **aplicaciones web interactivas** con solo unas pocas líneas de código.
* Los datos obtenidos de la $\text{API}$ se cargan en un $\text{DataFrame}$ de **Pandas**.
* **Elementos clave utilizados**:
    * **`st.selectbox`**: Para seleccionar el equipo o la temporada.
    * **`st.dataframe`**: Para mostrar las tablas de estadísticas.
    * **`st.bar_chart` / `st.line_chart`**: Para crear visualizaciones de datos (ej. carreras anotadas vs. permitidas).

---

## 💻 Uso

Para ejecutar la aplicación, navega hasta el directorio raíz del proyecto en la terminal y ejecuta el siguiente comando:

```bash
streamlit run app.py  
