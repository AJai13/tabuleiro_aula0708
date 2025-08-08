from inimigo import Inimigo
from personagem import Personagem
from tabuleiro import Tabuleiro
from player import Player
import time

def main():

    # Tamanho do tabuleiro
    while True:
        try:
            tamanho = int(input("Digite o tamanho do tabuleiro (ex: 5 para 5x5, 10 para 10x10): "))
            if tamanho < 3:
                print("Escolha um tamanho maior que 2.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    tab = Tabuleiro(tamanho)

    # Criação dos personagens
    jogador = Player(tamanho // 2, tamanho // 2)
    inimigos = [
        Inimigo(0, 0),
        Inimigo(tamanho - 1, tamanho - 1)
    ]
    todos = [jogador] + inimigos


    # Jogo
    while True:
        tab.desenhar(todos)

        direcao = input("\nMover (w, s, a, s): ")

        if direcao == "sair":
            print("Jogo encerrado")
            break

        jogador.mover(direcao, tab.tamanho)

        for inimigo in inimigos:
            inimigo.mover_aleatorio(tab.tamanho)
        
        time.sleep(0.5)

if __name__ == "__main__":
    main()