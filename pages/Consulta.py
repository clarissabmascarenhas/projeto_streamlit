import streamlit as st
import pandas as pd

dados = pd.read_csv("Produtos.csv")

st.title("Produtos Cadastrados:")
st.divider()

st.dataframe(dados)