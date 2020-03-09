def multiplication_table(n):
    if n < 1:
        return None
    lst = []
    tlst = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tlist.append(int(i * j))

        lst.append(tlst)
        tlst = []

    return lst
