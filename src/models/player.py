class Player:

    def escolher_jogada(self) -> str:
        messagem_de_escolha = 'Escolha uma opção (1, 2, 3 ou 4)\n'\
                                '1 - Pedra\n'\
                                '2 - Papel\n'\
                                '3 - Tesoura\n'\
                                '4 - Sair\n'
        return input(messagem_de_escolha).strip()
        
    def definir_jogada(self) -> int:
        jogada = self.escolher_jogada() 
        while self.jogada_nao_eh_valida(jogada):
            print ('\nValor fora das opções!!!\n')
            jogada = self.escolher_jogada() 
        
        return int(jogada)
    
    def jogada_nao_eh_valida(self, jogada: str) -> bool:
        return jogada not in ['1', '2', '3', '4']
