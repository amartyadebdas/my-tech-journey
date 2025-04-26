from kfp.dsl import component, Input, Output, Dataset, Model

@component(base_image="python:3.9")
def train_model(train_csv: Input[Dataset], saved_model_output: Output[Model]):
    import subprocess
    subprocess.run(["pip", "install", "pandas", "scikit-learn", "joblib"], check=True)

    import pandas as pd
    from sklearn.linear_model import LinearRegression
    import joblib
    
    df = pd.read_csv(train_csv.path)
    X = df.drop(columns=["price"])
    y = df["price"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    joblib.dump(model, saved_model_output.path)
    print(f"[Model Training] Model saved at {saved_model_output.path}")

