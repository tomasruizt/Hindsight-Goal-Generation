from unittest.mock import MagicMock

import numpy as np
from learner import HGGLearner
from learner.hgg import HGGLearnerInput


def test_hgg_can_instantiate():
    args = HGGLearnerInput(env="FetchReach-v1", logger=MagicMock())
    learner = HGGLearner(args)
    agent = MagicMock()
    agent.step.return_value = np.zeros(4)

    buffer = MagicMock()
    buffer.steps_counter = 1
    learner.learn(None, None, None, agent, buffer)
