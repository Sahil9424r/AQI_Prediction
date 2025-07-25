# 🌫️ AQI Prediction using Machine Learning

This project predicts the **Air Quality Index (AQI)** using a machine learning model trained on pollution data. A basic Flask interface is used to input values and get predictions.

## 📌 Project Goal

To build an ML model that takes air pollutant values like CO, NO2, PM2.5, etc., and predicts the AQI (Air Quality Index).

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Regressor  
- **Target**: AQI  
- **Features Used**:
  - CO (Carbon Monoxide)
  - NO2 (Nitrogen Dioxide)
  - PM2.5
  - PM10
  - O3 (Ozone)
  - SO2 (Sulfur Dioxide)
- **Model File**: `model.pkl`

## 💻 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Flask** (only for running a local form-based app)

### 🔹 Input Form  
![Input Form](Chatbotpic/aqi_input.png)

### 🔹 Prediction Result  
![Prediction Result](Chatbotpic/aqi_result.png)

