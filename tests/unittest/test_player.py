from src.player import Player
from unittest import mock
import pytest


@pytest.mark.unittest
@pytest.mark.player
class PlayerTests:
    @pytest.mark.parametrize('jogada_esperada', ['1', '2', '3', '4'])
    def test_player_escolhe_jogada_corretamente(self, jogada_esperada):
        player = Player()
        with mock.patch('builtins.input', return_value=jogada_esperada):
            assert player.escolher_jogada() == int(jogada_esperada)

    @mock.patch('builtins.print')
    def test_player_escolhe_jogada_invalida(self, mock_print):
        jogada_incorreta = '5'
        player = Player()
        with mock.patch('builtins.input', return_value=jogada_incorreta):
            player.escolher_jogada()
            mock_print.assert_called_with('\nValor fora das opções!!!\n')

    @pytest.mark.parametrize('jogada_esperada', ['1', '2', '3', '4'])
    def test_player_jogada_eh_valida_retorna_true(self, jogada_esperada):
        player = Player()
        assert player.jogada_eh_valida(jogada_esperada)

    def test_player_jogada_nao_eh_valida_retorna_false(self):
        jogada_incorreta = '5'
        player = Player()
        assert not player.jogada_eh_valida(jogada_incorreta)
