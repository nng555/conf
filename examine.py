with open("2Mdump.json", 'rb') as fh:
   offs = -200
   while True:
      fh.seek(offs, 2)
      lines = fh.readlines()
      if len(lines)>3:
         print lines[-2]
         break
      offs *= 2
