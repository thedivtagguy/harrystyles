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

with open('D:/Data Projects/Automated Newsletter/txt files/michael.txt','r',encoding = 'unicode_escape') as f:
    text1 = f.read()

with open('D:/Data Projects/Automated Newsletter/txt files/beatles.txt','r',encoding = 'unicode_escape') as f:
    text2 = f.read()
    
text_model1 = markovify.Text(text1)
text_model2 = markovify.Text(text2)

model_combo = markovify.combine([ text_model1, text_model2 ], [ 1, 1.5 ])

model_json = model_combo.to_json()

with open('michael_beatles.json', 'w') as outfile:
    json.dump(model_json, outfile)

# for i in range(10):
#     print(model_combo.make_sentence())