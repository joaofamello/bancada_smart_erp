import streamlit as st

from bancada_smart_erp.database.database import SessionLocal
from bancada_smart_erp.modules.auth.service import UsuarioAutenticado, autorizar_usuario

def exigir_login() -> UsuarioAutenticado:
    if not st.user.is_logged_in:
        st.title("Bancada Smart ERP")
        st.button("Entrar com Google", on_click=st.login)
        st.stop()

    with SessionLocal() as db:
        usuario = autorizar_usuario(
            db,
            email=st.user.get("email"),
            google_sub=st.user.get("sub"),
            email_verificado=st.user.get("email_verificado", False),
        )

    if usuario is None:
        st.error("Sua conta Google não está autorizada neste sistema.")
        st.button("Sair", on_click=st.logout)
        st.stop()

    st.session_state["usuario"] = usuario
    return usuario

def exigir_admin() -> UsuarioAutenticado:
    usuario = exigir_login()
    if usuario.nivel_acesso != "admin":
        st.error("Acesso restrito a administradores.")
        st.stop()

    return usuario