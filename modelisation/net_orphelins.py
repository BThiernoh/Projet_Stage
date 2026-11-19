import pandas as pd

def nettoyage_orphelins(fichier_cdr, fichier_abonne, fichier_destination):

 # Lire les fichiers CDR et abonnés
 df_cdr = pd.read_csv(fichier_cdr)
 df_ab = pd.read_csv(fichier_abonne)

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
 df_nettoye.to_csv(fichier_destination, index=False)

 print("Fichier nettoyé enregistré :", fichier_destination)