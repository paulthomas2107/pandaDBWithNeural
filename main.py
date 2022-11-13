import sqlite3
import pandas as pd

conn = sqlite3.connect("mydb.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS people (
    ssn INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER
    )
""")

cur.execute("""
INSERT INTO people (ssn, name, age) VALUES
(1, 'Mike', 25),
(90, 'Jenny', 26),
(7193, 'Dave', 30),
(2131, 'Rory', 19),
(82712, 'Caitlin', 21)
""")

conn.commit()

sql = pd.read_sql_query("SELECT * FROM people", conn)
df = pd.DataFrame(sql, columns=["ssn", "name", "age"])
df.set_index("ssn", inplace=True)

print(df)

# Panda to SQL
new_df = pd.DataFrame({
    "ssn": [21766, 818, 653],
    "name": ["Fox", "Lion", "Tiger"],
    "age": [30, 31, 29]
})

new_df.to_sql("people", con=conn, if_exists="append", index=False)
