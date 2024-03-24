# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:04:16 2024

@author: HP
"""

'''
You are parsing a news story from cnbc.com. News story is stores in news_story.txt which is on whatsapp. You need to, 
1.	Extract all NOUN tokens from this story. You will have to read the file in python first to collect all the text and
 then extract NOUNs in a python list
2.	Extract all numbers (NUM POS type) in a python list
3.	Print a count of all POS tags in this story


'''
import spacy

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Read the contents of the file
file_path = "D:/Documents/Machine_laerning(2)/NLP assignment/news_story.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Process the text using spaCy
doc = nlp(text)

# 1. Extract all NOUN tokens
nouns = [token.text for token in doc if token.pos_ == "NOUN"]

# 2. Extract all numbers (NUM POS type)
numbers = [token.text for token in doc if token.pos_ == "NUM"]

# 3. Count the occurrences of each POS tag
pos_counts = {}
for token in doc:
    pos_tag = token.pos_
    if pos_tag in pos_counts:
        pos_counts[pos_tag] += 1
    else:
        pos_counts[pos_tag] = 1

# Print the results
print("NOUN tokens:")
print(nouns)
print()

print("Numbers (NUM POS type):")
print(numbers)
print()

print("Count of POS tags:")
for pos_tag, count in pos_counts.items():
    print(f"{pos_tag}: {count}")
