from collections import Counter
import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "database.sqlite3")


sample_text_original = """I am Dheepak. I am a self-taught developer and I have been programming since 2014. I write SQL for food and Python for fun. outside of work, I am a confused bloke. In terms of food, I love dosa, and Blackcurrant (yea, it tastes like cough syrup) flavored ice cream. I tweet a lot """

sample_text = (
    sample_text_original.lower().replace("(", ".").replace(")", ".").replace(",", "")
)


def fetch_sentencs(paragraph):
    """This returns sentences & unique words from the paragraph.

    Args:
        paragraph (string): This is passed to the machine by the user
    """

    # todo Fetch sentences
    sentences = paragraph.split(".")
    return {"Sentences": sentences, "count": len(sentences)}


def fetch_words(paragraph):
    """Fetch unique words without trailing symbols.

    Args:
        paragraph (string): Passed by user
    """

    raw_words = paragraph.split(" ")
    cleaned_words = []
    for raw_word in raw_words:
        cleaned_word = raw_word.strip(".").strip().strip(")").strip("(")
        cleaned_words.append(cleaned_word.lower())
    uniq_words = list(set(cleaned_words))
    return {"unique words": uniq_words, "Word count": len(uniq_words)}


def succeeding_word_list(sentence_list, unique_words):
    word_follows = {}
    # succeeding_words = []
    for word in unique_words:
        succeeding_words = []
        for line in sentence_list:
            if word in line:
                words_in_line = line.split(" ")
                try:
                    succeeding_words.append(
                        words_in_line[words_in_line.index(word) + 1]
                    )
                except:
                    pass
            else:
                pass  # print("Word not present")

            word_follows[word] = succeeding_words

    return word_follows


def assign_weightage(suceeding_words_dict):
    """This assigns succeeding word's weightage

    Args:
        suceeding_words_dict (dict): Key - Word, Value - list (succeeding words)
    """


def count_elem_occurence_in_list(list_containing_elements):
    return dict(Counter(list_containing_elements))


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


def set_table():
    con = db_connect()  # connect to the database
    cur = con.cursor()  # instantiate a cursor obj

    next_word_ddl = """
    CREATE TABLE IF NOT EXISTS next_word (
        parent_word text NOT NULL,
        first_possible_word text,
        second_possible_word text,
        third_possible_word text
        )"""
    cur.execute(next_word_ddl)


def insert_into_table(dict_with_word_frequency):
    pass


def main():
    sent = fetch_sentencs(sample_text)

    words_1 = fetch_words(sample_text)
    golden_words = words_1["unique words"]

    succeding_words = succeeding_word_list(sent["Sentences"], golden_words)

    # print(succeding_words)

    some_dict = {}
    for item in succeding_words:
        # print(item, a[item])
        if len(item):
            val = dict(count_elem_occurence_in_list(succeding_words[item]))
            some_dict[item] = val

    print(some_dict)

    set_table()
    insert_into_table(some_dict)


main()

