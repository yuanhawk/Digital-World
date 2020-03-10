def get_base_counts2(inp):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = 'ACTG'
    dna = []
    for i in inp:
        if i in alp:
            if i in base:
                dna.append(i)
        else:
            return 'The input DNA string is invalid'
        
    
    dict = {}
    for b in base:
        dict[b] = dna.count(b)
    return dict