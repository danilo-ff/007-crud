import streamlit as st
import Controllers.ClienteController
import Pages.Cliente.Create


def List():
    paramId = st.experimental_get_query_params()
    if paramId == {}:
        st.experimental_set_query_params()
        columns = st.columns((1,2,1,2,2,2))
        campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']
        for col, campo_nome in zip(columns, campos):
            col.write(campo_nome)
        
        for item in Controllers.ClienteController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns((1,2,1,2,2,2))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            button_space_excluir = col5.empty()
            on_click_excluir = button_space_excluir.button('Excluir','btnExcluir' + str(item.id), help="Clique para excluir")
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button('Alterar','btnAlterar' + str(item.id), help="Clique para alterar")

            if on_click_excluir:
                Controllers.ClienteController.Excluir(item.id)
                button_space_excluir.button('Excluido','btnExcluido' + str(item.id), help="Cliente já excluído")

            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id]
                )
                st.experimental_rerun()

    else:
        on_click_voltar = st.button('Voltar')
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        Pages.Cliente.Create.IncluirClientePage()

