import pandas as pd

# 1. Lire le CDR et les cellules (dwh)
cdr = pd.read_parquet("sortie/dwh/cdr")
cellules = pd.read_csv("../donnee/cellules.csv")   # id_cellule, zone

# 2. Ajouter la zone et la colonne d'échec
cdr = cdr.merge(cellules[["id_cellule", "zone"]], on="id_cellule", how="left")
cdr["echec"] = (cdr["statut"] != "ok").astype(int)

# 3. Trafic par service : une colonne par service
trafic = cdr.pivot_table(
    index=["zone", "date", "heure"],
    columns="type_service",
    values="id_cdr",
    aggfunc="count",
    fill_value=0,
).add_prefix("nb_").reset_index()

# 4. Taux d'échec par zone, jour, heure
echec = (cdr.groupby(["zone", "date", "heure"])["echec"]
            .mean().round(4).rename("taux_echec").reset_index())

# 5. Assembler
dtm = trafic.merge(echec, on=["zone", "date", "heure"])

# 6. Sauvegarder dans la couche dtm
dtm.to_parquet("output/dtm/dtm_zone_heure.parquet")

# 7. Vérifier
print(dtm.shape, dtm.duplicated(["zone", "date", "heure"]).sum() == 0)
print("Zones manquantes :", cdr["zone"].isna().sum())
print(dtm.head(10))