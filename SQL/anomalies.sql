-- REPERER LES ANOMALIES:

-- Doublons avec le même id_cdr 
SELECT id_cdr, COUNT(*) AS nb
FROM CDR
GROUP BY id_cdr
HAVING COUNT(*) > 1
ORDER BY nb DESC;

-- Trouver toute les lignes ou l'horotatage est mauvais 
SELECT * FROM CDR WHERE horodatage = '1970-01-01';

-- Reperer les lignes avec des abonnées inconnue 
SELECT d.*
FROM CDR d
LEFT JOIN abonnes a ON d.id_abonne = a.id_abonne
WHERE a.id_abonne IS NULL

-- Cellules manquantes 
SELECT COUNT(*) AS nb_cellules_vides
FROM CDR
WHERE id_cellule IS NULL
   OR TRIM(id_cellule) = ''
   
-- Durée d'appel superieure à 3 heures 
SELECT *
FROM CDR
WHERE duree_sec > 10800
ORDER BY duree_sec DESC;

-- Au moins 1 valeurs du tableau est négative
SELECT *
FROM CDR
WHERE duree_sec < 0 OR volume_mo < 0 OR cout_gnf < 0
LIMIT 100
