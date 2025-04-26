from kfp.dsl import component, Input, Output, Dataset, Metrics

@component(base_image="python:3.9")
def process_data(input_csv: Input[Dataset], train_data: Output[Dataset], test_data: Output[Dataset], length_metrics:Output[Metrics]):
    import subprocess
    subprocess.run(["pip", "install", "pandas", "scikit-learn"], check=True)

    import pandas as pd
    from sklearn.model_selection import train_test_split
    
    df = pd.read_csv(input_csv.path)
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    length_metrics.log_metric('train_dataset_length',len(train_df))
    length_metrics.log_metric('test_dataset_length',len(test_df))
    
    train_df.to_csv(train_data.path, index=False)
    test_df.to_csv(test_data.path, index=False)
    print(f"[Data Processing] Train/Test data saved.")

