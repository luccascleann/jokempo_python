class Player:

    def jogar(self):
        jogada = None
        while jogada is None:
            jogada = self.escolher_jogada()
        return jogada
    
    def escolher_jogada(self) -> int:
        mensagem_de_escolha = '1 - Pedra\n' \
                              '2 - Papel\n' \
                              '3 - Tesoura\n' \
                              '4 - Sair\n' \
                              'Escolha uma opção (1, 2, 3 ou 4):'
        jogada = input(mensagem_de_escolha)
        if self.jogada_eh_valida(jogada):
            return int(jogada)
        
        print('\nValor fora das opções!!!\n')
        return
    
    @staticmethod
    def jogada_eh_valida(jogada: str) -> bool:
        jogadas_validas = ['1', '2', '3', '4']
        return jogada in jogadas_validas