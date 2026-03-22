from src.preprocessing import DataPreprocessor
from src.pipeline import Pipeline

if __name__ == "__main__":
    preprocessor = DataPreprocessor()

    X_train, X_test, y_train, y_test = preprocessor.process("data/dataset.csv")

    pipeline = Pipeline()
    model = pipeline.run(X_train, y_train)

    preds = model.predict(X_test)
    print("Pipeline executed successfully")
