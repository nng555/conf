import numpy as np
import scipy as sp
import cPickle as pickle
from sklearn.linear_model import LogisticRegression

print("Enter dataset to train on:")
dataset = raw_input()

print("Enter labels:")
labelset = raw_input()

#print("Enter label to train on (integer between 0 to 1000):")
#label = int(raw_input())

print("Enter validation set:")
validSet = raw_input()

print("Enter validation label set:")
validLabelSet = raw_input()

data = pickle.load(open('pickles/'+ dataset, 'rb'))
target = pickle.load(open('pickles/'+ labelset, 'rb'))
valid = pickle.load(open('pickles/'+ validSet, 'rb'))
validLabels = pickle.load(open('pickles/'+ validLabelSet, 'rb'))

output = "test\n"

for j in range(0, 20):
    logreg = LogisticRegression()

    validLabels1 = validLabels[:, j:j+1]
    validLabels1 = np.asarray(validLabels1.todense()).ravel()
    target1 = target[:, j:j+1]
    target1 = np.asarray(target1.todense()).ravel()

    logreg.fit(data, target1)
    result = logreg.predict(valid)

    count = 0
    length = len(validLabels1)
    for i in range(0, length):
        if(result[i] != validLabels1[i]):
            count += 1

    ratio = count / length

    output += "%d errors in %d examples. Overall error is %d for label %d" % (count, length, ratio, j)

    print("%d errors in %d examples. Overall error is %d for label %d") % (count, length, ratio, j)

    filename = 'skLogRegLabel%d' % (j)

    with open(filename, 'wb') as fp:
        pickle.dump(logreg, fp, -1)

with open('20labelstest.txt', 'wb') as file1:
    file1.write(output)
    file1.close()
