import random
from random import randint

class darcarta():
    def __init__(self):
        self.cartas = {'corazones':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 'diamantes':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 'picas':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 'treboles':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']}
    def primeravez(self):
        naipe = random.choice(list(self.cartas))
        carta = randint(0, len(self.cartas[naipe]) - 1)
        return self.cartas[naipe][carta], naipe
