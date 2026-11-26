import pandas as pd
df = pd.read_csv("../donnee/cdr_complet.csv", parse_dates=["horodatage"])
df["date"] = df["horodatage"].dt.date.astype(str)
df["heure"] = df["horodatage"].dt.hour
df.to_parquet("../airflow/donnees", partition_cols=["date"], engine="pyarrow")


#df_cellules = pd.read_csv("../donnee/cellules.csv")
#df_cellules.to_parquet("sortie/dwh/cellules.parquet", engine="pyarrow")