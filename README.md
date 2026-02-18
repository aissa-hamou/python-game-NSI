# 🎮 Jeu de combat — Python

Jeu de combat au tour par tour pour deux joueurs sur une carte qui rétrécit.  
**Fait par Aissa Hamou.**

---

## 📋 Description

Deux joueurs s'affrontent sur une carte. Chaque tour, vous pouvez **tirer**, **vous déplacer**, **changer d'arme** ou **abandonner**. La carte diminue au fil du temps : rester en dehors inflige des dégâts. La partie se joue en **3 manches** ; le joueur qui en gagne le plus remporte la partie.

---

## 🚀 Lancer le jeu

**Prérequis :** Python 3 installé.

```bash
python main.py
```

ou :

```bash
python3 main.py
```

---

## 📁 Fichiers du projet

Le code est réparti en plusieurs modules :

| Fichier | Rôle |
|---------|------|
| **`main.py`** | Point d'entrée : lance le jeu. |
| **`jeu.py`** | Classe `Jeu` : boucle de jeu, tours, manches, scores, affichage. |
| **`joueur.py`** | Classe `Joueur` et fonction `calculer_distance`. |
| **`arme.py`** | Classe `Arme` : portée, dégâts, coût en énergie. |
| **`carte.py`** | Classe `Carte` : taille, rétrécissement, zone rouge. |

---

## 🛠️ Structure du code

- **`arme.py`** — Portée, dégâts, coût en énergie, calcul des dégâts selon la distance et le hasard.
- **`carte.py`** — Taille, rétrécissement, détection de la zone rouge (hors carte).
- **`joueur.py`** — Position, PV, énergie, armes, déplacement, tir, changement d'arme, régénération d'énergie.
- **`jeu.py`** — Orchestration : boucle de jeu, tours, manches, scores, affichage de la carte et du résultat final.
- **`main.py`** — Instancie `Jeu` et appelle `jouer()`.

---

## 🎯 Règles

- **Manches :** Une partie = 3 manches. À chaque manche, les deux joueurs ont 100 PV et 10 points d'énergie.
- **Carte :** Grille 7×7 au départ. Elle rétrécit après un certain nombre de tours (zone rouge = hors carte = dégâts).
- **Zone rouge :** Si vous êtes en dehors de la carte, vous subissez 5 dégâts par tour.
- **Énergie :** Chaque action (tir, déplacement) coûte de l'énergie. Vous en régénérez un peu après une action.
- **Fin de manche :** Un joueur gagne la manche si l'autre a 0 PV ou abandonne. Match nul si les deux sont à 0 PV.
- **Vainqueur de la partie :** Celui qui a gagné le plus de manches sur les 3.

---

## ⚔️ Actions par tour

| Choix | Action | Détails |
|-------|--------|--------|
| **1** | Tirer | Touche l'adversaire s'il est à portée. Consomme l'énergie de l'arme. Peut rater (probabilité selon l'arme). |
| **2** | Se déplacer | Une case : haut, bas, droite ou gauche. Coût : 1 énergie. Maximum 3 cases par tour selon l'énergie. |
| **3** | Changer d'arme | Prend une arme au hasard parmi les 3. Prend tout le tour. |
| **4** | Abandonner | Abandon de la manche en cours. L'adversaire gagne la manche. |

---

## 🔫 Armes

Chaque joueur a trois armes :

| Arme | Portée | Dégâts | Coût énergie |
|------|--------|--------|----------------|
| Arme courte | 3 | 30 | 2 |
| Arme moyenne | 6 | 25 | 3 |
| Arme longue | 10 | 20 | 4 |

Les dégâts réels dépendent de la distance et du hasard (toucher / critique). Au-delà de la portée, le tir ne touche pas.

---

## 🗺️ Carte

- **Affichage :** `J1` = Joueur 1, `J2` = Joueur 2, `.` = case vide.
- **Rétrécissement :** Après un nombre fixe de tours, la carte perd en taille (par ex. 2 cases en largeur et en hauteur). Un message prévient quand la carte rétrécit.
- Rester sur une case devenue « hors carte » (zone rouge) inflige 5 dégâts par tour.

---

## 👤 Auteur

**Fait par Aissa Hamou.**

---

*Amusez-vous bien ! 🏆*
