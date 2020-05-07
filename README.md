Created Date: 8 March 2019

# Natural Langauge Processing (NLP) using Spacy
SpaCy is an open-source software library for advanced Natural Language Processing, written in the programming languages Python and Cython. The library is published under the MIT license.
Today we’ll be talking about how to get started with NLP using Spacy. But before starting, make sure that you have Python and Spacy installed in your system. <br>

To install Spacy and English Model:<br>
```sudo pip install spacy```
```python -m spacy download en``` <br>

In spacy, the object “nlp” is used to create documents, access linguistic annotations and different nlp properties.
The default model which is english-core-web, for which we load the “en” model. <br>

```
import spacy 
nlp = spacy.load(“en”)
```
1. WORD TOKENIZE <br>
Tokenize words to get the tokens of the text i.e breaking the sentences into words.
2. SENTENCE TOKENIZE<br>
Tokenize sentences if the there are more than 1 sentence i.e breaking the sentences to list of sentence.
3. STOP WORDS REMOVAL<br>
Remove irrelevant words using nltk stop words like is,the,a etc from the sentences as they don’t carry any information.
4. Lemma <br>
lemmatize the text so as to get its root form eg: functions,funtionality as function
5. Get word frequency<br>
counting the word occurrence using FreqDist library. Word frequency helps us to determine how important the word is in the document by knowing how many times the word is being used.
6. POS tags<br>
POS tag helps us to know the tags of each word like whether a word is noun, adjective etc.
7. NER<br>
NER(Named Entity Recognition) is the process of getting the entity names
<br>
BLOG: https://medium.com/@pemagrg/nlp-for-beninners-using-spacy-6161cf48a229
