import spacy
from collections import Counter
nlp = spacy.load("en")
text = """Most of the outlay will be at home. No surprise there, either."""
doc = nlp(text)
#remove stopwords and punctuations
words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
cleaned_words = " ".join(words)
print ("====Before removing Stopwords===")
print (text)
print ("====After removing Stopwords===")
print (cleaned_words)