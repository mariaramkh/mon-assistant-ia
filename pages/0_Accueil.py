import streamlit as st

# Style global NirWana
st.markdown("""
    <style>
        html, body {
            background: linear-gradient(to bottom right, #e65da6, #8a4fc4);
            color: #333;
            font-family: 'Quicksand', sans-serif;
        }
        .block-container {
            background-color: #ffffffcc;
            border-radius: 20px;
            padding: 2rem;
            margin-top: 2rem;
        }
        h1, h2 {
            text-align: center;
            color: #6a1b9a;
        }
        .welcome {
            text-align: center;
            margin-top: 2rem;
        }
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

#  Logo NirWana
st.image("logo_nirwana.jpg", width=180)

# Titre principal
st.markdown("<h1>Bienvenue sur l'Assistant IA NirWana</h1>", unsafe_allow_html=True)

#  Infos
st.markdown("""
<div class="welcome">
    <h2> Choisissez une page dans le menu à gauche </h2>
    <ul style="font-size: 18px; list-style-type: none; padding-left: 0;">
        <li> <b>Analyse de documents</b></li>
        <li> <b>Génération de mails</b></li>
        <li> <b>Connexion IONOS</b></li>
    </ul>
</div>
""", unsafe_allow_html=True)
