# app.py

import streamlit as st
import xarray as xr
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("🌍 ML on NetCDF Data (.nc) using Streamlit")

# File uploader
nc_file = st.file_uploader("Upload a NetCDF (.nc) file", type=["nc"])

if nc_file is not None:
    # Load the NetCDF file
    ds = xr.open_dataset(nc_file)
    st.success("NetCDF file loaded successfully!")

    # Show variables
    st.subheader("Available Variables:")
    st.write(list(ds.data_vars))

    # Select a variable
    var_name = st.selectbox("Select a variable to use", list(ds.data_vars))

    # Extract data as DataFrame
    df = ds[var_name].to_dataframe().dropna().reset_index()

    st.write("Preview of the extracted data:")
    st.dataframe(df.head())

    # Let’s assume we want to predict the selected variable based on latitude & longitude
    if 'lat' in df.columns and 'lon' in df.columns:
        st.subheader("Train Linear Regression Model")

        # Feature and target
        X = df[['lat', 'lon']]
        y = df[var_name]

        # Train model
        model = LinearRegression()
        model.fit(X, y)
        st.success("Model trained successfully!")

        # Input for prediction
        st.subheader("Make a Prediction")
        lat = st.number_input("Latitude", float(df['lat'].min()), float(df['lat'].max()), float(df['lat'].mean()))
        lon = st.number_input("Longitude", float(df['lon'].min()), float(df['lon'].max()), float(df['lon'].mean()))

        prediction = model.predict([[lat, lon]])
        st.write(f"📈 Predicted value of `{var_name}` at (lat: {lat}, lon: {lon}): `{prediction[0]:.2f}`")

        # Optional: Visualize original data
        st.subheader("Data Visualization")
        fig, ax = plt.subplots()
        sc = ax.scatter(df['lon'], df['lat'], c=df[var_name], cmap='viridis')
        plt.colorbar(sc, ax=ax, label=var_name)
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        st.pyplot(fig)

    else:
        st.warning("This example needs 'lat' and 'lon' coordinates in the dataset.")
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page using the index.html template."""
    return render_template('index.html', title='My Flask App', message='Welcome to a basic Flask app with templates!')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
