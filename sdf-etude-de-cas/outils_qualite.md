# Outils qualité — fiche de synthèse (notions)

> La'win Amouro · 2026-10-29 · appliquée à l'étude de cas « alimentation de secours du jeu de barres » (AMDEC N°15, scénario fictif). Source : *La boîte à outils de la qualité* (Gillet-Goinard & Seno, Dunod 2019) + `8D_N15_travail.md`.

## Les outils en une ligne
| Outil | À quoi il sert | Point clé à ne pas rater |
|---|---|---|
| **PDCA** | Amélioration continue : Plan → Do → Check → Act | Plan = objectifs SMART **+** plan d'action ; Act = standardiser ou relancer la boucle |
| **8D** | Résoudre un problème client / récurrent, en équipe, jusqu'à la cause racine | Cause d'**apparition** ET cause de **non-détection** · déploiement horizontal |
| **QRQC** | Réaction rapide terrain (*Quick Response Quality Control*) | Action immédiate = **protéger le client**, puis analyse sur les faits (3 réels : lieu, pièce, données) |
| **Ishikawa (5M)** | Classer les causes possibles : Milieu, Moyens, Méthodes, Main d'œuvre, Matière (+ Mesure) | Une branche = un **écart** (« ventilation arrêtée »), pas un composant |
| **5 pourquoi** | Remonter d'un symptôme à la cause racine | S'arrêter sur un processus, jamais sur une personne |
| **5S** | Organisation du poste : Seiri, Seiton, Seiso, Seiketsu, Shitsuke | Trier, ranger, nettoyer, standardiser, tenir dans la durée |
| **ISO 9001** | Système de management de la qualité | Approche processus + **approche par les risques** → une AMDEC en est une preuve |

## 8D — autonomie batteries onduleur (AMDEC N°15)
**Problème (D2, faits) :** 12/10, 03:10, perte réseau → batteries épuisées en 25 s, GE1 disponible en ~60 s → jeu de barres hors tension 35 s, 2 h de production perdues. Exigence « aucune coupure » non tenue.
- **D1 Équipe :** pilote qualité · maintenance électrique · exploitation · constructeur onduleur.
- **D3 Confinement :** batteries neuves / de location · ventilation remise en route · contrôle des autres onduleurs · vérif. : essai mesuré ≥ 10 min. *Le système reste exposé tant que le remplacement n'est pas fait.*
- **D4 Causes racines :** apparition = batteries au-delà de leur durée de vie, vieillissement accéléré à 30 °C (pas de remplacement à l'âge, pas de surveillance de température) · non-détection = essai « OK » sans durée mesurée ni critère d'acceptation.
- **D5 Actions correctives (validées avant déploiement) :**
  1. *Apparition :* registre de l'âge des batteries (GMAO) + **remplacement préventif avant la fin de vie fabricant**, avancé si l'autonomie chute fortement entre deux essais · ventilation + **alarme de température** du local (seuil à fixer avec le constructeur, ~25 °C).
  2. *Non-détection :* essai d'autonomie **chiffré** : durée mesurée, température du local, critère d'acceptation (≥ 10 min, bien au-delà des 60 s de reprise GE) et suivi de tendance.
  - *Validation :* essai mesuré sur le système réel après remplacement + relevés de température sur plusieurs semaines (un scénario théorique sur la durée de vie sert à **justifier** la périodicité, pas à valider).
- **D6 Mise en œuvre :** actions déployées, actions de D3 retirées · validation à chaud (essai conforme) puis à froid (3 essais mensuels conformes, 0 alarme de température non traitée).
- **D7 Prévention :** procédure + fiche d'essai standard · **déploiement horizontal** à tous les onduleurs du site · **mise à jour de l'AMDEC N°15** : O et D revus à la baisse → IPR' recalculé.
- **D8 Clôture :** retour d'expérience partagé, remerciements à l'équipe.

## PDCA — essai d'autonomie mensuel mesuré
- **Plan :** objectif = détecter toute dégradation avant que l'autonomie passe sous 10 min · plan d'action : fiche d'essai (durée, température, âge), pilote maintenance électrique, essai mensuel, alerte si baisse marquée entre deux essais.
- **Do :** appliquer 3 mois sur l'onduleur du jeu de barres (pilote).
- **Check :** % d'essais avec durée mesurée (cible 100 %) · dégradations détectées avant défaillance · 0 coupure du jeu de barres · modèle : arbre de défaillance → **P(TOP) −26 %** (semaine 3).
- **Act :** si conforme → standardiser (procédure, GMAO), étendre aux autres onduleurs, mettre à jour l'AMDEC ; sinon → ajuster périodicité / seuils et relancer un cycle.

## Pièges notés (session du 29/10)
- D2 = **faits uniquement** (pas de causes dans la description).
- Ishikawa : des écarts, pas des acteurs ni des équipements.
- QRQC : d'abord protéger le client.
