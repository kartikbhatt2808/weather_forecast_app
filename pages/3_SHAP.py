import streamlit as st
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("🔍 SHAP Explanation")

# Generate Sample Data
data = {
    "Temperature": np.random.randint(15, 40, 50),
    "Humidity": np.random.randint(30, 90, 50),
    "WindSpeed": np.random.randint(0, 20, 50),
    "Rainfall": np.random.randint(0, 10, 50),
    "Pressure": np.random.randint(900, 1100, 50),
}
df = pd.DataFrame(data)

# Train Model
X = df[["Temperature", "Humidity", "WindSpeed", "Pressure"]]
y = df["Rainfall"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# SHAP Explainer
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# SHAP Summary Plot
st.subheader("SHAP Summary Plot")
fig, ax = plt.subplots()
shap.summary_plot(shap_values, X_test, show=False)
st.pyplot(fig)
