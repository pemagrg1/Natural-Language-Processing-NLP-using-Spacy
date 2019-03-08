import spacy
nlp = spacy.load("en")
text = """Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. It was developed by Steven Bird and Edward Loper in the Department of Computer and Information Science at the University of Pennsylvania."""
text = nlp(text)
sent_tokenize = (list(text.sents))
for sent in sent_tokenize:
    print (sent)