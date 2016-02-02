import json
from spacy.en import English
#from nltk.tokenize import StanfordTokenizer
#import ijson.backends.yajl2 as ijson
import ijson
import cProfile


def test():
    nlp = English()
    #nlp = English(parser=False, tagger=False, entity=False)

    with open('stopwords.txt') as f:
       lines = f.readlines()
    stopWords = {}
    for line in lines:
        line = line.strip('\n')
        stopWords[line] = 1
    vocab = {}
    with open('500kdumpR.json') as f:
        data = ijson.items(f, 'item')
        #data = json.load(f)
        i = 0
        for article in data:
            if(i%100==0):
                print i
            text = article['abstractText']
            tokens = nlp(text, entity=False, tag=False)
            for token in tokens:
                token = token.orth_.lower()
                if not stopWords.has_key(token):
                    if not vocab.has_key(token):
                        vocab[token] = 0
                    vocab[token] += 1
            i += 1
    with open('500kVocab.json', 'w') as fp:
        json.dump(vocab, fp)



cProfile.run('test()');
