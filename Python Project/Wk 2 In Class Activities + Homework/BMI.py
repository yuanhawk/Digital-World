def bmi(w,h):
    
    #Conversion from cm to m
    h /= 100
    bmi_cal = w / h ** 2
    return round(bmi_cal, 1)

print(bmi(60, 120))
print(bmi(50, 150))
print(bmi(43.5, 142.3))