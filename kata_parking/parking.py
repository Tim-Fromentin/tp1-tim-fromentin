import math
from datetime import datetime


def calculer_duree_minutes(
    duree_minute: int, heure_entree: datetime, heure_sortie: datetime
) -> int:
    if not duree_minute and heure_entree and heure_sortie:
        difference = heure_sortie - heure_entree
        return int(difference.total_seconds() / 60)
    return duree_minute


def obtenir_minutes_gratuites(vehicule: str, abonnement: bool) -> int:
    if vehicule == "camion éléctrique" or abonnement:
        return 60
    return 30


def calculer_tarif_base(duree_minute: int) -> float:
    jour = duree_minute / 1440
    tranche = math.ceil((duree_minute - 30) / 30)
    total = tranche * 1.5
    prix_max = math.ceil(jour) * 18
    return min(total, prix_max)


def calculer_prix_parking(
    duree_minute=0,
    vehicule="voiture",
    heure_entree=None,
    heure_sortie=None,
    abonnement=False,
):
    duree_minute = calculer_duree_minutes(duree_minute, heure_entree, heure_sortie)

    if heure_entree and heure_sortie and heure_entree > heure_sortie:
        return "Attention, une erreur s'est produite concernant votre heure de sortie."
    if duree_minute > 4320:
        return 250.00

    min_gratuite = obtenir_minutes_gratuites(vehicule, abonnement)
    if duree_minute <= min_gratuite:
        return 0.0

    res = calculer_tarif_base(duree_minute)
    if vehicule == "camion":
        res *= 0.60

    return round(res, 2)
