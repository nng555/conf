import ijson.backends.yajl2 as ijson
from scipy.sparse import lil_matrix
from scipy.sparse import coo_matrix, vstack
import cPickle
import numpy

f = open("allMeSH.json");
wd = open("wordsN1.json");

wordDict = {}
words = ijson.items(wd, "item")
i = 0
for word in words:
   if(i > 99):
      break;
   wordDict[word[0]] = i
   i+=1

final = lil_matrix((1000,100))
count = 0
articles = ijson.items(f, "item")
start = coo_matrix((1,100))
for article in articles:
   if(count < 1000):
      freqDict = {}
      text = article["abstractText"]
      words = text.split()
      for word in words:
         word = word.lower()
         if(not freqDict.has_key(word)):
            freqDict[word] = 0
         freqDict[word] += 1
      a = numpy.zeros(100)
      for key, value in freqDict.iteritems():
         if(wordDict.has_key(key)):
            a[wordDict[key]] = value
      row = numpy.zeros(100)
      col = numpy.arange(100)
      finalRow = coo_matrix((a,(row,col)), shape=(1,100))
      start = vstack([start, finalRow])
      count += 1
   else:
      break

print start
f = open("1000r100wMat.pkl", 'wb')
cPickle.dump(start, f, -1)
f.close()
