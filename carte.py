class Carte:
    """Classe représentant la carte de jeu qui peut rétrécir"""

    def __init__(self, taille_x=7, taille_y=7):
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.taille_initial_x = taille_x
        self.taille_initial_y = taille_y
        self.tours_avant_reduction = 20  # Nombre de tours avant rétrécissement
        self.tours_ecoules = 0
        self.zone_rouge_active = False

    def est_dans_zone_rouge(self, x, y):
        """Vérifie si une position est dans la zone rouge (hors carte)"""
        return x < 0 or x >= self.taille_x or y < 0 or y >= self.taille_y

    def reduire_carte(self):
        """Réduit la taille de la carte"""
        if self.taille_x > 5:
            self.taille_x -= 2
        if self.taille_y > 5:
            self.taille_y -= 2
        self.zone_rouge_active = True
        print(f"⚠️ La carte rétrécit! Nouvelle taille: {self.taille_x}x{self.taille_y}")

    def incrementer_tour(self):
        """Incrémente le compteur de tours et réduit la carte si nécessaire"""
        self.tours_ecoules += 1
        if self.tours_ecoules >= self.tours_avant_reduction:
            self.reduire_carte()
            self.tours_avant_reduction += 10  # Prochaine réduction dans 10 tours
