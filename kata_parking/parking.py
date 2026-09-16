import math

def calculer_prix_parking(duree_minute):
    if duree_minute <= 30:
        return 0.0
    if duree_minute > 30:
        tranche = duree_minute / 30
        return math.floor(tranche) * 1.5