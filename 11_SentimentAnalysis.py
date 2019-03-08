import spacy
from spacy.tokens import Doc
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()


def polarity_scores(doc):
    return sentiment_analyzer.polarity_scores(doc.text)


Doc.set_extension('polarity_scores', getter=polarity_scores)

nlp = spacy.load('en')
doc = nlp("Loving this code.")
print(doc._.polarity_scores)
