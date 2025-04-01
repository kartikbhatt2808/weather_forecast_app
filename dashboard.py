import streamlit as st

st.set_page_config(page_title="Weather Forecast App", layout="wide")

st.title("🌦 Weather Forecast Prediction System")
st.markdown("Welcome to the Weather Forecast Prediction System! Use the navigation to explore different pages.")
st.image("https://upload.wikimedia.org/wikipedia/commons/e/e7/Weather_icon.png", width=300)

st.sidebar.success("Select a page above to get started.")
