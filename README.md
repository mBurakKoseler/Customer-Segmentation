# Customer-Segmentation
customer segmentation with python

This repository contains all the necessary code and documentation to perform customer segmentation analysis using transaction data. By leveraging Python and various data analysis libraries, this project aims to provide insights into customer behavior, enabling businesses to tailor their strategies more effectively. Customer segmentation is a crucial task for businesses looking to understand their customer base and tailor their marketing strategies accordingly. By segmenting customers based on their purchasing behavior, businesses can identify high-value customers, understand their needs, and design targeted marketing campaigns.

This project utilizes Python to perform customer segmentation using transaction data. The main techniques employed include data preprocessing, feature engineering, and clustering algorithms. Visualizations are also provided to help interpret the segmentation results.

**Features**
 > Data Preprocessing: Clean and preprocess transaction data for analysis.
 > Feature Engineering: Calculate total spending, purchase frequency, and other relevant features.
 > Clustering Algorithms: Implement k-means clustering to segment customers based on their purchasing behavior.
 > Visualization: Generate visualizations to interpret and present the segmentation results.
 > Country and Product Segmentation: Additional segmentation based on country and product sales.

**DataSet**
The data set used in this project was selected from Kaggle. The dataset contains 540K Samples from the online purchasing history of 2.4K customers. https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset/data
Thanks to the relevant people for preparing this data. You can access the data set from this link. (data set is also available in the project)

**Elbow Method**
Elbow method is a technique used to determine the optimal number of clusters in clustering operations using the K-means algorithm. In this method, total squared errors (inertia) are calculated for different cluster numbers and visualized on a graph. The breakpoint (elbow) in the graph indicates the optimal number of clusters.

![elbow_method](https://github.com/user-attachments/assets/9927bd04-63c6-4aa3-8227-f830db0e89da)

The Elbow method graph shows how the inertia values ​​change for different cluster numbers. Usually, the elbow point on the graph represents the optimal cluster number. This point is where the inertia value decreases significantly, but after a certain point the rate of decrease slows down. For this dataset, in the above graph the optimal number of clusters appears to be 4.

