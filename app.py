import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('traffic_model.pkl')

st.set_page_config(page_title="Traffic Optimizer", layout="centered")

st.title("🚦 Traffic Signal Optimization System")

st.write("Enter traffic parameters to predict green signal time")

# Inputs
hour = st.number_input("Hour (0-23)", 0, 23)
lane_length = st.number_input("Lane Length (m)", 0.0)
vehicle_count = st.number_input("Vehicle Count", 0)
avg_speed = st.number_input("Average Speed (km/h)", 0.0)

ambulance = st.selectbox("Ambulance Present", [0, 1])

lane_id = st.selectbox("Lane ID", ["A", "B", "C"])
weather = st.selectbox("Weather", ["Clear", "Rain", "Fog"])

# Predict
if st.button("Predict Green Time"):

    input_data = pd.DataFrame([{
        'Hour': hour,
        'Lane_Length_m': lane_length,
        'Vehicle_Count': vehicle_count,
        'Avg_Speed_kmh': avg_speed,
        'Ambulance_Present': ambulance,
        'Lane_ID': lane_id,
        'Weather': weather
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"🚀 Predicted Green Signal Time: {round(prediction,2)} seconds")