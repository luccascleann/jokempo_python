import pytest
from unittest import mock
from src.machine import Machine

@pytest.mark.unittest
@pytest.mark.machine
class MachineTests:
    def test_player_escolhe_jogada_corretamente(self):
        expected_results = [1, 2, 3]
        player = Machine()
        assert player.escolher_jogada() in expected_results
