import spacy
from collections import Counter
nlp = spacy.load("en")
text = """Most of the outlay will be at home. No surprise there, either. While Samsung has expanded overseas, South Korea is still host to most of its factories and research engineers. """
doc = nlp(text)
#remove stopwords and punctuations
words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
word_freq = Counter(words)
print ("=====WORD FREQUENCY=====")
print (word_freq)
common_words = word_freq.most_common(5)
print ("\n\n====TOP 5 words ===")
print (common_words)