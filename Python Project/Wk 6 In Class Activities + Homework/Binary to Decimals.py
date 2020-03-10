def binary_to_decimal(binstr):
    value = 0
    count = 0
    for x in binstr:
        count += 1
        
    for y in range(len(binstr)):
        if binstr[y] == "1":
            value += 2 ** (count - 1) 
        count -= 1
    
    return value