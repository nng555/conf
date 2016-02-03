import ijson
import json
import operator

with open("2mdumpR.json") as f:
    objects = ijson.items(f, "item")
    labelDict = {}
    i = 0;
    for article in objects:
        if i%10000 == 0:
            print i
        for label in article["meshMajor"]:
            if(not labelDict.has_key(label)):
                labelDict[label] = 0
            labelDict[label] += 1
        i = i + 1
    sorted_list = sorted(labelDict.items(), key=operator.itemgetter(1), reverse=True)
    with open('labels.json', 'w') as fp:
        json.dump(sorted_list, fp)
