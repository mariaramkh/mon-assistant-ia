import streamlit as st
import requests
import os
from dotenv import load_dotenv

st.markdown("##  Connexion IONOS avec API")

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv("IONOS_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Tester la connexion
dc_url = "https://api.ionos.com/cloudapi/v6/datacenters"
r = requests.get(dc_url, headers=headers)

if r.status_code == 200:
    data = r.json()
    nb = len(data.get("items", []))
    st.success(f" Connexion réussie. {nb} datacenter(s) trouvé(s).")
else:
    st.error(f" Erreur de connexion ({r.status_code})")

st.markdown("---")
st.markdown("### ➕ Créer un nouveau Data Center")

dc_name = st.text_input("Nom du nouveau Data Center", value="DC-NirWana")
location = st.selectbox(" Localisation", ["de/fra", "gb/lhr", "us/las"])

if st.button("Créer le Data Center"):
    payload = {
        "properties": {
            "name": dc_name,
            "location": location,
            "description": "Créé depuis l'assistant IA NirWana"
        }
    }
    res = requests.post(dc_url, headers=headers, json=payload)
    if res.status_code in [202, 201]:
        st.success(" Data Center en cours de création !")
        st.json(res.json())
    else:
        st.error(f"Erreur ({res.status_code}) : {res.text}")
