import spacy

nlp = spacy.load('en_core_web_md')
text = """While Samsung has expanded overseas,"""

tokens = nlp(text)

for token in tokens:
    print(token.text)
    print (token.vector)
    print ()