import spacy
# install: python -m spacy download en_core_web_lg
nlp = spacy.load('en_core_web_md')

doc1 = nlp(u"Do you have an ice cream?")
doc2 = nlp(u"Is ice cream available?")
print (doc1.similarity(doc2))