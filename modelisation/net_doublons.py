# Fonction de nettoyage des doublons
import pandas as pd 
def nettoyage_doublons(df_cdr): 
    # Affichier la taille initiale
    print("Taille initial :", df_cdr.shape)
    # Identifier les lignes entièrement identiques
    print("Lignes en doubles :")
    print(df_cdr[df_cdr.duplicated()])

    # Supprimer les doublons  
    df_nettoye = df_cdr.drop_duplicates()
    print("Taille après nettoyage :", df_nettoye.shape)

    # Enregistere les données nettoyées
    return df_nettoye
