import pytest
from unittest import mock
from estruturado.src.machine import Machine

@pytest.mark.parametrize('jogada_esperada', ['1','2','3','4'])
def test_player_escolhe_jogada_corretamente(jogada_esperada):
    player = Machine()
    assert player.escolher_jogada(jogada_esperada) == int(jogada_esperada)
