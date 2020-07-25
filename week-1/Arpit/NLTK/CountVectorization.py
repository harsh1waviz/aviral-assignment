from sklearn.feature_extraction.text import CountVectorizer
import pandas
import nltk

cv = CountVectorizer()

corpus= ["this is a sentence" ,
	  "this is another sentence" ,
	  "this is third sentence" ,
	  "this is fourth sentence" ]
	  
x= cv.fit(corpus)
print(x.vocabulary_)
print(cv.get_feature_names())

x= cv.transform(corpus)
print(x.shape)
print(x.toarray())
