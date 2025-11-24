import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide")

# ---------------------- CONFIGURAÇÃO INICIAL ---------------------- #
st.title("FinSight 📊")

# Inicializa o DataFrame na sessão (para não perder dados a cada interação)
COLUNAS = [
    "DATA:",
    "TIPO DE REGISTRO:",
    "CATEGORIA:",
    "DEFINIÇÃO ITEM:",
    "QUANT.:",
    "VALOR (R$):",
    "OBSERVAÇÕES:",
]

if "df_financeiro" not in st.session_state:
    st.session_state.df_financeiro = pd.DataFrame(columns=COLUNAS)

df = st.session_state.df_financeiro

# ---------------------- SIDEBAR ---------------------- #
with st.sidebar:
    st.markdown(
        "<h4 style='font-size:24px;'>Cadastro Financeiro 🔎</h4>",
        unsafe_allow_html=True
    )

    st.markdown("### Filtros de Visualização")
    ver_ganhos = st.checkbox("Mostrar Ganhos", value=True)
    ver_gastos = st.checkbox("Mostrar Gastos", value=True)

    st.markdown("---")
    if st.button("🧹 Limpar todos os lançamentos"):
        st.session_state.df_financeiro = pd.DataFrame(columns=COLUNAS)
        st.rerun()

# ---------------------- FORMULÁRIO DE LANÇAMENTO ---------------------- #
st.subheader("Novo Lançamento 💰")

with st.form("form_lancamento"):
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        data = st.date_input("Data", value=datetime.today())
    with col_b:
        tipo_registro = st.selectbox("Tipo de Registro", ["Ganho", "Gasto"])
    with col_c:
        categoria = st.text_input("Categoria (ex: Vendas, Compras, etc.)")

    definicao_item = st.text_input("Definição do Item", placeholder="Ex: Frete BH-SP, Abastecimento, etc.")
    
    col_d, col_e = st.columns(2)
    with col_d:
        quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)
    with col_e:
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")

    observacoes = st.text_area("Observações", placeholder="Opcional")

    adicionar = st.form_submit_button("Adicionar Lançamento ➕")

if adicionar:
    if categoria == "" or valor == 0:
        st.warning("Preencha pelo menos a **Categoria** e o **Valor (R$)** para adicionar o lançamento.")
    else:
        novo_registro = {
            "DATA:": pd.to_datetime(data),
            "TIPO DE REGISTRO:": tipo_registro,
            "CATEGORIA:": categoria,
            "DEFINIÇÃO ITEM:": definicao_item,
            "QUANT.:": quantidade,
            "VALOR (R$):": float(valor),
            "OBSERVAÇÕES:": observacoes,
        }
        st.session_state.df_financeiro = pd.concat(
            [st.session_state.df_financeiro, pd.DataFrame([novo_registro])],
            ignore_index=True
        )
        st.success("Lançamento adicionado com sucesso! ✅")

        # Atualiza df local
        df = st.session_state.df_financeiro

# ---------------------- ANÁLISE E GRÁFICOS ---------------------- #
if df.empty:
    st.info("Nenhum lançamento cadastrado ainda. Adicione lançamentos para ver os gráficos e métricas.")
else:
    # Garantir tipos
    df["VALOR (R$):"] = pd.to_numeric(df["VALOR (R$):"], errors="coerce")
    df["DATA:"] = pd.to_datetime(df["DATA:"], errors="coerce")

    # Filtrar por tipo (Ganho / Gasto)
    df_filtrado = pd.DataFrame()
    if ver_ganhos:
        df_filtrado = pd.concat([df_filtrado, df[df["TIPO DE REGISTRO:"] == "Ganho"]])
    if ver_gastos:
        df_filtrado = pd.concat([df_filtrado, df[df["TIPO DE REGISTRO:"] == "Gasto"]])

    if df_filtrado.empty:
        st.warning("Com os filtros atuais, não há dados para exibir.")
    else:
        total_ganhos = df_filtrado[df_filtrado["TIPO DE REGISTRO:"] == "Ganho"]["VALOR (R$):"].sum()
        total_gastos = df_filtrado[df_filtrado["TIPO DE REGISTRO:"] == "Gasto"]["VALOR (R$):"].sum()
        saldo = total_ganhos - total_gastos
        margem = (saldo / total_ganhos) * 100 if total_ganhos > 0 else 0

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Ganhos", f"R$ {total_ganhos:,.2f}")
        col2.metric("Total de Gastos", f"R$ {total_gastos:,.2f}")
        col3.metric("Saldo do Período", f"R$ {saldo:,.2f}")
        col4.metric("Margem de Lucro", f"{margem:.2f}%")

        st.markdown("<br>", unsafe_allow_html=True)

        # -------- Distribuição por Categoria (Barra) -------- #
        st.subheader("Distribuição por Categoria 📊")
        df_cat = df_filtrado.groupby("CATEGORIA:")["VALOR (R$):"].sum().reset_index()
        
        cores_personalizadas1 = {
        "Ganho": "#2ecc71",               # verde (lucro)
        "Gasto": "#e74c3c",               # vermelho (gasto)
    }

        fig_bar = px.bar(
            df_cat,
            x="CATEGORIA:",
            y="VALOR (R$):",
            title="Total por Categoria",
            color="CATEGORIA:",
            color_discrete_map=cores_personalizadas1,
            text_auto=True
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        # -------- Distribuição por Categoria (Pizza) -------- #
        st.subheader("Distribuição por Categoria (%) 🥧")
        
        cores_personalizadas2 = {
        "Ganho": "#2ecc71",               # verde (lucro)
        "Gasto": "#e74c3c",               # vermelho (gasto)
    }
        
        fig_pie = px.pie(
            df_cat,
            names="CATEGORIA:",
            values="VALOR (R$):",
            title="Distribuição por Categoria",
            color = "CATEGORIA:",
            color_discrete_map=cores_personalizadas2,
        )
        fig_pie.update_traces(textinfo="percent+label")
        st.plotly_chart(fig_pie, use_container_width=True)

        # -------- Tabela de Dados -------- #
        st.subheader("Tabela de Dados Filtrados")
        st.dataframe(df_filtrado.sort_values("DATA:"), use_container_width=True)
