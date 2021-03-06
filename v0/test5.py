import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "database.sqlite3")


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


con = db_connect()  # connect to the database
cur = con.cursor()


cur.execute("SELECT *  FROM next_word")

results = cur.fetchall()

print(results)
