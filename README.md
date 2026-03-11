# Customer Profiling & Anomaly Detection

This project analyzes banking transaction and customer demographic data to identify behavioral customer segments and detect potentially anomalous individuals.

The objective is to transform transaction level banking data into **customer behavioral profiles** and uncover patterns in financial activity.

---

## Dataset Overview

The dataset contains banking transaction records combined with customer demographic and relationship attributes.

- **116,201 transactions**
- **7,260 unique customers**

The data includes:

Transaction features  
- ACCOUNTNO  
- TRANSDATE  
- DEPOSITAMT  
- WITHDRAWALAMT  

Customer attributes  
- CUSTOMER_AGE  
- GENDER  
- EDUCATION_LEVEL  
- MARITAL_STATUS  
- INCOME_CATEGORY  
- CARD_CATEGORY  

Bank relationship features  
- CREDIT_LIMIT  
- TOTAL_REVOLVING_BAL  
- MONTHS_ON_BOOK  

---

## Methodology

The analysis follows four main steps:

### 1. Feature Engineering
Transaction-level data was aggregated to create customer-level behavioral features:

- total_deposit  
- total_withdrawal  
- average_deposit  
- average_withdrawal  
- transaction_count  
- net_flow  

These features summarize customer financial behavior.

---

### 2. Anomaly Detection
An **Isolation Forest** model was used to identify customers whose financial activity significantly deviates from the majority.

Approximately **2% of customers were identified as anomalous**.

---

### 3. Customer Segmentation
Customer segmentation was performed using **K-Means clustering**, which grouped customers into behavioral segments based on their financial activity.

---

### 4. Visualization
**Histogram** was used to show the distribution of transaction_count, total_deposit, CREDIT_LIMIT of the Customers
**Principal Component Analysis (PCA)** was used to project the high-dimensional feature space into two dimensions for visualization of clusters and anomalies.

---

---
## Project Structure
```
project/
│
├── notebooks/
│ 01_data_understanding.ipynb
│ 02_modelling_and_analysis.ipynb
│
├── src/
│ data_loader.py
│ preprocessing.py
│ feature_engineering.py
│ anomaly_detection.py
│ clustering.py
│
├── main.py
└── README.md

```
---


- **notebooks/** → exploratory analysis and modeling workflow  
- **src/** → reusable pipeline modules  
- **main.py** → example script to run the pipeline  

---

## How to Clone the Repository

To clone this repository locally:

```bash
git clone https://github.com/Ramiassaf/customer-profiling-anomaly-detection.git

Author
Rami Assaf
