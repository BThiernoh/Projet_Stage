import pandas as pd

def nettoyage_cellules_vides(df_cdr):

 print("Taille initiale :", df_cdr.shape)

 # Identifier les id_cellule manquants
 nb_nan = df_cdr["id_cellule"].isna().sum()

 print("Total id_cellule vides :", nb_nan)

 # Supprimer les lignes avec id_cellule vide
 df_nettoye = df_cdr.dropna(subset=["id_cellule"])

 print("Taille après nettoyage :", df_nettoye.shape)

 # Enregistrer le nouveau fichier
 return df_nettoye 