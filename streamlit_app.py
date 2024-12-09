import streamlit as st
import pandas as pd

st.title("🤖 Machine Learning App")
st.write("Welcome to world of Machine Learning with Streamlit.")

with st.expander("Data"):
    st.write("**Raw Data**")
    df = pd.read_csv("penguins_cleaned.csv")
    df

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