from nltk.stem import PorterStemmer
from nltk. tokenize import word_tokenize

ps= PorterStemmer()

text=["go","gone","going","goes"]

for x in text:
    print(ps.stem(x))