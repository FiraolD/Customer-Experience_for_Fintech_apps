import pandas as pd
import oracledb
from datetime import datetime

# Load CSV with expected column names
expected_columns = [
    'reviewId', 'userName', 'userImage', 'content1',
    'score', 'thumbsUpCount', 'reviewCreatedVersion', 'DateAt',
    'replyContent', 'repliedAt', 'appVersion', 'bank',
    'cleanedat', 'cleaned_content', 'sentiment', 'keywords', 'theme'
]

csv_file = 'C:/Users/firao/Source/Repos/Customer-Experience_for_Fintech_apps/data/thematic_reviews.csv'
df = pd.read_csv(csv_file, names=expected_columns, header=None)

# Replace NaN with None
df = df.where(pd.notnull(df), None)

def safe_convert_to_numeric(val, default=0):
    try:
        return int(float(val)) if val is not None else default
    except:
        return default

def validate_row(row):
    try:
        # Ensure required fields are not None
        if not row['reviewId'] or not row['userName']:
            raise ValueError("Missing required field: reviewId or userName")

        # Convert numeric columns
        row['score'] = safe_convert_to_numeric(row['score'])
        row['thumbsUpCount'] = safe_convert_to_numeric(row['thumbsUpCount'])

        # Convert dates
        for col in ['DateAt', 'repliedAt', 'cleanedat']:
            if row[col]:
                if isinstance(row[col], str):
                    try:
                        row[col] = datetime.strptime(row[col], "%m/%d/%Y %H:%M")
                    except ValueError:
                        try:
                            row[col] = datetime.strptime(row[col], "%m/%d/%Y")
                        except:
                            row[col] = None
            else:
                row[col] = None

        return row

    except Exception as e:
        print(f"❌ Invalid row: {e}")
        print("Problematic row:", row.to_dict())
        return None

# Validate all rows
valid_rows = []
for idx, row in df.iterrows():
    validated_row = validate_row(row)
    if validated_row is not None:
        valid_rows.append(validated_row.values.tolist())

if not valid_rows:
    print("⚠️ No valid rows to insert.")
else:
    # Connect to Oracle DB
    connection = oracledb.connect(
        user="SYS",
        password="Fira@0412",
        dsn="localhost:1521/xepdb1",
        mode=oracledb.SYSDBA
    )
    cursor = connection.cursor()

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
    cursor.close()
    connection.close()

    #print("✅ Successfully inserted  valid rows.")