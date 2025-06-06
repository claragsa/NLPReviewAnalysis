import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from collections import Counter

def plot_most_reviewed_products(df_info):
    most_reviews_products = df_info.sort_values(by= 'reviews', ascending=False).head(20)
    plt.figure(figsize=(12, 6))
    plot_most_reviews_product = sns.barplot(data= most_reviews_products, x = 'reviews', y='product_name', hue= 'product_name', orient = 'h')
    plt.title('Number of reviews per product')
    plt.xlabel('Number of reviews')
    plt.ylabel('Products')
    plt.tight_layout()
    plt.show()
    return plot_most_reviews_product

def plot_top_popular_products(df_info):
    top_products = df_info.sort_values(by= 'rating', ascending=False).head(20) 
    plt.figure(figsize=(12, 6))
    plot_top_products = sns.barplot(data= top_products, x = 'rating', y='product_name', hue= 'product_name', orient = 'h')
    plt.title('Top products per rating')
    plt.xlabel('Rating')
    plt.ylabel('Products')
    plt.tight_layout()
    plt.show()
    return plot_top_products

def plot_most_reviewed_brands (df_info):
    most_reviews_brands = df_info.groupby(['brand_id', 'brand_name']).agg({'reviews': 'sum'}).reset_index()
    most_reviews_brands = most_reviews_brands.sort_values(by= 'reviews', ascending=False).head(20)
    plt.figure(figsize=(12, 6))
    plot_most_reviewed_brands = sns.barplot(data= most_reviews_brands, x = 'reviews', y='brand_name', hue='brand_name',orient = 'h', errorbar=None)
    plt.title('Number of reviews per brand')
    plt.xlabel('Number of reviews')
    plt.ylabel('Brands')
    plt.tight_layout()
    plt.show()
    return plot_most_reviewed_brands


def plot_most_popular_brands(df_info):
    top_brands = df_info.groupby(['brand_id', 'brand_name']).agg({'rating': 'mean'}).reset_index()
    top_brands = top_brands.sort_values(by='rating', ascending= False).head(20)
    plt.figure(figsize=(12, 6))
    plot_top_brands = sns.barplot(data= top_brands, x = 'rating', y='brand_name', hue='brand_name', orient = 'h')
    plt.title('Top brands per rating')
    plt.xlabel('Rating')
    plt.ylabel('Brands')
    plt.tight_layout()
    plt.show()
    return plot_top_brands

def plot_ratings_distribuition(df_info):
    plt.figure(figsize=(10, 6))
    rating_distribuition = sns.histplot(df_info['rating'], bins= 5)
    plt.title('Rating Distribuition')
    plt.xlabel('Rating')
    plt.ylabel('Frequence')
    plt.tight_layout()
    plt.show()
    return rating_distribuition

def plot_word_cloud(dfs, column = 'review_text'):
    stopwords_custom = set(STOPWORDS).union(set(['im', 'ive', 'like', 'it', 'its', 'that', 'this', 'and', 'the', 'to', 'a', 'of', 'is', 'for', 'in', 'on', 'with', 'dont', 'make', 'didnt', 'cant']))

    all_text = ' '.join(
        ' '.join(df[column].astype(str) for df in dfs if column in df.columns)
    )
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
    plt.title('Word Cloud')
    plt.show()
    return wordcloud

def plot_temporal_analysis(df):
    plot_temporal_analysis = sns.lineplot(data=df, x='submission_time', y='rating')
    plt.title('Avaliação ao longo do tempo')
    plt.xlabel('Ano')
    plt.ylabel('Avaliação')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return plot_temporal_analysis
