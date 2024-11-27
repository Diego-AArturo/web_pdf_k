import streamlit as st
from src.components import card 


def main():
    st.title("Gestión de Maquinas")

    for i in range(10):
        card(header=f"Maquina{i+1}", link=f"pages/maquina{i+1}.py", label_link="Ir a recursos")


if __name__ == "__main__":
    main()




