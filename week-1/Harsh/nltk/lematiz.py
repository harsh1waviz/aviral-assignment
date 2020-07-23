from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats",pos="a"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
