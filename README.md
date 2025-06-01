
---

# 💻 Laptop Price Prediction using Machine Learning

This project demonstrates how machine learning can be used to estimate laptop prices based on their specifications. Built as part of a Machine Learning course, the project primarily focuses on data preprocessing and building a basic regression model to explore the potential of ML in real-world pricing tasks.

## 📌 Project Overview

Laptop prices in Pakistan vary significantly based on features such as RAM, processor type, screen size, resolution, and storage. In this project, we:

* Extracted product listings from local e-commerce websites: **Paklap** and **Mega.pk**
* Cleaned, merged, and preprocessed the datasets to ensure consistency
* Performed exploratory data analysis (EDA), visualized trends, and handled outliers
* Implemented a **basic Decision Tree Regression** model as a proof of concept
* Deployed the model using **Streamlit** for interactive, user-friendly predictions

> ⚠️ **Note:** This is a foundational-level ML project. The model is kept simple and was not optimized for high accuracy. The main goal was to understand the end-to-end ML pipeline.

## 🗂 Files Included

* `1st_file.ipynb` – Data collection, cleaning, and early preprocessing
* `Final_version_Project.ipynb` – Full EDA, basic model building, and Streamlit deployment
* `PAI Project presentation.pptx` – Summary presentation covering methodology and results

## ⚙️ Tech Stack

* **Python**
* **Pandas, NumPy** – Data manipulation
* **Matplotlib, Seaborn** – Visualization and EDA
* **Scikit-learn** – Machine Learning (Decision Tree Regressor)
* **Streamlit** – Web-based app deployment

## 📊 Highlights

* Merged and standardized datasets from two separate sources
* Applied **IQR** method to identify and remove outliers
* Conducted comprehensive EDA to understand key pricing factors
* Built an interactive Streamlit app for predicting laptop prices based on selected specifications

## 🚀 Run Locally

To run the project locally:

```bash
git clone https://github.com/bilalfarooq056/laptop-price-prediction.git
cd laptop-price-prediction
pip install -r requirements.txt
streamlit run Final_version_Project.ipynb
```

---

