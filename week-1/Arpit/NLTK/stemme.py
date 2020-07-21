
from nltk.stem import PorterStemmer 
import nltk

ps=PorterStemmer()

text= ["go","goes","gone","going"]

for x in text:
	print(ps.stem(x))
 
