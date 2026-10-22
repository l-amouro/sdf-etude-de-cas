# Arbre de défaillance — alimentation de secours du jeu de barres critique

Système : réseau · inverseur de source · GE1 // GE2 (nourrice par GE, cuve principale commune) · onduleur on-line + batteries (+ bypass statique) · jeu de barres et départs protégés.
Basé sur l'AMDEC `AMDEC_alim_secours.xlsx` (N° = ligne de l'AMDEC).
Version 1 — 2026-10-19 (construction qualitative) · Version 2 — 2026-10-20 (points ouverts traités + coupes minimales par MOCUS) · Version 3 — 2026-10-21 (numérotation alignée sur l'AMDEC + quantification) · **Version 4 — 2026-10-22 (valeur exacte + facteurs d'importance)**.

## Événement sommet
**TOP : jeu de barres critique hors tension (coupure, même brève) pendant la mission de 24 h qui suit la perte du réseau.**

## Conditions initiales et hypothèses
- t = 0 : perte soudaine du réseau. GE1 et GE2 à l'arrêt (en attente), inverseur en position réseau, onduleur sur batteries (autonomie 10 min), jeu de barres alimenté par l'onduleur.
- Le réseau ne revient pas pendant les 24 h (conservatif).
- GE1 et GE2 démarrent simultanément sur ordre de l'inverseur et fonctionnent en **redondance active 1 sur 2** pendant la mission (avant la sollicitation, leurs défaillances de démarrage sont cachées).
- **Chaque GE est dimensionné pour 100 % de la charge** du jeu de barres ; la charge reste dans le dimensionnement (surcharge hors périmètre).
- Carburant : **cuve principale commune** qui alimente une **nourrice par GE**. Nourrice vide (pompe / vanne de transfert du GE) = défaillance indépendante ; cuve principale vide = cause commune.
- Le bypass statique est alimenté depuis l'amont (sortie de l'inverseur) : sa partie « amont absent » est déjà dans l'arbre et disparaît par absorption ; seule sa défaillance propre (refus de basculement) est gardée.
- Agressions externes (incendie, inondation, malveillance) hors périmètre. Niveau de détail = composants de l'AMDEC.
- MTTR des GE et de l'inverseur ≫ autonomie batteries (10 min) : toute perte de l'alimentation amont mène au TOP. Une défaillance dans les 10 dernières minutes de la mission est comptée comme TOP (conservatif).
- N°15 est un état caché à t = 0 (autonomie < temps de démarrage + commutation du GE), donc l'ordre des événements n'intervient pas.
- Arbre statique : la chronologie est portée par la définition des événements ; les séquences où l'ordre compte (redondance passive, réparation) relèvent d'un arbre dynamique ou de Markov / Petri (semaine 4).

## Arbre (v2) — portes G0 à G12
```
G0  TOP : jeu de barres hors tension pendant les 24 h  [OU]
├─ G1  E1 : Défaut côté distribution  [OU]
│   ├─ N°16 Défaut d'isolement du jeu de barres (contamination de surface)
│   └─ G3  E1.1 : Défaut aval non éliminé  [ET]
│       ├─ CC  Court-circuit sur un départ
│       └─ G4  E1.2 : Défaut non éliminé sélectivement  [OU]
│           ├─ N°18 Refus de déclenchement du disjoncteur du départ
│           └─ N°19 Défaut de sélectivité (protection amont déclenche)
└─ G2  E2 : Pas de tension provenant de la chaîne de secours  [OU]
    ├─ G5  E2.1 : Défaut de l'inverseur  [OU]
    │   ├─ N°8  Commutation non effectuée (sélecteur en mauvaise position)
    │   └─ N°11 Commutation non maintenue (fusible de commande → bobine retombe)
    └─ G6  E2.2 : Défaut de la chaîne d'alimentation  [OU]
        ├─ G7  E2.2.1 : L'onduleur ne délivre pas de tension  [OU]
        │   ├─ G9  E2.2.1.1 : Perte de sortie non reprise par le bypass  [ET]
        │   │   ├─ N°14 Perte de sortie onduleur (surchauffe)
        │   │   └─ N°20 Refus de basculement du bypass statique
        │   └─ G10 E2.2.1.2 : Batteries épuisées avant la reprise stable de l'amont  [OU]
        │       ├─ N°15 Autonomie batteries insuffisante à t = 0
        │       └─ N°13 Retour intempestif / pompage de l'inverseur
        └─ G8  E2.2.2 : Perte des deux GE pendant la mission  [OU]
            ├─ G11 E2.2.2.1 : Défaillance de cause commune  [OU]
            │   ├─ N°5  Refus de démarrage simultané (carburant trop vieux)
            │   ├─ N°17 Arrêt simultané en fonctionnement (carburant pollué → filtres colmatés)
            │   └─ N°21 Cuve principale vide (niveau insuffisant pour 24 h)
            └─ G12 E2.2.2.2 : Perte de GE1 ET de GE2 (défaillances indépendantes)  [ET]
                ├─ GE1 [OU] : 1a nourrice vide (refus) · 2a huile · 3a batterie de démarrage · 4a robinet OFF · 6a nourrice vide (arrêt) · 7a puissance réduite
                └─ GE2 [OU] : 1b · 2b · 3b · 4b · 6b · 7b
```

