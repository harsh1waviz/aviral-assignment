
from nltk.corpus import wordnet

word= wordnet.synsets("program")

print(word[0].definition())

