import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    data = pd.read_csv("air_passenger_data.csv")
    data['Month'] = pd.to_datetime(data['Month'])
    data.set_index('Month', inplace=True)
    data.rename(columns={'#Passengers': 'Passengers'}, inplace=True)
    return data

data = load_data()

st.title("Air Passenger Dashboard")
st.write("Analyzing trends in air passenger numbers.")

if st.checkbox("Show Raw Data"):
    st.write(data)

st.subheader("Passenger Trends Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
data['Passengers'].plot(ax=ax, title="Air Passenger Trends", ylabel="Passengers")
st.pyplot(fig)

st.subheader("Seasonality")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data, x=data.index.month, y='Passengers', palette='viridis')
ax.set_title("Seasonal Trends in Passenger Data")
ax.set_xlabel("Month")
ax.set_ylabel("Passengers")
st.pyplot(fig)

st.subheader("Moving Average Forecast")
data['SMA_12'] = data['Passengers'].rolling(window=12).mean()
fig, ax = plt.subplots(figsize=(10, 6))
data['Passengers'].plot(ax=ax, label='Actual', legend=True)
data['SMA_12'].plot(ax=ax, label='12-Month SMA', legend=True, color='orange')
ax.set_title("12-Month SMA Forecast")
ax.set_ylabel("Passengers")
st.pyplot(fig)
