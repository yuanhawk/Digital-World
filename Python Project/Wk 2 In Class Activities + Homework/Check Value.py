def check_value(n1, n2, n3, x):
	if x > n1 and x > n2 and x < n3:
		return True
	else:
		return False

print("Test Case 1: check_value(1, 4, 8, 7)")
print("ans = True")
ans = check_value(1, 4, 8, 7)
print(ans)

print("Test Case 2: check_value(10, 4, 8, 7)")
print("ans = False")
ans = check_value(10, 4, 8, 7)
print(ans)

print("Test Case 3: check_value(1, 10, 8, 7)")
print("ans = False")
ans = check_value(1, 10, 8, 7)
print(ans)

print("Test Case 4: check_value(1, 4, 5, 7)")
print("ans = False")
ans = check_value(1, 4, 5, 7)
print(ans)