def wind_chill_temp(t_a, v):
	t_wc = 35.74 + 0.6215 * t_a - 35.75 * v ** 0.16 + 0.4275 * t_a * v ** 0.16
	return t_wc
	
print(wind_chill_temp(5.3, 6))
print(wind_chill_temp(2.2, 4))