def is_prime(inp):
  
  i = 2
  while i < inp:
    if inp % i == 0:
      return False
    i += 1
  return True