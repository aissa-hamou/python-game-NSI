from math import sqrt
import random

from arme import Arme


def calculer_distance(x1, y1, x2, y2):
    """Calcule la distance euclidienne entre deux points"""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Joueur:
    """Classe représentant un joueur"""

    def __init__(self, nom, x, y, pv=100, energie=10):
        self.nom = nom
        self.x = x
        self.y = y
        self.pv = pv
        self.energie = energie
        self.max_energie = 10
        # Création des 3 armes: courte, moyenne et longue portée
        self.armes = [
            Arme(portee=3, degats=30, nom="Arme courte", cout_energie=2),
            Arme(portee=6, degats=25, nom="Arme moyenne", cout_energie=3),
            Arme(portee=10, degats=20, nom="Arme longue", cout_energie=4),
        ]
        self.arme_actuelle = 0  # Index de l'arme actuelle
        self.abandonne = False

    def afficher_statut(self):
        """Affiche les informations d'un joueur"""
        print(f"\n{'='*40}")
        print(f"Joueur: {self.nom}")
        print(f"Position: ({self.x}, {self.y})")
        print(f"PV: {self.pv}/100")
        print(f"Énergie: {self.energie}/{self.max_energie}")
        print(f"Arme actuelle: {self.armes[self.arme_actuelle].nom} (portée: {self.armes[self.arme_actuelle].portee})")
        print(f"{'='*40}\n")

    def deplacer(self, direction, carte, cout_par_case=1):
        """Déplace un joueur sur la carte"""
        if self.energie < cout_par_case:
            print(f"❌ {self.nom} n'a pas assez d'énergie pour se déplacer!")
            return False

        # Calcul du nombre de cases possibles selon l'énergie
        cases_possibles = min(self.energie // cout_par_case, 3)  # Maximum 3 cases

        if cases_possibles == 0:
            print(f"❌ {self.nom} n'a pas assez d'énergie pour se déplacer!")
            return False

        # Déplacement d'une case dans la direction choisie
        nouvelle_x, nouvelle_y = self.x, self.y

        if direction == "haut":
            nouvelle_y += 1
        elif direction == "bas":
            nouvelle_y -= 1
        elif direction == "droite":
            nouvelle_x += 1
        elif direction == "gauche":
            nouvelle_x -= 1
        else:
            print("❌ Direction invalide!")
            return False

        # Vérifier si la nouvelle position est valide
        if 0 <= nouvelle_x < carte.taille_x and 0 <= nouvelle_y < carte.taille_y:
            self.x = nouvelle_x
            self.y = nouvelle_y
            self.energie -= cout_par_case
            print(f"✅ {self.nom} se déplace vers {direction} (nouvelle position: {self.x}, {self.y})")
            return True
        else:
            print(f"⚠️ {self.nom} ne peut pas sortir de la carte!")
            return False

    def tirer(self, adversaire, carte):
        """Gère le tir d'un joueur vers son adversaire"""
        arme = self.armes[self.arme_actuelle]

        # Vérifier l'énergie
        if self.energie < arme.cout_energie:
            print(f"❌ {self.nom} n'a pas assez d'énergie pour tirer!")
            return False

        # Calculer la distance
        distance = calculer_distance(self.x, self.y, adversaire.x, adversaire.y)

        # Vérifier la portée
        if distance > arme.portee:
            print(f"❌ {self.nom} tire mais rate! (distance: {distance:.1f}, portée: {arme.portee})")
            self.energie -= arme.cout_energie
            return False

        # Calculer les dégâts
        degats = arme.calculer_degats(distance)

        if degats > 0:
            adversaire.pv -= degats
            self.energie -= arme.cout_energie
            print(f"💥 {self.nom} touche {adversaire.nom} avec {arme.nom}! (-{degats} PV)")
            print(f"   {adversaire.nom} a maintenant {adversaire.pv} PV")
            return True
        else:
            print(f"❌ {self.nom} tire mais rate!")
            self.energie -= arme.cout_energie
            return False

    def changer_arme(self):
        """Change l'arme du joueur (coûte tout le tour)"""
        # Sélection aléatoire d'une nouvelle arme
        nouvelle_arme = random.randint(0, len(self.armes) - 1)
        while nouvelle_arme == self.arme_actuelle:
            nouvelle_arme = random.randint(0, len(self.armes) - 1)

        self.arme_actuelle = nouvelle_arme
        print(f"🔄 {self.nom} change d'arme: {self.armes[self.arme_actuelle].nom}")
        return True

    def regenerer_energie(self):
        """Régénère l'énergie du joueur (+1 ou +2)"""
        if self.energie < self.max_energie:
            gain = random.choice([1, 2])
            self.energie = min(self.energie + gain, self.max_energie)
            print(f"⚡ {self.nom} régénère {gain} point(s) d'énergie ({self.energie}/{self.max_energie})")

    def est_mort(self):
        """Vérifie si un joueur est mort"""
        return self.pv <= 0

    def prendre_degats_zone_rouge(self):
        """Applique les dégâts de la zone rouge"""
        degats = 5
        self.pv -= degats
        print(f"🔥 {self.nom} est dans la zone rouge! (-{degats} PV)")
