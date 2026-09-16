import math

def calculer_prix_parking(duree_minute):
    if duree_minute <= 30:
        return 0.0
    jour = duree_minute / 1440
    if duree_minute > 30:
        tranche = duree_minute / 30
        total = math.floor(tranche) * 1.5
        prix_max = math.ceil(jour) * 18
        return min(total, prix_max)
    