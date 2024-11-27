import streamlit as st

def card (header:str, link:str, label_link:str):
    with st.container(border=True):
        # st.write("Bienvenido al gestor de mantenimiento. Aquí puedes acceder a diferentes recursos.")
        with st.container():
            st.header(header, divider="gray")
            
        with st.container():
            # st.write("**Acceso informacion :**")
            with st.container(border=True):
                st.page_link(link, label=label_link, use_container_width=True)

def validate_password(correct_password: str):
    """Solicita una contraseña y devuelve True si es correcta."""
    password = st.text_input("Contraseña", type="password", key="password_input")
    if password == correct_password:
        return True
    elif password:
        st.error("Contraseña incorrecta. Inténtelo nuevamente.")
    return False