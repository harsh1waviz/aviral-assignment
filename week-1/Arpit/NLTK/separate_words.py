from nltk.tokenize import word_tokenize

text= "Hello everyone, i am Arpit Bansal and i am going to separate this sentence in words using python."
#print(word_tokenize(text))

for i in word_tokenize(text):
    print(i)
