import streamlit as st
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente



st.sidebar.title('Menu')
Page_cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Consultar'])

if Page_cliente == "Consultar":
    PageListCliente.List()
   

if Page_cliente == "Incluir":
    st.experimental_set_query_params()
    PageCreateCliente.IncluirClientePage()
