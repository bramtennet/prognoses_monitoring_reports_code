import unittest
import pandas as pd

from prognoses_monitoring_reports_code.automatic_checks.automatic_sanity_check import (
    automatic_check_forecast_da,
    check_if_predicted_is_suspicious,
)


class TestAutomaticSanityChecks(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_passeble(self):
        # Arrange
        ean = 123
        predicted = pd.DataFrame(
            data={"predicted": [0.8, -0.8, 7.5, 8, 9], "realised": [1, -1, 9, 9, 9]}
        )
        expected_reasons = []

        # Act
        report = check_if_predicted_is_suspicious(
            predicted["realised"], predicted["predicted"], ean
        )

        # Assert
        assert report.something_wrong == False
        assert report.ean == ean
        assert report.reasons == expected_reasons

    def test_zeros(self):
        # Arrange
        ean = 123
        predicted = pd.DataFrame(
            data={"predicted": [0, 0, 0, 0, 0], "realised": [9, 9, 9, 9, 9]}
        )
        expected_reasons = [
            "Error is larger than half the range of the realised values.",
            "Mean of predicted values is outside range realised.",
            "Predicted is series of zeros.",
        ]

        # Act
        report = check_if_predicted_is_suspicious(
            predicted["realised"], predicted["predicted"], ean
        )

        # Assert
        assert report.something_wrong == True
        assert report.ean == ean
        assert report.reasons == expected_reasons

    def test_too_small_range(self):
        # Arrange
        ean = 123
        predicted = pd.DataFrame(
            data={"predicted": [1, 2, 1, 2, 1], "realised": [-3, -5, 9, 8, 20]}
        )
        expected_reasons = [
            "Range of predicted less than half of the range of the realised values."
        ]

        # Act
        report = check_if_predicted_is_suspicious(
            predicted["realised"], predicted["predicted"], ean
        )

        # Assert
        assert report.something_wrong == True
        assert report.ean == ean
        assert report.reasons == expected_reasons

    def test_polarity_switched(self):
        # Arrange
        ean = 123
        predicted = pd.DataFrame(
            data={"predicted": [-1, -1, -1, -1, -1], "realised": [1, 1, 1, 1, 1]}
        )
        expected_reasons = [
            "Polarity probably inverted.",
            "Error is larger than half the range of the realised values.",
            "Mean of predicted values is outside range realised.",
        ]

        # Act
        report = check_if_predicted_is_suspicious(
            predicted["realised"], predicted["predicted"], ean
        )

        # Assert
        assert report.something_wrong == True
        assert report.ean == ean
        assert report.reasons == expected_reasons
