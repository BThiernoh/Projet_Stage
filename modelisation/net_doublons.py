# Fonction de nettoyage des doublons
import pandas as pd 
def nettoyage(fichier_source,fichier_destination): 
    df_cdr = pd.read_csv(fichier_source)
    # Affichier la taille initiale
    print("Taille initial :", df_cdr.shape)
    # Identifier les lignes entièrement identiques
    print("Lignes en doubles :")
    print(df_cdr[df_cdr.duplicated()])

    # Supprimer les doublons  
    df_nettoye = df_cdr.drop_duplicates()
    print("Taille après nettoyage :", df_nettoye.shape)

    # Enregistere les données nettoyées
    df_nettoye.to_csv(fichier_destination, index =False)

    print("Fichier nettoyé enregistré :", fichier_destination)

