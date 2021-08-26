sample_text = ""
cleaned_words = []


def read_text_from_user():
    # sample_text = input(">>")
    sample_text = "sample text"
    return len(sample_text)


def clean_inp_text():
    sentences = sample_text.split(".")
    raw_words = sample_text.split(" ")
    for raw_word in raw_words:
        cleaned_word = raw_word.strip(".").strip().strip(")").strip("(")
        cleaned_words.append(cleaned_word.lower())
    print(cleaned_words)
    print(list(set(cleaned_words)))
    return len(cleaned_words)

