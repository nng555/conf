import json
from nltk.tokenize import StanfordTokenizer
import ijson.backends.yajl2 as ijson

with open('stopwords.txt') as f:
   lines = f.readlines()
   stopWords = []
   for line in lines:
      line = line.strip('\n')
      stopWords.append(line)
with open('2mdumpR.json') as f:
   articles = ijson.items(f, 'item')
   out = open('2mToken.json', 'w')
   out.write('[\n')
   i = 0
   for article in articles:
      if(i%100==0):
         print i
      text = article['abstractText']
      tokens = StanfordTokenizer(path_to_jar='stanford-postagger.jar').tokenize(text)
      newTokens = []
      for token in tokens:
         token = token.lower()
         if token not in stopWords:
            newTokens.append(token)
      article['abstractText'] = newTokens
      if i == 49999:
         out.write(str(article) + '\n')
         break
      out.write(str(article) + ',\n')
      i += 1
   out.write(']')

