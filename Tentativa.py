# Versão da Linguagem Python
from platform import python_version
print(f'Versão da linguagem python usada neste Jupyter Notebook: {python_version()}')

# ---------------------------------------------------------------------------
#IMPORTS
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------------------
# Carrega os dados
df_dsa = pd.read_csv('dados/dados_clientes.csv')

type(df_dsa)

# Visualiza as 10 primeiras linhas
print(df_dsa.head(10))

# ---------------------------------------------------------------------------
## ANÁLISE EXPLORATÓRIA

# Resumo Estatístico
resumo_estat = df_dsa[['idade', 'renda_anual', 'pontuacao_gastos']].describe()
print(resumo_estat)

# ---------------------------------------------------------------------------
## PRÉ - PROCESSAMENTO DOS DADOS

# Cria o padronizador dos dados - KMEANS (algoritmo para não supervisionado)
# precisa de entradas padronizadas (investigar o que espera)
padronizador = StandardScaler() #Cria o objeto
#KMEANS Espera receber na mesma escala (cria escala logartmica)

#Aplica o padronizador nas colunas de interesse
dados_padronizados = padronizador.fit_transform(df_dsa[['idade', 'renda_anual', 'pontuacao_gastos']])
#Efetivamente transporta os dados

#Visualiza os dados
print(dados_padronizados)
# ---------------------------------------------------------------------------

## CONSTRUÇÃO DO MODELO DE MACHINE LEARNING PARA SEGMENTAÇÃO DE CLIENTES

# Definimos o número de clusters (grupos) = (k)
k = 3

#Criamos o modelo K - means
kmeans = KMeans(n_clusters = k)

#Treinamento do modelo com os dados padronizados
kmeans.fit(dados_padronizados)

#Atribuímos os rótulos dos clusters dos clientes
df_dsa['cluster'] = kmeans.labels_ #Associa os clusters a uma nova variável do dataframe

#Exibe o resultado das 10 primeiras linhas
amostra_result = df_dsa.sample(10)
print(amostra_result)

# ---------------------------------------------------------------------------
#Salvamos o resultado em disco
df_dsa.to_csv('dados/dados_segmentados.csv', index = False)
# ---------------------------------------------------------------------------

