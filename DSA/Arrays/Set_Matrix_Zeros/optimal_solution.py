'''This is the most optimal solution to this problem. If you look at the better solution,
it uses two additional lists to store the rows and columns that need to be set to zero.
In this solution we will use the first row and the first column to demarcate the rows and columns
to be converted. Now, the issue arises when we have to set the first row and first column to zero, 
because there is is one intersecting point, matrix[0][0]. So we'll use use a variable col0 and set it to 0
as default. If we find a zero in the first column, we will set col0 to 1.'''

def setMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = 1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j]!=0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0

    if col0 == 0:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix
    