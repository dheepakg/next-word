import logging

logger = logging.getLogger(__name__)

sample_text = ""
cleaned_words = []


def read_text_from_user():
    # sample_text = input(">>")
    sample_text = "Back when I worked at Zak (former Mimic) and even today at Lumos we format logs as JSON. That's a good standard for systems running in production that may contain many attributes. It's easier to visualize JSON than a regular long string, and you don't have to create your own formatter for that (check out python-json-logger)."
    logger.info("Sample text is received; of lenght {}".format(len(sample_text)))
    return sample_text


# TODO  integrate flask app to read from UI
# TODO Add loggers


def clean_inp_text():
    # sentences = sample_text.split(".")
    sample_text = read_text_from_user()
    print("sample text ", sample_text)
    raw_words = sample_text.split(".")
    print("raw_words ", raw_words)
    for raw_word in raw_words:
        cleaned_word = raw_word.strip(" ").strip().strip(")").strip("(")
        cleaned_words.append(cleaned_word.lower())
    print(cleaned_words)
    print(list(set(cleaned_words)))
    return len(cleaned_words)

