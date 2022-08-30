import pytest
from unittest import mock
from estruturado.src.machine import Machine

@pytest.mark.parametrize('jogada_esperada', ['1','2','3','4'])
def test_player_escolhe_jogada_corretamente(jogada_esperada):
    player = Machine()
    assert player.escolher_jogada(jogada_esperada) == int(jogada_esperada)

@mock.patch('builtins.print')
def test_player_escolhe_jogada_invalida(mock_print):
    jogada_incorreta = '5'
    player = Machine()
    player.escolher_jogada(jogada_incorreta)
    mock_print.assert_called_with('\nValor fora das opções!!!\n')

@pytest.mark.parametrize('jogada_esperada', ['1','2','3','4'])
def test_player_jogada_eh_valida_retorna_true(jogada_esperada):
    player = Machine()
    assert player.jogada_eh_valida(jogada_esperada)

def test_player_jogada_nao_eh_valida_retorna_false():
    jogada_incorreta = '5'
    player = Machine()
    assert not player.jogada_eh_valida(jogada_incorreta)