from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv("C:/Users/firao/Source/Repos/Customer-Experience_for_Fintech_apps/data/sentiment_reviews.csv")

# Extract keywords using TF-IDF
vectorizer = TfidfVectorizer(max_features=50, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['content'])
keywords = vectorizer.get_feature_names_out()

# Add keywords to DataFrame
df['keywords'] = df['content'].apply(lambda x: [word for word in x.split() if word in keywords])

# Group keywords into themes (manual mapping)
themes = {
    "account_access": ["login", "password", "access"],
    "transaction_performance": ["transfer", "slow", "fast"],
    "user_experience": ["ui", "design", "slow", "interface", "easy", "difficult", "crash", "accesbility", "complex", "fast", "convenient", "speed", "seamless", "reliable", "busy"]
}

df['theme'] = df['keywords'].apply(
    lambda x: next((theme for theme, words in themes.items() if any(word in x for word in words)), "other")
)

# Save results
thematic_file = "data/thematic_reviews.csv"
df.to_csv(thematic_file, index=False)
print(f"Thematic analysis completed and saved to {thematic_file}")