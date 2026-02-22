import os

import streamlit as st
from dotenv import load_dotenv

# Charge les variables d'environnement contenues dans le fichier .env
load_dotenv()

# Récupération des variables
ma_variable = os.getenv("MA_VARIABLE")
autre_variable = os.getenv("AUTRE_VARIABLE")

# Interface Streamlit
st.title("Test des variables d'environnement")

if ma_variable and autre_variable:
    st.write(f"Ma variable : **{ma_variable}**")
    st.write(f"Autre variable : **{autre_variable}**")
else:
    st.error("Les variables n'ont pas été trouvées. Vérifiez votre fichier .env.")