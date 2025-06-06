from transformers import pipeline
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from bertopic import BERTopic
from collections import Counter

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

def common_words_by_sentiment(df, sentiment_column='sentiment', text_column = 'review_text'):
    sentiment_groups = df.groupby(sentiment_column)[text_column].apply(lambda x: ' '.join(x)).reset_index()
    common_words ={}

    for _, row in sentiment_groups.iterrows():
        words = row[text_column].split()
        word_counts = Counter(words)
        common_words[row[sentiment_column]] = word_counts.most_common(10)
    
    return common_words
