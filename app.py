### Crop Disease Detection App using Streamlit

### Import libraries
import streamlit as st
import pandas as pd
import joblib

### load the model
model = joblib.load('model.joblib')

### app title
st.title("Crop Disease Predictor")

### load the dataset
data = pd.read_csv('dataset.csv')

### Build three KPI's for the app

st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)

### Average rainfall, average temperature, and average soil moisture
with col1:
    st.metric(label="Average Rainfall", value=f"{data['Rainfall_mm'].mean():.2f} mm")
with col2:
    st.metric(label="Average Temperature", value=f"{data['Temperature_C'].mean():.2f} °C")
with col3:
    st.metric(label="Average Soil Moisture", value=f"{data['Soil_Moisture'].mean():.2f} %")

### User input for the features

### Create a sidebar for user input
st.sidebar.header("Input Features")

### create a filter for regions
region = st.sidebar.selectbox("Select Region", data['Region'].unique())

### create a filter for crop types
crop_type = st.sidebar.selectbox("Select Crop Type", data['Crop_Type'].unique())

### create a filter fertilizer use
fertilizer_use = st.sidebar.selectbox("Fertilizer Use", data['Fertilizer_Used'].unique()) 

### create a filter for pest presence
pest_presence = st.sidebar.selectbox("Pest Presence", data['Pest_Presence'].unique())

### create a filter for day  
day = st.sidebar.slider("Day", 1, 31, 15) 

### Sidebar sliders for numeric features

### slider for rainfall
rainfall = st.sidebar.slider("Rainfall (mm)", float(data['Rainfall_mm'].min()), 
                             float(data['Rainfall_mm'].max()), float(data['Rainfall_mm'].mean()))
### slider for temperature
temperature = st.sidebar.slider("Temperature (°C)", float(data['Temperature_C'].min()),
                                float(data['Temperature_C'].max()), float(data['Temperature_C'].mean()))

### slider for soil moisture
soil_moisture = st.sidebar.slider("Soil Moisture (%)", float(data['Soil_Moisture'].min()),
                                   float(data['Soil_Moisture'].max()), float(data['Soil_Moisture'].mean()))


### Create a DataFrame for the user input
user_input = pd.DataFrame({
    'Region': [region],
    'Crop_Type': [crop_type],
    'Fertilizer_Used': [fertilizer_use],
    'Pest_Presence': [pest_presence],
    'Day': [day],
    'Rainfall_mm': [rainfall],
    'Temperature_C': [temperature],
    'Soil_Moisture': [soil_moisture]
})

### predict the disease presence using the model

### create a button to trigger the prediction
if st.button("Predict Disease"):
    prediction = model.predict(user_input)
    if prediction[0] == 1:
        st.error("Disease detected! Take necessary actions.")
    else:
        st.success("No Disease Detected. Keep monitoring your crops!")

st.markdown("---")  # Add a horizontal line


### Create a markdown section at the end the app page
st.markdown("""
            @2026 Code4Food Security | Developed by **SevenLabs** 
            """)
