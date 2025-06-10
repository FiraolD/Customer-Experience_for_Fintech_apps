import pandas as pd
import oracledb

# Step 1: Read Excel file
df = pd.read_excel("your_file.xlsx")  # Make sure openpyxl is installed

# Step 2: Set Oracle connection (update with your credentials)
dsn = cx_Oracle.makedsn("hostname", port, service_name="your_service_name")
conn = cx_Oracle.connect(user="your_username", password="your_password", dsn=dsn)
cursor = conn.cursor()

# Step 3: Prepare insert query (match your table structure)
sql = """
INSERT INTO your_table_name (column1, column2, column3)
VALUES (:1, :2, :3)
"""

# Step 4: Insert data row by row
data = [tuple(row) for row in df.values]
cursor.executemany(sql, data)

# Step 5: Commit and close
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully.")
