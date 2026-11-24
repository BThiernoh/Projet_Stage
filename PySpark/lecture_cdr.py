
from pyspark.sql import SparkSession

# Création de Spark
spark = SparkSession.builder \
    .appName("Lecture_CDR") \
    .master("local[*]") \
    .getOrCreate()

# Lecture du fichier CDR
df = spark.read.csv(
    "../donnee/cdr_propre.csv",
    header=True,
    inferSchema=True
)

# Afficher les données
df.show(10)

# Afficher la structure
df.printSchema()

# Compter toutes les lignes
print("Nombre total de CDR :", df.count())

# Arrêter Spark
spark.stop()
