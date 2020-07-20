from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text= " Hi there, this is an example of showing off dtop word filteration."
stop_words= set(stopwords.words("english"))

words= word_tokenize(text)
filtered_sentence= []

for x in words:
    if x not in stop_words:
        filtered_sentence.append(x)

print(filtered_sentence)