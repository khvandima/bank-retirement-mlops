import numpy as np
from sklearn.metrics import accuracy_score

from bank_classification_model.predict import make_prediction


def test_make_prediction(sample_input_data, sample_true_labels):
    # Given
    expected_no_predictions = 125

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")

    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.int64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    _predictions = list(predictions)
    y_true = sample_true_labels
    accuracy = accuracy_score(_predictions, y_true)

    assert accuracy > 0.9
