from google_play_scraper import reviews, Sort
import pandas as pd
import os
# Define app IDs for the three banks
app_ids = {
    "CBE": "com.combanketh.mobilebanking",  # App-Id for CBE
    "BOA": "com.boa.boaMobileBanking",      # App-Id for BOA
    "Dashen": "com.dashen.dashensuperapp",  # App-Id for Dashen bank
    "Awash": "com.awashbank.mobile",        #App-Id for Awash bank
    "COOP": "com.cbo.mobilebanking"         #App-Id for COOP
}

# Function to scrape reviews
def scrape_reviews(app_id, bank_name, count=400):
    review_data, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=count
    )
    df = pd.DataFrame(review_data)
    df['bank'] = bank_name
    return df

# Scrape reviews for all banks
all_reviews = []
for bank, app_id in app_ids.items():
    print(f"Scraping reviews for {bank}...")
    reviews_df = scrape_reviews(app_id, bank)
    all_reviews.append(reviews_df)

# Combine all reviews into one DataFrame
combined_reviews = pd.concat(all_reviews, ignore_index=True)


# Save to CSV
combined_reviews.to_csv("C:/Users/firao/Source/Repos/Customer-Experience_for_Fintech_apps/data/raw_reviews.csv", index=False)
print("Reviews saved to data/raw_reviews.csv")