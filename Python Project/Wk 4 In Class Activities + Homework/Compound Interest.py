def compound_value_months(s, i, n):
  amt = 0
  for p in range(n):
    amt += s
    amt *= (1 + i / 12)
  return round(amt, 2)