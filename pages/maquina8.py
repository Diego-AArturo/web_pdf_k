import streamlit as st

st.title("Gestión de Mantenimiento")

    # Contenedor principal
with st.container(border=True):
    # st.write("Bienvenido al gestor de mantenimiento. Aquí puedes acceder a diferentes recursos.")
    with st.container():
        st.header("Maquina8", divider="gray")
        
        # st.markdown('''
        #             Esta maquina es tiene no se que y no que mas
        #             Es muy importante porque si no se quema todo 
        #             ''')
    # Subcontenedor para el enlace
    with st.container():
        st.write("**Acceso informacion :**")
        with st.container(border=True):
            st.page_link("pages/mq8_options.py", label='Ir a recursos', use_container_width=True)