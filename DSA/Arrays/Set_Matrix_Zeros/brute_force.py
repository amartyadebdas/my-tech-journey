'''This solution is a brute force approach to this problem.
It's pretty simple, traverse through the entire matrix, if you find a zero, mark the entire row and column as -1.
Then, traverse the entire matrix again and set all -1s to 0. 
Time complexity is O(n*m)(n*m) + O(n*m) and space complexity is O(1) as we are not using any extra space.'''

def markCol( matrix,m,i):
        for j in range(m):
            if matrix[i][j]!=0:
                matrix[i][j]=-1
        return matrix

def markRow(matrix, n,j):
    for i in range(n):
        if matrix[i][j]!=0:
            matrix[i][j]=-1 
    return matrix

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    markCol( matrix, len(matrix[0]),i)
                    markRow( matrix, len(matrix), j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-1:
                    matrix[i][j]=0

        return matrix


        
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j]==-1:
                    matrix[i][j]=0

        return matrix