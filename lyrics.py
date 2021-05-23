import markovify

# Get raw text as string.
with open("D:/harry.txt") as f:
    text1 = f.read()

# Get raw text as string.
with open("D:/dwight.txt") as f:
    text2 = f.read()

# Build the model.
text_model1 = markovify.Text(text1)
text_model2 = markovify.Text(text2)

model_combo = markovify.combine([ text_model1, text_model2 ], [ 2, 1 ])

# Print five randomly-generated sentences
for i in range(15):
    print(model_combo.make_sentence())
