# Project_Group_10
Projeto Grupo Lab. Engenharia de Software - Grupo 10 - Luiz Felipe Aranhas e Poliana Andrade Brasil


# Análise Financeira

Um dashboard em Streamlit para análise financeira de ganhos e gastos.

## 📈 Link Excel Base
https://1drv.ms/x/c/57c81148717d5443/EXnWTx6jnqpOiRURZzQn_icBha6XhJvJkgtI4YwKjCrwyw?e=1R34lN

## 📋 Funcionalidades

- Upload de arquivos  Excel (.xlsx)
- Visualização de métricas financeiras:
    - Total de Ganhos
    - Total de Gastos
    - Saldo do Mês
    - Margem de Lucro
- Gráficos interativos:
    - Gráfico de barras por categoria
    - Gráfico de pizza por distribuição
- Tabela de dados filtrados
- Filtros laterais para mostrar/ocultar ganhos e gastos

## 🚀 Como usar

1. Execute o aplicativo Streamlit (Streamlit run #nome do arquivo#)
2. Faça upload do arquivo financeiro (.csv ou .xlsx) no painel lateral
3. Use os checkboxes para filtrar entre ganhos e gastos
4. Visualize as análises nos gráficos e tabelas

## 📊 Formato do arquivo de entrada

Para arquivos Excel (.xlsx):
- Pula as 2 primeiras linhas
- Usa as colunas E até K
- Colunas esperadas:
    - DATA:
    - TIPO DE REGISTRO:
    - CATEGORIA:
    - DEFINIÇÃO ITEM:
    - QUANT.:
    - VALOR (R$):
    - OBSERVAÇÕES:

## 🛠 Tecnologias utilizadas

- Streamlit
- Pandas
- Plotly Express
- PIL (Python Imaging Library)

## 📝 Notas

- O sistema espera registros classificados como "Ganho" ou "Gasto"
- As datas e valores são automaticamente convertidos para os formatos corretos
- O formato do excel é fixo e estará disponível para downloado do mesmo via Link
- A margem de lucro é calculada quando existem ganhos
