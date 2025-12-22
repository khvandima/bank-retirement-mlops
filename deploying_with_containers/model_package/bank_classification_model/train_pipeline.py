from sklearn.model_selection import train_test_split

from bank_classification_model.config.core import config
from bank_classification_model.pipeline import bank_pipe
from bank_classification_model.processing.data_manager import (
    load_dataset,
    save_pipeline,
)


def run_training() -> None:
    data = load_dataset(file_name=config.app_config.raw_data_file)

    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )

    bank_pipe.fit(X_train, y_train)

    save_pipeline(pipeline_to_persist=bank_pipe)


if __name__ == "__main__":
    run_training()
