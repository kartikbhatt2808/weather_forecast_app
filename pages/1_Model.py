import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("📊 Weather Forecast Model")

# Sample Weather Data
data = {
    "Temperature": np.random.randint(15, 40, 50),
    "Humidity": np.random.randint(30, 90, 50),
    "WindSpeed": np.random.randint(0, 20, 50),
    "Rainfall": np.random.randint(0, 10, 50),
    "Pressure": np.random.randint(900, 1100, 50),
}

df = pd.DataFrame(data)

# Train a Simple Model
X = df[["Temperature", "Humidity", "WindSpeed", "Pressure"]]
y = df["Rainfall"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# User Input for Prediction
st.sidebar.header("Enter Weather Conditions")
temp = st.sidebar.slider("Temperature (°C)", 15, 40, 25)
humidity = st.sidebar.slider("Humidity (%)", 30, 90, 60)
wind_speed = st.sidebar.slider("Wind Speed (km/h)", 0, 20, 5)
pressure = st.sidebar.slider("Pressure (hPa)", 900, 1100, 1000)

# Make Prediction
input_data = np.array([[temp, humidity, wind_speed, pressure]])
prediction = model.predict(input_data)[0]

st.write(f"**Predicted Rainfall:** {prediction:.2f} mm")
