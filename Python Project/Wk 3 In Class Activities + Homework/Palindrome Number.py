def is_palindrome(inp):
  #Check if inp is a palindrome

    value = list(map(int, str(inp)))
    
    i = 0
    j = len(value) - 1

    while i < len(value) / 2:
        if value[i] != value[j]:
            return False
            break
        i += 1
        j -= 1
    return True


print(is_palindrome(1))
print(is_palindrome(22))
print(is_palindrome(12321))
print(is_palindrome(441232144))
print(is_palindrome(44123114))
print(is_palindrome(144))
print(is_palindrome(12))