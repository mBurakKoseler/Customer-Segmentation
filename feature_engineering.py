#The function defined here calculates each customer's total spending and shopping frequency and transforms
# this information #into a new data frame.
import pandas as pd

def create_features(df):
    # Calculating total spend
    df['TotalSpend'] = df['Quantity'] * df['UnitPrice']

    # Calculating total spending and shopping frequency per customer
    customer_df = df.groupby('CustomerID').agg({
        'TotalSpend': 'sum',
        'InvoiceNo': 'count'
    }).rename(columns={'InvoiceNo': 'PurchaseFrequency'}).reset_index()

    return customer_df

#DataFrame named customer_df returned by the function contains CustomerID, TotalSpend, PurchaseFrequency values for each customer.