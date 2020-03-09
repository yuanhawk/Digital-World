def temp_convert(inp, temp):
  if inp == 'C':
    c = (temp - 32) * (5 / 9)
    return c
  elif inp == 'F':
    f = temp * (9 / 5) + 32
    return f
  else:
    return None

print(temp_convert('F', 32))
print(temp_convert('F', -40))
print(temp_convert('F', 212))
print(temp_convert('C', 0))
print(temp_convert('C', -40))
print(temp_convert('C', 100))
print(temp_convert('', 0))
print(temp_convert('A', 0))