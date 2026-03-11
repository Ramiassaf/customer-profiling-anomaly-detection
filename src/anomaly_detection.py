from sklearn.ensemble import IsolationForest


def detect_anomalies(X, contamination=0.02, random_state=42):
    """
    Detect anomalous customers using Isolation Forest.

    Parameters
    ----------
    X : Scaled feature matrix
    contamination : Expected proportion of anomalies
    random_state : Random seed for reproducibility

    Returns
    -------
    anomalies : Isolation Forest predictions
        (-1 = anomaly, 1 = normal)l
    """

    model = IsolationForest(
        n_estimators=200,
        contamination=contamination,
        random_state=random_state
    )

    anomalies = model.fit_predict(X)

    return anomalies, model