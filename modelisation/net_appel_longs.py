import pandas as pd

def nettoyage_appels_longs(df_cdr):

 print("Taille initiale :", df_cdr.shape)

 # Identifier les appels vocaux de plus de 24 heures
 appels_longs = df_cdr[
 (df_cdr["type_service"].str.lower() == "voix")
 & (df_cdr["duree_sec"] > 86400)
 ]
 print("Nombre d'appels de plus de 24 heures :", len(appels_longs))

 # Supprimer les appels concernés
 df_nettoye = df_cdr.drop(appels_longs.index)

 print("Taille après nettoyage :", df_nettoye.shape)

 # Enregistrer le nouveau fichier
 return df_nettoye 