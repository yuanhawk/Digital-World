def uncompress(inp):
    list_op = []
    num = '0123456789'
    alp = 'abcdefghijklmnopqrstuvwxyz'
    
    val = ''
    for x in inp:
        val += x
        if x in alp:
            list_op.append(val)
            val = ''
    
    list_num = []
    list_alp = []
    for y in list_op:
        n = ''
        alph = ''
        for i in y:
            if i in num:
                n += i
            if i in alp:
                alph += i
        list_num.append(int(n))
        list_alp.append(alph)
    
    op = ''
    for i in range(len(list_num)):
        op += list_num[i] * list_alp[i]
    return op