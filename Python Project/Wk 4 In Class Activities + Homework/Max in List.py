def max_list(inlist):
  outlist = []
  for innerlist in inlist:
    outlist.append(max(innerlist))
  return outlist

print(max_list([[1,2,3],[4,5]]))