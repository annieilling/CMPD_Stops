import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df


stops = load_data("data/Officer_Traffic_Stops.csv")

# create histohram for driver's age 
driver_age_hist = plt.figure(figsize=(12, 6))
plt.hist(stops['Driver_Age'], bins=10, color='lightblue', edgecolor='white')
plt.title('Histogram of Driver Age')
plt.xlabel('Driver Age (binned)')
plt.ylabel('Count of Records')
plt.grid(True)

st.pyplot(driver_age_hist)

