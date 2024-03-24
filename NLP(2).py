# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:01:58 2024

@author: HP
"""

'''
.convert the given text into it's base form using both stemming and lemmatization
text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, 
playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""


'''

import spacy
from nltk.stem import PorterStemmer

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Initialize the Porter Stemmer from NLTK
porter_stemmer = PorterStemmer()

# Input text
text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""

# Lemmatization function using spaCy
def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc])
    return lemmatized_text

# Stemming function using NLTK
def stem_text(text):
    words = text.split()
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    stemmed_text = ' '.join(stemmed_words)
    return stemmed_text

# Lemmatize the text
lemmatized_text = lemmatize_text(text)
print("Lemmatized Text:")
print(lemmatized_text)
print()

# Stem the text
stemmed_text = stem_text(text)
print("Stemmed Text:")
print(stemmed_text)
