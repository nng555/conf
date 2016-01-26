import ijson
def load_json(filename):
   with open(filename) as fd:
      parser = ijson.parse(fd)
      for prefix, event, value in parser:
         print prefix, value

if __name__ == "__main__":
   load_json('allMeSH.json')
