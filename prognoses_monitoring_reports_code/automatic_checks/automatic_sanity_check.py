import pandas as pd
import numpy as np


class CheckReport:
    def __init__(self, ean: int):
        self.ean = ean
        self.something_wrong = False
        self.reasons = []

    def add_check_failed(self, reason: str) -> None:
        self.something_wrong = True
        self.reasons.append(reason)


def automatic_check_forecast_da(df_month, ean):
    """Initialises automatic check

    Args:
        df_month: pd.Dataframe with timeseries data for specific ean
        ean: EAN of connection point.

    Returns: Checkreport object that indicates if any checks failed and for what reason.

    """
    time_combined = df_month[df_month["Connection point EAN"] == ean][
        ["Realised [MW]", "Prognosis [MW] (DA)", "Prognosis [MW] (ID)"]
    ]

    return check_if_predicted_is_off(
        time_combined["Realised [MW]"], time_combined["Prognosis [MW] (DA)"], ean
    )


def check_if_predicted_is_off(
    realised: pd.Series, predicted: pd.Series, ean: int
) -> CheckReport:
    """Simple function to check forecasts on a few basic rules

    Args:
        realised: realised values
        predicted: predicted value
        ean: ean of specific connection

    Returns: Checkreport object that indicates if any checks failed and for what reason.

    """

    # Initialize report
    report = CheckReport(ean)

    # Check polarity of prediction
    if realised.corr(predicted) < -0.5:
        report.add_check_failed(
            reason=f"Polarity probably switched, correlation coeficient: {realised.corr(predicted)}"
        )

    # Check for extremely large error
    if (realised - predicted).abs().mean() > np.abs(
        (realised.max() - realised.min())
    ) * 0.5:
        report.add_check_failed(
            reason="Error is larger than half the range of the realised values!"
        )
    # Check if predicted mean fall within any of the realised values
    if predicted.mean() > realised.max() or predicted.mean() < realised.min():
        report.add_check_failed(
            reason="Mean of predicted values is outside range realised!"
        )

    # Check if the predicted range is not tiny with respect to the realised range
    if (
        np.abs(predicted.max() - predicted.min())
        < np.abs((realised.max() - realised.min())) * 0.5
    ):
        report.add_check_failed(
            reason="Range of predicted less than half of the range of the realised values!"
        )

    # Check if predicted consists of a series of zeros
    if (predicted.mean() == 0) and (realised.mean() != 0):
        report.add_check_failed(reason="Predicted is series of zeros!")

    return report
