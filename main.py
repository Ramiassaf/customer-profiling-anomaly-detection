from src.data_loader import load_data
from src.preprocessing import clean_transaction_amounts, fill_transaction_na, convert_dates
from src.feature_engineering import build_customer_features


def main():

    print("Loading data...")
    df = load_data()

    print("Preprocessing data...")
    df = clean_transaction_amounts(df)
    df = fill_transaction_na(df)
    df = convert_dates(df)

    print("Building customer features...")
    customer_df = build_customer_features(df)

    print("Dataset ready.")
    print(customer_df.head())


if __name__ == "__main__":
    main()