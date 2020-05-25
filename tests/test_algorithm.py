from typing import NamedTuple

import pytest

from algorithm import DDPG


class DDPGInput(NamedTuple):
    pass

@pytest.mark.skip
def test_ddpg():
    args = DDPGInput()
    DDPG(args)