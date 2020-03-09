def describe_bmi(bmi):
    if (bmi < 18.5):
        return "nutritional deficiency"
    elif (bmi >= 18.5 and bmi < 23):
        return "low risk"
    elif (bmi >= 23 and bmi < 27.5):
        return "moderate risk"
    else:
        return "high risk"

print(describe_bmi(18))
print(describe_bmi(18.5))
print(describe_bmi(20))
print(describe_bmi(23))
print(describe_bmi(27.5))
print(describe_bmi(30))