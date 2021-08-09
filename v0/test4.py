# db_utils.py
import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "database.sqlite3")


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


con = db_connect()  # connect to the database
cur = con.cursor()  # instantiate a cursor obj

# next_word_ddl = """
#  CREATE TABLE IF NOT EXISTS next_word (
#     parent_word text NOT NULL,
#     first_possible_word text,
#     second_possible_word text,
#     third_possible_word text
#     )"""
# cur.execute(next_word_ddl)


next_word_sql = "INSERT INTO next_word (parent_word, first_possible_word, second_possible_word,third_possible_word) VALUES (?,?,?, ?)"

# cur.execute(next_word_sql, ("Introduction to Combinatorics", 7.99))
# cur.execute(next_word_sql, ("A Guide to Writing Short Stories", 17.99))
# cur.execute(next_word_sql, ("Data Structures and Algorithms", 11.99))
# cur.execute(next_word_sql, ("Advanced Set Theory", 16.99))

val = {
    "self-taught": {"developer": 1},
    "bloke": {},
    "dosa": {"and": 1},
    "am": {"dheepak": 1, "a": 2},
    "and": {"i": 1, "python": 1, "blackcurrant": 1},
}

next_word_sql = "INSERT INTO next_word (parent_word, first_possible_word, second_possible_word,third_possible_word) VALUES (?,?,?, ?)"


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


for elem in val:
    if len(val[elem]) == 0:
        print("len == 0", elem, "", "", "", "")
        cur.execute(next_word_sql, (elem, "", "", ""))
    elif len(val[elem]) == 1:
        print("len == 1", elem, [key for key in val[elem].keys()][0], "", "")
        cur.execute(next_word_sql, (elem, [key for key in val[elem].keys()][0], "", ""))
    elif len(val[elem]) > 1:
        occurence = [key for key in val[elem].values()]
        occurence.sort(reverse=True)
        print("descending ", occurence)
        try:
            print(
                "len==3",
                elem,
                get_key(occurence[0], val[elem]),
                get_key(occurence[1], val[elem]),
                get_key(occurence[2], val[elem]),
            )
            cur.execute(
                next_word_sql,
                (
                    elem,
                    get_key(occurence[0], val[elem]),
                    get_key(occurence[1], val[elem]),
                    get_key(occurence[2], val[elem]),
                ),
            )

        except IndexError:
            print(
                "len==2",
                elem,
                get_key(occurence[0], val[elem]),
                get_key(occurence[1], val[elem]),
                "",
            )
            cur.execute(
                next_word_sql,
                (
                    elem,
                    get_key(occurence[0], val[elem]),
                    get_key(occurence[1], val[elem]),
                    "",
                ),
            )


cur.execute("SELECT *  FROM next_word")

results = cur.fetchall()

print(results)
