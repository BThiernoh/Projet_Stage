import pandas as pd

def nettoyage_volumes(df_cdr, fichier_destination):

    # Lire le fichier CDR

    print("Taille initiale :", df_cdr.shape)

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
    print("Volumes négatifs détectés :", len(negatifs))
    print("Volumes corrigés :", len(coherents))
    print("Volumes supprimés :", len(non_fiables))
    print("Taille après nettoyage :", df_nettoye.shape)

    # Enregistrer le fichier nettoyé
    df_nettoye.to_csv(fichier_destination, index=False)

    print("Fichier final_nettoyé enregistré :", fichier_destination)
    return df_nettoye