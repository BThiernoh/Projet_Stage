import pandas as pd
import logging
logger = logging.getLogger(__name__)

def nettoyage_orphelins(df_cdr):

 # Lire le fichier abonnés
 df_ab = pd.read_csv("../donnee/abonnes.csv")

 logger.info("Orphelins : taille initiale %s", df_cdr.shape)

 # Identifier les id_abonne orphelins
 orphelins = df_cdr[
 df_cdr["id_abonne"].notna()
 & ~df_cdr["id_abonne"].isin(df_ab["id_abonne"])
 ]

 logger.info("Orphelins : %d ligne(s) CDR orpheline(s)", len(orphelins))
 logger.debug("Aperçu :\n%s", orphelins.head(20))

 # Supprimer les lignes orphelines
 df_nettoye = df_cdr.drop(orphelins.index)

 logger.info("Orphelins : taille après nettoyage %s", df_nettoye.shape)

 # Enregistrer le nouveau fichier
 return df_nettoye 