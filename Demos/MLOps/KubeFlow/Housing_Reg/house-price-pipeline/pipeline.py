from kfp import dsl, compiler
from components.data_ingestion import generate_simple_data
from components.data_processing import process_data
from components.model_training import train_model
from components.model_evaluation import evaluate_model

@dsl.pipeline(name="house-price-prediction-pipeline")
def house_price_pipeline():
    data_ingestion_task = generate_simple_data()
    data_processing_task = process_data(input_csv=data_ingestion_task.outputs["output_csv"])
    model_training_task = train_model(train_csv=data_processing_task.outputs["train_data"])
    evaluate_model(test_csv=data_processing_task.outputs["test_data"], model=model_training_task.outputs["saved_model_output"])

if __name__ == "__main__":
    compiler.Compiler().compile(pipeline_func=house_price_pipeline, package_path="kubeflow_pipeline.yaml")

