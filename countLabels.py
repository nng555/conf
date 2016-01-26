import ijson.backends.yajl2 as ijson
import json
import operator

with open("allMeSH.json") as f:
   objects = ijson.items(f, "item")
   labelDict = {}
   for article in objects:
      for label in article["meshMajor"]:
         if(not labelDict.has_key(label)):
            labelDict[label] = 0
         labelDict[label] += 1
   sorted_list = sorted(labelDict.items(), key=operator.itemgetter(1), reverse=True)
   with open('labels.json', 'w') as fp:
       json.dump(sorted_list, fp)
