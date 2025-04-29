import os
import streamlit as st

# Debug : Afficher le contenu du répertoire courant
print("Contenu du dossier courant :", os.listdir())

# Obtenir le port fourni par Render (ou 8501 par défaut en local)
port = int(os.environ.get("PORT", 8501))

# Configuration de la page
st.set_page_config(page_title="Mon Assistant IA")

# Redirige vers la page d'accueil
st.switch_page("pages/0_Accueil.py")
