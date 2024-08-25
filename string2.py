# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:07:50 2024

@author: HP
"""

text = "i’m a cat"
#1
def title_case(text):
    words = text.split() 
    capitalized_words = [word.capitalize() for word in words]  
    return ' '.join(capitalized_words) 

text_title = title_case(text)
print(text_title) 


# 2
text_upper = text.upper()
print(text_upper)
def custom_format(text):
    words = text.split() 
    formatted_words = []
    for word in words:
        if word.lower() == "i’m": 
            formatted_words.append(word[0].lower() + word[1:].upper()) 
        elif word.lower() == "a":
            formatted_words.append(word.lower()) 
        elif word.lower() == "cat": 
            formatted_words.append(word[:1].lower() + word[1:].upper()) 
    return ' '.join(formatted_words) 
#3
text = "i’m a cat"
text_custom = custom_format(text)
print(text_custom)

# 4. 
def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

text_capitalized = capitalize_first_letter(text)
print(text_capitalized) 

