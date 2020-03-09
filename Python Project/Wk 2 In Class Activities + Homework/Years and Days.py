def minutes_to_years_days(min):
  day = int(min / 60 / 24)
  year = day // 365
  day %= 365
  return year, day
	
print(minutes_to_years_days(1000000000))
print(minutes_to_years_days(2000000000))