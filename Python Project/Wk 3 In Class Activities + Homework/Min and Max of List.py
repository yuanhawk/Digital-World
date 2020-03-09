def minmax_in_list(inp):
  value = []
  value.extend(inp)

  if value == []:
    return None, None

  min = 5000
  max = 0
  i = 0
  while i < len(value):
    if value[i] < min:
      min = value[i]

    if value[i] > max:
      max = value[i]

    i += 1
  return min, max

print(minmax_in_list([1,2,3,4,5]))
print(minmax_in_list([1,1,3,0]))
print(minmax_in_list([3,2,1]))
print(minmax_in_list([0,10]))
print(minmax_in_list([1]))
print(minmax_in_list([]))
print(minmax_in_list([1,1,1,1,1]))
  #input - list of integer
  #return min, maxdef minmax_in_list(ls):
