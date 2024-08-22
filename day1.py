# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:15:14 2024
 
@author: RUSHI
"""
#----------------------TEXT MINING-----------------------------#
'''text mining is the process of exploring and analyzing 
large amount of unstructured text data with the help 
 software that can find
 1.concept
 .patterns
 3.topics '''

sentence = "we are learning textmining from sanjivani AI"

#To find location/position of "learning"
sentence.index("learning")
#it will show the position which is 7

#---------------------------------------------------
#we want to know position of textmining word
sentence.split().index("textmining")

#Print any word in reverse order
sentence .split()[2][::-1]
#the word at the location 2 will be printed in reverse order


#print first and last word of the sentence
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word

#now we want to concate the first and last word
concat_word=first_word+" "+last_word
concat_word

#----------------------------------------------------
# we want to print even words from the sentences
[words[i] for i in range(len(words)) if i%2==0]


sentence
#display only AI
sentence[-2:]

#display entire sentence in reverse order
sentence[::-1]

#select each word and print in reverse
words
print(" ".join(word[::-1]for word in words))

#punkt is sentence tokenizer
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP fundamentals")
print(words)

#parts of speech (PoS) tagging
#tags the word of the sentences
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)

#stop_words from NLTK library
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words=stopwords.words('english')

print(stop_words)

#replace words in string
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)


#auto correction in sentence
from autocorrect import Speller
#declare the function speller defined for english
spell=Speller(lang='en')
spell("Engilish")

#-----------------------------------------------------------------
#correct whole sentence
import nltk
nltk.download('punkt')
from nltk import word_tokenize
sentence3="Ntural lanaguage processin deals with the artt of "
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
corrected_sentence

#stemming
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")

#--------------------------------------------------------------
#lematizer
#lematizer looks like into dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")

lemmatizer.lemmatize('battling')

lemmatizer.lemmatize("amazing")

#===============================================================
#chunking (shallow parsing)Identifying named entities
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="we are learing nlp in python"
#first we will tokenize
nltk.download('averaged_preceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]


#sentence tokenization
#tokenization is act of breaking the sentence into phrases or words 
#two types of tokenization 
#1.sentence tokenization
#2.word tokenization

from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning NLP in python . It is taught by naik sir")
sent

#---------------------------------------------------------------
# he went to bank and checked account. it was almost 0 looking this
# he went to river bank and was crying
from nltk.wsd import lesk
sentence1="keep your savings in the bank"
print(lesk(word_tokenize(sentence1),'bank'))

#---------------------------------------------------
