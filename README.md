
FinSight - Aplicação de Gestão Financeira com Streamlit
# README - FinSight 📊
## Descrição
FinSight é uma aplicação web interativa desenvolvida com Streamlit para gerenciamento e análise financeira pessoal ou empresarial. 
A aplicação permite o cadastro de lançamentos financeiros (ganhos e gastos), visualização de métricas em tempo real e análises 
gráficas detalhadas dos dados financeiros.
## Funcionalidades Principais
### 1. Cadastro de Lançamentos 💰
- Registre transações financeiras com as seguintes informações:
    - **Data**: Data do lançamento
    - **Tipo de Registro**: Classificação como Ganho ou Gasto
    - **Categoria**: Categorização da transação (ex: Vendas, Compras, Frete)
    - **Definição do Item**: Descrição detalhada do lançamento
    - **Quantidade**: Quantidade de itens
    - **Valor (R$)**: Valor monetário da transação
    - **Observações**: Notas adicionais (campo opcional)
### 2. Filtros de Visualização 🔎
- Filtro dinâmico na barra lateral para visualizar:
    - Apenas Ganhos
    - Apenas Gastos
    - Ganhos e Gastos simultaneamente
- Atualização em tempo real dos gráficos e métricas
### 3. Métricas Principais 📈
- **Total de Ganhos**: Soma de todos os lançamentos classificados como Ganho
- **Total de Gastos**: Soma de todos os lançamentos classificados como Gasto
- **Saldo do Período**: Diferença entre ganhos e gastos
- **Margem de Lucro**: Percentual de lucro em relação aos ganhos
### 4. Visualizações Gráficas 📊
- **Gráfico de Barras**: Distribuição dos valores por categoria com diferenciação entre Ganhos (verde) e Gastos (vermelho)
- **Gráfico de Pizza**: Representação percentual da distribuição por categoria
- **Tabela Detalhada**: Visualização de todos os lançamentos filtrados em formato tabular
### 5. Gerenciamento de Dados 🧹
- Persistência de dados durante a sessão usando `st.session_state`
- Botão para limpar todos os lançamentos
## Requisitos Técnicos
### Dependências
- Python 3.7+
- streamlit
- pandas
- plotly
### Instalação
import pandas as pd
import plotly.express as px
from datetime import datetime
