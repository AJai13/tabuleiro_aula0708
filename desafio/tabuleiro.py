class Tabuleiro:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.grid = [[" " for _ in range(tamanho)] for _ in range(tamanho)]

    def limpar(self):
        self.grid = [[" " for _ in range(self.tamanho)] for _ in range(self.tamanho)]

    def desenhar(self, personagens):
        self.limpar()
        for p in personagens:
            if 0 <= p.x < self.tamanho and 0 <= p.y < self.tamanho:
                self.grid[p.y][p.x] = p.simbolo

        for linha in self.grid:
            print("+---" * self.tamanho + "+")
            print("".join([f"| {c} " for c in linha]) + "|")
        print("+---" * self.tamanho + "+")
