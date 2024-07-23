# Customer-Segmentation
customer segmentation with python

*This repository includes code and documentation for performing customer segmentation analysis using transaction data. Utilizing Python and various data analysis libraries, this project provides insights into customer behavior, helping businesses tailor their strategies more effectively. Customer segmentation is essential for understanding the customer base and creating targeted marketing strategies. By segmenting customers based on purchasing behavior, businesses can identify high-value customers, understand their needs, and design focused marketing campaigns.*

This project utilizes Python to perform customer segmentation using transaction data. The main techniques employed include data preprocessing, feature engineering, and clustering algorithms. Visualizations are also provided to help interpret the segmentation results.

**Features**
      
        • Data Preprocessing: Clean and preprocess transaction data for analysis.
        
        • Feature Engineering: Calculate total spending, purchase frequency, and other relevant features.
        
        • Clustering Algorithms: Implement k-means clustering to segment customers based on their purchasing behavior.
        
        • Visualization: Generate visualizations to interpret and present the segmentation results.
        
        • Country and Product Segmentation: Additional segmentation based on country and product sales.

**DataSet**

The data set used in this project was selected from Kaggle. The dataset contains 540K Samples from the online purchasing history of 2.4K customers. 
Thanks to the relevant people for preparing this data. You can access the data set from this link. (data set is also available in the project)

https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset/data

**Elbow Method**

Elbow method is a technique used to determine the optimal number of clusters in clustering operations using the K-means algorithm. In this method, total squared errors (inertia) are calculated for different cluster numbers and visualized on a graph. The breakpoint (elbow) in the graph indicates the optimal number of clusters.

![elbow_method](https://github.com/user-attachments/assets/9927bd04-63c6-4aa3-8227-f830db0e89da)

The Elbow method graph shows how the inertia values ​​change for different cluster numbers. Usually, the elbow point on the graph represents the optimal cluster number. This point is where the inertia value decreases significantly, but after a certain point the rate of decrease slows down. For this dataset, in the above graph the optimal number of clusters appears to be 4.





**Customer Segmentation Chart**

![customer_segmentation](https://github.com/user-attachments/assets/cc6289f0-89b9-43bb-9334-c921f44a385e)

According to the customer segments seen on this chart, we can define customer segments by giving appropriate names to each cluster and specifying cluster properties. The chart divides customers into four clusters based on the values ​​of TotalSpendand PurchaseFrequency. These segments and their properties can be as follows:

   **Cluster 0 - Low Spend, Low Frequency**

   **Cluster 1 - Medium Spending, Medium Frequency**

   **Cluster 2 - High Spending, High Frequency**

   **Cluster 3 - High Spending, Low Frequency**


These segments can be used to better understand customer behavior and adjust marketing strategies accordingly. For example, special campaigns can be run to encourage customers in the Low Spend, Low Frequency segment to shop more. You can also see a list of which users are in which clusters in the **customer_clusters.txt** file.


**Counter Segmentation Chart**

![segmentation_plot](https://github.com/user-attachments/assets/971ccc1c-5794-4e48-bad5-4660b20254b5)


The provided bar chart represents country-wise total spending segmentation on a logarithmic scale. 

**High Spending Countries (Green)**

**Medium Spending Countries (Blue)**

**Low Spending Countries (Red)**

This segmentation is valuable for businesses to target their marketing and sales efforts more effectively based on the spending behavior of customers in different countries. High spending countries might be targeted for premium products or services, while medium and low spending countries might require different strategies to increase customer engagement and spending. Detailed information about which countries are in which clusters with how much spending is printed in the **segmentation_report.txt** file.


**Product Segmentation Chart**

![product_segmentation_plot](https://github.com/user-attachments/assets/98adef39-7ea6-401d-98ab-02fecdd4e7a7)


Aggregating the frequency with which the product is sold ensures accurate product advertising. You can find detailed information about which products are in which clusters in the product_segmentation_report.txt file.


*This project effectively segmented customers based on their spending behavior using transaction data. By identifying high, medium, and low spending countries, it provides actionable insights for businesses to tailor their marketing strategies. High spending countries can be targeted with premium offerings, while engagement strategies can be designed for medium and low spending countries. This data-driven approach helps businesses optimize marketing efforts and improve customer satisfaction and profitability.*
