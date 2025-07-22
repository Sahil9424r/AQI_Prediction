from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

def load_model():
    with open('aqi_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    PM2_5 = float(request.form['PM2.5'])
    NO2 = float(request.form['NO2'])
    CO = float(request.form['CO'])
    SO2 = float(request.form['SO2'])
    O3 = float(request.form['O3'])
    
    features = np.array([[PM2_5, NO2, CO, SO2, O3]])
    prediction = model.predict(features)[0]
    
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
