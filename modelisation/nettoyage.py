# Programme principal : doublons -> horodatage -> orphelins
# -> cellules vides -> appels longs -> volumes négatifs
import pandas as pd
import logging
logger = logging.getLogger(__name__)

from journal import configurer_journal
from net_doublons import nettoyage_doublons
from net_horodatage import nettoyage_horodatage
from net_orphelins import nettoyage_orphelins
from net_cellules_vides import nettoyage_cellules_vides
from net_appel_longs import nettoyage_appels_longs
from net_volumes_negatifs import nettoyage_volumes


def nettoyage(fichier_cdr, fichier_destination):
    df = pd.read_csv(fichier_cdr)
    logger.info("Fichier chargé : %s %s", fichier_cdr, df.shape)

    df = nettoyage_doublons(df)         # 1. doublons
    df = nettoyage_horodatage(df)       # 2. horodatage 1970
    df = nettoyage_orphelins(df)        # 3. orphelins
    df = nettoyage_cellules_vides(df)   # 4. cellules vides
    df = nettoyage_appels_longs(df)     # 5. appels longs
    df = nettoyage_volumes(df)          # 6. volumes négatifs

    print("\nTaille finale :", df.shape)
    if fichier_destination:
        df.to_csv(fichier_destination, index=False)
        logger.info("Fichier final enregistré : %s", fichier_destination)
    return df

