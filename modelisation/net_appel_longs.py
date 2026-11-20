import pandas as pd
import logging
logger = logging.getLogger(__name__)

def nettoyage_appels_longs(df_cdr):

 logger.info("Appels longs : taille initiale %s", df_cdr.shape)

 # Identifier les appels vocaux de plus de 24 heures
 appels_longs = df_cdr[
 (df_cdr["type_service"].str.lower() == "voix")
 & (df_cdr["duree_sec"] > 86400)
 ]
 logger.info("Appels longs : %d appel(s) vocal(aux) de plus de 24 h", len(appels_longs))

 # Supprimer les appels concernés
 df_nettoye = df_cdr.drop(appels_longs.index)

 logger.info("Appels longs : taille après nettoyage %s", df_nettoye.shape)
 # Enregistrer le nouveau fichier
 return df_nettoye 