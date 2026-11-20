import pandas as pd
import logging
logger = logging.getLogger(__name__) 
def nettoyage_horodatage(df_cdr):
    # Affichier la taille initiale
    logger.info("Horodatage : taille initiale %s", df_cdr.shape)
    # Identifier les horodatages du 1er janvier 1970
    cdr_1970 = df_cdr[df_cdr["horodatage"].astype(str).str.startswith("1970-01-01")]
    logger.info("Horodatage : %d ligne(s) au 1er janvier 1970", len(cdr_1970))
    logger.debug("Aperçu :\n%s", cdr_1970.head(20))

    df_nettoye = df_cdr[
        ~df_cdr["horodatage"].astype(str).str.startswith("1970-01-01")].copy()
    logger.info("Horodatage : taille après nettoyage %s", df_nettoye.shape)
    return df_nettoye 
 