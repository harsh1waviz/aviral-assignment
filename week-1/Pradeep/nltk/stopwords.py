from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sentence="this is stopwords example "
stop_words=set(stopwords.words("english"))

words=word_tokenize(example_sentence)

filtered_sentence=[]
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)
