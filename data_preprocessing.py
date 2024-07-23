#The function defined here includes the pre-processing steps to be performed on the data set.

import pandas as pd


def load_and_clean_data(filepath):
    df = pd.read_excel(filepath, engine='openpyxl')

    # Removes rows with missing values from the dataframe w/pandas .
    df.dropna(subset=['CustomerID'], inplace=True)

    # Removes any quantity or price that is negative or equal to 0.
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    return df
