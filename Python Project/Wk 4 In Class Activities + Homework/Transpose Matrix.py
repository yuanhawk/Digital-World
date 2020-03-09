def transpose_matrix(mat):
  matrix = []

  for i in range(len(mat[0])):
    sub = []
    for j in range(len(mat)):
      sub.append(mat[j][i])
    matrix.append(sub)
  return matrix