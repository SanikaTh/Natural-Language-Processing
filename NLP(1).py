# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:37:52 2024

@author: HP
"""

"""
text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.

Using tokenization , Extract all money transaction from below sentence along with currency. Output should be,
wo $
500 €
2.
1.Use stemming for following docs
doc = nlp("Mando talked for 3 hours although talking isn't his thing")
doc = nlp("eating eats eat ate adjustable rafting ability meeting better")

"""
import re

# Text containing transactions
text = '''
I owe you $500 and you owe me 200€. Let's settle this.
'''

# Regular expression pattern to match money transactions
money_pattern = r'\b\d+(\.\d+)?\s*(?:\$|€)\b'

# Extract money transactions with currency
transactions = re.findall(money_pattern, text)

# Print the extracted transactions
for transaction in transactions:
    print(transaction)

import spacy
pip install en_core_web_sm
# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Define a function for stemming using spaCy
def stem_text(text):
    doc = nlp(text)
    stemmed_text = ' '.join([token.lemma_ for token in doc])
    return stemmed_text

# Test the function with the provided documents
doc1 = "Mando talked for 3 hours although talking isn't his thing"
doc2 = "eating eats eat ate adjustable rafting ability meeting better"

stemmed_doc1 = stem_text(doc1)
stemmed_doc2 = stem_text(doc2)

print("Stemmed document 1:", stemmed_doc1)
print("Stemmed document 2:", stemmed_doc2)
