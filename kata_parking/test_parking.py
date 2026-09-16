from parking import calculer_prix_parking

def test_30min_stationnement_gratuit():
    duree_minute = 30
    prix = calculer_prix_parking(duree_minute)
    assert prix == 0.0

def test_tout_demi_heure_facturee_1_50():
    duree_minute = 31
    prix = calculer_prix_parking(duree_minute)
    assert prix == 1.50