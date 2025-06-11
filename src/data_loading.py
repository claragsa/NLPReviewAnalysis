import pandas as pd

def load_data():
    df_info = pd.read_csv(r'data\product_info.csv')
    df_reviews_files = [
        r'data\reviews_0-250.csv',
        r'data\reviews_250-500.csv',
        r'data\reviews_500-750.csv',
        r'data\reviews_750-1250.csv',
        r'data\reviews_1250-end.csv'
    ]
    df_reviews = [pd.read_csv(f) for f in df_reviews_files]
    return df_info, df_reviews
