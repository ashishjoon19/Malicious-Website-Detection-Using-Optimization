# config.py

# Dataset
DATA_PATH = "data/dataset.csv"
TARGET_COLUMN = "label"

# Split settings
TEST_SIZE = 0.2
RANDOM_STATE = 42

# WOA (Feature Selection)
WOA_NUM_WHALES = 8
WOA_MAX_ITER = 15

# SMO (Hyperparameter Optimization)
SMO_POP_SIZE = 8
SMO_MAX_ITER = 15

# CatBoost Parameters (default/baseline)
CATBOOST_PARAMS = {
    "iterations": 300,
    "depth": 6,
    "learning_rate": 0.1,
    "l2_leaf_reg": 3,
    "verbose": False
}
