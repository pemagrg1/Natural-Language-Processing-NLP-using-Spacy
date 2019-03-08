import spacy
# install: python -m spacy download en_core_web_lg
nlp = spacy.load('en_core_web_md')
text1 = nlp("dog")
text2 = nlp("cat")

print("similarity between "+text1.text+" and "+text2.text, text1.similarity(text2))