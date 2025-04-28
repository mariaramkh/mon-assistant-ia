import os
import streamlit as st

# Obtenir le bon port
port = int(os.environ.get("PORT", 8501))

# Redirection vers la page d'accueil
st.switch_page("pages/0_Accueil.py")

# Lancer Streamlit correctement
if __name__ == "__main__":
    import streamlit.web.cli as stcli
    import sys
    sys.argv = ["streamlit", "run", "app.py", "--server.port", str(port)]
    sys.exit(stcli.main())
