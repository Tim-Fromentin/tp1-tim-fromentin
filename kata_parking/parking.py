import math

def calculer_prix_parking(duree_minute=0, vehicule="voiture", heure_entree=None, heure_sortie=None, abonnement=False):
    if duree_minute > 4320:
        return 250.00
    if heure_entree and heure_sortie and heure_entree > heure_sortie:
        return "Attention, une erreur s'est produite concernant votre heure de sortie."
    min_gratuite = 30
    if vehicule == "camion éléctrique" or abonnement == True:
        min_gratuite = 60
    if duree_minute <= min_gratuite:
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