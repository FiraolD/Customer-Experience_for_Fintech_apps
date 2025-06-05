from textblob import TextBlob
import pandas as pd

df = pd.read_csv("C:/Users/firao/Source/Repos/Customer-Experience_for_Fintech_apps/data/clean_reviews.csv")
# Function to calculate sentiment
def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

# Apply sentiment analysis
df['sentiment'] = df['content'].apply(get_sentiment)

# Save results
sentiment_file = "data/sentiment_reviews.csv"
df.to_csv(sentiment_file, index=False)
print(f"Sentiment analysis completed and saved to {sentiment_file}")