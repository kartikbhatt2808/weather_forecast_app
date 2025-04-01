import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Weather Data Visualization")

# Generate Sample Data
data = {
    "Temperature": np.random.randint(15, 40, 50),
    "Humidity": np.random.randint(30, 90, 50),
    "WindSpeed": np.random.randint(0, 20, 50),
    "Rainfall": np.random.randint(0, 10, 50),
    "Pressure": np.random.randint(900, 1100, 50),
}
df = pd.DataFrame(data)

# Correlation Heatmap
st.subheader("🔍 Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Scatter Plot
st.subheader("🌡️ Temperature vs. Rainfall")
fig, ax = plt.subplots()
sns.scatterplot(x=df["Temperature"], y=df["Rainfall"], ax=ax)
st.pyplot(fig)
