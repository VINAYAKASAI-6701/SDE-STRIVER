class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        #step1->Transpose has beeen done
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        #step2->reversing eacch row to obtain result 
        for i in range(n):
            matrix[i].reverse()
        return matrix