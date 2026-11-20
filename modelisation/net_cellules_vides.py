import pandas as pd
import logging
logger = logging.getLogger(__name__)

def nettoyage_cellules_vides(df_cdr):

 logger.info("Cellules vides : taille initiale %s", df_cdr.shape)

 # Identifier les id_cellule manquants
 nb_nan = df_cdr["id_cellule"].isna().sum()

 logger.info("Cellules vides : %d id_cellule manquant(s)", nb_nan)
 # Supprimer les lignes avec id_cellule vide
 df_nettoye = df_cdr.dropna(subset=["id_cellule"])

 logger.info("Cellules vides : taille après nettoyage %s", df_nettoye.shape)
 # Enregistrer le nouveau fichier
 return df_nettoye 