from typing import Generator
import pandas as pd
from sklearn.model_selection import train_test_split
import pytest
from fastapi.testclient import TestClient
from bank_classification_model.config.core import config
from bank_classification_model.preprocessing.data_manager import load_dataset
from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    data = load_dataset(file_name=config.app_config.raw_data_file)

    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )

    return X_test


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
