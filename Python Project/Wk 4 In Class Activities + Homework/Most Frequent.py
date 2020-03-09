def most_frequent(inp):
  most = 0
  lister = []
  frequent = {}
  for i in range(len(inp)):
    frequent[inp[i]] = inp.count(inp[i])
  print(frequent)
  
  most = 0
  for y in frequent.values():
    if y > most:
      most = y
  
  for x, y in frequent.items():
    if y == most:
      lister.append(x)
  return lister