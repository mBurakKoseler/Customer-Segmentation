import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # backend setting

def product_segmentation(file_path, output_path, plot_path):

    df = pd.read_excel(file_path)
    df['TotalQuantity'] = df['Quantity']

    # Total sales amount by product
    product_summary = df.groupby('StockCode').agg({'TotalQuantity': 'sum'}).reset_index()
    product_summary.columns = ['StockCode', 'TotalQuantity']

    # Sort by sales amounts
    product_summary = product_summary.sort_values(by='TotalQuantity', ascending=False)

    # Segmentation: Top, normal and least sold products
    high_selling_threshold = product_summary['TotalQuantity'].quantile(0.75)
    low_selling_threshold = product_summary['TotalQuantity'].quantile(0.25)

    product_summary['Segment'] = pd.cut(product_summary['TotalQuantity'],
                                        bins=[-float('inf'), low_selling_threshold, high_selling_threshold, float('inf')],
                                        labels=['Low Selling', 'Medium Selling', 'High Selling'])

    # Group segments and calculate total sales amount
    segment_summary = product_summary.groupby('Segment').agg({'TotalQuantity': 'sum'}).reset_index()

    # Visualizing segments
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Segment', y='TotalQuantity', data=segment_summary, palette="Set1")
    plt.title('Product-wise Total Quantity Sold Segmentation')
    plt.xlabel('Selling Segment')
    plt.ylabel('Total Quantity Sold')
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()

    # Print segment information to text file
    with open(output_path, 'w') as f:
        for segment in ['High Selling', 'Medium Selling', 'Low Selling']:
            f.write(f'{segment}:\n')
            segment_products = product_summary[product_summary['Segment'] == segment]
            for _, row in segment_products.iterrows():
                f.write(f"  {row['StockCode']}: {row['TotalQuantity']}\n")
            f.write('\n')

    return product_summary


file_path = 'data/dataset.xlsx'
output_path = 'output/product_segmentation_report.txt'
plot_path = 'output/product_segmentation_plot.png'
segmented_products = product_segmentation(file_path, output_path, plot_path)
print(segmented_products)
