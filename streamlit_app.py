import streamlit as st
import pandas as pd

st.title("🤖 Machine Learning App")

st.write("Welcome to world of Machine Learning with Streamlit.")

df = pd.read_csv("penguins_cleaned.csv")
df