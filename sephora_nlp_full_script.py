#--------------------Bibliotecas necessárias
import pandas as pd
import numpy as np

#--------------------Coleta de dados
df_info = pd.read_csv(r'product_info.csv')
df_reviews1 = pd.read_csv(r'reviews_0-250.csv')
df_reviews2 = pd.read_csv(r'reviews_250-500.csv')
df_reviews3 = pd.read_csv(r'reviews_500-750.csv')
df_reviews4 = pd.read_csv(r'reviews_750-1250.csv')
df_reviews5 = pd.read_csv(r'reviews_1250-end.csv')

#--------------------Entendimento do dados
print(df_info.head())
print(df_reviews1.head())

print(df_info.info())
print(df_reviews1.info())

print(df_info.describe())
print(df_reviews1.describe())

#--------------------Limpeza e pré-processamento

#--------------------Análise exploratória

#--------------------Natural Language Processing

#--------------------Visualizações
