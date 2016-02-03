import json, sys, operator, os.path
import ijson
import numpy as np
from scipy.sparse import csr_matrix, vstack, coo_matrix
import cPickle
from spacy.en import English

def main(argv):
    vocabDict = {}
    nlp = English(parser=False, tagger=False, entity=False)
    with open("vocabIndex100k.json") as f:
        vocabDict = json.load(f)
    numWords = len(vocabDict)
    with open('2mdumpR.json') as f:
        i = 0
        articles = ijson.items(f, 'item')
        finalRow = []
        finalCol = []
        finalData = []
        for article in articles:
            if i%1000 == 0:
                print i
            row = []
            col = []
            data = []
            freqDict = {}
            text = article['abstractText']
            tokens = nlp(text, entity=False, tag=False)
            for token in tokens:
                token = token.orth_.lower()
                if vocabDict.has_key(token):
                    if not freqDict.has_key(vocabDict[token]):
                        freqDict[vocabDict[token]] = 0
                    freqDict[vocabDict[token]] = freqDict[vocabDict[token]] + 1
            for key, value in freqDict.iteritems():
                row.append(i)
                col.append(key)
                data.append(value)
            finalRow.extend(row)
            finalCol.extend(col)
            finalData.extend(data)
            i += 1
    output = csr_matrix((finalData, (finalRow, finalCol)), shape = (2000000, 100000))
    with open('labelMat.pkl', 'wb') as fp:
        cPickle.dump(output, fp, -1)


if __name__ == "__main__":
    main(sys.argv[1:])
