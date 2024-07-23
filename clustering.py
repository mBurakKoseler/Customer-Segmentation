# K-means algorithm is a clustering algorithm widely used in data mining and machine learning. K-means aims to separate
# data points into k clusters. Each cluster is determined based on the similarity of data points, and each data point
# is assigned to the centroid of the cluster to which it is closest.

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Feature Scaling, Standardizing transforms the data to have a mean of 0 and a standard deviation of 1. In this way,
# the data is brought to the same scale and the model works better with data at different scales.
def scale_features(customer_df):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(customer_df[['TotalSpend', 'PurchaseFrequency']])
    return scaled_features


# Elbow Method used to determine the optimal number of clusters
def find_optimal_clusters(data):
    inertia = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertia.append(kmeans.inertia_)

    plt.plot(range(1, 11), inertia)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.savefig('output/elbow_method.png')
    plt.show()


def apply_kmeans(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    return kmeans.labels_
