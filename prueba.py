import ETL


data = ETL.Obtener_juegos(2024)


stadisticas = ETL.Estadisticas(data)

print(stadisticas[0])