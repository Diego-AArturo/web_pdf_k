import streamlit as st
from src.components import validate_password



st.page_link("pages/maquina8.py", label='Volver a inicio')
st.title("Opciones de Máquina 8")

if validate_password("pato"):
        st.success("Acceso concedido.")
        st.write("Recursos disponibles para esta máquina:")

        col1, col2 = st.columns(2)
        with col1:
            st.page_link("pages/pagepdf.py", label="Manual de Operación", use_container_width=True)
            st.page_link("pages/pagepdf.py", label="Especificaciones Técnicas", use_container_width=True)
        with col2:
            st.page_link("pages/pagepdf.py", label="Procedimientos de Mantenimiento", use_container_width=True)
            st.page_link("pages/pagepdf.py", label="Historial de Reparaciones", use_container_width=True)
else:
        st.info("Por favor, ingrese la contraseña para acceder a los recursos.")