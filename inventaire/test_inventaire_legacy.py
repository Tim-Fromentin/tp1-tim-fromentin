from datetime import datetime
from inventaire import valeur_stocks_global, alerte_de_stocks, mouvement_stock, cout_reapprovisionnement, classer_stocks, rotation_stocks, rapport

ARTICLES = [
    {"ref": "VIS-M6", "lib": "Vis M6 acier", "q": 2, "pu": 0.15, "seuil": 20, "cat": "piece"},
    {"ref": "PERC-18", "lib": "Perceuse 18V", "q": 10, "pu": 1, "seuil": 3, "cat": "outil"},
]

def test_valeur_stocks_global():
    resultat = valeur_stocks_global(ARTICLES)
    assert resultat == 10.30

def test_alerte():
    resultatAlerte = alerte_de_stocks(ARTICLES)
    assert resultatAlerte == ["VIS-M6"]

def test_entree_sortie(): 
   estCeQueLeStockEstInsuffisant = mouvement_stock(ARTICLES[0], quantite=5)
   assert estCeQueLeStockEstInsuffisant == False
   
def test_entree_sortie_negatif(): 
   estCeQueLeStockEstInsuffisant = mouvement_stock(ARTICLES[0], quantite=-5)
   assert estCeQueLeStockEstInsuffisant == False

def test_cout_reapprovisionnement():
    cout = cout_reapprovisionnement(ARTICLES[0])
    assert cout == 9.45

def test_classement_des_stocks():
    classement = classer_stocks(ARTICLES)
    
    assert classement == [
        {'ref': 'PERC-18', 'lib': 'Perceuse 18V', 'q': 10, 'pu': 1, 'seuil': 3, 'cat': 'outil'},
        {'ref': 'VIS-M6', 'lib': 'Vis M6 acier', 'q': -3, 'pu': 0.15, 'seuil': 20, 'cat': 'piece'}
    ]

def test_stock_jours_restant():
    jours_restant = rotation_stocks(ARTICLES[1], 30)
    assert jours_restant == 10

def test_rapport_mensuel():
    date_fixe = datetime(2026, 1, 1)
    articles = [
        {"ref": "VIS-M6", "lib": "Vis M6 acier", "q": 2, "pu": 0.15, "seuil": 20, "cat": "piece"}
    ]

    resultat = rapport(articles, d=date_fixe)
    assert resultat == {
        "date": "2026-01-01 00:00:00",
        "valeur": 0.3,
        "nb": 1,
        "alertes": ["VIS-M6"],
        "ttc": 0.36,
    }