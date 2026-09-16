from datetime import datetime
from parking import calculer_prix_parking

def test_30min_stationnement_gratuit():
    duree_minute = 30
    prix = calculer_prix_parking(duree_minute)
    assert prix == 0.0

def test_tout_demi_heure_facturee_1_50():
    duree_minute = 31
    prix = calculer_prix_parking(duree_minute)
    assert prix == 1.50

def test_maximum_18_euro_par_tranche_24h():
    duree_minute = 480
    prix = calculer_prix_parking(duree_minute)
    assert prix == 18

def test_remise_camion_60pourcent():
    duree_minute = 480
    vehicule = "camion"
    prix = calculer_prix_parking(duree_minute, vehicule)
    assert prix == 10.80

def test_camion_electrique_60min_gratuit():
    duree_minute = 60
    vehicule = "camion"
    prix = calculer_prix_parking(duree_minute, vehicule)
    assert prix == 0.00

def test_heure_sortie_anterieure_heure_entree():
    duree_minute = 60
    heure_entree = datetime(2026, 9, 16, 14, 30, 0)
    heure_sortie = datetime(2026, 9, 16, 13, 30, 0)
    alerte = calculer_prix_parking(
        duree_minute, heure_entree=heure_entree, heure_sortie=heure_sortie
    )
    assert alerte == "Attention, une erreur s'est produite concernant votre heure de sortie."

