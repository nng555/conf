import ijson
def load_json(filename):
   with open(filename) as fd:
      count = 0
      for line in fd:
         count+=1
   print count-2

if __name__ == "__main__":
   load_json('allMeSH.json')
