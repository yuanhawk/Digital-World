def get_base_counts(inp):
  dna = {}

  a = 0
  c = 0
  g = 0
  t = 0
  for i in inp:
    if i == 'A':
      a += 1
    elif i == 'C':
      c += 1
    elif i == 'G':
      g += 1
    elif i == 'T':
      t += 1
    else:
      return 'The input DNA string is invalid'
  
  dna['A'] = a
  dna['C'] = c
  dna['G'] = g
  dna['T'] = t

  return dna