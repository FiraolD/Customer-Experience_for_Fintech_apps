# Customer-Experience_for_Fintech_apps
Below is a well-structured `README.md` file for the   web scraping and preprocessing   part of your project. This README provides clear instructions, explanations, and guidance for collaborators or anyone reviewing your code.


#   Web Scraping and Preprocessing  

This repository contains scripts and documentation for   scraping reviews   from the Google Play Store and performing   data preprocessing   to prepare the data for downstream analysis. The goal is to collect user reviews for three Ethiopian banks—  Commercial Bank of Ethiopia (CBE)  ,   Bank of Abyssinia (BOA)  , and   Dashen Bank  —and clean the data for sentiment and thematic analysis.


##   Overview  
The objective of this module is to:
- Scrape user reviews from the Google Play Store using the `google-play-scraper` library.
- Preprocess the scraped data to remove duplicates, handle missing values, and normalize dates.
- Save the cleaned dataset as a CSV file for further analysis.

This module forms the foundation of the larger   Customer Experience Analytics for Fintech Apps   project.

##   Dataset Description  
The dataset includes the following fields for each review:
-   Review Text  : User feedback (e.g., "Love the UI, but it crashes often").
-   Rating  : 1–5 stars.
-   Date  : Posting date (time optional).
-   Bank/App Name  : E.g., "Commercial Bank of Ethiopia Mobile".
-   Source  : Google Play Store.

Each bank should have at least   400 reviews   (1,200 total).


##   Installation  

###   Prerequisites  
- Python 3.8 or higher
- A working internet connection

###   Dependencies  
Install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:
- `google-play-scraper`: For scraping reviews.
- `pandas`: For data manipulation.
- `numpy`: For numerical operations.


##   Usage  

###   Step 1: Clone the Repository  
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

###   Step 2: Run the Web Scraper  
Navigate to the `scripts/` folder and run the web scraper script:

```bash
python src/web_scrapper.py
```

This script will scrape reviews for the three banks and save the raw data as `raw_reviews.csv` in the `data/` directory.

###   Step 3: Preprocess the Data  
Run the preprocessing script to clean the data:

```bash
python src/preprocessing.py
```

This script performs the following tasks:
- Removes duplicates.
- Handles missing values.
- Normalizes dates.
- Saves the cleaned data as `clean_reviews.csv` in the `data/` directory.


##   Folder Structure  
The project follows a modular structure:

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── web_scrapper.py         # Script for scraping reviews
│   ├── preprocessing.py        # Script for data cleaning
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── data/
    ├── raw_reviews.csv         # Raw scraped data
    ├── clean_reviews.csv       # Cleaned data after preprocessing
```


##   Preprocessing Steps  

###   1. Remove Duplicates  
Duplicate reviews are removed based on unique combinations of `review_text`, `rating`, and `date`.

###   2. Handle Missing Values  
- Rows with missing `review_text` or `rating` are dropped.
- Missing `date` values are imputed using the nearest available date.

###   3. Normalize Dates  
Dates are converted to the format `YYYY-MM-DD` for consistency.

###   3. Remove stopwords

###   5. Save Processed Data  
The cleaned dataset is saved as `clean_reviews.csv` in the `data/` directory.


##   Contributing  
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/task-1`).
3. Commit your changes (`git commit -m "Add descriptive message"`).
4. Push to the branch (`git push origin feature/task-1`).
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.


##   References  
-   Google Play Scraper Library  : [https://pypi.org/project/google-play-scraper/](https://pypi.org/project/google-play-scraper/)
-   Pandas Documentation  : [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
-   Data Cleaning Techniques  : [https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)


This `README.md` file ensures that collaborators and reviewers can easily understand the purpose, structure, and usage of your web scraping and preprocessing module. 