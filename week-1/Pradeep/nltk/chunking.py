import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

'''
pos tag list:

CC    coordinating conjunction
CD    cardinal digit
DT    determiner
EX    exitentia there
IN    preposition/subordinating conjunction
jj    adjective   'big'
'''
tarin_text = state_union.raw("2005-GWBush.txt")
sample_texr = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=PunktsentenceTokenizer(tain_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
        print(tagged)
