from kfp.dsl import component, Output, Dataset

@component(base_image="python:3.9")
def generate_simple_data(output_csv: Output[Dataset]):
    import subprocess
    subprocess.run(["pip", "install", "pandas", "numpy"], check=True)

    import pandas as pd
    import numpy as np    

    np.random.seed(42)
    data = {
        "bedrooms": np.random.randint(1, 5, size=100),
        "bathrooms": np.random.randint(1, 3, size=100),
        "sqft": np.random.randint(500, 3500, size=100),
        "price": np.random.randint(100000, 500000, size=100)
    }

    df = pd.DataFrame(data)
    df.to_csv(output_csv.path, index=False)
    print(f"[Data Ingestion] Data saved to: {output_csv.path}")
