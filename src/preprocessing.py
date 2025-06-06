import pandas as pd
import re
import unicodedata
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clean_info(df):
    df = df.dropna(subset=['rating', 'reviews'], inplace=True)
    return df

def clean_reviews(df):
    df = df.dropna(subset=['review_text', 'is_recommended', 'helpfulness'])
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis=1, inplace=True)
    if 'submission_time' in df.columns:
        df['submission_time'] = pd.to_datetime(df['submission_time'])
    return df
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