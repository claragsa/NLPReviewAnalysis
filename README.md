# Product Review Analysis of Sephora Using NLP and Visualizations

This project aims to analyze thousands of beauty product reviews from Sephora, answering key questions about popularity, customer perception, most discussed topics, and user sentiment. Using NLP techniques and exploratory analysis, we seek insights that can support the company in marketing strategies and product development.

---

## Business Questions

- Which products have the most reviews?
- Which products and brands are the highest rated?
- What is the overall sentiment of reviews by product type?
- What are the main topics mentioned in the reviews?
- Which topics show the most positive or negative sentiments?

---

## Data

Metadata:

Product Data Content

| Feature              | Description |
|----------------------|-------------|
| product_id           | The unique identifier for the product from the site |
| product_name         | The full name of the product |
| brand_id             | The unique identifier for the product brand from the site |
| brand_name           | The full name of the product brand |
| loves_count          | The number of people who have marked this product as a favorite |
| rating               | The average rating of the product based on user reviews |
| reviews              | The number of user reviews for the product |
| size                 | The size of the product, which may be in oz, ml, g, packs, or other units depending on the product type |
| variation_type       | The type of variation parameter for the product (e.g. Size, Color) |
| variation_value      | The specific value of the variation parameter for the product (e.g. 100 mL, Golden Sand) |
| variation_desc       | A description of the variation parameter for the product (e.g. tone for fairest skin) |
| ingredients          | A list of ingredients included in the product |
| price_usd            | The price of the product in US dollars |
| value_price_usd      | The potential cost savings of the product, presented on the site next to the regular price |
| sale_price_usd       | The sale price of the product in US dollars |
| limited_edition      | Indicates whether the product is a limited edition or not (1-true, 0-false) |
| new                  | Indicates whether the product is new or not (1-true, 0-false) |
| online_only          | Indicates whether the product is only sold online or not (1-true, 0-false) |
| out_of_stock         | Indicates whether the product is currently out of stock or not (1 if true, 0 if false) |
| sephora_exclusive    | Indicates whether the product is exclusive to Sephora or not (1 if true, 0 if false) |
| highlights           | A list of tags or features that highlight the product's attributes |
| primary_category     | First category in the breadcrumb section |
| secondary_category   | Second category in the breadcrumb section |
| tertiary_category    | Third category in the breadcrumb section |
| child_count          | The number of variations of the product available |
| child_max_price      | The highest price among the variations of the product |
| child_min_price      | The lowest price among the variations of the product |

Reviews Data Content

| Feature                 | Description |
|-------------------------|-------------|
| author_id               | The unique identifier for the author of the review on the website |
| rating                  | The rating given by the author for the product on a scale of 1 to 5 |
| is_recommended          | Indicates if the author recommends the product or not (1-true, 0-false) |
| helpfulness             | The ratio of all ratings to positive ratings for the review |
| total_feedback_count    | Total number of feedback (positive and negative ratings) left by users for the review |
| total_neg_feedback_count| The number of users who gave a negative rating for the review |
| total_pos_feedback_count| The number of users who gave a positive rating for the review |
| submission_time         | Date the review was posted on the website in the 'yyyy-mm-dd' format |
| review_text             | The main text of the review written by the author |
| review_title            | The title of the review written by the author |
| skin_tone               | Author's skin tone (e.g. fair, tan, etc.) |
| eye_color               | Author's eye color (e.g. brown, green, etc.) |
| skin_type               | Author's skin type (e.g. combination, oily, etc.) |
| hair_color              | Author's hair color (e.g. brown, auburn, etc.) |
| product_id              | The unique identifier for the product on the website |

The project uses two datasets:

- `df_info`: Product information (name, brand, rating, number of reviews, etc.)
- `dfs_reviews`: A list with five DataFrames containing textual reviews and metadata (rating, recommendation, date, etc.)

### Preprocessing

- Removal of irrelevant columns (`Unnamed: 0`)
- Elimination of null values in critical columns (rating, reviews, review_text, etc.)
- Tokenization, cleaning, and normalization of text

---

## Exploratory Data Analysis (EDA)

### Most Popular and Highest-Rated Products
![Top 20 Most Reviewed Products](images/top_20_most_reviewed_products.png)
![Top 20 Highest Rated Products](images/top_20_highest_rated_products.png)

💡 The most popular products are not necessarily the highest-rated ones, suggesting that niche items may have better acceptance, while popular products tend to have diluted averages.

---

### Most Popular vs. Highest-Rated Brands
![Top 20 Most Reviewed Products](images/top_20_most_reviewed_brands.png)
![Top 20 Highest Rated Brands](images/top_20_highest_rated_brands.png)

💡 The pattern repeats for brands — the most reviewed are not the best rated. Niche brands with loyal audiences stand out positively.

---

### Rating Distribution
![Rating Distribution](images/rating_distribuition.png)
💡 The distribution is right-skewed. Most reviews have high ratings, highlighting overall customer satisfaction.

---

### Word Cloud
![Word Cloud](images/wordcloud.png)

💡 Terms related to skincare, such as “skin,” “cream,” “moisturizer,” “love,” and “great,” are predominant. This reinforces the success of the skincare line and the positive sentiment.

---

### Temporal Analysis
![Temporal Analysis](images/temporal_analysis.png)

💡 The chart shows a trend toward more positive and less dispersed reviews starting in 2020, suggesting a possible improvement in product quality or a change in consumer behavior over time.

---

## Natural Language Processing (NLP)

### Sentiment

![Sentiments Proportion](images/sentiment_proportion.png)
💡 Among the 15 most-reviewed products, most reviews are positive, with proportions above 50%. Only two products show a more mixed sentiment, but still with the majority being positive (over 40%).

---

### Topics with BERTopic

- **50 unique topics** were extracted using BERTopic to reduce redundancy.

### Most Discussed Topics

💡 Skincare-related topics dominate — moisturizers, sunscreens, serums, etc.

### Most Positive Topics

💡 The most popular topics are also closely related to skincare. Additionally, issues like oily skin, dark circles, and chapped lips appear to be well addressed by the products.

### Most Negative Topics

💡 It is not possible to gather 10 topics where negative sentiment is predominant. Thus, the main complaints revolve around:

- Packaging that doesn't work properly  
- Changes in formulas that customers disliked  
- Products that caused a burning sensation on sensitive skin  

---

## Insights and Recommended Actions

### For the Marketing Team:

- Leverage campaigns around the highest-rated products and topics, especially **skincare**
- Promote well-rated niche products

### For the Product/Partner Team:

- Investigate products that had formula changes and consider reverting to the previous formula  
- Review packaging for products reported to have quick defects  
- **Report to brands** any issues related to formulas or allergic reactions

---

## Conclusion

Sephora demonstrates excellent product curation, with very high levels of customer satisfaction. The dominance of skincare products in the reviews highlights an opportunity to strengthen this segment. Sentiment and topic analysis proved to be an effective tool for understanding customer pain points and desires at scale.
