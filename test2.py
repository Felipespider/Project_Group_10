import streamlit as st 
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide") #página mais larga

with st.sidebar:
    #st.title("Souza Transportes ")
    # logo = Image.open("../images/SOUZA_TRANSPORTES_LOGO.jpg")
    st.markdown(
    "<h4 style='font-size:24px;'>Coloque Seu Arquivo Do Mês Aqui 📁</h4>",
    unsafe_allow_html=True
)
    uploaded_file = st.file_uploader(label="", type=["csv", "xlsx"])
    
    ver_ganhos = st.sidebar.checkbox("Mostrar Ganhos", value=True)
    ver_gastos = st.sidebar.checkbox("Mostrar Gastos", value=True)
    

st.title("FinSight 📊")

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file, skiprows=2, usecols="E:K")
        # df = df.iloc[:, 6:13]
        df.columns = [
            "DATA:", "TIPO DE REGISTRO:", "CATEGORIA:", "DEFINIÇÃO ITEM:",
            "QUANT.:", "VALOR (R$):", "OBSERVAÇÕES:"
        ]
    
    df["VALOR (R$):"] = pd.to_numeric(df["VALOR (R$):"], errors="coerce")
    df["DATA:"] = pd.to_datetime(df["DATA:"], errors="coerce")
    
    df_filtrado = pd.DataFrame()
    if ver_ganhos:
         df_filtrado = pd.concat([df_filtrado, df[df["TIPO DE REGISTRO:"] == "Ganho"]])
    if ver_gastos:
         df_filtrado = pd.concat([df_filtrado, df[df["TIPO DE REGISTRO:"] == "Gasto"]])
         
    total_ganhos = df_filtrado[df_filtrado["TIPO DE REGISTRO:"] == "Ganho"]["VALOR (R$):"].sum()
    total_gastos = df_filtrado[df_filtrado["TIPO DE REGISTRO:"] == "Gasto"]["VALOR (R$):"].sum()
    
    saldo = total_ganhos - total_gastos
    
    margem = (saldo / total_ganhos) * 100 if total_ganhos > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Ganhos", f"R$ {total_ganhos:,.2f}")
    col2.metric("Total de Gastos", f"R$ {total_gastos:,.2f}")
    col3.metric("Saldo do Mês", f"R$ {saldo:,.2f}")
    col4.metric("Margem de Lucro", f"{margem:.2f}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    #Um jeito de exibir os dados
    st.subheader("Distribuição por Categoria 📊")
    
    cores_personalizadas1 = {
        "Ganho": "#2ecc71",               # verde (lucro)
        "Gasto": "#e74c3c",               # vermelho (gasto)
    }
    
    fig = px.bar(
        df_filtrado.groupby("CATEGORIA:")["VALOR (R$):"].sum().reset_index(),
        x="CATEGORIA:",
        y="VALOR (R$):",
        color="CATEGORIA:",
        color_discrete_map=cores_personalizadas1,
        title="Total por Categoria",
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)
    
    #Outro jeito de exibir os dados
    st.subheader("Distribuição por Categoria 📊")
    
    # não especificar mapa de cores — usar paleta automática do Plotly
    cores_personalizadas2 = {
        "Ganho": "#2ecc71",               # verde (lucro)
        "Gasto": "#e74c3c",               # vermelho (gasto)
    }
    
    fig = px.pie(
        df_filtrado,
        names="CATEGORIA:",
        values="VALOR (R$):",
        title="Distribuição por Categoria",
        color="CATEGORIA:",  # <== isso é necessário para o color_discrete_map funcionar
        color_discrete_map=cores_personalizadas2
    )
    
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Tabela de Dados Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)
    
    
