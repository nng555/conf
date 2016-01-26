with open("/Volumes/Storage/allMeSH.json") as f:
   with open("allMeSH.json", 'w') as g:
      i = 0
      previous = "[\n"
      for line in f:
         if(i==0):
            i+=1
            continue
         g.write(previous)
         previous = line
      g.write("]")

