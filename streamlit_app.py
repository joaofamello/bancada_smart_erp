import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st

from bancada_smart_erp.modules.auth import exigir_login, exigir_admin

st.set_page_config(page_title="Bancada Smart ERP", layout="wide")

usuario = exigir_login()

paginas = [
    st.Page("src/bancada_smart_erp/pages/pagina_autenticacao.py", title="Início", default=True),
]

if exigir_admin():
    paginas.append(
        st.Page("src/bancada_smart_erp/pages/admin.py", title="Admin")
    )

st.sidebar.write(f"Olá, {usuario.nome}!")
st.sidebar.button("Sair", on_click=st.logout)

st.navigation(paginas).run()