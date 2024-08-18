import streamlit as st
import pandas as pd
from datetime import date



def gravar_dados(nome_produto, cod_produto, tipo):
    if nome_produto and cod_produto:
        with open ("Produtos.csv", "a", encoding="utf-8") as file:
           file.write (f"{nome_produto}, {cod_produto}, {tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de Produtos",
    page_icon="📙",
    layout = "wide",
    menu_items={
        'About': "#This is my first Streamlit Project"
    }
)

st.title("Cadastro de Produtos")
st.divider()

nome_produto = st.text_input("Digite o nome do Produto", key = "nome_produto")

cod_produto = st.number_input("Código do Produto", key = "cod_produto", min_value=0,)

tipo = st.selectbox("Tipo de Produto", 
                     ["Alimentos", "Produtos de Higiene", "Produtos de Casa"])

btn_cadastrar = st.button("Cadastrar!", 
                          on_click=gravar_dados,
                          args=[nome_produto, cod_produto, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Produto cadastrado com sucesso!")
    else:
        st.error("Houve algum problema no cadastro!")