import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:

    # Given
    payload = {
        'inputs': test_data.replace({np.nan: None}).to_dict(orient='records'),
    }

    # When
    response = client.post(
        'https://localhost:8001/api/v1/predict',
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data['predictions']
    assert prediction_data['errors'] is None
    valid_classes = [0, 1]
    print(prediction_data['predictions'])
    for prediction in prediction_data['predictions']:
        assert prediction in valid_classes, f"Invalid prediction: {prediction}"
