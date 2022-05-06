# -*- coding: utf-8 -*-
"""Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IjxVukVWB2LOF1KIAH5XbxtDt7mXterG
"""

#Load the libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
import spacy
import re,string,unicodedata
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import LancasterStemmer,WordNetLemmatizer

import nltk
nltk.download('stopwords')
tokenizer=ToktokTokenizer()
stopword_list=nltk.corpus.stopwords.words('english')

#Removing punctuations
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
def remove_punc(data):
  return "".join([i for i in data if i not in punc])

#Converting to lowercase
def lowercase(data):
  return data.lower()

#Removing white spaces
def remove_whitespace(data):
    return  " ".join(data.split())


#Removing special characters
def remove_special_characters(text, remove_digits=True):
    pattern=r'[^a-zA-z0-9\s]'
    text=re.sub(pattern,'',text)
    return text
    


#removing the stopwords
#set stopwords to english
stop=set(stopwords.words('english'))
def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text

#Stemming the text
def stemmer(text):
    ps=nltk.porter.PorterStemmer()
    return ' '.join([ps.stem(word) for word in text.split()])
