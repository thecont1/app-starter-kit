import streamlit as st
import pandas as pd

st.title("🤖 Namma Metro Ridership Tracker")
st.write("The Bangalore Metro Rail Corporation Limited (BMRCL) publishes daily ridership data every 24 hours. Unfortunately, they do not provide historical data beyond one day. This repository contains a Python script and Jupyter Notebook to automate the process of downloading ridership data from BMRCL and storing it in a csv file. As the dataset evolves over time, it will allow for analysis of ridership and usage patterns.")

with st.expander("Data"):
    st.write("**Raw Data**")
    df = pd.read_csv("https://raw.githubusercontent.com/thecont1/namma-metro-ridership-tracker/refs/heads/main/NammaMetro_Ridership_Dataset.csv")

    st.write("**X**")
    X = df.drop("species",axis=1)
    X

    st.write("**y**")
    y = df.species
    y

with st.expander("Data Visualization"):
    st.scatter_chart(
        df,
        x="bill_length_mm",
        y="body_mass_g",
        color="species",
    )