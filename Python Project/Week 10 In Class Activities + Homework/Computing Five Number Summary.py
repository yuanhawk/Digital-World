from numpy import percentile
from numpy.random import rand

data = rand(1000)

quartiles = percentile(data, [25, 50, 75])

data_min, data_max = data.min(), data.max()

print('Min: %.3f' % data_min)
print('Q1: %.3f' % quartiles[0])
print('Median: %.3f' % quartiles[1])
print('Q3: %.3f' % quartiles[2])
print('Max: %.3f' % data_max)