import random


class Machine:

    def jogar(self):
        jogada = None
        while jogada is None:
            jogada = self.escolher_jogada()
        return jogada
    
    def escolher_jogada(self) -> int:
        jogada = str(random.randint(1,3))
        return int(jogada)