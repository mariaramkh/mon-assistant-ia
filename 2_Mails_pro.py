import streamlit as st
from langchain_community.llms import Ollama
from langchain.chat_models import ChatOpenAI

st.markdown("## Génération de mails professionnels")

# Choix du modèle IA
model = st.selectbox("Modèle IA", ["llama3", "mistral", "gemma", "gpt-4"])
# Contexte du mail
message_input = st.text_area("Instructions ou contexte du mail", height=200)
# Ton du message
tone = st.selectbox("Ton souhaité", ["Professionnel", "Amical", "Concis", "Empathique"])
# Bouton
submit = st.button("Générer le mail")

# Génération du mail
if submit and message_input:
    with st.spinner("L'IA rédige le mail..."):
        prompt = f"""
Tu es un assistant expert en rédaction de mails. Utilise un ton {tone.lower()}.
Consigne : {message_input}
Commence par une salutation adaptée, sois clair et termine de façon polie.
"""
        try:
            if model == "gpt-4":
                llm = ChatOpenAI(model_name="gpt-4", temperature=0)
            else:
                llm = Ollama(model=model, base_url="http://localhost:11434")  # Pas de "host.docker.internal" en local

            response = llm.invoke(prompt)
            st.success("Mail généré :")
            st.markdown(response)

        except Exception as e:
            st.error(f"Erreur avec le modèle sélectionné : {e}")
