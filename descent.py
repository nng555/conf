import cPickle as pickle
from scipy.sparse import coo_matrix, csr_matrix, csc_matrix
import numpy as np
import math

def sigm(w, x):
   return 1/(1+math.exp(-np.dot(w, x.transpose())))

def loss(w, data, target):
   sum = 0
   for i in range(10000):
      sum += -target[i]*math.log(sigm(w, data[i])) - (1-target[i])*math.log(1 - sigm(w, data[i]))
   return sum/10000

def update(w, data, target):
   sum = np.zeros((101,1))
   for i in range(10000):
      sum += (sigm(weight, data[i]) - target[i]).item(0) * data[i].transpose()
   sum /= 10000
   return w - 0.1*sum.transpose()

if __name__ == '__main__':
   data = pickle.load(open("trainMat.pkl", 'rb'))
   target = pickle.load(open("trainLabelMat.pkl", 'rb'))
   testData = data[10000:11000,:100].todense()
   testTarget = target[10000:11000,:1].todense()
   data = data[:10000,:100].todense()
   target = target[:10000,:1].todense()
   data = np.hstack((data, np.ones((10000,1))))
   testData = np.hstack((testData, np.ones((1000,1))))
   weight = np.zeros(101)
   cost = loss(weight, data, target).item(0)
   for i in range(100):
      print cost
      weight = update(weight, data, target)
      cost = loss(weight, data, target).item(0)
   print weight
   count = 0
   for i in range(1000):
      if(sigm(weight, testData[i]) >= 0.5):
         pred = 1
      else:
         pred = 0
      if(pred != testTarget[i]):
         count += 1
   print count

