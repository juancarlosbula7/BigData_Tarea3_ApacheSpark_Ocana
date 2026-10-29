
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Iniciar Apache Spark
spark = SparkSession.builder \
    .appName("Accidentes_Ocana_Batch") \
    .master("local[2]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Cargar el conjunto de datos
df = spark.read.csv(
    "accidentes_norte_santander.csv",
    header=True,
    inferSchema=True
)

print("\nTOTAL DE REGISTROS")
print(df.count())

print("\nESTRUCTURA DEL CONJUNTO DE DATOS")
df.printSchema()

print("\nPRIMEROS CINCO REGISTROS")
df.select(
    "tipo_vehiculo",
    "fecha_accidente",
    "gravedad_accidente",
    "municipio_accidente"
).show(5, truncate=False)

# Limpieza y normalizacion
df_limpio = df \
    .withColumn(
        "municipio_accidente",
        F.upper(F.trim(F.col("municipio_accidente")))
    ) \
    .withColumn(
        "tipo_vehiculo",
        F.upper(F.trim(F.col("tipo_vehiculo")))
    ) \
    .withColumn(
        "gravedad_accidente",
        F.upper(F.trim(F.col("gravedad_accidente")))
    )

df_limpio = df_limpio.filter(
    F.col("municipio_accidente").isNotNull() &
    (F.col("municipio_accidente") != "")
)

# Seleccionar los registros de Ocana
df_ocana = df_limpio.filter(
    F.col("municipio_accidente") == "OCAÑA"
)

print("\nRESULTADOS DE LIMPIEZA")
print("Registros originales:", df.count())
print("Registros limpios:", df_limpio.count())
print("Registros de Ocaña:", df_ocana.count())

# Analisis exploratorio
print("\nVEHICULOS INVOLUCRADOS EN OCAÑA")
df_ocana.groupBy("tipo_vehiculo") \
    .count() \
    .orderBy(F.desc("count")) \
    .show(20, truncate=False)

print("\nGRAVEDAD DE LOS SINIESTROS")
df_ocana.groupBy("gravedad_accidente") \
    .count() \
    .orderBy(F.desc("count")) \
    .show(truncate=False)

# Guardar los resultados del procesamiento
df_ocana.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("resultados_batch/ocana_limpio")

spark.stop()

