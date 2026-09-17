from itertools import product

from config.settings import API_KEYS, MODELS


class ModelManager:

    def __init__(self):
        self.combinations = list(product(MODELS, API_KEYS))

    def get_combinations(self):
        return self.combinations