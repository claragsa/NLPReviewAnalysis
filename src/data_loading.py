import pandas as pd

def data_load():
    df_info = pd.read_csv(r'data\product_info.csv')
    df_reviews_files = [
        'data\reviews_0-250.csv',
        'data\reviews_250-500.csv',
        'data\reviews_500-750.csv',
        'data\reviews_750-1250.csv',
        'data\reviews_1250-end.csv'
    ]
    df_reviews = [pd.read_csv(f) for f in df_reviews_files]
    return df_info, df_reviews