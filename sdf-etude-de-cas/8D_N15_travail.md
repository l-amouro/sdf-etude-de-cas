# 8D — autonomie batteries onduleur (AMDEC N°15) — document de travail

> Exercice : scénario fictif construit sur l'étude de cas (alimentation de secours du jeu de barres). Rédigé le 2026-10-29 à partir des réponses de La'win (session `/study` outils qualité), corrections incluses. Sert de base à la fiche `outils_qualite.md` (créneau 16:30).

**Scénario.** 12 octobre, 03:10 : perte réseau. L'onduleur passe sur batteries ; GE1 démarre et l'inverseur bascule en ~60 s, mais les batteries ne tiennent que 25 s (alarme « batterie faible » à 15 s) → jeu de barres hors tension ~35 s, redémarrage des serveurs, 2 h de production perdues. Batteries de 6 ans (durée de vie fabricant 5 ans à 20 °C) ; local onduleur à 30 °C (ventilation arrêtée depuis l'été) ; dernier essai d'autonomie il y a 5 mois noté « OK », sans durée mesurée.

## D1 — Équipe
Pilote : ingénieur qualité · maintenance électrique (réalise les essais) · exploitation / client interne (charges critiques) · constructeur de l'onduleur.

## D2 — Description (faits uniquement)
- **Quoi :** perte d'alimentation du jeu de barres pendant ~35 s lors d'une perte réseau.
- **Qui :** détecté par l'exploitation de nuit (alarme) ; touchés : serveurs critiques, production.
- **Où :** jeu de barres secouru ; défaillance localisée sur les batteries de l'onduleur.
- **Quand :** 12 octobre, 03:10, à la sollicitation.
- **Comment :** batteries épuisées après 25 s alors que la reprise par GE1 demande ~60 s.
- **Combien :** 1 occurrence · 35 s hors tension · 2 h de production perdues · 1 onduleur (nombre de blocs à préciser).
- **Pourquoi c'est un problème :** exigence « aucune coupure tolérée » non tenue.
- **Est / N'est pas :** le défaut **est** sur l'autonomie batteries ; il **n'est pas** sur le GE (démarrage normal en 60 s) ni sur l'inverseur. La perte réseau est l'événement initiateur attendu (hors périmètre du 8D).

## D3 — Actions de confinement
- Batteries neuves (stock) ou de location immédiatement ; à défaut, consigne d'exploitation + information du client interne sur le risque temporaire.
- Remise en route de la ventilation ou refroidissement mobile.
- Contrôle de l'âge et de l'autonomie des autres onduleurs du site (isoler / trier).
- **Vérification :** essai d'autonomie mesuré après remplacement, résultat ≥ 10 min.

## D4 — Causes racines
**Ishikawa (5M + Mesure)**
- Milieu : local à 30 °C, ventilation arrêtée depuis l'été → vieillissement accéléré.
- Moyens : batteries de 6 ans > durée de vie de 5 ans · pas d'alarme de température du local.
- Méthodes : pas de remplacement préventif à l'âge · essai semestriel seulement · pas de critère d'acceptation.
- Main d'œuvre : arrêt de la ventilation non signalé · pas de valeur cible pour la personne qui fait l'essai (écart de processus, pas de faute individuelle).
- Matière : sans objet.
- Mesure : autonomie et température jamais relevées.

**5 pourquoi (La'win)**
1. Serveurs redémarrés ? → jeu de barres hors tension 35 s, GE disponible en 60 s.
2. Batteries 25 s seulement ? → capacité fortement dégradée (âge + chaleur).
3. Batteries usées laissées en service ? → le dernier essai les a validées (« OK »).
4. Essai « OK » malgré tout ? → essai qualitatif : ni durée, ni température relevées.
5. Pourquoi un tel essai ? → plan de maintenance préventive non adapté aux conditions réelles ; âge des batteries non suivi.

- **Cause d'apparition :** batteries au-delà de leur durée de vie, vieillissement accéléré par 30 °C → *racine* : pas de remplacement à l'âge, pas de surveillance de la température.
- **Cause de non-détection :** essai « OK » sans durée mesurée ni critère d'acceptation → *racine* : procédure d'essai.

## D5–D8 — à faire (16:30)
- D5 : une action par cause racine (apparition + non-détection), validée avant déploiement.
- D6 : mise en œuvre, retrait des actions de D3, validation à chaud puis à froid (indicateurs ?).
- D7 : standardiser (procédure, fiche d'essai), déploiement horizontal, **mise à jour de l'AMDEC N°15** (O, D → IPR').
- D8 : retour d'expérience, félicitations de l'équipe.
- Puis PDCA sur « essai d'autonomie mensuel avec durée mesurée » (Check : P(TOP) −26 % d'après l'arbre, semaine 3).
