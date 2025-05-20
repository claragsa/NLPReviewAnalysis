#--------------------Bibliotecas necessárias
import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
import unicodedata

#--------------------Coleta de dados
df_info = pd.read_csv(r'product_info.csv')
df_reviews1 = pd.read_csv(r'reviews_0-250.csv')
df_reviews2 = pd.read_csv(r'reviews_250-500.csv')
df_reviews3 = pd.read_csv(r'reviews_500-750.csv')
df_reviews4 = pd.read_csv(r'reviews_750-1250.csv')
df_reviews5 = pd.read_csv(r'reviews_1250-end.csv')

#--------------------Entendimento do dados
print('Primeiras informações dos dataframes:')
print('Head df_info:')    
print(df_info.head())
print('\nHead df_reviews1:')
print(df_reviews1.head())

print('\nInfo df_info:')
print(df_info.info())
print('\nInfo df_reviews1:')
print(df_reviews1.info())

print('\nDescriptive statistics df_info:')
print(df_info.describe())
print('\nDescriptive statistics df_reviews1:')
print(df_reviews1.describe())

print('\nValores únicos por coluna:')
print('df_info:')
print(df_info.nunique())
print('\ndf_reviews1:')
print(df_reviews1.nunique())
print('\ndf_reviews2:')
print(df_reviews2.nunique())
print('\ndf_reviews3:')
print(df_reviews3.nunique())
print('\ndf_reviews4:')
print(df_reviews4.nunique())
print('\ndf_reviews5:')
print(df_reviews5.nunique())

print('\nValores nulos por coluna:')
print('df_info:')
print(df_info.isnull().sum())
print('\ndf_reviews1:')
print(df_reviews1.isnull().sum())
print('\ndf_reviews2:')
print(df_reviews2.isnull().sum())
print('\ndf_reviews3:')
print(df_reviews3.isnull().sum())
print('\ndf_reviews4:')
print(df_reviews4.isnull().sum())
print('\ndf_reviews5:')
print(df_reviews5.isnull().sum())

print('\nValores duplicados por coluna:')
print('\ndf_info:')
print(df_info.duplicated().sum())
print('\ndf_reviews1:')
print(df_reviews1.duplicated().sum())
print('\ndf_reviews2:')
print(df_reviews2.duplicated().sum())
print('\ndf_reviews3:')
print(df_reviews3.duplicated().sum())
print('\ndf_reviews4:')
print(df_reviews4.duplicated().sum())
print('\ndf_reviews5:')
print(df_reviews5.duplicated().sum())

# produtos com mais avaliações e melhores avaliados
most_reviews_products = df_info.sort_values(by= 'reviews', ascending=False).head(20)
print('\nTop 20 produtos com mais avaliações:')
print(most_reviews_products[['product_id', 'product_name', 'reviews']])

top_products = df_info.sort_values(by= 'rating', ascending=False).head(20)
print('\nTop 20 produtos melhor avaliados:')
print(top_products[['product_id', 'product_name', 'rating']])

# quais as marcas tem mais avaliações e quais sao melhores avaliadas
most_reviews_brands = df_info.sort_values(by= 'reviews', ascending=False).head(20)
print('\nTop 20 marcas com mais avaliações:')
print(most_reviews_brands[['brand_id', 'brand_name', 'reviews']])

top_brands = df_info.groupby(['brand_id', 'brand_name']).agg({'rating': 'mean'}).reset_index()
top_brands = top_brands.sort_values(by='rating', ascending= False).head(20)
print('\nTop 20 marcas melhor avaliadas:')
print(top_brands[['brand_id', 'brand_name', 'rating']])


#--------------------Limpeza e pré-processamento
# limpeza dos dados
df_info.dropna(subset=['rating', 'reviews'], inplace=True)

df_reviews1 = df_reviews1.dropna(subset=['review_text', 'is_recommended', 'helpfulness'])
df_reviews2 = df_reviews2.dropna(subset=['review_text', 'is_recommended', 'helpfulness'])
df_reviews3 = df_reviews3.dropna(subset=['review_text', 'is_recommended', 'helpfulness'])
df_reviews4 = df_reviews4.dropna(subset=['review_text', 'is_recommended', 'helpfulness'])
df_reviews5 = df_reviews5.dropna(subset=['review_text', 'is_recommended', 'helpfulness'])

df_reviews1.drop('Unnamed: 0', axis=1, inplace=True)
df_reviews2.drop('Unnamed: 0', axis=1, inplace=True)
df_reviews3.drop('Unnamed: 0', axis=1, inplace=True)
df_reviews4.drop('Unnamed: 0', axis=1, inplace=True)
df_reviews5.drop('Unnamed: 0', axis=1, inplace=True)


# limpeza do texto
def clean_text(text):
    text = re.sub(r'<.*?>', '', text) #remove tags HTML
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) #remove caracteres especiais
    text = re.sub(r'\s+', ' ', text) #remove espaços em branco extras

    text = text.lower() # converte para minusculas
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8') # remove acentos

    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english')) 
    tokens = [ word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)
df_reviews1['review_text'] = df_reviews1['review_text'].apply(clean_text)
df_reviews2['review_text'] = df_reviews2['review_text'].apply(clean_text)
df_reviews3['review_text'] = df_reviews3['review_text'].apply(clean_text)
df_reviews4['review_text'] = df_reviews4['review_text'].apply(clean_text)
df_reviews5['review_text'] = df_reviews5['review_text'].apply(clean_text)

#--------------------Análise exploratória

#--------------------Natural Language Processing

#--------------------Visualizações
