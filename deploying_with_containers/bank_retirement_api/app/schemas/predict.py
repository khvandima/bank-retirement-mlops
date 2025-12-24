from typing import Any, List, Optional
from pydantic import BaseModel
from bank_classification_model.processing.validation import BankRetirementDataInputsSchema


class PredictionResults(BaseModel):

    errors: Optional[Any] = None
    version: str
    predictions: Optional[List[int]]


class MultipleBankRetirementDataInputs(BaseModel):

    inputs: List[BankRetirementDataInputsSchema]

    class Config:
        schema_extra = {
            'example': {
                'inputs': [
                    {
                        'Age': 39.1807143,
                        'Savings': 322349.874
                    }
                ]
            }
        }
