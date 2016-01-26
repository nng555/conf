with open("2Mdump.json", 'rb') as f:
   lines = f.readlines()
   lines.reverse()
   begin = 0
   i = 0
   end = 2000001
   w = open("2mdumpR.json", 'wb')
   w.write("[\n")
   for line in lines:
      if(i != end and i != begin):
         w.write(line)
      i += 1
   w.write("]")
