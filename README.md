# 🧴 Sephora Product Review Analysis with NLP and Visualizations

This project aims to analyze thousands of product reviews from Sephora to answer key business questions about popularity, customer perception, most discussed topics, and overall sentiment. By applying NLP techniques and exploratory data analysis, we extract insights that can guide marketing and product development strategies.

---

## 🧠 Business Questions

- Which products have the most reviews?
- Which products and brands are the highest rated?
- What is the overall sentiment of reviews by product type?
- What are the main topics mentioned in the reviews?
- Which topics have more positive or negative sentiment?

---

## 📦 Data

The project uses two datasets:

- `df_info`: Product information (name, brand, rating, number of reviews, etc.)
- `dfs_reviews`: A list of DataFrames containing review texts and metadata (rating, recommendation, date, etc.)

### Preprocessing
- Removal of irrelevant columns (`Unnamed: 0`)
- Elimination of missing values in key columns (rating, reviews, review_text, etc.)
- Text tokenization, cleaning, and normalization

---

## 🔍 Exploratory Data Analysis (EDA)

### Most Popular and Highest Rated Products

![Top 20 Most Reviewed Products](INSERT_IMAGE_PATH1)
![Top 20 Highest Rated Products](INSERT_IMAGE_PATH2)

💡 The most popular products are not necessarily the highest rated, suggesting that niche products often have better acceptance, while popularity dilutes the average rating.

---

### Most Popular vs. Best Rated Brands

![Top 20 Most Reviewed Brands](INSERT_IMAGE_PATH3)
![Top 20 Highest Rated Brands](INSERT_IMAGE_PATH4)

💡 The same pattern applies to brands — the most reviewed are not always the best rated. Niche brands with loyal customers stand out positively.

---

### Rating Distribution

![Ratings Histogram](INSERT_IMAGE_PATH5)

💡 The distribution is right-skewed. Most reviews have high ratings, indicating high customer satisfaction overall.

---

### Word Cloud

![Wordcloud of Reviews](INSERT_IMAGE_PATH6)

💡 Words like “skin”, “cream”, “hydrating”, “love”, and “good” dominate. This highlights the success of the skincare segment and a generally positive tone in reviews.

---

### Temporal Analysis

![Review Trends Over Time](INSERT_IMAGE_PATH7)

💡 There's a noticeable drop in ratings in 2020 followed by recovery. This might reflect external events (e.g., pandemic) or product/marketing changes.

---

## 💬 Natural Language Processing (NLP)

### Sentiment Analysis

![Sentiment of Top 20 Products](INSERT_IMAGE_PATH8)

💡 Among the 20 most reviewed products, more than 60% of reviews are negative — except for just two products.

---

### Topic Modeling with BERTopic

- **50 unique topics** were extracted using BERTopic to reduce redundancy.

#### Most Discussed Topics

![Most Frequent Topics](INSERT_IMAGE_PATH9)

💡 Skincare-related topics dominate — moisturizers, sunscreens, serums, etc.

#### Most Positive Topics

![Most Positive Topics](INSERT_IMAGE_PATH10)

💡 The most popular topics also tend to be the most positively rated.

#### Most Negative Topics

![Most Negative Topics](INSERT_IMAGE_PATH11)

💡 Complaints revolve around:
- “NuFace” brand
- Sample sizes
- Formula changes
- Allergic reactions

---

## 📈 Insights & Recommendations

### For the Marketing Team:
- Highlight and promote products and topics with the most positive sentiment — especially **skincare**
- Give visibility to niche, well-rated products

### For the Product/Partner Teams:
- Investigate low-rated products like the **Trinity + Eye and Lip Enhancer**
- Re-evaluate **sample policies**
- **Report to brands** issues regarding formulas or adverse reactions

---

## ✅ Conclusion

Sephora offers excellent product curation, with high customer satisfaction overall. The dominance of skincare in reviews reveals an opportunity to double down on this segment. Sentiment and topic analysis proved effective in uncovering customer pain points and desires at scale.

---

## 🔧 Future Improvements

- Implement parallelization to speed up sentiment analysis
- Analyze reviews by customer age group (if data available)
- Build an interactive dashboard using Streamlit or Power BI
- Automatically classify reviews by category (skincare, perfume, makeup, etc.)

---
