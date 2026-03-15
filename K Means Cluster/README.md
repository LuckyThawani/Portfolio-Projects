# K-Means Clustering: Age vs Income Segmentation

## Overview

This project demonstrates how to apply **K-Means Clustering** using
Python to segment individuals based on **Age** and **Income**.

The notebook walks through the full workflow of an unsupervised machine
learning project: 1. Loading and exploring the dataset 2. Visualizing
the relationship between age and income 3. Applying K-Means clustering
4. Scaling the data using MinMaxScaler 5. Re-running clustering on
normalized data 6. Using the Elbow Method to determine the optimal
number of clusters

The goal is to group individuals with similar characteristics into
clusters.

------------------------------------------------------------------------

## Dataset

The dataset used is **income.csv**, which contains the following
columns:

  Column       Description
  ------------ --------------------------
  Age          Age of the individual
  Income(\$)   Annual income in dollars

Example:

  Age   Income(\$)
  ----- ------------
  25    40000
  30    50000
  40    65000

------------------------------------------------------------------------

## Project Workflow

### 1. Import Required Libraries

-   pandas -- data manipulation
-   matplotlib -- data visualization
-   scikit-learn -- machine learning algorithms

``` python
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
```

------------------------------------------------------------------------

### 2. Load Dataset

``` python
df = pd.read_csv("income.csv")
```

------------------------------------------------------------------------

### 3. Data Visualization

A scatter plot is used to visualize the relationship between **Age** and
**Income**.

``` python
plt.scatter(df.Age, df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income($)')
```

------------------------------------------------------------------------

### 4. Applying K-Means Clustering

``` python
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])
df['cluster'] = y_predicted
```

Each data point now belongs to a cluster.

------------------------------------------------------------------------

### 5. Cluster Centers

``` python
km.cluster_centers_
```

These represent the **average Age and Income values** for each cluster.

------------------------------------------------------------------------

### 6. Feature Scaling

``` python
scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])
```

Scaling ensures both features contribute proportionally to clustering.

------------------------------------------------------------------------

### 7. Re-running K-Means

``` python
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])
df['cluster'] = y_predicted
```

------------------------------------------------------------------------

### 8. Elbow Method for Optimal Clusters

``` python
sse = []
k_rng = range(1,10)

for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)
```

Plotting:

``` python
plt.plot(k_rng, sse)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
```

The optimal number of clusters is typically where the curve forms an
**elbow**.

------------------------------------------------------------------------

## Project Structure

    KMeans-Age-Income-Clustering
    │
    ├── KmeansCluster_age_vs_income.ipynb
    ├── income.csv
    └── README.md

------------------------------------------------------------------------

## Requirements

Install dependencies:

``` bash
pip install pandas matplotlib scikit-learn
```

------------------------------------------------------------------------

## How to Run

1.  Clone the repository
2.  Navigate to the project folder
3.  Open Jupyter Notebook

``` bash
jupyter notebook
```

4.  Run all cells in:

```{=html}
<!-- -->
```
    KmeansCluster_age_vs_income.ipynb

------------------------------------------------------------------------

## Key Concepts Demonstrated

-   Unsupervised Learning
-   K-Means Clustering
-   Cluster Centroids
-   Feature Scaling
-   MinMax Normalization
-   Elbow Method

------------------------------------------------------------------------
