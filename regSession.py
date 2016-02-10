# coding: utf-8
import cPickle as pickle
from scipy.sparse import coo_matrix, csr_matrix
train = pickle.load(open("trainMat.pkl", 'rb'))
train = train.tocsr()
train
train[:10]
toy = train[:100]
toy
toy = toy.tocsc()
toy[:100}
toy[:100]
toy[:.:100]
toy[:,:100]
toy = toy[:,:100]
get_ipython().magic(u'ls ')
toyX = toy
target = pickle.load(open("testLabelMat.pkl", 'rb'))
target
target = pickle.load(open("trainLabelMat.pkl", 'rb'))
target
target[:100,:100]
target[:100,:1]
target = target[:100,:1]
target
toyY = target
toyY
data = toyX.todense()
data
target = toyY.todense()
target
get_ipython().magic(u'clear ')
data
target
get_ipython().magic(u'clear ')
import numpy as np
weight = np.ones(100)
weight
weight[0]
target[0]
target[1]
data[0]
np.dot(weight, data[0])
np.dot(weight, data[0].transpose())
1/(1+exp(16))
add = np.ones(100)
add
add = add.transpose()
add
add.transpose()
add = [add]
add
add.transpose()
add
np.ones(,100)
np.ones(1,100)
test = np.ones((100,101))
test
test = np.ones((1,100))
test
test = np.ones((100,1))
test
test.hstack(data)
hstack(data, test)
np.hstack(data, test)
np.hstack((data, test))
data = np.hstack((data, test))
weight = np.ones(101
)
weight
np.dot(weight, data[0].transpose())
1/(1+math.exp(-17))
import math
1/(1+math.exp(-17))
sigmoid = 1/(1+math.exp(-17))
sum = 0
sum = np.zeros(101)
sum
sum = np.zeros((101,1))
sum
get_ipython().magic(u'clear ')
get_ipython().magic(u'ls ')
for i in range(100)
for i in range(100):
    sum += x[i] * (target[i] - 1/(1 - math.exp(np.dot(weight,x[i].transpose()))))

for i in range(100):
    sum += data[i] * (target[i] - 1/(1 - math.exp(np.dot(weight,data[i].transpose()))))

data[i]
data[i] * 1
data[i] * 2
target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose())))
target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose()))) * data[0]
data[0]
target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose()))) * data[0]
(target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose()))) * data[0])[0]
(target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose()))))[0]
(target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose()))))[0][0]
(target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose())))).item(0)
(target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose())))).item(0) * data[0]
i
for i in range(100):
    sum += (target[0] - 1/(1-math.exp(np.dot(weight,data[0].transpose())))).item(0) * data[0]

for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i]

sum
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum
sum = sum/100
sum
weight = weight - 0.1*sum
weight
weight
weight = ones((1,101))
weight = np.ones((1,101))
weight
weight[0]
weight = np.ones((101,1))
weight
weight - 0.1*sum.transpose()
sum
weight - sum
0.1*sum
weight - 0.1*sum
weight = weight - 0.1*sum
weight
weight
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum
sum = np.zeros((101,1))
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum = np.zeros(101)
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum = np.zeros((1,101))
sum
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

data[0]
sum = np.zeros(101)
sum
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum = np.zeros((101,1))
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

weight
weight = weight.transpose()
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum
weight - 0.1*sum.transpose()
weight = weight-0.1*sum.transpose()
sum
sum = sum/100
weight
sum = sum*100
weight = weight + 0.1*sum.transpose()
weight
sum=sum/100
weight = weight - 0.1*sum.transpose()
weight
loss = 0
for i in range(100)
for i in range(100):
    loss += target[i]*math.log(1/(1-exp(-np.dot(weight,data[i].transpose())))) + (1-target[i])*math.log(1/(1-exp(-np.dot(weight,data[i].transpose()))))

for i in range(100):
    loss += target[i]*math.log(1/(1-math.exp(-np.dot(weight,data[i].transpose())))) + (1-target[i])*math.log(1/(1-math.exp(-np.dot(weight,data[i].transpose()))))

loss
sum = np.zeros(101
)
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(-np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum
weight
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(-np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum = np.zeros(101)
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(-np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum = np.zeros((101,1))
for i in range(100):
    sum += (target[i] - 1/(1-math.exp(-np.dot(weight,data[i].transpose())))).item(0) * data[i].transpose()

sum=sum/100
sum
weight = weight - 0.1*um
weight = weight - 0.1*sum
weight
weight
weight + 0.1*sum
get_ipython().magic(u'save regsession.py')
