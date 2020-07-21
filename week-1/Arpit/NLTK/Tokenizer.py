from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text= "Hello everyone, i am Arpit Bansal. I am going to separate this sentence in words using python."
print(word_tokenize(text))

#for i in word_tokenize(text):
#    print(i)

print(sent_tokenize(text))
