import math

def calculer_prix_parking(duree_minute, vehicule="voiture"):
    if duree_minute <= 30:
        return 0.0
    jour = duree_minute / 1440
    if duree_minute > 30:
        tranche = math.ceil((duree_minute - 30) / 30)
        total = tranche * 1.5
        prix_max = math.ceil(jour) * 18
        res = min(total, prix_max)
        if vehicule == "camion":
            res = res * 0.60
        return round(res, 2)