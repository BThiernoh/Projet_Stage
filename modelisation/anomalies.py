
import pandas as pd


df_cdr = pd.read_csv("../donnee/cdr_complet.csv")
df_ab = pd.read_csv("../donnee/abonnes.csv")
df_cel = pd.read_csv("../donnee/cellules.csv")

# Determiner le nombre de doublons 
nb_doublons = df_cdr.duplicated().sum()
print("Le nombre de lignes doubles  :", nb_doublons)

# Determiner le nombre d'id_abonne orphelin
orphelins = df_cdr[
    df_cdr["id_abonne"].notna()
    & ~df_cdr["id_abonne"].isin(df_ab["id_abonne"])
]
# 2. Résultats
print("Lignes CDR orphelines        :", len(orphelins))

# Determiner les lignes avec un id_cellules vide 
# Valeurs manquantes (NaN / None)
nb_nan = df_cdr["id_cellule"].isna().sum()

print("Total id_cellule vides        :", nb_nan)

# Determiner les appels > 1 jours 
appels_longs = df_cdr[
    (df_cdr["type_service"] == "voix")      # adapte à ta valeur
    & (df_cdr["duree_sec"] > 86400)
]

print(len(appels_longs))
print(appels_longs.sort_values("duree_sec", ascending=False))

# Detrminer les volumes de data négatifs 
data_neg = df_cdr[
    (df_cdr["type_service"] == "data")     
    & (df_cdr["volume_mo"] < 0)
]

print(len(data_neg))
print(data_neg.sort_values("volume_mo").head())


# Horodatage du 1er janvier 1970 
cdr_1970 = df_cdr[df_cdr["horodatage"].str.startswith("1970-01-01")] #startswith :True si elle commance par ("...")

print("Lignes au 1er janvier 1970 :", len(cdr_1970))
print(cdr_1970)