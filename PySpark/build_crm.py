import pandas as pd

# 1. Lire le Parquet du dwh
cdr = pd.read_parquet("sortie/dwh/cdr")

# 2. Colonnes de travail
cdr["echec"] = (cdr["statut"] != "ok").astype(int)
cdr["is_appel"] = (cdr["type_service"] == "voix").astype(int)
cdr["min_voix"] = cdr["duree_sec"].where(cdr["type_service"] == "voix", 0) / 60
cdr["mo_data"] = cdr["volume_mo"].where(cdr["type_service"] == "data", 0)

# 3. Une ligne par abonné
crm = cdr.groupby("id_abonne").agg(
    nb_appels=("is_appel", "sum"),
    minutes_voix=("min_voix", "sum"),
    volume_data_mo=("mo_data", "sum"),
    cout_total=("cout_gnf", "sum"),
    jours_actifs=("date", "nunique"),
    taux_echec=("echec", "mean"),
).round(2).reset_index()

# 4. Sauvegarder
crm.to_parquet("output/crm/crm_abonnes.parquet")

# 5. Vérifier
print(crm.shape, crm["id_abonne"].is_unique)
print(crm.head(10))