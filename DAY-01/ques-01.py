class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #Most Optimal Solution
        #space efficeint
        # int row[n] = {0}; --> matrix[..][0]
        # int col[m] = {0}; --> matrix[0][..]
        #step 1 marking exempting first row
        n=len(matrix)
        m=len(matrix[0])
        col0=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        #any row wise col wise 1 are marked to xero if present
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]!=0:
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
        #step 3:marking zero row and col
        if matrix[0][0]==0:
            for j in range(m):
                matrix[0][j]=0
        if col0==0:
            for i in range(n):
                matrix[i][0]=0
        return matrix
        """
        Do not return anything, modify matrix in-place instead.
        """
        