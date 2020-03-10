def get_fundamental_constants(f):
    d = {}
    value = []
    for line in f:
        value.append(line)
        
    for i in range(2, len(value)):
        r = value[i].split()
        print(r)
        d[r[0]] = float(r[1])
        
    return d
        