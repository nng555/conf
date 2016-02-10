import numpy as np
import scipy as sp
import cPickle as pickle
from sklearn.linear_model import LogisticRegression

print("Enter dataset to train on:")
dataset = raw_input()

print("Enter labels:")
labelset = raw_input()

print("Enter label to train on (integer between 0 to 1000):")
label = int(raw_input())

print("Enter validation set:")
validSet = raw_input()

print("Enter validation label set:")
validLabelSet = raw_input()

logreg = LogisticRegression()

data = pickle.load(open('pickles/'+ dataset, 'rb'))
target = pickle.load(open('pickles/'+ labelset, 'rb'))
valid = pickle.load(open('pickles/'+ validSet, 'rb'))
validLabels = pickle.load(open('pickles/'+ validLabelSet, 'rb'))

validLabels = validLabels[:, label:label+1]
validLabels = np.asarray(validLabels.todense()).ravel()
target = target[:, label:label+1]
target = np.asarray(target.todense()).ravel()

logreg.fit(data, target)
result = logreg.predict(valid)

count = 0
for i in range(0, len(validLabels)):
    if(result[i] != validLabels[i]):
        count += 1

print(count + " errors in " + len(valid) + " examples.")


