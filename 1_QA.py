import streamlit as st
from langchain_community.llms import Ollama
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

st.markdown("## Chat IA libre")

selected_model = st.selectbox("Modèle IA", ["llama3", "mistral", "gemma", "gpt-4"])
user_input = st.chat_input("Pose une question à l'IA")

if user_input:
    if selected_model == "gpt-4":
        llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    else:
        llm = Ollama(model=selected_model, base_url="http://host.docker.internal:11434")

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("L'IA réfléchit..."):
            response = llm.invoke(user_input)
            st.markdown(response)
