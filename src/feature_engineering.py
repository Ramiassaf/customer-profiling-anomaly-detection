import pandas as pd


def build_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert transaction-level dataset into customer-level features.
    """

    # Aggregate transaction behavior
    customer_transactions = df.groupby("ACCOUNTNO").agg(
        total_deposit=("DEPOSITAMT", "sum"),
        total_withdrawal=("WITHDRAWALAMT", "sum"),
        average_deposit=("DEPOSITAMT", "mean"),
        average_withdrawal=("WITHDRAWALAMT", "mean"),
        transaction_count=("ACCOUNTNO", "count")
    ).reset_index()

    # Create net flow feature
    customer_transactions["net_flow"] = (
        customer_transactions["total_deposit"]
        - customer_transactions["total_withdrawal"]
    )

    # Extract customer demographic information
    customer_profile = df.groupby("ACCOUNTNO").first().reset_index()

    customer_profile = customer_profile.drop(
        ["TRANSDATE", "VALUEDATE", "TRANSACTIONDETAILS", "WITHDRAWALAMT", "DEPOSITAMT"],
        axis=1
    )

    # Merge behavioral and demographic features
    customer_df = customer_profile.merge(
        customer_transactions,
        on="ACCOUNTNO",
        how="left"
    )

    return customer_df