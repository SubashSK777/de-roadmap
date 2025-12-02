import psycopg2

conn = psycopg2.connect(
    dbname="de_db",
    user="de_user",
    password="strong",
    host="localhost",
    port=5432,
)

cur = conn.cursor()
cur.execute("SELECT 1;")
print("DB result:", cur.fetchone())

cur.close()
conn.close()
print("Connection OK")