import random

from personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, x, y):
        super().__init__(x, y, simbolo="I")

    def mover_aleatorio(self, tamanho):
        w = "cima"
        s = "baixo"
        a = "esquerda"
        d = "direita"
        
        direcao = random.choice([w, s, a, d])
        self.mover(direcao, tamanho)


