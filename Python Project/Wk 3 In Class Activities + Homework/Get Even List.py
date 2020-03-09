def get_even_list(inp):
  value = []
  value.extend(inp)

  i = 0
  while i < len(value):
    if value[i] % 2 == 1:
      value.remove(value[i])
    else:
      i += 1
  return value