from personagem import Personagem


class Player(Personagem):
    def __init__(self, x, y):
        super().__init__(x, y, simbolo="P")