# Fiche de formules — Sûreté de fonctionnement, semaine 1

Fiabilité, structures redondantes, MTTF et disponibilité, appliquées à une alimentation électrique de secours.

Notations : `R` = fiabilité d'un composant, `q = 1 − R` = sa défiabilité, `λ` = taux de défaillance (h⁻¹).

## 1. Lois de durée de vie

### Loi exponentielle

Loi sans mémoire : elle s'applique lorsque le taux de défaillance reste constant, quelle que soit la durée d'utilisation déjà écoulée.

| Grandeur | Formule | Signification |
|---|---|---|
| Fiabilité | `R(t) = e^(−λt)` | Probabilité que l'objet survive à l'intervalle [0 ; t] |
| Défiabilité | `F(t) = 1 − e^(−λt)` | Probabilité que l'objet tombe en panne dans l'intervalle [0 ; t] |
| Densité de défaillance | `f(t) = λ·e^(−λt)` | Dérivée de F(t) |
| Taux de défaillance | `z(t) = f(t) / R(t) = λ` | Constant |
| MTTF | `MTTF = 1/λ` | Temps moyen avant défaillance |

### Loi de Weibull

`R(t) = e^(−(t/θ)^α)`, avec `θ` le paramètre d'échelle et `α` le paramètre de forme.

| Forme | Comportement |
|---|---|
| α < 1 | Pannes concentrées au démarrage du système (défaillances de jeunesse) |
| α = 1 | Taux de défaillance constant : on retrouve la loi exponentielle |
| α > 1 | Pannes dues à l'usure, concentrées loin dans le temps |

## 2. Structures

| Structure | Fiabilité | Composants identiques |
|---|---|---|
| Série | `R_sys = ∏ Rᵢ` | `Rⁿ` |
| Parallèle | `R_sys = 1 − ∏ (1 − Rᵢ)` | `1 − (1 − R)ⁿ` |
| k sur n | `R_sys = Σ (i = k à n) C(n, i)·Rⁱ·(1 − R)ⁿ⁻ⁱ` | — |

### Défiabilité des structures redondantes

On compte les combinaisons de pannes qui font tomber le système.

| Structure | Défiabilité | Justification |
|---|---|---|
| 1 sur 2 | `F_sys = q²` | Le système tombe avec 2 pannes : `C(2,2)·q²·(1 − q)⁰`. Cohérent avec deux composants identiques en parallèle. |
| 2 sur 3 | `F_sys = 3q² − 2q³ ≈ 3q²` | 3 = nombre de paires de groupes qui tombent en panne ensemble, soit le nombre de coupes minimales d'ordre 2. Si q est petit, le terme en q² domine. |

## 3. MTTF

Définition : `MTTF = ∫₀^∞ R(t) dt`

Pour des composants de taux de défaillance constant λ :

| Architecture | MTTF |
|---|---|
| 1 composant | `1/λ` |
| 1 sur 2 actif | `3/(2λ)` |
| 2 sur 3 actif | `5/(6λ)` |
| Secours à froid, 2 éléments | `2/λ` |

## 4. Système réparable

- **MTBF** (*mean time between failures*) : temps moyen entre deux défaillances consécutives. N'a de sens que pour un système réparable. `MTBF = MTTF + MTTR`, avec MTTR le *mean time to repair*.
- **Disponibilité asymptotique** : `A∞ = MTTF / (MTTF + MTTR)`. N'a de sens que pour un système réparable en régime établi : probabilité que le système soit fonctionnel sur une longue période.
- **Disponibilité instantanée** `A(t)` : probabilité que le système soit disponible à un instant t. Elle dépend de t, contrairement à la disponibilité asymptotique.

## 5. Cas d'étude : alimentation électrique de secours

Diagramme de fiabilité :

```
Inverseur — Onduleur + Batteries — (GE1 // GE2) — Jeu de barres
```

Coupes minimales (4) : `{Inverseur}`, `{Onduleur + Batteries}`, `{GE1, GE2}`, `{Jeu de barres}`.

Hypothèses d'exercice : durée de mission 24 h, `λ_GE = 2·10⁻³ /h`.

### Fiabilité du système complet à 24 h

| Configuration des groupes | R(24 h) |
|---|---|
| 1 GE | 0,952 |
| 1 sur 2 | 0,996 |
| 2 sur 3 | 0,992 |

### Groupe seul : exponentielle ou Weibull

| Loi | R(24 h) |
|---|---|
| Exponentielle | 0,953 |
| Weibull, α = 1,5 (θ calculé pour le même MTTF que l'exponentielle) | 0,991 |

Code : `expo_law_ex_1.py`, `weibull_law_ex_1.py`, `rbd_chain_ex_2.py`, `rbd_koon_ex_3.py`, `mttf_ex_4.py`.
