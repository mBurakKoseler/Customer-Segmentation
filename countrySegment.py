import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def country_segmentation(file_path, output_path):

    df = pd.read_excel(file_path)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalSpend'] = df['Quantity'] * df['UnitPrice']

    # Total number of expenditures and purchases by country
    country_summary = df.groupby('Country').agg({'TotalSpend': 'sum', 'InvoiceNo': 'nunique'}).reset_index()
    country_summary.columns = ['Country', 'TotalSpend', 'PurchaseFrequency']

    # Sort by expenses
    country_summary = country_summary.sort_values(by='TotalSpend', ascending=False)

    # Segmentation: High, Medium and Low spending countries
    high_spending_threshold = country_summary['TotalSpend'].quantile(0.75)
    medium_spending_threshold = country_summary['TotalSpend'].quantile(0.25)

    country_summary['Segment'] = pd.cut(country_summary['TotalSpend'],
                                        bins=[-float('inf'), medium_spending_threshold, high_spending_threshold,
                                              float('inf')],
                                        labels=['Low Spending', 'Medium Spending', 'High Spending'])

    # Visualizing segments
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Country', y='TotalSpend', hue='Segment', data=country_summary, palette="Set1")
    plt.yscale('log')
    plt.xticks(rotation=90)
    plt.title('Country-wise Total Spend Segmentation (Log Scale)')
    plt.xlabel('Country')
    plt.ylabel('Total Spend (Log Scale)')
    plt.legend(title='Spending Segment')
    plt.tight_layout()
    plt.savefig('output/segmentation_plot.png')
    plt.show()

    # Print segment information to text file
    with open(output_path, 'w') as f:
        for segment in ['High Spending', 'Medium Spending', 'Low Spending']:
            f.write(f'{segment}:\n')
            segment_countries = country_summary[country_summary['Segment'] == segment]
            for _, row in segment_countries.iterrows():
                f.write(f"  {row['Country']}: {row['TotalSpend']:.2f}\n")
            f.write('\n')

    return country_summary


# Function call
file_path = 'data/dataset.xlsx'
output_path = 'output/segmentation_report.txt'
segmented_countries = country_segmentation(file_path, output_path)

