from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from bank_classification_model.config.core import config


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    input_data.rename(columns=config.model_config.variables_to_rename, inplace=True)
    validated_data = input_data[config.model_config.features].copy()

    errors = None

    try:
        MultipleBankRetirementDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records"),
        )

    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class BankRetirementDataInputsSchema(BaseModel):
    Age: Optional[float]
    Savings: Optional[float]


class MultipleBankRetirementDataInputs(BaseModel):
    inputs: List[BankRetirementDataInputsSchema]
