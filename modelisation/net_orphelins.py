import pandas as pd

def nettoyage_orphelins(df_cdr):

 # Lire le fichier abonnés
 df_ab = pd.read_csv("../donnee/abonnes.csv")

 print("Taille initiale :", df_cdr.shape)

 # Identifier les id_abonne orphelins
 orphelins = df_cdr[
 df_cdr["id_abonne"].notna()
 & ~df_cdr["id_abonne"].isin(df_ab["id_abonne"])
 ]

 print("Lignes CDR orphelines :", len(orphelins))
 print(orphelins)

 # Supprimer les lignes orphelines
 df_nettoye = df_cdr.drop(orphelins.index)

 print("Taille après nettoyage :", df_nettoye.shape)

 # Enregistrer le nouveau fichier
 return df_nettoye 