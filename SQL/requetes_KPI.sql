
-- Requêtes de KPI : 

--  Minutes de voix par zones 
SELECT
    c.zone,
    ROUND(SUM(d.duree_sec) / 60) AS minutes_voix
FROM CDR d
JOIN cellules c ON d.id_cellule = c.id_cellule
WHERE LOWER(d.type_service) IN ('voix')
GROUP BY c.zone
ORDER BY minutes_voix DESC;

-- Volume data par région 
SELECT
    c.region,
    ROUND(SUM(d.volume_mo) / 1024, 2) AS volume_data_go
FROM CDR d
JOIN cellules c ON d.id_cellule = c.id_cellule
WHERE d.type_service IN ('data')
GROUP BY c.region
ORDER BY volume_data_go DESC;

-- Pics Horaire 
SELECT
    HOUR(d.horodatage) AS heure,
    COUNT(*) AS nb_appel
FROM CDR d
GROUP BY HOUR(d.horodatage)
ORDER BY nb_appel DESC;

-- Les 10 premiers abonnées 
SELECT id_abonne, date_activation, forfait, tranche_age
FROM abonnes
ORDER BY date_activation ASC
LIMIT 10;



-- Top 10 des abbonées par consommation 
SELECT
    d.id_abonne,
    ROUND(SUM(d.duree_sec) / 60, 2) AS minutes_voix,
    ROUND(SUM(d.volume_mo), 2)      AS volume_data_mo,
    ROUND(SUM(d.cout_gnf), 2)       AS cout_total_gnf
FROM CDR d
GROUP BY d.id_abonne
ORDER BY cout_total_gnf DESC
-- ORDER BY volume_data_mo DESC
-- ORDER BY minutes_voix DESC
LIMIT 10;


-- Taux d'échec par technologie 
SELECT
    c.technologie,
    COUNT(*) AS nb_total,
    SUM(d.statut IN ('echec')) AS nb_echecs,
    ROUND(100 * SUM(d.statut IN ('echec')) / COUNT(*), 2) AS taux_echec_pct
FROM CDR d
JOIN cellules c ON d.id_cellule = c.id_cellule
GROUP BY c.technologie
ORDER BY taux_echec_pct DESC;

-- Répartition prépayé/ postpayé
SELECT
    a.forfait,
    COUNT(*) AS nb_abonnes,
    ROUND(100 * COUNT(*) / (SELECT COUNT(*) FROM abonnes), 2) AS pourcentage
FROM abonnes a
GROUP BY a.forfait
ORDER BY nb_abonnes DESC;

-- Répartition des abonnés par tranche d’âge 
SELECT
    a.tranche_age,
    COUNT(*) AS nb_abonnes
FROM abonnes a
GROUP BY a.tranche_age
ORDER BY tranche_age;

-- Part du coût d'envoie d'un sms 
SELECT cout_gnf, COUNT(*) AS nb_sms,
    ROUND(100 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS `%` 
    FROM CDR
    WHERE type_service = 'sms' AND direction = 'sortant'
    GROUP BY cout_gnf
    ORDER BY nb_sms DESC;


-- Differents tarif de gnf par mo 
SELECT ROUND(cout_gnf / volume_mo,2) AS gnf_par_mo, COUNT(*) AS nb_lignes
    FROM CDR
    WHERE type_service = 'data' AND volume_mo > 0 AND cout_gnf >= 0
    GROUP BY ROUND(cout_gnf / volume_mo,2)
    ORDER BY nb_lignes DESC;


-- J'ai comparer les données de deux abonnes qui on chaqu'un appeler l'autre au moins une fois mais les deux apppels ne coresponde pas (soit il ya un pbm soit il manque des donnes)


-- Windows fonction VS GROUP BY

-- GROUP BY 
SELECT
    type_service,
    SUM(duree_sec) AS nb_total
FROM CDR 
GROUP BY type_service; 

-- WINDOWS FUNCTION 
SELECT
    id_cdr,
    type_service,
    duree_sec,
    SUM(duree_sec) OVER (
        PARTITION BY type_service
    ) AS total 
FROM CDR 
LIMIT 5; 
-- LAG() va chercher la valeur de la lignes précédantes   

SELECT DATE(horodatage) AS jour,
       COUNT(*) AS trafic,
       COUNT(*) - LAG(COUNT(*)) OVER (ORDER BY DATE(horodatage)) AS evolution
FROM CDR
GROUP BY DATE(horodatage)
ORDER BY jour;

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
