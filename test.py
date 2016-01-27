import json
from spacy.en import English
from nltk.tokenize import StanfordTokenizer
import ijson.backends.yajl2 as ijson

nlp = English()
with open('stopwords.txt') as f:
   lines = f.readlines()
   stopWords = {}
   for line in lines:
      line = line.strip('\n')
      stopWords[line] = 1
vocab = {}
with open('2mdumpR.json') as f:
   data = ijson.items(f, 'item')
   i = 0
   for article in data:
      if(i%100==0):
         print i
      text = article['abstractText']
      tokens = nlp(text)
      for token in tokens:
         token = token.orth_.lower()
         if not stopWords.has_key(token):
            if not vocab.has_key(token):
               vocab[token] = 0
            vocab[token] += 1
      i += 1
with open('2mVocab.json', 'w') as fp:
   json.dump(vocab, fp)

