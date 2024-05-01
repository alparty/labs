""" Given a matrix, transpose it. Transposing a matrix means the rows are now the column and vice-versa. """


def transpose(mat):
    transposed = []
    tmp = []
    for y in range(len(mat[0])):
        for x in range(len(mat)):
            tmp.append(mat[x][y])
        transposed.append(tmp)
        tmp = []

    return transposed


mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
# [[1, 4],
#  [2, 5],
#  [3, 6]]
