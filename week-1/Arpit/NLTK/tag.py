import nltk
text="hello everyone, i am arpit bansal."
sentence= nltk.sent_tokenize(text)

for x in sentence:
	print (nltk.pos_tag(nltk.word_tokenize(x)))



 

