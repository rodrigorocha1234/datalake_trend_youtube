import trino

conn = trino.dbapi.connect(
    host="172.40.0.32",
    port=8080,
    user="admin",
    catalog="hive",
    schema="runtime",
)
print(type(conn))

cur = conn.cursor()
cur.execute("SELECT 1")
print(cur.fetchone())
cur.close()
conn.close()
