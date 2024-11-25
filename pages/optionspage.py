import streamlit as st
from streamlit_pdf_reader import pdf_reader



st.page_link("app.py", label='Volver a inicio')
password = st.text_input("Contraseña", type="password", key="password_input")
        
        # Verificar contraseña
        
if password:
    
    if password == "pato":
        # source1 = 'resnet50.pdf'
        # st.write("Cargando PDF...")
        with st.container(border=True):
                st.page_link("pages/pagepdf.py", label='Abrir Manual de Usuario', use_container_width=True)
        with st.container(border=True):
                st.page_link("pages/pagepdf.py", label='Abrir Manual de Usuario', use_container_width=True)
        with st.container(border=True):
                st.page_link("pages/pagepdf.py", label='Abrir Manual de Usuario', use_container_width=True)
        with st.container(border=True):
                st.page_link("pages/pagepdf.py", label='Abrir Manual de Usuario', use_container_width=True)
        with st.container(border=True):
                st.page_link("pages/pagepdf.py", label='Abrir Manual de Usuario', use_container_width=True)

        # pdf_reader(source1)
    else:
        st.error("Contraseña incorrecta. Por favor, inténtelo nuevamente.")
else:
    st.info("Por favor, ingrese la contraseña.")
