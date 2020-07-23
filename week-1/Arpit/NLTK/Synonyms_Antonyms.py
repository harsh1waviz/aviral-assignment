import nltk
from nltk.corpus import wordnet
synonyms=[]
antonyms=[]


for syn in wordnet.synsets("good"):
	for x in syn.lemmas():
		synonyms.append(x.name())
		if x.antonyms():
			antonyms.append(x.antonyms()[0].name())


print(set(synonyms))
print(set(antonyms))


