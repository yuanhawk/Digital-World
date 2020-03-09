def list_sum(inp):
  value = []
  value.extend(inp)

  d = 0
  sum = 0.0
  while d < len(value):
    sum += value[d]
    d += 1
  return sum

print(list_sum([]))
print(list_sum([5.0]))
print(list_sum([4.25, 5.0, 10.75]))