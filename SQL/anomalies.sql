-- REPERER LES ANOMALIES:

-- Trouver toute les lignes ou l'horotatage est mauvais 
SELECT * FROM CDR WHERE horodatage < '2026-09-01 00:00:01' OR horodatage > '2026-10-01 00:00:01';

-- Reperer les lignes avec des abonnées inconnue 
SELECT d.*
FROM CDR d
LEFT JOIN abonnes a ON d.id_abonne = a.id_abonne
WHERE a.id_abonne IS NULL

-- Durée d'appel superieure à 3 heures 
SELECT *
FROM CDR
WHERE duree_sec > 10800
ORDER BY duree_sec DESC;

-- Au moins 1 valeurs du tableau est négative
SELECT *
FROM CDR
WHERE duree_sec < 0 OR volume_mo < 0 OR cout_gnf < 0
LIMIT 100;
