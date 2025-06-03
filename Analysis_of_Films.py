import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import ast 

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 5)

#Carregar dataset
df = pd.read_csv('tmdb_5000_movies.csv')

#Pré processamento
df['genres'] = df['genres'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)])
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['year'] = df['release_date'].dt.year
df['profit'] = df['revenue'] - df['budget']

#Análise
top10 = df [['title','vote_average']].sort_values(by='vote_average', ascending=False).head(10)
print('Top 10 filmes mais bem avaliados: ')
print(top10)

#Gráfico 
sns.histplot(df['vote_average'], bins=20)
plt.title('Notas dos Filmes')
plt.show()


