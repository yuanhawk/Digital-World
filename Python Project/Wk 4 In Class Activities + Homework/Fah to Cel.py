cel = 0
def f_to_c(fah):
  cel = (fah - 32) * (5 / 9)
  return round(cel,1)

cel_approx = 0
def f_to_c_approx(fah):
  cel_approx = (fah - 30) / 2
  return cel_approx

def get_conversion_table_a():
  f_to_c_list = []
  for fah in range(0, 101, 10):
    lister = []
    lister.append(fah)
    lister.append(f_to_c(fah))
    lister.append(f_to_c_approx(fah))
    
    f_to_c_list.append(lister)
  return f_to_c_list

print(get_conversion_table_a())