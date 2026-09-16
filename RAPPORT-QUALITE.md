# Rapport qualité, module inventaire

Nom : 
Date :
Empreinte du commit de départ :

---

## 1. Tableau de bord initial

Mesures relevées avant toute modification.

### Complexité par fonction


| Fonction    | Ligne | Complexité cyclomatique | Rang |
| ----------- | ----- | ----------------------- | ---- |
| rapport     | 122   | 22                      | D    |
| par_cat     | 94    | 10                      | B    |
| mouv        | 37    | 9                       | B    |
| classer     | 74    | 5                       | A    |
| val         | 19    | 3                       | A    |
| alerte      | 29    | 3                       | A    |
| cout        | 62    | 3                       | A    |
| rot         | 87    | 2                       | A    |
| maj_prix    | 175   | 1                       | A    |
| export_json | 185   | 1                       | A    |


Commande utilisée :

```bash
radon cc -s -a inventaire/inventaire.py
```

### Synthèse du fichier

| **Mesure**               | **Valeur** | **Commande**                                                                    |
| ------------------------ | ---------- | ------------------------------------------------------------------------------- |
| Lignes de code réelles   | 146        | pytest --cov=inventaire --cov-branch --cov-report=term-missing                  |
| Complexité moyenne       | B (5.9)    | radon cc -s -a inventaire/inventaire.py                                         |
| Indice de maintenabilité | A (36.80)  | radon mi -s  inventaire/inventaire.py                                           |
| Score pylint             | 7.76/10    | pylint inventaire/inventaire.py                                                 |
| Problèmes ruff           | 14 erreurs | ruff check inventaire/inventaire.py                                             |
| Entrées vulture          | 14         | vulture inventaire/inventaire.py                                                |
| Couverture de branches   | 0%         | pytest --cov=. --cov-branch --cov-report=term-missing                           |
| Barrière xenon           | échec      | xenon --max-absolute B --max-modules A --max-average A inventaire/inventaire.py |


---

## 2. Catalogue des odeurs

Douze entrées minimum. Trois au moins doivent être invisibles pour les outils.
La colonne conséquence décrit ce qui arrive à la personne qui devra modifier ce
fichier dans six mois.


| **#**  | **Ligne** | **Odeur ou défaut**             | **Détecté par** | **Conséquence concrète** |
| ------ | --------- | ------------------------------- | --------------- | ------------------------ |
| **1**  | 15        | `unused variable 'STOCK'`       | **vulture**     | Code mort                |
| **2**  | 19        | `unused function 'val'`         | **vulture**     | Code mort                |
| **3**  | 29        | `unused function 'alerte'`      | **vulture**     | Code mort                |
| **4**  | 37        | `unused function 'mouv'`        | **vulture**     | Code mort                |
| **5**  | 62        | `unused function 'cout'`        | **vulture**     | Code mort                |
| **6**  | 74        | `unused function 'classer'`     | **vulture**     | Code mort                |
| **7**  | 78        | `unused variable 'i'`           | **vulture**     | Code mort                |
| **8**  | 87        | `unused function 'rot'`         | **vulture**     | Code mort                |
| **9**  | 94        | `unused function 'par_cat'`     | **vulture**     | Code mort                |
| **10** | 122       | `unused function 'rapport'`     | **vulture**     | Code mort                |
| **11** | 175       | `unused function 'maj_prix'`    | **vulture**     | Code mort                |
| **12** | 175       | `unused variable 'p'`           | **vulture**     | Code mort                |
| **13** | 175       | `unused variable 'ref'`         | **vulture**     | Code mort                |
| **14** | 185       | `unused function 'export_json'` | **vulture**     | Code mort                |


---

## 3. Faut-il tout réécrire


Non, il ne faut pas tout réécrire. La plupart des fonctions n'ont pas beaucoup de complexité cyclomatique (B (5,9)) et affichent un bon indice de maintenabilité (A (36,80)). Cependant, plusieurs choses sont à corriger. Pour commencer, il faut supprimer tout le code mort afin de faciliter la correction du fichier. Supprimer le code mort offre tout d'abord aux développeurs une meilleure visibilité pour corriger le reste du code et évite d'entretenir du code non utilisé.

Cela cause aussi :

Une relecture inutile par toutes les nouvelles personnes arrivant sur le projet ;

Une maintenance par erreur lors des refactorings globaux ;

Un risque de réactivation intempestive : en 2012, chez Knight Capital, un drapeau de configuration recyclé a réactivé une fonction morte depuis 8 ans, entraînant 45 minutes de trading incontrôlé.

En plus de tous ces soucis, le code mort coûte également de l'argent. Par exemple, l'entreprise Knight Capital a perdu 460 millions de dollars à cause de ce problème.

On peut penser que supprimer du code mort présente un risque, par exemple si l'on s'aperçoit qu'il était encore utile. Mais l'utilisation de Git permet de résoudre ce problème en versionnant le fichier pour le récupérer ultérieurement si besoin.

Pour lister les différentes variables, fonctions, etc. non utilisées, on utilise Vulture, qui permet de repérer le code mort avec son pourcentage de confiance, c'est-à-dire la probabilité que le code soit réellement inutilisé.

---

## 4. Écarts constatés entre le code et les règles métier

Rempli pendant la mission 3, sans rien corriger.

| Règle | Ligne | Ce que le code fait | Ce que la règle dit |
|---|---|---|---|
|  |  |  |  |

---

## 5. Tableau de bord après refactoring

Mêmes mesures, mêmes commandes qu'en partie 1.

| Mesure | Avant | Après | Écart |
|---|---|---|---|
|  |  |  |  |

Ce que ce delta prouve, en trois phrases maximum :

---

## 6. Bugs prouvés puis corrigés

| Règle violée | Ligne d'origine | Commit red | Commit fix | Conséquence métier |
|---|---|---|---|---|
|  |  |  |  |  |

Pour au moins un de ces bugs, la conséquence est chiffrée en euros ou en ruptures de stock.
