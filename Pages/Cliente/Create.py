import streamlit as st
import Controllers.ClienteController
import models.Cliente as cliente

def IncluirClientePage():
    st.title("Incluir Cliente")

    with st.form(key = "include_cliente",clear_on_submit=True):
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="Insira sua idade", format="%d", step = 1)
            input_occupation = st.selectbox("Selecione sua opção", ["Desenvolvedor", "Militar", "Músico"])
            input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
            
            Controllers.ClienteController.Incluir(cliente.Cliente(0, input_name, input_age, input_occupation))
            st.success("Cliente incluido com sucesso.")