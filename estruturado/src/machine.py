class Machine:

    def escolher_jogada(self, jogada: str) -> int:
        if self.jogada_eh_valida(jogada):
            return int(jogada)
        
        print('\nValor fora das opções!!!\n')
        return
    
    @staticmethod
    def jogada_eh_valida(jogada: str) -> bool:
        jogadas_validas = ['1', '2', '3', '4']
        return jogada in jogadas_validas