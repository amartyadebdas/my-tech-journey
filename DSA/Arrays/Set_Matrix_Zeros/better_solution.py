'''This includes two lists, one for rows and one for columns.
We will traverse through the entire matrix, if we find a zero, we will mark the row and column as 1.
We will then traverse through the entire matrix again, and check if column[i] or row[j] is 1, if it is, we will set the matrix[i][j] to 0.

Time complexity: 2(O(n*m)) = O(n*m)
Space complexity: O(n)+O(m)'''

def setZeroes(matrix):
    row = [0]*len(matrix)
    col = [0]*len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0

    return matrix