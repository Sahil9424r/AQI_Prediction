# 🌫️ AQI Prediction using Machine Learning

This project predicts the **Air Quality Index (AQI)** using a machine learning model trained on pollution data from Indian cities. A simple Flask interface is used to input pollutant values and get the predicted AQI.

---

## 📊 Dataset Used

- **Source**: [Air Quality Data in India – Kaggle](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)  
- **File Used**: `city_day.csv`  
- **Description**: Contains daily air quality data from multiple cities in India, including values for PM2.5, PM10, NO2, SO2, CO, O3, and calculated AQI.

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Regressor  
- **Target**: AQI  
- **Input Features**:
  - CO (Carbon Monoxide)
  - NO2 (Nitrogen Dioxide)
  - PM2.5
  - PM10
  - O3 (Ozone)
  - SO2 (Sulfur Dioxide)
- **Model File**: `model.pkl`

---

## 💻 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Flask** *(used only to run the local form interface)*

### 🔹 Input Form  
![Input Form](Chatbotpic/aqi_input.png)

### 🔹 Prediction Result  
![Prediction Result](Chatbotpic/aqi_result.png)
