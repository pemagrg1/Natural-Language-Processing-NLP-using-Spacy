import spacy
nlp = spacy.load("en")
text = """Natural Language Toolkit, or more commonly NLTK."""
text = nlp(text)
for w in text:
    print (w,"==", w.pos_)