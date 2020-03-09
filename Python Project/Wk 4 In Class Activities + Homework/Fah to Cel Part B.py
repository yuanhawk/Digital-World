cel = 0
def f_to_c(fah):
  cel = (fah - 32) * (5 / 9)
  return round(cel,1)

cel_approx = 0
def f_to_c_approx(fah):
  cel_approx = (fah - 30) / 2
  return cel_approx

def get_conversion_table_b():
  lister = []
  fah_list = []
  f_to_c_list = []
  f_to_c_approx_list = []
  for fah in range(0, 101, 10):
    fah_list.append(fah)
    f_to_c_list.append(f_to_c(fah))
    f_to_c_approx_list.append(f_to_c_approx(fah))
    
  lister.append(fah_list)
  lister.append(f_to_c_list)
  lister.append(f_to_c_approx_list)
  return lister

print(get_conversion_table_b())