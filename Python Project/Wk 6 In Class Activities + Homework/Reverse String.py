def reverse(string):
    rev = ''
    for s in range(-1, -len(string) - 1, -1):
        rev += string[s]
    return rev