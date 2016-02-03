import json, sys, operator, os.path
import ijson
import numpy as np
from scipy.sparse import csr_matrix, vstack, coo_matrix
import cPickle

def main(argv):
    vocabDict = {}
    labelDict = {}
    with open("labelIndex1k.json") as f:
        labelDict = json.load(f)
    numTokens = len(labelDict)
    with open('2mdumpR.json') as f:
        i = 0
        articles = ijson.items(f, 'item')
        finalRow = []
        finalCol = []
        for article in articles:
            if i%1000 == 0:
                print i
            row = []
            col = []
            labels = article['meshMajor']
            for label in labels:
                if labelDict.has_key(label):
                    row.append(i)
                    col.append(labelDict[label])
            finalRow.extend(row)
            finalCol.extend(col)
            i += 1
    freq = numpy.ones(len(finalRow))
    output = csr_matrix((freq, (row, col)), shape = (2000000, 1000))
    with open('labelMat.pkl', 'wb') as fp:
        cPickle.dump(output, fp, -1)


if __name__ == "__main__":
    main(sys.argv[1:])
