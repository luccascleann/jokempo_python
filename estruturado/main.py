from src.player import Player
from src.machine import Machine
from src.jogo import Jogo


def main():

    player = Player()
    machine = Machine()    
    jogo = Jogo(player, machine)
    while True:
        jogo.jogada()

main()
