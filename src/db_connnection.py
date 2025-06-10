import pandas as pd
import oracledb
from datetime import datetime
import numpy

# Load CSV
csv_file = 'C:/Users/firao/Source/Repos/Customer-Experience_for_Fintech_apps/data/thematic_reviews.csv'
df = pd.read_csv(csv_file)

# Replace NaN with None
df = df.where(pd.notnull(df), None)

def validate_row(row):
    try:
        # Ensure required fields are not None
        if not row['reviewId'] or not row['userName']:
            raise ValueError("Missing required field: reviewId or userName")

        # Convert numeric columns
        #row['score'] = numpy.long(row['score']) if row['score'] else 0
        #row['thumbsUpCount'] = numpy.long(row['thumbsUpCount']) if row['thumbsUpCount'] else 0

        # Convert dates
        for col in ['DateAt', 'repliedAt', 'cleanedat']:
            if row[col]:
                try:
                    row[col] = pd.to_datetime(row[col], errors='coerce')
                except Exception:
                    row[col] = None
            else:
                row[col] = None

        # Final clean row tuple for DB insertion
        return (
            row['reviewId'],
            row['userName'],
            row['userImage'],
            row['content1'],
            row['score'],
            row['thumbsUpCount'],
            row['reviewCreatedVersion'],
            row['DateAt'],
            row['replyContent'],
            row['repliedAt'],
            row['appVersion'],
            row['bank'],
            row['cleanedat'],
            row['cleaned_content'],
            row['sentiment'],
            row['keywords'],
            row['theme']
        )
    except Exception as e:
        print(f"❌ Invalid row skipped: {e}")
        return None

# Validate and prepare data
valid_rows = []
for idx, row in df.iterrows():
    validated = validate_row(row)
    if validated:
        valid_rows.append(validated)

if not valid_rows:
    print("⚠️ No valid rows to insert.")
    exit()

# Connect to Oracle DB (Thin mode)
connection = oracledb.connect(
    user="sys",               # Change as needed
    password="Fira@0412",  # Change as needed
    dsn="localhost/xepdb1"          # For Oracle XE 21c
    )
cursor = connection.cursor()

    # Insert data
insert_query = """
    INSERT INTO REVIEWS (
        REVIEWID, USERNAME, USERIMAGE, CONTENT1, SCORE,
        THUMBSUPCOUNT, REVIEWCREATEDVERSION, DATEAT,
        REPLYCONTENT, REPLIEDAT, APPVERSION, BANK,
        CLEANEDAT, CLEANED_CONTENT, SENTIMENT, KEYWORDS, THEME
    ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17)
    """

cursor.executemany(insert_query, valid_rows)
connection.commit()

print(f"✅ Successfully inserted {len(valid_rows)} rows into REVIEWS.")
