from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
# for w in example_words:
#    print(ps.stem(w))
new_text="It is very important to be pythonly while you are pythoning with python.All pythoners have pthon"

words=word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
