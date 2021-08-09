sample_text = """I am Dheepak. I am a self-taught developer and I have been programming since 2014. I write SQL for food and Python for fun. Outside of work, I am a confused bloke. In terms of food, I love dosa, and Blackcurrant (yea, it tastes like cough syrup) flavored ice cream. I tweet a lot """

word = "I"
word_follows = {}
succeeding_words = []
for line in sample_text.split("."):
    if word in line:
        print("valid words")
        words_in_line = line.split(" ")
        print(words_in_line)
        print(words_in_line.index(word))
        try:
            succeeding_words.append(words_in_line[words_in_line.index(word) + 1])
        except:
            pass
    else:
        print("invalid word")

word_follows[word] = succeeding_words


print(word_follows)
