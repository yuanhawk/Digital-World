def longest_common_prefix(string1, string2):
    string = ''
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            string += string1[i]
        else:
            break
        if i >= len(string2) - 1:
            break
    return string