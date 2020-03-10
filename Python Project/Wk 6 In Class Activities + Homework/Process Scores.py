def process_scores(f):
    lister = []
    for line in f:
        num = line.split()
        lister.extend(num)
        
        
    total = 0
    count = 0
    for t in lister:
        total += float(t)
        count += 1
    mean = total / count
        
    return total, mean