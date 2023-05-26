import streamlit as st
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente



st.sidebar.title('Menu')
Page_cliente = st.sidebar.selectbox('Cliente', ['Incluir','Alterar','Excluir', 'Consultar'])

if Page_cliente == "Consultar":
    PageListCliente.List()
   

if Page_cliente == "Incluir":
    PageCreateCliente.IncluirClientePage()
