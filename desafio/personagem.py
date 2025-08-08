class Personagem:
    def __init__(self, x, y, simbolo="O"):
        self.x = x
        self.y = y
        self.simbolo = simbolo

    def mover(self, direcao, tamanho_tabuleiro):
        w = "cima"
        s = "baixo"
        a = "esquerda"
        d = "direita"

        if direcao == w and self.y > 0:
            self.y -= 1
        elif direcao == s and self.y < tamanho_tabuleiro - 1:
            self.y += 1
        elif direcao == a and self.x > 0:
            self.x -= 1
        elif direcao == d and self.x < tamanho_tabuleiro - 1:
            self.x += 1

