with open("allMeSH.json", 'rb') as fh:
   offs = -200
   while True:
      fh.seek(offs, 2)
      lines = fh.readlines()
      if len(lines)>1:
         print lines[-1]
         break
      offs *= 2
