import oracledb
connection = oracledb.connect(
    user="sys as sysdba",
    password="Fira@0412",
    dsn="localhost/XEPDB1"
)
print("✅ Connected")