# Visualizing clusters of customer data

import seaborn as sns
import matplotlib.pyplot as plt


def visualize_clusters(customer_df):
    sns.scatterplot(x='TotalSpend', y='PurchaseFrequency', hue='Cluster', data=customer_df, palette='viridis')
    plt.title('Customer Segmentation')
    plt.savefig('output/customer_segmentation.png')
    plt.show()


def cluster_summary(customer_df):
    summary = customer_df.groupby('Cluster').mean()
    print(summary)
