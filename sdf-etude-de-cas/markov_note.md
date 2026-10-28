# Semaine 4 — Modèles de Markov : alimentation de secours du jeu de barres

Étude de cas : alimentation électrique de secours d'un jeu de barres critique (réseau · inverseur · GE1 // GE2 · onduleur + batteries · jeu de barres). Cette note porte sur le sous-système **GE1 // GE2**.
Scripts : `markov_1comp_ex_6.py`, `markov_1oo2_ex_7.py`, `markov_mttf_ex_8.py`, `markov_standby_ex_9.py`.

## 1. Hypothèses
- λ_GE = 2·10⁻³ /h (**hypothèse d'exercice**, non sourcée), MTTR = 24 h → μ = 1/24 /h.
- Lois exponentielles pour les défaillances **et** les réparations (propriété de Markov : temps de séjour exponentiel dans chaque état).
- Inverseur de source parfait (il est traité dans l'arbre de défaillance, `arbre_defaillance.md`).
- GE identiques ; défaillances de cause commune (DCC) **non modélisées** ici (traitées dans l'AMDEC N°5 et l'arbre).

## 2. Un GE réparable (ex. 6)
États : 1 = en marche, 0 = en panne. Matrice des taux (ordre [0, 1]) :

```
A = [[-μ,  μ],
     [ λ, -λ]]
```

Résolution de P·A = 0 avec ΣP = 1 (équation de normalisation, car les équations sont dépendantes) :
- **A∞ = μ / (λ + μ) = 0,9542** (Ā∞ ≈ λ·MTTR quand λ ≪ μ)
- **A(24 h) = 0,9703**, A(100 h) = 0,9548 — calcul par `expm`, identique à la solution analytique.
- A(t) > A∞ au début : ce n'est pas un vieillissement (la loi exponentielle n'en a pas), c'est le **régime transitoire** depuis A(0) = 1, qui décroît à la vitesse **λ + μ**.

## 3. GE1 // GE2 réparable, 1 sur 2 (ex. 7)
États : 2 = 2 GE en marche, 1 = 1 GE en marche, 0 = 0 GE. Taux : 2 → 1 = **2λ** (k GE en marche → k·λ), 1 → 0 = λ ; réparation 1 → 2 = μ ; 0 → 1 = 2μ (2 équipes) ou μ (1 équipe).
Vecteur de disponibilité [0, 1, 1] (système disponible dans les états 1 et 2).

| Politique de réparation | Ā∞ | A(24 h) |
|---|---|---|
| 2 équipes | **2,10·10⁻³** (= Ā_GE², exactement) | 0,99912 |
| 1 équipe | **4,19·10⁻³** (≈ ×2) | 0,99883 |

Avec une seule équipe, l'indisponibilité du **système** double : l'équipe partagée rend les deux GE **dépendants** (quand les deux sont en panne, le second attend que l'équipe soit libre), donc le produit Ā_GE² ne s'applique plus.

## 4. MTTF du système (ex. 8)
Pour le temps jusqu'à la **première** défaillance du système, l'état 0 est rendu **absorbant** (pas de réparation depuis 0). Matrice réduite Q (états 2, 1) et temps moyens d'absorption : −Q·T = 1.

```
Q = [[-2λ,       2λ ],
     [  μ,  -(μ + λ)]]
```

- T₂ = (3λ + μ) / (2λ²) = **5 958 h** = MTTF (le système part de l'état 2)
- T₁ = (2λ + μ) / (2λ²) = 5 708 h
- Contrôle μ = 0 : T₂ = 3/(2λ) = **750 h** (même valeur que `mttf_ex_4.py`)

**La réparation multiplie le MTTF par ~8** : le système ne tombe que si le 2ᵉ GE lâche **pendant la réparation du 1ᵉʳ**, probabilité ≈ λ/(λ + μ) ≈ 5 % à chaque première panne.

## 5. Redondance tiède (ex. 9) — lien avec le PFE
GE1 en marche, GE2 en attente ; en attente, GE2 peut tomber en panne à un taux **λ_s** (0 ≤ λ_s ≤ λ). Seul le taux 2 → 1 change : **λ + λ_s**. La redondance tiède généralise les deux cas classiques : λ_s = λ → redondance active (chaude) ; λ_s = 0 → redondance froide.

| λ_s | MTTF avec réparation | MTTF sans réparation | R(24 h) avec réparation | R(24 h) sans réparation |
|---|---|---|---|---|
| λ (chaude) | 5 958 h | 750 h | 0,998372 | 0,997804 |
| 0,5 λ | 7 778 h | 833 h | 0,998771 | 0,998340 |
| 0,1 λ | 10 424 h | 955 h | 0,999094 | 0,998775 |
| 0 (froide) | 11 417 h | 1 000 h | 0,999175 | 0,998884 |

Lecture :
- Classement froide > tiède > chaude : un taux 2 → 1 plus faible fait quitter l'état 2 plus tard.
- **La réparation change beaucoup le MTTF (×8 à ×11) mais très peu R(24 h)** : la mission de 24 h est courte devant le MTTF, il y a rarement le temps d'une panne *et* d'une réparation. Pour une mission courte, c'est la redondance qui compte, pas l'équipe de réparation.
- λ_s = 0 est une **hypothèse optimiste** : un GE en attente a des défaillances cachées, découvertes seulement à l'essai périodique (logique de l'AMDEC N°15).

**Réseau de Petri stochastique équivalent (sans réparation)** — 5 places, marquage initial entre parenthèses :
- Places : GE1 marche (1) · GE2 attente (1) · GE2 marche (0) · GE1 panne (0) · GE2 panne (0)
- T1 : GE1 marche → GE1 panne, taux λ
- T2 : GE2 attente → GE2 panne, taux λ_s (défaillance cachée en attente)
- T3 (immédiate, démarrage) : GE2 attente → GE2 marche, validée seulement si GE1 panne est marquée (arc de test)
- T4 : GE2 marche → GE2 panne, taux λ
- Défaillance du système : plus aucun jeton dans GE1 marche ni dans GE2 marche.

## 6. Limites de Markov et lien PFE
Un modèle de Markov repose sur la propriété sans mémoire : il ne peut pas représenter une loi de Weibull, qui dépend de l'âge du composant. Dans le PFE, le composant de secours **vieillissait** (lois de Weibull, échantillonnées avec l'âge du composant) : le modèle était donc simulé par **Monte-Carlo** (automates stochastiques hybrides, outil de simulation Python), avec une horloge par composant.
- Avantage : n'importe quelle loi (Weibull, dégradation Gamma), dépendances, vieillissement.
- Coût : résultat **statistique**, avec un **intervalle de confiance** dont la largeur décroît en **1/√N** (4× plus d'histoires → erreur divisée par 2) ; les événements rares (P ≈ 10⁻³) demandent beaucoup d'histoires. Markov donne un résultat exact et quasi instantané → préféré quand les lois sont exponentielles.

## 7. Usage métier
Choisir 1 ou 2 équipes de réparation est une décision de **méthodes maintenance** (dimensionnement des équipes, astreinte) : ici, une 2ᵉ équipe divise par 2 l'indisponibilité du système. MTTF et MTTR alimentent le plan de maintenance et la politique d'essais périodiques des secours.
