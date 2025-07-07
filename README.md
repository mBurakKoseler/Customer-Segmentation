# 🧠 Customer Segmentation with Python

This repository includes code and documentation for performing **customer segmentation analysis using transaction data**.  
Utilizing Python and various data science libraries, this project provides actionable insights into customer behavior — helping businesses **identify high-value customers**, **understand their spending habits**, and **design targeted marketing strategies**.

---

## 📊 Project Overview

Customer segmentation is essential for understanding a business's customer base and optimizing marketing efforts.  
In this project, customer behavior is analyzed based on **total spend**, **purchase frequency**, **country**, and **product preferences**, with clear visualizations for each segment.

---

## 🚀 Features

- 🔄 **Data Preprocessing**: Clean and transform transaction data  
- 🧮 **Feature Engineering**: Calculate total spending, purchase frequency, and more  
- 🔍 **Clustering**: Segment customers using K-Means algorithm  
- 🌍 **Country-Based Segmentation**  
- 📦 **Product-Based Segmentation**  
- 📈 **Visualizations**: Graphical insights for all segmentations

---

## 📂 Dataset

The dataset was obtained from Kaggle:  
🔗 https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset/data  
It contains **540K transactions** from the **online purchasing history of 2.4K customers**.

> The dataset is also included in this repository under the `data/` folder as `dataset.xlsx`.

---

## ⚙️ How to Run

1. Install required packages:

```bash
pip install pandas matplotlib seaborn scikit-learn openpyxl
```

2. Run the main analysis script:

```bash
python main.py
```

3. Segment results and charts will be generated.

---

## 📌 Clustering Method: Elbow Method

The **Elbow Method** is used to determine the optimal number of clusters in K-Means.  
It plots the **inertia (total squared error)** for various `k` values and detects where the drop in inertia slows down (the “elbow”).

![elbow_method](https://github.com/user-attachments/assets/9927bd04-63c6-4aa3-8227-f830db0e89da)

In this dataset, the optimal number of clusters is determined to be **4**.

---

## 👥 Customer Segmentation Chart

![customer_segmentation](https://github.com/user-attachments/assets/cc6289f0-89b9-43bb-9334-c921f44a385e)

Customers are grouped into 4 clusters based on **Total Spend** and **Purchase Frequency**:

- **Cluster 0** – Low Spend, Low Frequency  
- **Cluster 1** – Medium Spend, Medium Frequency  
- **Cluster 2** – High Spend, High Frequency  
- **Cluster 3** – High Spend, Low Frequency  

> The file `customer_clusters.txt` contains detailed listings of which users belong to which cluster.

---

## 🌍 Country Segmentation Chart

![segmentation_plot](https://github.com/user-attachments/assets/971ccc1c-5794-4e48-bad5-4660b20254b5)

This bar chart represents **total spending per country** on a logarithmic scale.

- 🟩 High Spending Countries  
- 🟦 Medium Spending Countries  
- 🟥 Low Spending Countries  

> The `segmentation_report.txt` file includes country-wise segmentation results and spend amounts.

This segmentation is valuable for:

- Targeting premium products to high-spending countries  
- Developing growth strategies for medium/low spending regions

---

## 📦 Product Segmentation Chart

![product_segmentation_plot](https://github.com/user-attachments/assets/98adef39-7ea6-401d-98ab-02fecdd4e7a7)

Segmenting products based on purchase frequency enables **smarter product promotion** and **category targeting**.

> Product segmentation results are saved in `product_segmentation_report.txt`.

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

---

## ✅ Summary

This project demonstrates how **clustering algorithms and behavioral features** can be used to meaningfully segment customers.  
By identifying customer clusters based on spending habits, businesses can:

- Tailor marketing and pricing strategies  
- Prioritize loyal or high-value customers  
- Identify opportunities for growth across product lines and geographies

📈 **Understand your customers → Segment them smartly → Drive business value**
