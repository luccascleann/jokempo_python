from src.player import Player
from src.machine import Machine


class Jogo:

    def __init__(self, player: Player, machine: Machine) -> None:
        print('BEM VINDO AO JOKEMPO')
        self.player = player
        self.machine = machine
        self.dict_jokempo = {
            1: 'Pedra', 
            2: 'Papel', 
            3: 'Tesoura'
        }
    
    def jogada(self):
        jogada_player = self.player.jogar()
        jogada_machine = self.machine.jogar()
        self.player_deseja_sair(jogada_player)
        self.escolher_vencedor(jogada_player, jogada_machine)
    
    def escolher_vencedor(self, jogada1, jogada2):
        if jogada1 == 4:
            return
        dict_jogada_que_ganha_do_adversario = {
            1: 3,
            2: 1,
            3: 2
        }
        print(f'Sua jogada -> {self.dict_jokempo[jogada1]}')
        print(f'Jogada da máquina -> {self.dict_jokempo[jogada2]}')
        if jogada1 == jogada2:
            print('Você empatou!\n')
        elif dict_jogada_que_ganha_do_adversario[jogada1] == jogada2:
            print('Você ganhou!\n')
        else:
            print('Você perdeu!\n')
    
    def player_deseja_sair(self, jogada_player):
        if jogada_player == 4:
            print('Obrigado por jogar.\nAté logo!')
            exit()