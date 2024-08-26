# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:32:57 2024

@author: rushi
"""

import re
sentences5="sharat twitted, Wittnessing 68th republic day India from Rajpath. \new Delhi,Mesmorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+' , ' ' , sentences5).split()


###extracting n-grams
#extracting 2 or more words in called n-grams
#extracting once is 1 gram , twice is diagram ----N grams.



import re
def n_gram_extractor(input_str , n):
    tokens = re.sub(r'([^\s\w]|_)+' , '' , input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_extractor("The cute little boy is playing with kitten" , 2)
n_gram_extractor("The cute little boy is playing with kitten" , 3)

#---------------------------------------------------------

from nltk import ngrams
#extraction n-grams with nltk
list(ngrams("the cute little boy is playing with kitten.".split(),2))
list(ngrams("the cute little boy is playing with kitten.".split(),5))

#---------------------------------------------------------
#textblob

from textblob import TextBlob
blob=TextBlob("the cute little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)


#-----------------------------------------------------------
#tokenization using keras

sentences5
from keras.preprocessing.text import text_to_word_sequence
sentences5="sharat twitted, Wittnessing 68th republic day India from Rajpath. \new Delhi,Mesmorizing performance by Indian Army!"
text_to_word_sequence(sentences5)

#-----------------------------------------------------------
#tokenization using textblob
from textblob import TextBlob
blob=TextBlob(sentences5)
blob.words


#tweet tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentences5)

#---------------------------------------------------------
#multi - word tokenizer

from nltk.tokenize import MWETokenizer

'''multi word tokenizer are essential for tasks where
 the meaning of the text heavily depends on the interpretetion
 of phrases as wholes rather than as sums of indivisual words.
 For instances, in sentiment analysis, recognizing "not good"
 as a single negative sentiment unit rather thas as "not"
 and "good" seprately can significantly can affect the outcome'''
 

sentences5
mwe_tokenizer=MWETokenizer([('republic' , 'day')]) 
mwe_tokenizer.tokenize(sentences5.split())
mwe_tokenizer.tokenize(sentences5.replace('!' , ' ').split())


#-----------------------------------------------------------



