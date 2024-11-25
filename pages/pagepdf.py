import streamlit as st
from streamlit_pdf_reader import pdf_reader

st.page_link("app.py", label='Volver a inicio', use_container_width=True)
# password = st.text_input("Contraseña", type="password", key="password_input")
        
        # Verificar contraseña
        

source1 = 'resnet50.pdf'
# st.write("Cargando PDF...")

pdf_reader(source1)
