# -*- coding: utf-8 -*-
# gestion de stock entrepot nord - v4
# repris de la v3 de Kevin, TODO refactorer un jour
# NE PAS TOUCHER A mouv() SANS PREVENIR L'EQUIPE LOGISTIQUE
import datetime
import json
import math
import random

TVA = 0.2
S = 3
R = 0.1
Q = 100
JOURNAL = []
DERNIER = 0


def valeur_stocks_global(articles):
    total = 0
    for article in articles:
        if article["q"] > 0:
            total = total + article["q"] * article["pu"]
        else:
            total = total + 0
    return round(total, 2)


def alerte_de_stocks(articles):
    article_en_alerte = []
    for article in articles:
        if article["q"] < article["seuil"]:
            article_en_alerte.append(article["ref"])
    return article_en_alerte


def mouvement_stock(article, quantite, t="out", j=[], force=False, log=True):
    global DERNIER
    if quantite <= 0:
        if log:
            print("quantite invalide : " + str(quantite))
        return False
    if t == "out":
        article["q"] = article["q"] - quantite
        if article["q"] < 0:
            if force == False:
                if log:
                    print("stock insuffisant pour " + article["ref"])
                return False
    elif t == "in":
        article["q"] = article["q"] + quantite
    else:
        if log:
            print("type de mouvement inconnu : " + str(t))
        return False
    DERNIER = DERNIER + 1
    j.append({"id": DERNIER, "ref": article["ref"], "q": quantite, "t": t})
    JOURNAL.append({"id": DERNIER, "ref": article["ref"], "q": quantite, "t": t})
    return True


def cout_reapprovisionnement(articles):
    if articles["q"] < articles["seuil"]:
        n = articles["seuil"] * S - articles["q"]
        if n > Q:
            c = n * articles["pu"] - n * articles["pu"] * R
        else:
            c = n * articles["pu"]
        return round(c, 2)
    else:
        return 0


def classer_stocks(articles):
    liste_article = []
    for article in articles:
        liste_article.append(article)
    for i in range(len(liste_article)):
        for k in range(len(liste_article) - 1):
            if liste_article[k]["q"] * liste_article[k]["pu"] < liste_article[k + 1]["q"] * liste_article[k + 1]["pu"]:
                tmp = liste_article[k]
                liste_article[k] = liste_article[k + 1]
                liste_article[k + 1] = tmp
    return liste_article


def rotation_stocks(article, achat_30_dernier_jour):
    try:
        return math.floor(article["q"] / (achat_30_dernier_jour / 30))
    except:
        return 0


def article_par_categorie(articles):
    d = {}
    for article in articles:
        if article["cat"] == "outil":
            if "outil" in d:
                d["outil"] = d["outil"] + a["q"] * a["pu"]
            else:
                d["outil"] = article["q"] * article["pu"]
        elif article["cat"] == "consommable":
            if "consommable" in d:
                d["consommable"] = d["consommable"] + article["q"] * article["pu"]
            else:
                d["consommable"] = article["q"] * article["pu"]
        elif article["cat"] == "piece":
            if "piece" in d:
                d["piece"] = d["piece"] + article["q"] * article["pu"]
            else:
                d["piece"] = a["q"] * article["pu"]
        else:
            if "autre" in d:
                d["autre"] = d["autre"] + article["q"] * article["pu"]
            else:
                d["autre"] = article["q"] * article["pu"]
    for k in d:
        d[k] = round(d[k], 2)
    return d


def rapport(articles, ventes=None, cat=None, seuil_min=None, export=False, verbose=True, d=None):
    if d is None:
        d = datetime.datetime.now()
    res = {}
    res["date"] = str(d)
    tot = 0
    nb = 0
    liste_alerte = []
    boucle_rapport(articles=articles)


    res["valeur"] = round(tot, 2)
    res["nb"] = nb
    res["alertes"] = liste_alerte
    res["ttc"] = round(tot * (1 + TVA), 2)
    if export:
        export_rapport(res)
    return res

def export_rapport(res): 
        f = open("/tmp/rapport_" + str(random.randint(1, 9999)) + ".json", "w")
        f.write(json.dumps(res))
        f.close()


def boucle_rapport(articles):
    for a in articles:
        verfication_article()
        if a["q"] > 0:
            if a["pu"] > 0:
                tot = tot + a["q"] * a["pu"]
                nb = nb + 1
                if a["q"] < a["seuil"]:
                    liste_alerte.append(a["ref"])
                    if verbose:
                        print("ALERTE " + a["ref"] + " : " + str(a["q"]) + " restants")
                if ventes is not None:
                    verfication_vente()
            else:
                if verbose:
                    print("prix invalide " + a["ref"])
        else:
            if verbose:
                print("stock vide " + a["ref"])

def verfication_article():
    if cat is not None:
        if a["cat"] != cat:
            continue
    if seuil_min is not None:
        if a["q"] < seuil_min:
            continue
def verfication_vente():
    if a["ref"] in ventes:
        if ventes[a["ref"]] > 0:
            j = math.floor(a["q"] / (ventes[a["ref"]] / 30))
            if j < 7:
                if verbose:
                    print("RUPTURE IMMINENTE " + a["ref"])
            elif j < 30:
                if verbose:
                    print("a surveiller " + a["ref"])
        else:
            if verbose:
                print("aucune vente pour " + a["ref"])

def export_json(res, chemin="/tmp/inv.json", hist=[]):
    hist.append(res)
    f = open(chemin, "w")
    f.write(json.dumps(hist))
    f.close()
    return hist
