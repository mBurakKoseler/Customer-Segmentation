from data_preprocessing import load_and_clean_data
from feature_engineering import create_features
from clustering import scale_features, find_optimal_clusters, apply_kmeans
from visualization import visualize_clusters, cluster_summary
from countrySegment import country_segmentation

# Load and clear data
df = load_and_clean_data('data/dataset.xlsx')

# Do feature engineering
customer_df = create_features(df)

# Standardize features
scaled_features = scale_features(customer_df)

# Determine the appropriate number of clusters
find_optimal_clusters(scaled_features)

# For example, training the model using 4 clusters
customer_df['Cluster'] = apply_kmeans(scaled_features, 4)

# Visualize and summarize results
visualize_clusters(customer_df)
cluster_summary(customer_df)

# See which customer IDs are in each cluster
clusters = customer_df.groupby('Cluster')['CustomerID'].apply(list)


# Print the results to a text file
with open('output/customer_clusters.txt', 'w') as f:
    for cluster_id, customer_ids in clusters.items():
        f.write(f"Cluster {cluster_id}: {customer_ids}\n")
