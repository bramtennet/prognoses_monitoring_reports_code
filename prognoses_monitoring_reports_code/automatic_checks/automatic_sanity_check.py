import pandas as pd
import numpy as np
import openstef.metrics.metrics as metrics


MINIMAL_R_MAE: float = 0.15
MINIMAL_SKILL_SCORE: float = 0.6


class CheckReport:
    def __init__(self, ean: int):
        self.ean = ean
        self.reasons = []

    @property
    def something_wrong(self):
        return len(self.reasons) != 0

    def add_check_failed(self, reason: str) -> None:

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

    return check_if_predicted_is_suspicious(
        time_combined["Realised [MW]"], time_combined["Prognosis [MW] (DA)"], ean
    )


def check_if_predicted_is_suspicious(
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
    if realised.corr(predicted) < -0.5 or (
        (realised - predicted).abs().mean() > (realised + predicted).abs().mean()
    ):
        report.add_check_failed(reason=f"Polarity probably inverted")

    # Check for extremely large error
    if (realised - predicted).abs().mean() > np.abs(
        (realised.max() - realised.min())
    ) * 0.5:
        report.add_check_failed(
            reason="Error is larger than half the range of the realised values"
        )
    # Check if predicted mean fall within any of the realised values
    if predicted.mean() > realised.max() or predicted.mean() < realised.min():
        report.add_check_failed(
            reason="Mean of predicted values is outside range realised"
        )

    # Check if the predicted range is not tiny with respect to the realised range
    if (
        np.abs(predicted.max() - predicted.min())
        < np.abs((realised.max() - realised.min())) * 0.5
    ):
        report.add_check_failed(
            reason="Range of predicted less than half of the range of the realised values"
        )

    # Check if predicted consists of a series of zeros
    if (predicted.mean() == 0) and (realised.mean() != 0):
        report.add_check_failed(reason="Predicted is series of zeros")

    return report


def check_quality_sufficient(
    realised: pd.Series, predicted: pd.Series, ean: int
) -> CheckReport:

    # Initialize report
    report = CheckReport(ean)

    # Format data to fit the metric functions in openSTEF
    realised = realised.rename("load")

    # Create a basecase forecast by shifting the realised load 7 days (7*96 PTU's)
    basecase = realised.copy(deep=True).rename("basecase")
    basecase.index = basecase.index - (7 * 96)

    # Combine everything and perform an "inner" join as we do not have a basecase for the first week
    combined = pd.concat(
        [realised, predicted.rename("predicted"), basecase], axis=1, join="inner"
    ).dropna()

    # Calucaltate metrics
    skill_score = metrics.skill_score(
        combined["load"], combined["predicted"], combined["basecase"]
    )
    skill_score_positive_peaks = metrics.skill_score_positive_peaks(
        combined["load"], combined["predicted"], combined["basecase"]
    )
    r_mae = metrics.r_mae(combined["load"], combined["predicted"])

    # Cary out checks on calculated metrics
    if r_mae > MINIMAL_R_MAE:
        report.add_check_failed(reason="rMAE below 15%")

    if (
        skill_score < MINIMAL_SKILL_SCORE
        and skill_score_positive_peaks < MINIMAL_SKILL_SCORE
    ):
        report.add_check_failed(
            reason="Skill score or Skill score positive peaks bellow 0.6"
        )

    return report
