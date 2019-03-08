import spacy
nlp = spacy.load("en")
text = """Most of the outlay will be at home. No surprise there, either. While Samsung has expanded overseas, South Korea is still host to most of its factories and research engineers. """
text = nlp(text)
labels = set([w.label_ for w in text.ents])
for label in labels:
    entities = [e.string for e in text.ents if label==e.label_]
    entities = list(set(entities))
    print( label,entities)