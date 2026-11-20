import pandas as pd
import logging
logger = logging.getLogger(__name__)

def nettoyage_volumes(df_cdr):

    # Lire le fichier CDR

    logger.info("Volumes : taille initiale %s", df_cdr.shape)
    # Calculer la médiane des coûts pour chaque volume positif
    references = (
    df_cdr[df_cdr["volume_mo"] > 0]
    .groupby("volume_mo")["cout_gnf"]
    .median()
    )

    # Identifier les volumes négatifs
    negatifs = df_cdr[df_cdr["volume_mo"] < 0].copy()

    # Associer chaque volume négatif à la médiane de son volume absolu
    negatifs["mediane"] = (
    negatifs["volume_mo"].abs().map(references)
    )

    # Garder uniquement les lignes dont le coût est égal à la médiane
    coherents = negatifs[
    negatifs["cout_gnf"] == negatifs["mediane"]
    ]

    # Identifier les lignes à supprimer
    non_fiables = negatifs[(
    negatifs["cout_gnf"] != negatifs["mediane"])
    | (negatifs["mediane"].isna())
    ]

    # Supprimer les lignes non fiables
    df_nettoye = df_cdr.drop(
    index=non_fiables.index
    ).copy()

    # Corriger le signe des volumes conservés
    df_nettoye.loc[coherents.index, "volume_mo"] = (
    df_nettoye.loc[coherents.index, "volume_mo"].abs()
    )

    # Afficher le bilan
    logger.info("Volumes : %d négatif(s) détecté(s)", len(negatifs))
    logger.info("Volumes : %d corrigé(s)", len(coherents))
    logger.warning("Volumes : %d ligne(s) non fiable(s) supprimée(s)", len(non_fiables))
    logger.info("Volumes : taille après nettoyage %s", df_nettoye.shape)

    # Enregistrer le fichier nettoyé
    return df_nettoye