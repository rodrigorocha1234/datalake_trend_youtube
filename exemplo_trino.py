import trino

conn = trino.dbapi.connect(
    host="localhost",
    port=8080,
    user="test",
    catalog="system",
    schema="runtime",
)

cur = conn.cursor()
cur.execute("SELECT 1")
print(cur.fetchone())
cur.close()
conn.close()
