import pandas as pd 
def nettoyage_horodatage(df_cdr):
    # Affichier la taille initiale
    print("Taille initial :", df_cdr.shape)
    # Identifier les horodatages du 1er janvier 1970
    cdr_1970 = df_cdr[df_cdr["horodatage"].astype(str).str.startswith("1970-01-01")]
    print("Lignes au 1er janvier 1970 :", len(cdr_1970))
    print(cdr_1970)

    df_nettoye = df_cdr[
        ~df_cdr["horodatage"].astype(str).str.startswith("1970-01-01")].copy()
    print("Taille après nettoyage :", df_nettoye.shape)
    return df_nettoye 
 