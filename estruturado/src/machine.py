import random


class Machine:

    def __init__(self) -> None:
        self.jogada_adversaio = []
    
    def jogar(self, jogada_player):
        self.memorizar_jogada_do_adversario(jogada_player)
        return self.escolher_jogada()
    
    def escolher_jogada(self) -> int:
        jogada = str(random.randint(1,3))
        return int(jogada)
    
    def memorizar_jogada_do_adversario(self, jogada_adversario):
        self.jogada_adversaio.append(jogada_adversario)
