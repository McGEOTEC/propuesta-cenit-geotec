import sqlite3, os

db_path = r'C:\Users\Camila\.gemini\antigravity-ide\conversations\2a0e1f7f-07b5-473b-ac20-a586ddf02103.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print('Tables in DB:', tables)

for t in tables:
    tname = t[0]
    cursor.execute(f"SELECT COUNT(*) FROM {tname};")
    cnt = cursor.fetchone()[0]
    print(f"Table {tname}: {cnt} rows")

conn.close()
