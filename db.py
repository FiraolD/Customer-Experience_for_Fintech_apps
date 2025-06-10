import oracledb

conn = oracledb.connect(
    user="sys",
    password="Fira@0412",
    dsn="localhost/xepdb1"
)
print("✅ Connected")
