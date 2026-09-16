from kata_parking.parking import calculer_prix_parking

def test_30min_stationnement_gratuit():
    duree_minute = 30
    prix = calculer_prix_parking(duree_minute)
    assert prix == 0.0