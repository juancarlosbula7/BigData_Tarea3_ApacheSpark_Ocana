# BigData_Tarea3_ApacheSpark_Ocana

# Descripción del proyecto
Este proyecto corresponde a la Tarea 3 del curso Big Data de la Universidad Nacional Abierta y a Distancia (UNAD); se desarrolló una aplicación en Python mediante Apache Spark para procesar registros de vehículos involucrados en siniestros de tránsito en Norte de Santander, con especial atención al municipio de Ocaña.
La aplicación permite cargar un archivo CSV, normalizar las variables, seleccionar los registros del municipio y realizar un análisis exploratorio según el tipo de vehículo y la gravedad del siniestro.

# Fuente de los datos
Los registros provienen del conjunto de datos Vehículos involucrados en un accidente de tránsito – Ley 2251 de 2022, disponible en el Portal Nacional de Datos Abiertos de Colombia.

https://www.datos.gov.co/Transporte/VEHICULOS-INVOLUCRADOS-EN-UN-ACCIDENTE-DE-TRANSITO/6jmc-vaxk

Para la práctica se utilizó una selección de 4.000 registros correspondientes a Norte de Santander, de los cuales 382 pertenecen a Ocaña.

# Herramientas utilizadas

Python 3.12
Apache Spark 3.5.3
PySpark (DataFrames)
Java 17
Ubuntu Server 24.04 LTS

# Instrucciones de ejecución
1. Instalar y configurar Apache Spark con Python y Java.

2. Descargar los registros de Norte de Santander desde la fuente oficial y guardar el archivo como accidentes_norte_santander.csv.

3. Colocar el archivo CSV en la misma carpeta que batch_accidentes.py.

4. Abrir una terminal en esa carpeta y ejecutar:

spark-submit --master local[2] batch_accidentes.py

5. Consultar los resultados en la terminal; la aplicación mostrará los registros cargados, los resultados de limpieza y las estadísticas agrupadas según el tipo de vehículo y la gravedad.

Los registros filtrados de Ocaña se guardan en la carpeta resultados_batch/ocana_limpio.

# Resultados del ejercicio
El procesamiento permitió analizar 4.000 registros de Norte de Santander e identificar 382 correspondientes a Ocaña; entre estos se encontraron 235 registros de motocicletas, 42 de automóviles y 36 de tractocamiones. Según la gravedad, 290 registros se clasificaron como siniestros con heridos y 92 como siniestros con muertos.
Estas cifras corresponden a vehículos involucrados y no representan necesariamente el número de accidentes independientes o de víctimas.

# Autor
Juan Carlos Bula Guadarrama
Universidad Nacional Abierta y a Distancia – UNAD
Curso: Big Data
Tarea 3 – Procesamiento de Datos con Apache Spark
2026
