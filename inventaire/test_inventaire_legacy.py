from inventaire import val, alerte

ARTICLES = [
    {"ref": "VIS-M6", "lib": "Vis M6 acier", "q": 2, "pu": 0.15, "seuil": 20, "cat": "piece"},
    {"ref": "PERC-18", "lib": "Perceuse 18V", "q": 10, "pu": 1, "seuil": 3, "cat": "outil"},
]

def test_val():
    resultat = val(ARTICLES)
    assert resultat == 10.30

def test_alerte():
    resultatAlerte = alerte(ARTICLES)
    assert resultatAlerte == ["VIS-M6"]
