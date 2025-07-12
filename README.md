# 🌾 Crop Prediction Web App

A machine learning-based web application that helps farmers and agricultural stakeholders predict the most suitable crop to cultivate based on soil and environmental conditions. The app was built using Streamlit for interactive deployment.

## 📊 Project Overview

The app aims to:
- Recommend the best crop to grow based on inputs like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall.
- Provide a user-friendly interface for easy access to predictions.
- Promote data-driven smart farming decisions.

## 🧠 Machine Learning Model

- **Algorithm Used:** Support Vector Machine (SVM) with a linear kernel.
- **Dataset:** Crop Recommendation Dataset from [Kaggle](https://www.kaggle.com/datasets)
- **Features Used:**
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - pH
  - Rainfall (mm)
- **Target Variable:** Crop Label (e.g., rice, maize, cotton)


## 🔧 Tech Stack

- **Python** – Programming language
- **Scikit-learn** – ML model training
- **Flask** – Web framework for backend
- **HTML, CSS** – Frontend UI
- **Jinja2** – For rendering dynamic HTML content

## 🚀 Features

- Simple form input to collect soil and weather conditions.
- Instant prediction of the best crop based on input values.
- Clean and intuitive UI with Streamlit.
- Lightweight and fast model integration.

## 🔍 Sample Input Fields

```text
Nitrogen: 90  
Phosphorus: 42  
Potassium: 43  
Temperature: 22°C  
Humidity: 80%  
pH: 6.5  
Rainfall: 200 mm
