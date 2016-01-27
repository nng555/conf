import json, sys, operator, os.path
from nltk.tokenize import StanfordTokenizer
import ijson.backends.yajl2 as ijson
import numpy as np
from scipy.sparse import csr_matrix, vstack
import cPickle

def main(argv):
   numArticles = int(argv[0])
   topTokens = int(argv[1])
   wordDict = {}
   sorted_list = []
   if os.path.isfile('t' + str(numArticles) + 'a.json'):
      with open('t' + str(numArticles) + 'a.json') as f:
         data = ijson.items(f, 'item')
         for word in data:
            sorted_list.append(word)
   else:
      with open("/Users/nathanng/Downloads/stcn/patterns/stopwords.txt") as f:
          lines = f.readlines()
          stopWords = []
          for line in lines:
             line = line.strip('\n')
             stopWords.append(line)
      with open('2mdumpR.json') as f:
         articles = ijson.items(f, 'item')
         count = 0
         for article in articles:
            if(count % 100 == 0):
               print count
            if(count >= numArticles):
               break
            text = article['abstractText']
            tokens = StanfordTokenizer(path_to_jar="/Users/nathanng/Downloads/stpt/stanford-postagger.jar").tokenize(text)
            tokens = [x.lower() for x in tokens]
            for token in tokens:
               if token not in stopWords:
                  if not wordDict.has_key(token):
                     wordDict[token] = 0
                  wordDict[token] += 1
            count += 1
         sorted_list = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
         with open('t' + str(numArticles) + 'a.json', 'w') as fp:
            json.dump(sorted_list, fp)
   indexDict = {}
   i = 0
   sorted_list_top = sorted_list[:topTokens]
   print sorted_list_top
   for token in sorted_list_top:
      indexDict[token[0]] = i
      i += 1

   with open('2mdumpR.json') as f:
      i = 0
      articles = ijson.items(f, 'item')
      for article in articles:
         print i
         if(i >= numArticles):
            break
         freqDict = {}
         text = article['abstractText']
         tokens = StanfordTokenizer(path_to_jar="/Users/nathanng/Downloads/stpt/stanford-postagger.jar").tokenize(text)
         tokens = [x.lower() for x in tokens]
         freq = np.zeros(topTokens)
         for token in tokens:
            if indexDict.has_key(token):
               freq[indexDict[token]] = freq[indexDict[token]] + 1
         row = np.zeros(topTokens)
         col = np.arange(topTokens)
         output = csr_matrix((freq, (row, col)), shape=(1,topTokens))
         if i == 0:
            start = output
            i += 1
            continue
         start = vstack([start, output])
         i += 1
      with open(str(topTokens) + 't' + str(numArticles) + 'a.pkl', 'wb') as fp:
         cPickle.dump(start, fp, -1)

if __name__ == "__main__":
   main(sys.argv[1:])
