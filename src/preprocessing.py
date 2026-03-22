import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


class DataPreprocessor:
    def __init__(self, test_size=0.2, random_state=42):
        self.test_size = test_size
        self.random_state = random_state
        self.scaler = MinMaxScaler()

    def load_data(self, file_path):
        """
        Load dataset from CSV
        """
        df = pd.read_csv(file_path)
        return df

    def clean_data(self, df):
        """
        Handle missing values and duplicates
        """
        df = df.drop_duplicates()
        df = df.dropna()
        return df

    def split_features_labels(self, df, target_column="label"):
        """
        Split dataset into features (X) and labels (y)
        """
        X = df.drop(columns=[target_column]).values
        y = df[target_column].values
        return X, y

    def normalize(self, X):
        """
        Normalize features using MinMax scaling
        """
        return self.scaler.fit_transform(X)

    def train_test_split(self, X, y):
        """
        Split into train and test sets
        """
        return train_test_split(
            X, y,
            test_size=self.test_size,
            random_state=self.random_state
        )

    def process(self, file_path):
        """
        Full pipeline: load → clean → split → normalize → train/test split
        """
        df = self.load_data(file_path)
        df = self.clean_data(df)

        X, y = self.split_features_labels(df)
        X = self.normalize(X)

        X_train, X_test, y_train, y_test = self.train_test_split(X, y)

        return X_train, X_test, y_train, y_test