## Lignes AMDEC exclues (justifiées)
- N°9 commutation trop lente — événement ponctuel de quelques secondes, couvert par les batteries : pas de TOP seul.
- N°10 commutation sans perte de réseau — sans objet : le réseau est déjà perdu à t = 0.
- N°12 contacts usés — état dégradé, pas de TOP seul.

## Coupes minimales (MOCUS, 2026-10-20)
Aucun événement répété (carburant séparé en nourrices indépendantes + cuve principale en DCC) → MOCUS donne directement des coupes minimales, pas d'absorption nécessaire.

**47 coupes minimales :**
- **Ordre 1 (8) — points uniques de défaillance :** {N°5}, {N°8}, {N°11}, {N°13}, {N°15}, {N°16}, {N°17}, {N°21}
- **Ordre 2 (39) :** {CC, N°18}, {CC, N°19}, {N°14, N°20}, et 36 paires {Xa, Yb} avec X, Y ∈ {1, 2, 3, 4, 6, 7} (une défaillance de GE1 et une de GE2)

Type des événements (classement CCPS, SRT §4.3.6) : humain = N°8, N°4a/b, N°13 et N°19 (erreurs latentes de réglage) · passif = N°16, N°21, N°11 · actif = les autres (changement d'état ou pièces mobiles).

**Les plus critiques (qualitatif) :** {N°8} et {N°13} (ordre 1, erreur humaine), puis les coupes d'ordre 1 actives {N°5}, {N°17}, {N°15}.
**Lecture :** la redondance des GE ne donne que des coupes d'ordre 2 ; la faiblesse du système est dans ses 8 points uniques (inverseur, carburant commun, batteries, jeu de barres). À comparer avec l'AMDEC : N°8 n'y a qu'un IPR de 30 (D = 1).

## Quantification (2026-10-21) — `quantif_arbre_ex_5.py`
Données **d'exercice (hypothèses, non sourcées)**. Défaillances cachées (présentes à t = 0) : q ≈ λτ/2, τ = intervalle d'essai (GE mensuel 730 h ; autonomie onduleur et bypass semestriel 4380 h ; disjoncteur annuel 8760 h). Erreurs humaines latentes (N°4, N°8, N°19) : 10⁻³ par sollicitation. Défaillances en mission : q = 1 − e^(−λ·24 h). λ_GE en fonctionnement = 5·10⁻⁴ (N°6) + 1,5·10⁻³ (N°7) = 2·10⁻³ /h (valeur de la semaine 1).

| Méthode | P(TOP) sur 24 h |
|---|---|
| Événements rares (6.95) | 7,16·10⁻³ |
| Borne supérieure (6.94) | 7,14·10⁻³ |
| **Exacte (porte par porte, pas d'événement répété)** | **7,08·10⁻³** |

Écart à la valeur exacte : événements rares + 1,1 %, borne supérieure + 0,8 %. Les deux approximations sont conservatives (rares ≥ borne sup. ≥ exacte), car elles ignorent ou ne corrigent qu'en partie les intersections entre coupes. Le calcul porte par porte n'est exact que parce que les événements sont indépendants et qu'aucun n'est répété dans l'arbre.

Top 5 des coupes : {N°15} 2,19·10⁻³ (≈ 31 %) · {7a, 7b} 1,25·10⁻³ (≈ 17 %) · {N°8} 1,0·10⁻³ (≈ 14 %) · {N°5} 5·10⁻⁴ · {N°17} 4,8·10⁻⁴.
**Lecture :** la coupe la plus probable est l'autonomie batteries (N°15), une défaillance cachée testée seulement tous les 6 mois → levier direct : raccourcir l'intervalle d'essai (q ∝ τ). Les 36 paires de GE pèsent ≈ 37 % au total, dominées par N°7 (q ≈ 3,5·10⁻², ≥ 10⁻² → l'approximation des événements rares surestime légèrement). Écart entre méthodes ≈ 1 %.

## À faire
- [x] AMDEC : N°18, N°19, N°20 (bypass), N°21 (cuve principale), N°1/N°6 « nourrice vide » (2026-10-21).
- [ ] AMDEC : action sur N°19 (IPR 280, le plus élevé, sans action) — vérification de l'étude de sélectivité et des réglages à chaque modification.
- [x] Quantification en Python (SRT §6.7.3–6.7.5) : P(TOP) par les coupes minimales (2026-10-21).
- [ ] Valeur exacte porte par porte (6.89 / 6.90) + comparaison.
- [ ] Facteurs d'importance (SRT ch. 7, survol) + arbre d'événements (SRT §4.4).
