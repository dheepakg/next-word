sample_text = """I am Dheepak. I am a self-taught developer and I have been programming since 2014. I write SQL for food and Python for fun. Outside of work, I am a confused bloke. In terms of food, I love dosa, and Blackcurrant (yea, it tastes like cough syrup) flavored ice cream. I tweet a lot """

# Todo Split the sample text into sentences, store it in list.
sentences = sample_text.split(".")
# print(sentences)

# Todo Split each of sentence, and get the unique words.
raw_words = sample_text.split(" ")
cleaned_words = []
for raw_word in raw_words:
    cleaned_word = raw_word.strip(".").strip().strip(")").strip("(")
    cleaned_words.append(cleaned_word.lower())
print(cleaned_words)
print(list(set(cleaned_words)))

#     word = str(line).split(' ')
#     words.append(word)

# print(words)

