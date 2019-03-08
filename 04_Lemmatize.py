import spacy
nlp = spacy.load('en')
text = """While Samsung has expanded overseas, South Korea is still host to most of its factories and research engineers. """
doc = nlp(text)
for token in doc:
    print(token,"=Lemma=>", token.lemma_)