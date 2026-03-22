# src/feature_selection/woa.py
import numpy as np

class WOAFeatureSelector:
    def __init__(self, num_whales=8, max_iter=15):
        self.num_whales = num_whales
        self.max_iter = max_iter

    def optimize(self, fitness_fn, dim):
        whales = np.random.randint(0, 2, (self.num_whales, dim))
        best = whales[0]
        best_score = -1

        for t in range(self.max_iter):
            for i in range(self.num_whales):
                score = fitness_fn(whales[i])
                if score > best_score:
                    best_score = score
                    best = whales[i].copy()

        return best, best_score
