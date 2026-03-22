# src/pipeline.py
from src.feature_selection.woa import WOAFeatureSelector
from src.optimization.smo import SMOOptimizer
from src.models.catboost_model import CatBoostModel

class Pipeline:
    def __init__(self):
        self.selector = WOAFeatureSelector()
        self.optimizer = SMOOptimizer()

    def run(self, X, y):
        # feature selection
        best_features, _ = self.selector.optimize(lambda f: 0.9, X.shape[1])

        # optimization
        best_params, _ = self.optimizer.optimize(lambda p: 0.95, bounds=None)

        model = CatBoostModel(best_params)
        model.train(X, y)

        return model
