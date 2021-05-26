import markovify
import re
import spacy
import json

nlp = spacy.load("en_core_web_lg")

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

with open('D:/Data Projects/Automated Newsletter/txt files/breakingbad.txt','r',encoding = 'unicode_escape') as f:
    text1 = f.read()


  
text_model1 = markovify.Text(text1)

def text():
    for i in range(10):
        print(text_model1.make_short_sentence(100))
    
strings = ["I'm not in danger, Skyler.", 
           "My name is ASAC Schrader, and you deserve to die.",
           "I hide in plain sight, same as his taste in lawyers.", 
           "This is my own private domicile and I will kill your infant daughter.", 
           "And I watched Jane die.", 
           "I do not constitute plans in my heart.",
           ]