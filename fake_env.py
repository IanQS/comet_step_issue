# Fake gym env

from comet_ml import Experiment, ExistingExperiment, OfflineExperiment
import numpy as np

class FakeEnv():
    def __init__(self, comet_config):
        self.comet_config = comet_config
        self.comet_logger = self.create_logger()

    def create_logger(self):
        return Experiment(**self.comet_config)

    def step(self, action):
        return np.random.randint(0, 5)

