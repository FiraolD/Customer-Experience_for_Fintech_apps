import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import WordCloud
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