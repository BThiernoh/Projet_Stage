
-- TABLE 1: CELLULES
CREATE TABLE Cellules(
 id_cellules VARCHAR(20),
 nom_zone VARCHAR(100),
 region VARCHAR(100),
 type_zone VARCHAR(20),
 techologie VARCHAR(20),
 latitude DECIMAL(9,6),
 longitude DECIMAL(9,6),
 PRIMARY KEY (id_cellules)
)
-- TABLE 2: ABONNES
CREATE TABLE abonnes(
 id_abonne INT,
 date_activation DATE,
 forfait VARCHAR(30),
 appareil VARCHAR(30),
 tranche_age VARCHAR(20),
 zone_residence VARCHAR(100),
 region_residence VARCHAR(100),
 id_cellule_domicile VARCHAR(20),
 PRIMARY KEY (id_abonne),
 id_cellules VARCHAR(20) 
 REFERENCES Cellules(id_cellules)
)
-- TABLE 3: CDR

CREATE TABLE CDR(
  id_cdr INT,
  id_abonne INT REFERENCES abonnes(id_abonne),
  horodatage DATETIME,
  type_service VARCHAR(30),
  direction VARCHAR(30),
  duree_sec INT,
  volume_mo DECIMAL(10,2),
  id_cellule VARCHAR(20) REFERENCES cellules(id_cellule),
  id_correspondant INT,
  statut VARCHAR(30),
  cout_gnf DECIMAL(12,2),
  PRIMARY KEY (id_cdr)
)
