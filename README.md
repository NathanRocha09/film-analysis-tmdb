# 🎬 Projeto de Análise de Dados: Filmes (TMDB)

Este projeto realiza uma análise exploratória dos dados de filmes disponíveis no [TMDB (The Movie Database)](https://www.themoviedb.org/), utilizando **Python**, **Pandas** e **Matplotlib/Seaborn**. A base de dados contém mais de 5.000 filmes, com informações como orçamento, receita, nota, popularidade, gêneros e datas de lançamento.

---

## 📌 Objetivos

- Entender a distribuição das notas dos filmes
- Identificar os filmes mais bem avaliados
- Calcular o lucro dos filmes e encontrar os mais lucrativos
- Analisar tendências de avaliação ao longo dos anos
- Explorar os gêneros mais frequentes no dataset

---

## 📂 Estrutura do Projeto


---

## 🧪 Tecnologias e Bibliotecas

- [Python 3.x](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [AST (Abstract Syntax Trees)](https://docs.python.org/3/library/ast.html)

---

## 🔍 Principais Etapas da Análise

### ✅ 1. Carregamento dos dados
```python

df = pd.read_csv('data/tmdb_5000_movi
es.csv')

✅ 2. Limpeza e transformação
Conversão de colunas JSON (como genres) para listas de strings

Conversão de datas com pd.to_datetime

Criação da coluna year

Cálculo do lucro: revenue - budget

✅ 3. Análises realizadas
Top 10 filmes com maior nota

Gêneros mais frequentes

Lucros dos filmes

Evolução das notas médias por ano

✅ 4. Visualizações
Gráficos feitos com Matplotlib e Seaborn:

Histograma das notas

Linha temporal das médias anuais

Barra dos gêneros mais frequentes

📊 Exemplo de Gráfico

💡 Principais Aprendizados
Uso de apply com funções para tratar colunas JSON

Manipulação de datas com datetime

Criação de colunas calculadas (profit)

Agrupamento de dados com groupby

Explosão de listas e contagem de frequências com explode + Counter

Visualização com bibliotecas profissionais de Python

🚀 Possíveis Extensões
Exportar resultados para uso no Power BI

Construir um dashboard com Streamlit

Análise cruzada entre orçamento, gênero e avaliação

📎 Fonte dos Dados
TMDB Movie Metadata - Kaggle

🤝 Contribuições
Sinta-se livre para abrir issues ou enviar pull requests!

📧 Contato
[Nathan Rocha] – [n4rocha.7@gmail.com]
GitHub – LinkedIn 
/in/nathanrocha09/

