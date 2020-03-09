def letter_grade(mark):
    if not isinstance(mark, int):
        return False
    else:
        if mark > 100 or mark < 0:
            return None
        elif mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"
        return grade

print(letter_grade(102))
print(letter_grade(100))
print(letter_grade(83))
print(letter_grade(75))
print(letter_grade(67))
print(letter_grade(52))
print(letter_grade(-2))