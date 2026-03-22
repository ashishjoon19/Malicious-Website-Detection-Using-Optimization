# src/models/catboost_model.py
from catboost import CatBoostClassifier

class CatBoostModel:
    def __init__(self, params):
        self.model = CatBoostClassifier(**params, verbose=False)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)
