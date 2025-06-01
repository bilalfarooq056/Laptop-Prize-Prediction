# 💻 Laptop Price Prediction using Machine Learning

This project aims to predict laptop prices based on their specifications using a Decision Tree model. It was developed as part of a Machine Learning course to explore how well ML can estimate the value of tech products using real-world data.

## 📌 Project Overview

Laptop prices vary significantly depending on features such as RAM, screen size, resolution, storage capacity, and processor type. In this project, we:
- Extracted product data from Pakistani tech sites: **Paklab** and **Mega.pk**
- Cleaned, merged, and preprocessed the data
- Performed exploratory data analysis (EDA) and handled outliers
- Built and evaluated a **Decision Tree Regression** model
- Deployed the model using **Streamlit** for user-friendly price prediction

## 🗂 Files Included

- `1st_file.ipynb` – Initial data extraction, cleaning, and preprocessing steps
- `Final_version_Project.ipynb` – Complete EDA, modeling, evaluation, and final implementation
- `PAI Project presentation.pptx` – Project presentation slides (summary of objectives, methods, and results)

## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy** – Data manipulation
- **Matplotlib, Seaborn** – Visualization
- **Scikit-learn** – Machine Learning (Decision Tree)
- **Streamlit** – Web-based deployment

## 📊 Highlights

- Cleaned and merged datasets from two different sources
- Applied **IQR** method to detect and remove outliers
- Built an interpretable and efficient Decision Tree model
- Created an interactive web app to predict laptop prices

## 🚀 Run Locally

To run the project locally:

```bash
git clone https://github.com/bilalfarooq056/laptop-price-prediction.git
cd laptop-price-prediction
pip install -r requirements.txt
streamlit run Final_version_Project.ipynb
