import streamlit as st
import os

ma_variable = os.environ.get("MA_VARIABLE")
autre_variable = os.environ.get("AUTRE_VARIABLE")

st.write(f"Ma variable : {ma_variable}")
st.write(f"Autre variable : {autre_variable}")