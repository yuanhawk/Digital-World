def investment_val(amt, interest, years):
  amt *= (1 + interest / 12 / 100) ** (years * 12)
  return round(amt, 2)

print(investment_val(1000, 4.25, 1))
print(investment_val(1500, 3.25, 2))
print(investment_val(1000, 2.25, 0.5))
print(investment_val(2000, 4.25, 3))