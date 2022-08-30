import random
import typing


class Machine:

    def __init__(self) -> None:
        self.jogada_adversario = []

    def jogar(self, jogada_player):
        self.memorizar_jogada_do_adversario(jogada_player)
        return self.escolher_jogada()

    def escolher_jogada(self) -> int:
        if len(self.jogada_adversario) < 5:
            return random.randint(1, 3)
        pesos_de_escolha = self.otimizacao_de_escolha()
        machine = random.choices([2, 3, 1], weights=pesos_de_escolha)
        return int(machine[0])

    def otimizacao_de_escolha(self):
        dict_numero_de_jogadas_por_opcao = self.gerar_dict_contagens_de_jogadas()
        return self.gerar_list_pesos_de_escolha(dict_numero_de_jogadas_por_opcao)

    def memorizar_jogada_do_adversario(self, jogada_adversario):
        self.jogada_adversario.append(jogada_adversario)

    def gerar_dict_contagens_de_jogadas(self):
        dict_numero_de_jogadas_por_opcao = {
            1: 0,
            2: 0,
            3: 0
        }
        for jogada in self.jogada_adversario:
            dict_numero_de_jogadas_por_opcao[jogada] = self.jogada_adversario.count(
                jogada)
        return dict_numero_de_jogadas_por_opcao

    def gerar_list_pesos_de_escolha(self, dict_numero_de_jogadas_por_opcao: typing.Dict):
        dict_pesos_por_escolha = {
            1: 1,
            2: 1,
            3: 1
        }
        quantidade_mais_jogada = max(dict_numero_de_jogadas_por_opcao.values())

        for escolha, quantidade_de_jogadas in dict_numero_de_jogadas_por_opcao.items():
            if quantidade_de_jogadas == quantidade_mais_jogada:
                dict_pesos_por_escolha[escolha] = self.calculo_zeror(quantidade_mais_jogada)
        
        return list(dict_pesos_por_escolha.values())

    def calculo_zeror(self, quantidade_mais_jogada):
        return quantidade_mais_jogada / len(self.jogada_adversario)*10