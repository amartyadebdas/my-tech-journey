from kfp.dsl import component, Input, Output, Dataset, Model, Metrics
# from sklearn.metrics import confusion_matrix, classification_report

@component(base_image="python:3.9")
def evaluate_model(test_csv: Input[Dataset], model: Input[Model], metrics_output: Output[Metrics]):
    import subprocess
    subprocess.run(["pip", "install", "pandas", "scikit-learn", "joblib"], check=True)
    
    import pandas as pd
    import joblib
    from sklearn.metrics import mean_squared_error, r2_score
    import json
    
    df = pd.read_csv(test_csv.path)
    X = df.drop(columns=["price"])
    y = df["price"]
    
    model = joblib.load(model.path)
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    # cm = confusion_matrix(y_pred, y).tolist()
    # cr = classification_report(y_pred, y)

    metrics_output.log_metric("Mean Squared Error", mse)
    metrics_output.log_metric("R2 Score", r2)    
    # metrics_output.log_metric("Confusion Matrix", str(cm))
    # metrics_output.log_metric("Classification Report", cr)

    # print(confusion_matrix)

    metrics = {"mean_squared_error": mse}
    with open(metrics_output.path, 'w') as f:
        json.dump(metrics, f)
    
    print(f"[Evaluation] MSE: {mse}")
    print(f"[Evaluation] R2 Score: {r2}")


