import logging
from typing import List

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from bank_classification_model import __version__ as _version
from bank_classification_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


logger = logging.getLogger(__name__)


def load_dataset(*, file_name: str) -> pd.DataFrame:
    dataframe = pd.read_csv(f"{DATASET_DIR}/{file_name}")
    renamed_data = dataframe.rename(columns=config.model_config.variables_to_rename)
    return renamed_data


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"

    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])

    joblib.dump(pipeline_to_persist, save_path)


def remove_old_pipelines(*, files_to_keep: List[str]) -> None:
    do_not_delete = files_to_keep + ["__init__.py"]

    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()


def load_pipeline(*, file_name: str) -> Pipeline:
    file_path = TRAINED_MODEL_DIR / file_name
    return joblib.load(filename=file_path)
