import pandas as pd
from sklearn.preprocessing import StandardScaler


def clean_transaction_amounts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert deposit and withdrawal columns to numeric values.
    Removes commas and converts strings to numbers.
    """

    df["DEPOSITAMT"] = df["DEPOSITAMT"].astype(str).str.replace(",", "")
    df["WITHDRAWALAMT"] = df["WITHDRAWALAMT"].astype(str).str.replace(",", "")

    df["DEPOSITAMT"] = pd.to_numeric(df["DEPOSITAMT"], errors="coerce")
    df["WITHDRAWALAMT"] = pd.to_numeric(df["WITHDRAWALAMT"], errors="coerce")

    return df


def fill_transaction_na(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing deposit and withdrawal values with 0.
    """

    df["DEPOSITAMT"] = df["DEPOSITAMT"].fillna(0)
    df["WITHDRAWALAMT"] = df["WITHDRAWALAMT"].fillna(0)

    return df


def convert_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert transaction date columns to datetime format.
    """

    df["TRANSDATE"] = pd.to_datetime(df["TRANSDATE"])
    df["VALUEDATE"] = pd.to_datetime(df["VALUEDATE"])

    return df


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """
    One-hot encode categorical variables.
    """

    df_encoded = pd.get_dummies(df)

    return df_encoded


def scale_features(df: pd.DataFrame, feature_columns: list):
    """
    Scale numerical features using StandardScaler.
    """

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(df[feature_columns])

    return X_scaled, scaler