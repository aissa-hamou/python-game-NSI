import random


class Arme:
    """Classe représentant une arme avec sa portée, ses dégâts et son coût en énergie"""

    def __init__(self, portee, degats, nom, cout_energie):
        self.portee = portee
        self.degats = degats
        self.nom = nom
        self.cout_energie = cout_energie

    def calculer_degats(self, distance):
        """Calcule les dégâts en fonction de la distance et du type d'arme"""
        if distance > self.portee:
            return 0

        # Probabilité de toucher selon la portée
        if self.portee >= 5:  # Arme longue portée
            proba_toucher = random.randint(1, 10)
            if proba_toucher > 2:  # 80% de chance
                proba_critique = random.randint(1, 10)
                if proba_critique > 8:  # 20% de critique
                    return self.degats // 2
                return self.degats
            return 0
        else:  # Arme courte portée
            proba_toucher = random.randint(1, 10)
            if proba_toucher > 3:  # 70% de chance
                proba_critique = random.randint(1, 10)
                if proba_critique > 6:  # 40% de critique
                    return self.degats // 2
                return self.degats
            return 0
