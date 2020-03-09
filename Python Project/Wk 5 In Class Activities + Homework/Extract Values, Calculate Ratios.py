def extract_values(values):
    value1 = ''
    value2 = ''
    
    for i in range(len(values)):
        if values[i] == ' ':
            value1 = int(values[:i])
            value2 = int(values[i+1:])
    return value1, value2

def calc_ratios(values):
    v1 = values[0]
    v2 = values[1]
    if v2 == 0:
        return None
    return v1 / v2