import streamlit as st
import Controllers.ClienteController
import pandas as pd

def List():
    st.title("Consultar Cliente")
    costumerList = []

    for item in Controllers.ClienteController.SelecionarTodos():
        costumerList.append([item.nome, item.idade, item.profissao])

    df = pd.DataFrame(
        costumerList,
        columns=["Nome", "Idade", "Profissão"]
        )

    st.table(df)