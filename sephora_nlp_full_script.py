#--------------------Bibliotecas necessárias
import pandas as pd
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
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
from transformers import pipeline
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from bertopic import BERTopic

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
# produtos mais populares por avaliações e melhores notas
most_reviews_products = df_info.sort_values(by= 'reviews', ascending=False).head(20) #refiltrar pós limpeza
plt.figure(figsize=(12, 6))
sns.barplot(data= most_reviews_products, x = 'reviews', y='product_name', hue= 'product_name', orient = 'h')
plt.title('Quantidade de avaliações por produto')
plt.xlabel('Número de avaliações')
plt.ylabel('Produtos')
plt.tight_layout()
plt.show()

top_products = df_info.sort_values(by= 'rating', ascending=False).head(20) #refiltrar pós limpeza
plt.figure(figsize=(12, 6))
sns.barplot(data= top_products, x = 'rating', y='product_name', hue= 'product_name', orient = 'h')
plt.title('Melhores produtos por avaliação')
plt.xlabel('Avaliação')
plt.ylabel('Produtos')
plt.tight_layout()
plt.show()

# quais as marcas tem mais avaliações e quais sao melhores avaliadas
most_reviews_brands = df_info.groupby(['brand_id', 'brand_name']).agg({'reviews': 'sum'}).reset_index()
most_reviews_brands = most_reviews_brands.sort_values(by= 'reviews', ascending=False).head(20)
plt.figure(figsize=(12, 6))
sns.barplot(data= most_reviews_brands, x = 'reviews', y='brand_name', hue='brand_name',orient = 'h', errorbar=None)
plt.title('Quantidade de avaliações por marca')
plt.xlabel('Número de avaliações')
plt.ylabel('Marcas')
plt.tight_layout()
plt.show()

top_brands = df_info.groupby(['brand_id', 'brand_name']).agg({'rating': 'mean'}).reset_index()
top_brands = top_brands.sort_values(by='rating', ascending= False).head(20)
plt.figure(figsize=(12, 6))
sns.barplot(data= top_brands, x = 'rating', y='brand_name', hue='brand_name', orient = 'h')
plt.title('Melhores marcas por avaliação')
plt.xlabel('Avaliação')
plt.ylabel('Marcas')
plt.tight_layout()
plt.show()

# distribuição de avaliações 
plt.figure(figsize=(10, 6))
sns.histplot(df_info['rating'], bins= 5)
plt.title('Distribuição de avaliações')
plt.xlabel('Avaliação')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# nuvem de palavras
stopwords_custom = set(STOPWORDS).union(set(['im', 'ive', 'like', 'it', 'its', 'that', 'this', 'and', 'the', 'to', 'a', 'of', 'is', 'for', 'in', 'on', 'with', 'dont', 'make', 'didnt', 'cant']))

all_text = ' '.join(df_reviews1['review_text'].astype(str)) + ' ' + \
           ' '.join(df_reviews2['review_text'].astype(str)) + ' ' + \
           ' '.join(df_reviews3['review_text'].astype(str)) + ' ' + \
           ' '.join(df_reviews4['review_text'].astype(str)) + ' ' + \
           ' '.join(df_reviews5['review_text'].astype(str))
words = [word.lower() for word in all_text.split() if word.lower() not in stopwords_custom]
word_freq = Counter(words)
wordcloud = WordCloud(width=800, 
                      height=400, 
                      background_color='white', 
                      colormap='magma',
                      stopwords=stopwords_custom)
wordcloud.generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvem de palavras')
plt.show()

# analise temporal
sns.lineplot(data=df_reviews1, x='submission_time', y='rating')
plt.title('Avaliação ao longo do tempo')
plt.xlabel('Ano')
plt.ylabel('Avaliação')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#--------------------Natural Language Processing
# análise de sentimentos
def get_sentiment(df):
    sentiment = []
    scores = []
    sentiment_pipeline = pipeline('sentiment-analysis', model = 'cardiffnlp/twitter-roberta-base-sentiment')
    label_mapping = {
        'LABEL_0': 'negative',
        'LABEL_1': 'neutral',
        'LABEL_2': 'positive'
    }
    for text in tqdm(df['review_text']):
        result = sentiment_pipeline(text)
        label = result[0]['label']
        score = result[0]['score']
        mapped_label = label_mapping[label]
        sentiment.append(mapped_label)
        scores.append(score)
    df['sentiment_score'] = scores
    df['sentiment'] = sentiment
    return df
