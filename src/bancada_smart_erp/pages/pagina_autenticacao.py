import streamlit as st

from bancada_smart_erp.modules.auth import exigir_login

st.set_page_config(page_title="Login")

usuario = exigir_login()

st.warning(f"Autenticado: {usuario.nome} ({usuario.nivel_acesso}).")
st.button("Sair", on_click=st.logout)