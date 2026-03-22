# src/optimization/smo.py
import numpy as np

class SMOOptimizer:
    def __init__(self, pop_size=8, max_iter=15):
        self.pop_size = pop_size
        self.max_iter = max_iter

    def optimize(self, fitness_fn, bounds):
        population = np.random.uniform(bounds[:,0], bounds[:,1], (self.pop_size, len(bounds)))
        best, best_score = None, -1

        for _ in range(self.max_iter):
            scores = [fitness_fn(ind) for ind in population]
            idx = np.argmax(scores)

            if scores[idx] > best_score:
                best_score = scores[idx]
                best = population[idx]

        return best, best_score
