import numpy as np

def five_number_summary(x):
    shape = list(x.shape)

    if len(shape) == 1:
        return None

    if shape[1] == 1:
        high = np.max(x)
        low = np.min(x)
        f_quartile = np.percentile(x, 25)
        center = np.median(x)
        t_quartile = np.percentile(x, 75)

        outdict = {}
        outdict['minimum'] = low
        outdict['first quartile'] = f_quartile
        outdict['median'] = center
        outdict['third quartile'] = t_quartile
        outdict['maximum'] = high
        return [outdict]
    elif shape[1] == 3:
        large_list = []
        list_z = []
        list_o = []
        list_t = []
        for r in range(len(x)):
            list_z.append(x[r][0])
            list_o.append(x[r][1])
            list_t.append(x[r][2])

        large_list.append(list_z)
        large_list.append(list_o)
        large_list.append(list_t)

        outlist = []
        for x in range(len(large_list)):
            high = np.max(large_list[x])
            low = np.min(large_list[x])
            f_quartile = np.percentile(large_list[x], 25)
            center = np.median(large_list[x])
            t_quartile = np.percentile(large_list[x], 75)

            outdict = {}
            outdict['minimum'] = low
            outdict['first quartile'] = f_quartile
            outdict['median'] = center
            outdict['third quartile'] = t_quartile
            outdict['maximum'] = high
            outlist.append(outdict)
        return outlist
    else:
        return None