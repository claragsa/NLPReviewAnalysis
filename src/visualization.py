import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def sentiment_analysis_by_product(df, product_col = 'product_name', sentiment_col = 'sentiment', top_n=10):
    sent_count = df.groupby(by=['product_name','sentiment']).size().reset_index(name='count')

    total_sent = sent_count.groupby(by='product_name')['count'].sum().reset_index(name='total')
    sent_count = sent_count.merge(total_sent, on='product_name')
    sent_count['proportion']=sent_count['count']/sent_count['total']

    top_products = total_sent.sort_values(by='total', ascending=False).head(10)['product_name']
    bottom_products = total_sent.sort_values(by='total', ascending=True).head(10)['product_name']

    sent_df_barplot = sent_count.pivot(index='product_name', columns= 'sentiment', values='proportion')
    sent_df_barplot = sent_df_barplot.merge(total_sent.set_index('product_name'), left_index=True, right_index=True, how='left')

    sent_top_barplot = sent_df_barplot.loc[top_products].fillna(0)
    sent_bottom_barplot = sent_df_barplot.loc[bottom_products].fillna(0)
    
    return sent_top_barplot, sent_bottom_barplot

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

def plot_top_commented_topics(df, topic_col = 'topic_text', sentiment_col ='sentiment', top_n=10):
    topic_sentiment = pd.crosstab(df['topic_text'], df['sentiment'])
    topic_counts = df['topic_text'].value_counts()
    top_topics = topic_counts.head(10).index

    top_topic_sent = topic_sentiment.loc[top_topics]

    if 'Outliers' in top_topic_sent.index:
        top_topic_sent = top_topic_sent.drop(index='Outliers', axis='index')

    plt.figure(figsize=(8,6))
    sns.heatmap(top_topic_sent.astype(int), annot=True, cmap='Spectral', fmt = 'd')
    plt.xlabel('Sentiment')
    plt.ylabel('Topics')
    plt.title('Top 10 topics with most reviews')
    plt.show()

def plot_most_positive_topics(df, topic_col= 'topic_text', sentiment_col='sentiment', top_n=10):
    topic_sentiment = pd.crosstab(df[topic_col], df[sentiment_col])
    topic_sentiment['diff_pos_neg'] = abs(topic_sentiment['positive'] - topic_sentiment['negative'])
    top_pol_pos_topics = topic_sentiment.sort_values(by='diff_pos_neg', ascending= False).head(top_n).index.tolist()

    top_pol_pos_topic_sent = topic_sentiment.loc[top_pol_pos_topics, ['negative', 'positive', 'neutral']]

    if 'Outliers' in top_pol_pos_topic_sent.index:
        top_pol_pos_topic_sent = top_pol_pos_topic_sent.drop(index='Outliers', axis='index')

    plt.figure(figsize=(8,6))
    sns.heatmaptop_pol_pos_topic_sent.astype(int), annot=True, cmap='YlGnBu', fmt= 'd')
    plt.xlabel('Sentiment')
    plt.ylabel('Topics')
    plt.title('Top 10 Polarized topics - Positive')
    plt.show()

def plot_most_negative_topics(df, topic_col='topic_text', sentiment_col='sentiment', top_n=10):
    topic_sentiment = pd.crosstab(df[topic_col], df[sentiment_col])
    top_pol_neg_topics = topic_sentiment.sort_values(by='negative', ascending=False).head(10).index.tolist()

    top_pol_neg_topic_sent = topic_sentiment.loc[top_pol_neg_topics, ['negative', 'positive', 'neutral']]
    top_pol_neg_topic_sent_percentage = top_pol_neg_topic_sent.div(top_pol_neg_topic_sent.sum(axis=1), axis=0)*100

    if 'Outliers' in top_pol_neg_topic_sent_percentage.index:
        top_pol_neg_topic_sent_percentage = top_pol_neg_topic_sent_percentage.drop(index='Outliers', axis= 'index')

    plt.figure(figsize=(10,6))
    sns.heatmap(top_pol_neg_topic_sent_percentage, annot=True, cmap='YlOrRd')
    plt.xlabel('Sentiment')
    plt.ylabel('Topics')
    plt.title('Most polarized topics - negative')
    plt.show()
