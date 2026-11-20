# Fonction de nettoyage des doublons
import pandas as pd 
import logging
logger = logging.getLogger(__name__)
def nettoyage_doublons(df_cdr): 
    # Affichier la taille initiale
    logger.info("Doublons : taille initiale %s", df_cdr.shape) # Remplacement du print() pour la journalisation
    # Identifier les lignes entièrement identiques
    logger.info("Doublons : %d ligne(s) en double", df_cdr.duplicated().sum())
    logger.debug("Aperçu :\n%s", df_cdr[df_cdr.duplicated()].head(20))

    # Supprimer les doublons  
    df_nettoye = df_cdr.drop_duplicates()
    logger.info("Doublons : taille après nettoyage %s", df_nettoye.shape)

    # Enregistere les données nettoyées
    return df_nettoye
