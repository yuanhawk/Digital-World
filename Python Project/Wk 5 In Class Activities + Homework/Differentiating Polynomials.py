def diff(polynomial):
    dict_diff = {}
    for indice, power in polynomial.items():
        if indice >= 1:
            dict_diff[indice - 1] = indice * power
    return dict_diff
