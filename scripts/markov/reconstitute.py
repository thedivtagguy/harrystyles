import markovify
import re
import json

with open('michael_beatles.json') as json_file:
    model_json = json.load(json_file)
    

reconstituted_model = markovify.Text.from_json(model_json)

 
for i in range(10):
    print(reconstituted_model.make_sentence())
    
    
    
    
    