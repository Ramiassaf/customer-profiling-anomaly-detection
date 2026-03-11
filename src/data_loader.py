import pandas as pd
import numpy as np

# Load the dataset
def load_data(path):
    """
    load the data set 
    """
    df = pd.read_csv(path)
    return df
    

def data_overview(df):

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    
    print("\nUnique Customers:")
    print(df["ACCOUNTNO"].nunique())

    # Average Transaction per Customers
    print("\nAverage Transaction per Customers:",len(df)/ df['ACCOUNTNO'].nunique())