from src.data_loading import load_data
from src.preprocessing import clean_info, clean_reviews, clean_text
from src.eda import plot_most_popular_brands, plot_most_reviewed_brands, plot_most_reviewed_products, plot_top_popular_products, plot_ratings_distribuition, plot_word_cloud, plot_temporal_analysis
from src.nlp_analysis import get_sentiment, get_topics, common_words_by_sentiment
from src.visualization import sentiment_analysis_by_product, stacked_plot, plot_top_commented_topics, plot_most_positive_topics, plot_most_negative_topics


def main():
    df_info, dfs_reviews = load_data()

    df_info = clean_info(df_info)
    dfs_reviews = [clean_reviews(df) for df in dfs_reviews]
    dfs_reviews = [clean_text(df) for df in dfs_reviews]

    import pandas as pd
    df_sampled = pd.concat([df.sample(n=min(1000, len(df)), random_state=42) for df in dfs_reviews], ignore_index=True)

    plot_most_reviewed_products(df_info)
    plot_top_popular_products(df_info)
    plot_most_reviewed_brands(df_info)
    plot_most_popular_brands(df_info)
    plot_ratings_distribuition(df_info)
    plot_word_cloud(df_sampled)
    plot_temporal_analysis(dfs_reviews)

    df_sentiment = get_sentiment(df_sampled)
    df_topics, topic_model, topics, probs = get_topics(df_sampled)
    common_words = common_words_by_sentiment(df_sampled)

    sent_top_barplot, sent_bottom_barplot = sentiment_analysis_by_product(dfs_reviews)
    stacked_plot(sent_top_barplot, 'Sentiment proportion of the top 10 products better reviewed')
    stacked_plot(sent_bottom_barplot, 'Sentiment proportion of the top 10 products worst reviewed')
    plot_top_commented_topics(dfs_reviews)
    plot_most_positive_topics(dfs_reviews)
    plot_most_negative_topics(dfs_reviews)

if __name__ == '__main__':
    main()