df_reviews5 = get_sentiment(df_reviews5) #apenas um df_reviews para poupar tempo

# verificando os sentimentos analisados
print('\nSentimentos após NLP:')
print(df_reviews5[['review_text', 'sentiment', 'sentiment_score']].head())

# descobrir os temas mais comuns (utilizando df_reviews5)
def get_topics(df, text_column = 'review_text', language = 'english', min_topic_size=50, n_gram_range=(1,2), n_top_words=10):
    texts = df[text_column].astype(str).tolist()
    vectorizer_model = CountVectorizer(
        stop_words = 'english',
        ngram_range=n_gram_range
    )
    topic_model = BERTopic(
        language=language,
        min_topic_size=min_topic_size,
        vectorizer_model=vectorizer_model,
        verbose = True
    )
    topics, probs = topic_model.fit_transform(texts)

    topic_words = {}
    for topic_num in set(topics):
        if topic_num == -1:
            topic_words[topic_num] = "Outliers"
        else:
            words = topic_model.get_topic(topic_num)
            top_words = [word for word, _ in words[:n_top_words]]
            topic_words[topic_num] = ", ".join(top_words)

    df['topic'] = topics
    df['topic_text'] = [topic_words[t] for t in topics]
    return df, topic_model, topics, probs

df_reviews5, topic_model, topics, probs = get_topics(df_reviews5)
topic_model.visualize_topics()

# quais as palavras mais comuns em cada tipo de avaliação (positiva, negativa, neutra)
def common_words_by_sentiment(df, sentiment_column='sentiment', text_column = 'review_text'):
    sentiment_groups = df.groupby(sentiment_column)[text_column].apply(lambda x: ' '.join(x)).reset_index()
    common_words ={}

    for _, row in sentiment_groups.iterrows():
        words = row[text_column].split()
        word_counts = Counter(words)
        common_words[row[sentiment_column]] = word_counts.most_common(10)
    
    return common_words

common_words_review5 = common_words_by_sentiment(df_reviews5, sentiment_column = 'sentiment', text_column='review_text')


#--------------------Geração de insights
# sentimento geral por produto
sent_count = df_reviews5.groupby(by=['product_name','sentiment']).size().reset_index(name='count')

total_sent = sent_count.groupby(by='product_name')['count'].sum().reset_index(name='total')
sent_count = sent_count.merge(total_sent, on='product_name')
sent_count['proportion']=sent_count['count']/sent_count['total']

top_products = total_sent.sort_values(by='total', ascending=False).head(10)['product_name']
bottom_products = total_sent.sort_values(by='total', ascending=True).head(10)['product_name']

sent_df_barplot = sent_count.pivot(index='product_name', columns= 'sentiment', values='proportion')
sent_df_barplot = sent_df_barplot.merge(total_sent.set_index('product_name'), left_index=True, right_index=True, how='left')

sent_top_barplot = sent_df_barplot.loc[top_products]
sent_bottom_barplot = sent_df_barplot.loc[bottom_products]
sent_top_barplot = sent_top_barplot.fillna(0)
sent_bottom_barplot = sent_bottom_barplot.fillna(0)

def stacked_plot(data, title):
    ax=data[['negative', 'neutral', 'positive']].plot(
        kind = 'bar',
        stacked = True,
        color = ['red', 'gray', 'green'],
        figsize = (12,10)
    )
    for idx, row in data.iterrows():
        cumulative =0
        for sentiment in ['negative', 'neutral', 'positive']:
            proportion = row[sentiment]
            if proportion >0.05:
                ax.text(
                    x = list(data.index).index(idx),
                    y = cumulative + proportion/2,
                    s = f"{proportion *100:.1f}%",
                    ha = 'center',
                    va = 'center',
                    color = 'white',
                    fontweight = 'bold'
                )
            cumulative += proportion
    for idx, total in enumerate(data['total']):
        ax.text(
            idx,
            1.02,
            str(total),
            ha = 'center',
            va = 'bottom'
        )
    plt.ylabel('Proportion')
    plt.xlabel('Products')
    plt.title(title)
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.show()

stacked_plot(sent_top_barplot, 'Proporção dos sentimentos para os 10 produtos mais avaliados')
stacked_plot(sent_bottom_barplot, 'Proporção dos sentimentos para os 10 produtos menos avaliados')
# identificação dos principais temas de interesse/dor

