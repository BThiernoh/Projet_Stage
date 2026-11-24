import time
import pandas as pd
from pyspark.sql import SparkSession, functions as F

CSV = "../donnee/cdr_propre.csv"
PARQUET = "sortie/dwh/cdr"

def chrono(f, n=3):
    temps = []
    for _ in range(n):
        t = time.perf_counter()
        f()
        temps.append(time.perf_counter() - t)
    return min(temps)

spark = SparkSession.builder.appName("benchmark").getOrCreate()

def pandas_csv():
    df = pd.read_csv(CSV, parse_dates=["horodatage"])
    df["date"] = df["horodatage"].dt.date.astype(str)
    df["echec"] = (df["statut"] != "reussi").astype(int)
    return df.groupby(["id_abonne", "id_cellule", "date"]).agg(
        nb=("id_cdr", "count"),
        duree=("duree_sec", "sum"),
        data_mo=("volume_mo", "sum"),
        cout=("cout_gnf", "sum"),
        taux_echec=("echec", "mean"),
        nb_services=("type_service", "nunique"),
    )

t1 = chrono(pandas_csv)


def pandas_parquet():
    df = pd.read_parquet(PARQUET)
    df["echec"] = (df["statut"] != "reussi").astype(int)
    return df.groupby(["id_abonne", "id_cellule", "date"]).agg(
        nb=("id_cdr", "count"),
        duree=("duree_sec", "sum"),
        data_mo=("volume_mo", "sum"),
        cout=("cout_gnf", "sum"),
        taux_echec=("echec", "mean"),
        nb_services=("type_service", "nunique"),
    )

t2 = chrono(pandas_parquet)

def spark_csv():
    df = spark.read.csv(CSV, header=True, inferSchema=True)
    df = (df.withColumn("date", F.to_date("horodatage"))
            .withColumn("echec", (F.col("statut") != "reussi").cast("int")))
    return df.groupBy("id_abonne", "id_cellule", "date").agg(
        F.count("id_cdr").alias("nb"),
        F.sum("duree_sec").alias("duree"),
        F.sum("volume_mo").alias("data_mo"),
        F.sum("cout_gnf").alias("cout"),
        F.avg("echec").alias("taux_echec"),
        F.countDistinct("type_service").alias("nb_services"),
    ).count()          # .count() force l'exécution

t3 = chrono(spark_csv)

def spark_parquet():
    df = spark.read.parquet(PARQUET)
    df = df.withColumn("echec", (F.col("statut") != "reussi").cast("int"))
    return df.groupBy("id_abonne", "id_cellule", "date").agg(
        F.count("id_cdr").alias("nb"),
        F.sum("duree_sec").alias("duree"),
        F.sum("volume_mo").alias("data_mo"),
        F.sum("cout_gnf").alias("cout"),
        F.avg("echec").alias("taux_echec"),
        F.countDistinct("type_service").alias("nb_services"),
    ).count()

t4 = chrono(spark_parquet)


tableau = pd.DataFrame({
    "Outil":     ["pandas", "pandas", "Spark", "Spark"],
    "Format":    ["CSV", "Parquet", "CSV", "Parquet"],
    "Temps (s)": [t1, t2, t3, t4],
}).round(2)
print(tableau)