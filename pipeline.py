import kfp
from kfp import dsl

# Define your image names or registry paths
combined_image = "your-combined-image:latest"

# Define combined data_filter and data_balanced task
@dsl.component
def data_filter_and_balance_task(file_path: str):
    return dsl.ContainerOp(
        name="data-filter-and-balance",
        image=combined_image,
        command=["python", "/code/data_filter_and_balance.py"],
        arguments=["--file-path", file_path],
    )

# Define preprocess_text_data task
@dsl.component
def preprocess_text_data_task(df_balanced: kfp.dsl.InputPath("File")):
    return dsl.ContainerOp(
        name="preprocess-text-data",
        image=combined_image,
        command=["python", "/code/preprocess_text_data.py"],
        arguments=["--df-balanced", df_balanced],
    )

# Define train_lstm_model task
@dsl.component
def train_lstm_model_task(X_train: kfp.dsl.InputPath("File"), Y_train: kfp.dsl.InputPath("File")):
    return dsl.ContainerOp(
        name="train-lstm-model",
        image=combined_image,
        command=["python", "/code/train_lstm_model.py"],
        arguments=["--X-train", X_train, "--Y-train", Y_train],
    )

# Define the main pipeline
@dsl.pipeline(
    name="Text Classification Pipeline",
    description="A Kubeflow pipeline for text classification."
)
def text_classification_pipeline(file_path: str):
    data_filter_and_balance = data_filter_and_balance_task(file_path)
    preprocess_text_data = preprocess_text_data_task(data_filter_and_balance.output)
    train_model = train_lstm_model_task(preprocess_text_data.output, preprocess_text_data.output)

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(text_classification_pipeline, "text_classification_pipeline.yaml")
