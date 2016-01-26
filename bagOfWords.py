import ijson.backends.yajl2 as ijson
import json
import operator
from nltk.corpus import stopwords

with open("allMeSH.json") as f:
   objects = ijson.items(f, "item")
   wordDict = {}
   stop = stopwords.words('english')
   for article in objects:
      text = article["abstractText"]
      words = text.split()
      for word in words:
         word = word.lower();
         if(word not in stop):
            if(not wordDict.has_key(word)):
               wordDict[word] = 0;
            wordDict[word] += 1;
   sorted_list = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
   with open('wordsN1.json', 'w') as fp:
       json.dump(sorted_list, fp)
   sorted_list = sorted(wordDict.items(), key=operator.itemgetter(0))
   with open('wordsA1.json', 'w') as fp:
      json.dump(sorted_list, fp)
