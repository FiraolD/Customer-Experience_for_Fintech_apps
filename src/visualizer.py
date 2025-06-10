import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import wordcloud
from collections import Counter
import ast

# Load data
df = pd.read_csv('C:/Users/firao/Source/Repos/Customer-Experience_for_Fintech_apps/data/thematic_reviews.csv', on_bad_lines='skip')

# Clean and parse keywords
def safe_parse_keywords(keywords):
    try:
        return ast.literal_eval(keywords.replace("['", "['").replace("']", "']"))
    except:
        return []

df['keywords_list'] = df['keywords'].apply(safe_parse_keywords)

print(df.columns.tolist())
positive_keywords = [kw for kws in df[df['sentiment'] == 'positive']['keywords_list'] for kw in kws]
positive_counts = Counter(positive_keywords)

plt.figure(figsize=(10, 6))
sns.barplot(x=pd.Series(positive_counts).sort_values(ascending=False).head(10).values,
            y=pd.Series(positive_counts).sort_values(ascending=False).head(10).index,
            palette="Greens_d")
plt.title("Top Positive Keywords")
plt.xlabel("Frequency")
plt.ylabel("Keywords")
plt.show()

negative_keywords = [kw for kws in df[df['sentiment'] == 'negative']['keywords_list'] for kw in kws]
negative_counts = Counter(negative_keywords)

plt.figure(figsize=(10, 6))
sns.barplot(x=pd.Series(negative_counts).sort_values(ascending=False).head(10).values,
            y=pd.Series(negative_counts).sort_values(ascending=False).head(10).index,
            palette="Reds_d")
plt.title("Top Negative Keywords")
plt.xlabel("Frequency")
plt.ylabel("Keywords")
plt.show()

bank_avg_score = df.groupby('bank')['score'].mean().sort_values(ascending=False)
print(bank_avg_score)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=bank_avg_score.values, y=bank_avg_score.index, palette="Blues_d")
plt.title("Average Rating by Bank")
plt.xlabel("Average Score")
plt.ylabel("Bank")
plt.show()

bank_sentiment = df.groupby(['bank', 'sentiment']).size().unstack(fill_value=0)
bank_sentiment.plot(kind='bar', stacked=True, figsize=(10, 6), color=['green', 'gray', 'red'])
plt.title("Sentiment Distribution by Bank")
plt.ylabel("Count")
plt.xlabel("Bank")
plt.xticks(rotation=0)
plt.legend(title='Sentiment')
plt.show()

sns.countplot(data=df, x='sentiment', order=df['sentiment'].value_counts().index, palette="Set2")
plt.title("Overall Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

sns.histplot(df['score'], bins=range(1,6), discrete=True, shrink=0.8, color="skyblue")
plt.title("Rating Distribution")
plt.xlabel("Score")
plt.ylabel("Count")
plt.xticks(range(1,6))
plt.show()

all_keywords = ' '.join([kw for kws in df['keywords_list'] for kw in kws])
wordcloud = Wordcloud(width=800, height=400, background_color='white').generate(all_keywords)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Keyword Cloud")
plt.show()